#!/usr/bin/env python3
"""Build a text-only GitHub profile README from stored ASCII and profile data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build():
    profile = json.loads((ROOT / 'profile.json').read_text())
    portrait = (ROOT / 'assets/portrait.txt').read_text().splitlines()
    if not portrait or any(not row.isascii() for row in portrait):
        raise ValueError('The portrait must use ordinary ASCII characters.')
    width = max(map(len, portrait))
    bio = {
        2: profile['name'],
        3: '@' + profile['username'],
        4: '-' * 28,
        6: 'Focus',
        7: profile['focus'],
        10: 'Stack',
        11: profile['languages'],
        12: profile['frameworks'],
        15: 'Exploring',
        16: profile['exploring'],
        19: 'Projects',
        20: profile['projects'][0]['name'],
        21: profile['projects'][1]['name'],
        22: 'RescueMesh (iOS + Android)',
        25: 'Approach',
        26: profile['approach'],
        29: 'GitHub',
        30: 'github.com/' + profile['username'],
    }
    lines = [f'{row:<{width}}   {bio.get(i, "")}'.rstrip() for i, row in enumerate(portrait)]
    if max(map(len, lines)) > 96:
        raise ValueError('Keep lines within 96 characters for the GitHub profile layout.')
    if any('```' in line for line in lines):
        raise ValueError('A line would terminate the Markdown code fence.')
    readme = '```text\n' + '\n'.join(lines) + '\n```\n\n'
    readme += '''[Agent Evaluation](https://github.com/Sampoornnagpal/Agent-Evaluation) · [AI Cowork](https://github.com/Sampoornnagpal/coworkAI) · [RescueMesh iOS](https://github.com/Sampoornnagpal/RescueMesh_iOS) · [RescueMesh Android](https://github.com/Sampoornnagpal/RescueMesh_Android)

<details>
<summary>About me · accessible text</summary>

I'm **Sampoorn Nagpal**. I build AI tools and explore how to evaluate agents and connect useful systems.

- **Agent Evaluation** — evaluation tools with FastAPI, React and DeepEval.
- **AI Cowork** — a team AI workspace with document RAG, MCP tools and an LLM gateway.
- **RescueMesh** — exploring emergency messaging over Bluetooth Low Energy.

My project stack includes **Python, JavaScript, Swift, FastAPI, React and SwiftUI**.

</details>
'''
    (ROOT / 'README.md').write_text(readme)
    print(f'Built README.md: {len(portrait)} portrait rows; maximum line width {max(map(len, lines))}.')

if __name__ == '__main__':
    build()
