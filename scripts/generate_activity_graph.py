#!/usr/bin/env python3
"""Generate assets/activity-graph.svg: last 31 days of GitHub contributions.

Uses only the Python standard library. Needs GH_TOKEN (the Action provides it).
Env: GH_USER (default: tassu1), GRAPH_TITLE (default: "Tahseen's Contribution Graph")
"""
import json, os, sys, urllib.request
from datetime import date, timedelta
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "tassu1")
TITLE = os.environ.get("GRAPH_TITLE", "Tahseen's Contribution Graph")
OUT = os.environ.get("GRAPH_OUT", "assets/activity-graph.svg")
DAYS = 31

QUERY = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    contributionsCollection(from:$from,to:$to){
      contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
    }
  }
}"""

def fetch(token):
    end = date.today()
    start = end - timedelta(days=DAYS - 1)
    body = json.dumps({"query": QUERY, "variables": {
        "login": USER,
        "from": f"{start}T00:00:00Z",
        "to": f"{end}T23:59:59Z"}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "activity-graph-script"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    days = {}
    for w in data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]:
        for d in w["contributionDays"]:
            days[d["date"]] = d["contributionCount"]
    out = []
    for i in range(DAYS):
        d = start + timedelta(days=i)
        out.append((d, days.get(d.isoformat(), 0)))
    return out

def render(series):
    W, H = 900, 320
    L, R, T, B = 62, 24, 62, 52
    pw, ph = W - L - R, H - T - B
    counts = [c for _, c in series]
    ymax = max(5, max(counts))
    step = 1 if ymax <= 6 else (2 if ymax <= 12 else (5 if ymax <= 30 else 10))
    ymax = ((ymax + step - 1) // step) * step
    n = len(series)
    xs = [L + pw * i / (n - 1) for i in range(n)]
    ys = [T + ph - ph * c / ymax for c in counts]

    g = []
    for v in range(0, ymax + 1, step):
        y = T + ph - ph * v / ymax
        g.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#ffffff" stroke-opacity=".12"/>')
        g.append(f'<text x="{L-10}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#fff">{v}</text>')
    for i, (d, _) in enumerate(series):
        g.append(f'<line x1="{xs[i]:.1f}" y1="{T}" x2="{xs[i]:.1f}" y2="{T+ph}" stroke="#ffffff" stroke-opacity=".06"/>')
        g.append(f'<text x="{xs[i]:.1f}" y="{T+ph+18}" text-anchor="middle" font-size="10" fill="#fff">{d.day}</text>')

    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    area = f"{xs[0]:.1f},{T+ph} {pts} {xs[-1]:.1f},{T+ph}"
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#fff"><title>{d}: {c}</title></circle>'
                   for x, y, (d, c) in zip(xs, ys, series))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="'Segoe UI', Ubuntu, Arial, sans-serif" role="img" aria-label="{escape(TITLE)}">
  <defs>
    <linearGradient id="a" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="6" fill="#000" stroke="#30363d"/>
  <text x="{W/2}" y="32" text-anchor="middle" font-size="16" font-weight="600" fill="#fff">{escape(TITLE)}</text>
  {''.join(g)}
  <polygon points="{area}" fill="url(#a)"/>
  <polyline points="{pts}" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  {dots}
  <text x="{L+pw/2}" y="{H-10}" text-anchor="middle" font-size="11" fill="#fff">Days</text>
  <text transform="translate(16 {T+ph/2}) rotate(-90)" text-anchor="middle" font-size="11" fill="#fff">Contributions</text>
</svg>
'''

if __name__ == "__main__":
    token = os.environ.get("GH_TOKEN")
    if token:
        series = fetch(token)
    else:  # offline placeholder (all zeros)
        today = date.today()
        series = [(today - timedelta(days=DAYS - 1 - i), 0) for i in range(DAYS)]
        print("GH_TOKEN not set: wrote empty placeholder", file=sys.stderr)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(series))
    print(f"wrote {OUT}")
