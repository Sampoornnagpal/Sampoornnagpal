#!/usr/bin/env python3
"""Generate a GitHub-safe SVG terminal card from editable profile data and ASCII text."""
from pathlib import Path
from html import escape
import json
ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT / 'profile.json').read_text())
portrait = (ROOT / 'assets/portrait.txt').read_text().splitlines()
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc">',
'<title id="title">Sampoorn Nagpal — developer terminal profile</title>',
'<desc id="desc">ASCII portrait of Sampoorn beside his projects, stack and GitHub link.</desc>',
'<rect x="1" y="1" width="1198" height="758" rx="18" fill="#0d1117" stroke="#30363d" stroke-width="2"/>',
'<path d="M19 1H1181Q1199 1 1199 19V58H1V19Q1 1 19 1" fill="#161b22"/>',
'<path d="M1 58H1199" stroke="#30363d"/>']
for x, c in [(29,'#ff5f57'),(51,'#febc2e'),(73,'#28c840')]:
 parts.append(f'<circle cx="{x}" cy="29" r="6" fill="{c}"/>')
def text(x,y,s,size=18,color='#c9d1d9',weight='normal'):
 parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans Mono, Consolas, monospace" font-size="{size}" font-weight="{weight}" xml:space="preserve">{escape(s)}</text>')
text(600,35,'sampoorn@github: ~',14,'#8b949e')
text(32,94,'$ whoami',16,'#7ee787')
text(32,119,'Sampoorn Nagpal',20,'#f0f6fc','bold')
for i,row in enumerate(portrait):
 text(30,157+i*9.7,row,9.5,'#b9ddd4')
parts.append('<path d="M513 92V678" stroke="#21262d"/>')
text(549,100,'sampoorn@github',25,'#7ee787','bold')
text(549,128,'-----------------------------',18,'#484f58')
def field(y,k,v):
 text(549,y,k,17,'#79c0ff')
 text(686,y,v,17)
field(163,'Name',p['name'])
field(192,'Focus',p['focus'])
field(221,'Approach',p['approach'])
text(549,272,'// STACK',15,'#d2a8ff','bold')
field(307,'Languages',p['languages'])
field(336,'Frameworks',p['frameworks'])
field(365,'Exploring',p['exploring'])
text(549,416,'// PROJECTS',15,'#d2a8ff','bold')
for i,project in enumerate(p['projects']):
 y=452+i*56
 text(549,y,project['name'],18,'#f0f6fc','bold')
 text(549,y+23,project['summary'],15,'#8b949e')
text(549,645,'// CONNECT',15,'#d2a8ff','bold')
text(549,675,'github.com/'+p['username'],17,'#79c0ff')
for i,c in enumerate(['#ff7b72','#ffa657','#e3b341','#7ee787','#79c0ff','#d2a8ff']):
 parts.append(f'<rect x="{32+i*31}" y="686" width="27" height="12" rx="2" fill="{c}"/>')
parts.append('<path d="M1 719H1199" stroke="#30363d"/>')
text(28,745,'~/Sampoornnagpal',14,'#8b949e')
text(792,745,'build. evaluate. improve.',14,'#7ee787')
parts.append('</svg>')
(ROOT/'assets/profile.svg').write_text('\n'.join(parts))
print('Generated assets/profile.svg')
