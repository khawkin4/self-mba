#!/usr/bin/env python3
"""Add a 'gaps' track (Technical Foundations — the benchmark gap-fillers) to manifest.json."""
import json, os
P = os.path.join(os.path.dirname(__file__), "manifest.json")
m = json.load(open(P))
m["gaps"] = {
    "managerial-accounting": {"yt": ["Edspira managerial accounting CVP", "activity based costing", "variance analysis standard costing"], "reddit": [{"sub": "Accounting"}], "tickers": []},
    "statistics-quant":       {"yt": ["StatQuest hypothesis testing", "StatQuest linear regression", "business statistics regression forecasting"], "reddit": [{"sub": "statistics", "q": "hypothesis testing"}], "tickers": []},
    "marketing-strategy":     {"yt": ["April Dunford positioning", "Byron Sharp How Brands Grow", "segmentation targeting positioning STP", "CAC LTV unit economics"], "reddit": [{"sub": "marketing"}], "tickers": []},
    "information-systems":    {"yt": ["management information systems explained", "ERP enterprise systems", "relational database fundamentals", "data governance basics"], "reddit": [{"sub": "BusinessIntelligence"}], "tickers": []},
    "business-law":           {"yt": ["business law contracts", "intellectual property law business", "employment law managers", "antitrust law explained"], "reddit": [{"sub": "smallbusiness", "q": "legal contracts"}], "tickers": []},
}
json.dump(m, open(P, "w"), indent=2, ensure_ascii=False)
print("gaps track added:", list(m["gaps"].keys()))
