#!/usr/bin/env python3
"""Annual financials and returns on capital for the market-structure company set, from SEC XBRL.

Pulls each company's XBRL company facts (via edgar.py), takes one value per fiscal
year per metric using SEC "frames" (CY{year} for flows, CY{year}Q4I for balances),
and computes the same derived metrics for every firm:

  FCF = operating cash flow - capex (PP&E + capitalised software)
  ROIC = NOPAT / average invested capital, NOPAT = operating income x (1 - tax rate),
         invested capital = debt + total equity (cash not netted, so heavy buyback filers stay meaningful)
  ROIC ex-goodwill = NOPAT / (invested capital - goodwill - intangibles)
  Banks: ROE, ROTCE (net income to common / average tangible common equity), efficiency ratio.
         FCF is not meaningful for banks and is left blank. JPM's preferred stock has no annual
         XBRL frame, so its ROTCE here is approximate (understated).

Every value records the XBRL tag it came from so it can be checked against the filing.
LSEG (UK) and Bloomberg (private) are not on EDGAR.

Quarterly series (from 10-Q frames CY{year}Q{n}; Q4 derived as FY minus Q1-Q3 when not reported)
are written to quarterly.csv for revenue, operating income, pre-tax and net income.

    python3 _ingest/financials.py            # writes raw/financials/annual.csv, derived.csv, quarterly.csv
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edgar  # noqa: E402

OUT = os.path.join(HERE, "raw", "financials")
YEARS = range(2018, 2026)
# BlackRock re-registered under a new holding company in 2024; its history sits under the old CIK.
EXTRA_CIKS = {"BLK": [1364742]}
COMPANIES = {"TW": "venue", "MKTX": "venue", "ICE": "exchange", "SPGI": "data", "TRI": "data",
             "BLK": "asset_manager", "GS": "bank", "JPM": "bank"}

# metric -> candidate tags, tried in order (us-gaap first, then ifrs-full for TRI's 40-F)
FLOW = {
    "revenue": ["RevenuesNetOfInterestExpense", "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenuesExcludingInterestAndDividends", "Revenue"],
    "operating_income": ["OperatingIncomeLoss", "ProfitLossFromOperatingActivities"],
    "pretax_income": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                      "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
                      "ProfitLossBeforeTax"],
    "income_tax": ["IncomeTaxExpenseBenefit", "IncomeTaxExpenseContinuingOperations"],
    "net_income": ["NetIncomeLoss", "ProfitLossAttributableToOwnersOfParent"],
    "net_income_common": ["NetIncomeLossAvailableToCommonStockholdersBasic", "NetIncomeLoss",
                          "ProfitLossAttributableToOwnersOfParent"],
    "nci_income": ["NetIncomeLossAttributableToNoncontrollingInterest", "ProfitLossAttributableToNoncontrollingInterests"],
    "d_and_a": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
                "DepreciationAndAmortization", "DepreciationAndAmortisationExpense"],
    "amort_intangibles": ["AmortizationOfIntangibleAssets"],
    "op_cash_flow": ["NetCashProvidedByUsedInOperatingActivities", "CashFlowsFromUsedInOperatingActivities"],
    "capex_ppe": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
                  "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "capex_software": ["PaymentsToDevelopSoftware", "PaymentsForSoftware", "PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"],
    "acquisitions": ["PaymentsToAcquireBusinessesNetOfCashAcquired", "PaymentsToAcquireBusinessesGross",
                     "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock", "PaymentsToAcquireOrRedeemEntitysShares"],
    "dividends": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends", "PaymentsOfOrdinaryDividends",
                  "DividendsPaidClassifiedAsFinancingActivities", "DividendsPaidOrdinaryShares", "DividendsCash"],
    "noninterest_expense": ["NoninterestExpense"],
    "operating_expenses": ["OperatingExpenses", "CostsAndExpenses"],
    "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding",
                       "AdjustedWeightedAverageShares"],
}
INSTANT = {
    "cash": ["CashAndCashEquivalentsAtCarryingValue", "CashAndDueFromBanks", "CashAndCashEquivalents"],
    "debt_long": ["LongTermDebt", "LongTermDebtNoncurrent", "LongtermBorrowings", "NoncurrentPortionOfNoncurrentBorrowings"],
    "debt_current": ["LongTermDebtCurrent", "DebtCurrent", "CurrentPortionOfLongtermBorrowings"],
    "short_borrowings": ["ShortTermBorrowings", "CommercialPaper", "ShorttermBorrowings"],
    "equity": ["StockholdersEquity", "EquityAttributableToOwnersOfParent"],
    "equity_total": ["StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "Equity"],
    "preferred": ["PreferredStockValue"],
    "goodwill": ["Goodwill"],
    "intangibles": ["IntangibleAssetsNetExcludingGoodwill", "IntangibleAssetsOtherThanGoodwill"],
    "assets": ["Assets"],
}


def _days(r):
    from datetime import date
    try:
        return (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
    except (KeyError, ValueError):
        return 0


def pick_max(facts, tags, year):
    """Largest value across candidate tags: total revenue is the biggest revenue figure filed."""
    best = (None, "")
    for tax in ("us-gaap", "ifrs-full"):
        for tag in tags:
            for r in facts.get(tax, {}).get(tag, {}).get("units", {}).get("USD", []):
                if r.get("frame") == f"CY{year}" and (best[0] is None or r["val"] > best[0]):
                    best = (r["val"], f"{tax}:{tag}")
    return best


def pick(facts, tags, year, instant):
    for tax in ("us-gaap", "ifrs-full"):
        for tag in tags:
            node = facts.get(tax, {}).get(tag)
            if not node:
                continue
            for unit, rows in node["units"].items():
                if unit not in ("USD", "shares"):
                    continue
                want = f"CY{year}Q4I" if instant else f"CY{year}"
                hits = [r for r in rows if r.get("frame") == want]
                if not hits and not instant:
                    # SEC sometimes leaves a 10-K value unframed: fall back to the annual filing's own FY figure
                    hits = [r for r in rows if r.get("form") in ("10-K", "40-F", "20-F") and r.get("fp") == "FY"
                            and r.get("end", "").startswith(str(year)) and 350 <= _days(r) <= 380]
                if hits:
                    return hits[-1]["val"], f"{tax}:{tag}"
    return None, ""


def _facts(cik, cache):
    if os.path.exists(cache):
        return json.load(open(cache))
    facts = edgar.company_facts(cik)["facts"]
    json.dump(facts, open(cache, "w"))
    return facts


def fetch(ticker):
    """Company facts for the ticker's current CIK, with older CIKs merged in (current wins)."""
    facts = _facts(edgar.cik_for(ticker)[0], os.path.join(OUT, f"facts_{ticker}.json"))
    for old in EXTRA_CIKS.get(ticker, []):
        for tax, tags in _facts(old, os.path.join(OUT, f"facts_{ticker}_{old}.json")).items():
            for tag, node in tags.items():
                cur = facts.setdefault(tax, {}).setdefault(tag, {"units": {}})
                for unit, rows in node["units"].items():
                    have = {r.get("frame") for r in cur["units"].get(unit, []) if r.get("frame")}
                    cur["units"].setdefault(unit, []).extend(r for r in rows if r.get("frame") not in have)
    return facts


