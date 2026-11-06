#!/usr/bin/env python3
"""Build the profile around the user's cleaned ASCII portrait."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build():
    p = json.loads((ROOT / 'profile.json').read_text())
    portrait = (ROOT / 'assets/portrait.txt').read_text()
    lines = portrait.splitlines()
    if not portrait.isascii() or any('\t' in line for line in lines):
        raise ValueError('The portrait must contain ASCII text with spaces, not tabs.')
    if len(set(map(len, lines))) != 1:
        raise ValueError('Every portrait row must have the same width.')
    e = lambda value: escape(str(value), quote=True)
    contribution = p['contribution']
    org = p['organization']
    # Preserve the original grid and the previous display size. Background
    # removal changes only characters outside the subject to spaces.
    readme = f'''<p><samp>~/Sampoornnagpal &nbsp; $ whoami</samp></p>

<table>
<tr>
<td valign="top">
<sub><sub><pre>{escape(portrait, quote=False)}</pre></sub></sub>
</td>
<td valign="middle">
<h2>{e(p['name'])}</h2>
<p>Building AI tools.<br>Testing how they behave.</p>
<p><samp>FOCUS</samp><br><b>AI agents &amp;<br>evaluation</b></p>
<p><samp>LANGUAGES</samp><br>Python · JavaScript<br>Swift</p>
<p><samp>WORKING WITH</samp><br>FastAPI · React<br>SwiftUI · DeepEval</p>
<p><samp>EXPLORING</samp><br>RAG · MCP<br>Agent memory</p>
<p><samp>OPEN SOURCE</samp><br>NVIDIA NeMo<br><a href="{e(contribution['url'])}">Merged contribution ↗</a></p>
<p><a href="{e(org['url'])}">{e(org['name'])} ↗</a></p>
</td>
</tr>
</table>

### Selected work

| Project | What I'm building | Tools |
| :--- | :--- | :--- |
'''
    for project in p['projects']:
        link = f"**[{project['name']}]({project['url']})**"
        if 'secondary_url' in project:
            link += f"<br>[iOS]({project['url']}) · [Android]({project['secondary_url']})"
        readme += f"| {link} | {project['summary']} | {project['stack']} |\n"
    readme += f'''
### Open source

**[{contribution['repository']} #{contribution['number']}]({contribution['url']}) · {contribution['status']}**  
{contribution['summary']}

---

<p align="center"><samp>{e(p['approach'])}</samp></p>
'''
    (ROOT / 'README.md').write_text(readme)
    print(f'Built README.md with the original {len(lines)} × {len(lines[0])} ASCII grid.')

if __name__ == '__main__':
    build()
