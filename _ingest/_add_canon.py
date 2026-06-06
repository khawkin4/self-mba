#!/usr/bin/env python3
"""One-shot: add a book-keyed `canon` track to manifest.json (idempotent)."""
import json, os
P = os.path.join(os.path.dirname(__file__), "manifest.json")
m = json.load(open(P))

canon = {
  "strategy":                {"yt": ["Richard Rumelt good strategy bad strategy kernel", "Roger Martin playing to win strategy cascade"], "reddit": [{"sub": "strategy"}, {"sub": "consulting", "q": "strategy frameworks"}], "tickers": []},
  "leadership-presence":     {"yt": ["Andy Grove High Output Management leverage", "David Marquet turn the ship around intent"], "reddit": [{"sub": "leadership"}, {"sub": "managers"}], "tickers": []},
  "mental-models":           {"yt": ["Charlie Munger mental models latticework", "Kahneman thinking fast and slow system 1 2"], "reddit": [{"sub": "decisionmaking"}], "tickers": []},
  "org-design-mechanisms":   {"yt": ["Jeff Bezos shareholder letters mechanisms day 1", "Will Larson engineering management elegant puzzle"], "reddit": [{"sub": "ExperiencedDevs"}, {"sub": "managers"}], "tickers": []},
  "landscape-competitive":   {"yt": ["Clayton Christensen innovators dilemma disruption", "Hamilton Helmer 7 powers moat"], "reddit": [{"sub": "strategy"}], "tickers": []},
  "negotiation-influence":   {"yt": ["Robert Cialdini influence six principles persuasion", "Dale Carnegie how to win friends and influence people"], "reddit": [{"sub": "negotiation"}, {"sub": "sales"}], "tickers": []},
  "execution-operations":    {"yt": ["Goldratt theory of constraints the goal bottleneck", "4 disciplines of execution lead measures whirlwind"], "reddit": [{"sub": "operations"}], "tickers": []},
  "culture-change":          {"yt": ["Kotter 8 steps leading change", "Edgar Schein three levels of organizational culture"], "reddit": [{"sub": "managers"}], "tickers": []},
  "risk-fragility":          {"yt": ["Nassim Taleb antifragile explained", "Philip Tetlock superforecasting calibration"], "reddit": [{"sub": "decisionmaking"}], "tickers": []},
  "product-innovation":      {"yt": ["Eric Ries lean startup MVP build measure learn", "Marty Cagan inspired product discovery", "Peter Thiel zero to one monopoly"], "reddit": [{"sub": "ProductManagement"}], "tickers": []},
  "power-politics":          {"yt": ["Jeffrey Pfeffer power organizational", "48 laws of power Robert Greene summary"], "reddit": [{"sub": "cscareerquestions", "q": "office politics"}], "tickers": []},
  "personal-effectiveness":  {"yt": ["Cal Newport deep work", "James Clear atomic habits four laws"], "reddit": [{"sub": "productivity"}], "tickers": []},
  "financial-literacy":      {"yt": ["Seth Klarman margin of safety value investing", "Michael Mauboussin skill versus luck success equation"], "reddit": [{"sub": "SecurityAnalysis"}], "tickers": []},
  "behavioral-decision":     {"yt": ["Richard Thaler nudge choice architecture defaults", "Dan Ariely predictably irrational", "Gary Klein recognition primed decision making"], "reddit": [{"sub": "decisionmaking"}], "tickers": []},
  "game-theory":             {"yt": ["Dixit Nalebuff thinking strategically game theory", "Thomas Schelling focal point credible commitment", "Axelrod tit for tat evolution of cooperation"], "reddit": [{"sub": "gametheory"}], "tickers": []},
  "platform-strategy":       {"yt": ["platform business model network effects cold start", "two sided market subsidize which side pricing"], "reddit": [{"sub": "startups", "q": "network effects platform"}], "tickers": []},
  "systems-complexity":      {"yt": ["Peter Senge fifth discipline systems thinking archetypes", "beer game bullwhip effect supply chain", "Donella Meadows leverage points"], "reddit": [{"sub": "systemsthinking"}], "tickers": []},
  "information-communication": {"yt": ["Claude Shannon information theory explained", "Edward Tufte data visualization chartjunk", "crucial conversations skills summary"], "reddit": [{"sub": "dataisbeautiful"}], "tickers": []},
  "economics-incentives":    {"yt": ["Akerlof market for lemons asymmetric information", "principal agent problem agency theory explained"], "reddit": [{"sub": "AskEconomics"}], "tickers": []},
  "history-judgment":        {"yt": ["Graham Allison essence of decision three models", "Thucydides trap Athens Sparta Allison", "Clausewitz on war friction fog"], "reddit": [{"sub": "geopolitics"}], "tickers": []},
  "communication-storytelling": {"yt": ["Barbara Minto pyramid principle", "Nancy Duarte resonate presentation structure", "Simon Sinek start with why golden circle"], "reddit": [{"sub": "PublicSpeaking"}], "tickers": []},
  "design-problem-solving":  {"yt": ["Roger Martin integrative thinking opposable mind", "first principles thinking problem solving"], "reddit": [{"sub": "consulting"}], "tickers": []},
  "ethics-judgment":         {"yt": ["Michael Sandel justice what is the right thing to do", "right versus right ethical leadership decisions"], "reddit": [{"sub": "Ethics"}], "tickers": []},
}

m["canon"] = canon
json.dump(m, open(P, "w"), indent=2, ensure_ascii=False)
print(f"canon track written: {len(canon)} clusters, "
      f"{sum(len(v['yt']) for v in canon.values())} yt queries, "
      f"{sum(len(v['reddit']) for v in canon.values())} reddit pulls")