QUARTERLY = ["revenue", "operating_income", "pretax_income", "net_income", "operating_expenses"]


def quarterly(facts, ticker, model):
    out = []
    for y in list(YEARS) + [2026]:
        qs = {}
        for q in (1, 2, 3, 4):
            rec = {"ticker": ticker, "model": model, "year": y, "quarter": q}
            for m in QUARTERLY:
                v, tag = pick_frame(facts, FLOW[m], f"CY{y}Q{q}", largest=(m == "revenue" and model != "bank"))
                rec[m], rec[m + "_basis"] = v, ("reported" if v is not None else "")
            qs[q] = rec
        for m in QUARTERLY:
            fy, _ = pick_frame(facts, FLOW[m], f"CY{y}", largest=(m == "revenue" and model != "bank"))
            if qs[4][m] is None and fy is not None and all(qs[q][m] is not None for q in (1, 2, 3)):
                qs[4][m] = fy - sum(qs[q][m] for q in (1, 2, 3))
                qs[4][m + "_basis"] = "derived FY-Q1-Q3"
        if ticker == "ICE":  # report ICE net of transaction-based expenses, as in the annual series
            for q in qs.values():
                if q["operating_income"] is not None and q["operating_expenses"] is not None:
                    q["revenue"], q["revenue_basis"] = q["operating_income"] + q["operating_expenses"], "net (op income + opex)"
        out += [qs[q] for q in (1, 2, 3, 4) if any(qs[q][m] is not None for m in QUARTERLY)]
    return out


def pick_frame(facts, tags, frame, largest=False):
    best = (None, "")
    for tax in ("us-gaap", "ifrs-full"):
        for tag in tags:
            node = facts.get(tax, {}).get(tag)
            if not node:
                continue
            hits = [r for r in node["units"].get("USD", []) if r.get("frame") == frame]
            if hits and not largest:
                return hits[-1]["val"], f"{tax}:{tag}"
            for r in hits:
                if best[0] is None or r["val"] > best[0]:
                    best = (r["val"], f"{tax}:{tag}")
    return best


def div(a, b):
    return a / b if a is not None and b not in (None, 0) else None


def main():
    os.makedirs(OUT, exist_ok=True)
    rows, derived, qrows = [], [], []
    for tk, model in COMPANIES.items():
        facts = fetch(tk)
        qrows += quarterly(facts, tk, model)
        by_year = {}
        for y in YEARS:
            rec = {"ticker": tk, "model": model, "year": y, "revenue_gross": None}
            for m, tags in FLOW.items():
                rec[m], rec[m + "_tag"] = (pick_max(facts, tags, y) if m == "revenue" and model != "bank"
                                           else pick(facts, tags, y, False))
            if tk == "ICE" and rec["operating_income"] is not None and rec["operating_expenses"] is not None:
                # ICE files gross revenue; net of transaction-based expenses = operating income + opex
                rec["revenue_gross"] = rec["revenue"]
                rec["revenue"], rec["revenue_tag"] = rec["operating_income"] + rec["operating_expenses"], "derived: OperatingIncomeLoss + OperatingExpenses (net)"
            for m, tags in INSTANT.items():
                rec[m], rec[m + "_tag"] = pick(facts, tags, y, True)
            rows.append(rec)
            by_year[y] = rec
        prev = None
        for y in YEARS:
            r = by_year[y]
            debt = sum(v for v in (r["debt_long"], r["debt_current"], r["short_borrowings"]) if v) or None
            eq_total = r["equity_total"] or r["equity"]
            capex = sum(v for v in (r["capex_ppe"], r["capex_software"]) if v)
            fcf = r["op_cash_flow"] - capex if r["op_cash_flow"] is not None else None
            tax_rate = div(r["income_tax"], r["pretax_income"])
            tax_rate = min(max(tax_rate, 0.0), 0.35) if tax_rate is not None else 0.21
            nopat = r["operating_income"] * (1 - tax_rate) if r["operating_income"] is not None else None
            ic = (debt or 0) + eq_total if eq_total else None  # cash not netted: buyback-heavy filers go near zero
            ic_ex = ic - (r["goodwill"] or 0) - (r["intangibles"] or 0) if ic is not None else None
            tce = (r["equity"] or 0) - (r["preferred"] or 0) - (r["goodwill"] or 0) - (r["intangibles"] or 0) if r["equity"] else None
            d = {"ticker": tk, "model": model, "year": y,
                 "revenue_m": r["revenue"] and r["revenue"] / 1e6,
                 "op_margin": div(r["operating_income"], r["revenue"]),
                 "net_margin": div(r["net_income"], r["revenue"]),
                 "fcf_m": fcf and fcf / 1e6, "fcf_margin": div(fcf, r["revenue"]),
                 "capex_to_rev": div(capex, r["revenue"]),
                 "debt_m": debt and debt / 1e6, "cash_m": r["cash"] and r["cash"] / 1e6,
                 "net_debt_to_ebitda": div((debt or 0) - (r["cash"] or 0),
                                           (r["operating_income"] or 0) + (r["d_and_a"] or 0)) if r["operating_income"] else None,
                 "goodwill_intang_to_assets": div((r["goodwill"] or 0) + (r["intangibles"] or 0), r["assets"]),
                 "buybacks_m": r["buybacks"] and r["buybacks"] / 1e6, "dividends_m": r["dividends"] and r["dividends"] / 1e6,
                 "acquisitions_m": r["acquisitions"] and r["acquisitions"] / 1e6,
                 "payout_of_fcf": div((r["buybacks"] or 0) + (r["dividends"] or 0), fcf),
                 "diluted_shares_m": r["diluted_shares"] and r["diluted_shares"] / 1e6,
                 "nci_share_of_income": div(r["nci_income"], (r["net_income"] or 0) + (r["nci_income"] or 0)) if r["nci_income"] else None,
                 "invested_capital_m": ic and ic / 1e6,
                 "roic": None, "roic_ex_goodwill": None, "roe": None, "rotce": None,
                 "efficiency_ratio": div(r["noninterest_expense"], r["revenue"]) if model == "bank" else None}
            if prev:
                p_ic, p_ex, p_eq, p_tce = prev["ic"], prev["ic_ex"], prev["equity"], prev["tce"]
                if nopat is not None and ic and p_ic:
                    d["roic"] = nopat / ((ic + p_ic) / 2)
                if nopat is not None and ic_ex and p_ex and ic_ex > 0 and p_ex > 0:
                    d["roic_ex_goodwill"] = nopat / ((ic_ex + p_ex) / 2)
                if r["net_income"] and r["equity"] and p_eq:
                    d["roe"] = r["net_income"] / ((r["equity"] + p_eq) / 2)
                if r["net_income_common"] and tce and p_tce and tce > 0 and p_tce > 0:
                    d["rotce"] = r["net_income_common"] / ((tce + p_tce) / 2)
            prev = {"ic": ic, "ic_ex": ic_ex, "equity": r["equity"], "tce": tce}
            if model == "bank":
                d.update(fcf_m=None, fcf_margin=None, payout_of_fcf=None, capex_to_rev=None)
            derived.append(d)
    with open(os.path.join(OUT, "annual.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    with open(os.path.join(OUT, "derived.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(derived[0])); w.writeheader()
        for d in derived:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in d.items()})
    with open(os.path.join(OUT, "quarterly.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(qrows[0])); w.writeheader(); w.writerows(qrows)
    print(f"wrote {OUT}/annual.csv ({len(rows)} rows), derived.csv, quarterly.csv ({len(qrows)} rows)")


if __name__ == "__main__":
    main()
