# Updating this profile

The portrait in `README.md` is literal ASCII text. `assets/portrait.txt` preserves the supplied 140-column, 70-row portrait exactly. No portrait PNG, SVG, remote card or image embed is used.

## Change the profile

1. Edit `profile.json` to update project descriptions, links and the contribution highlight.
2. Run `python3 scripts/build_readme.py`.
3. Commit `profile.json` and the regenerated `README.md` together.

The generator uses only Python's standard library. The short hero copy and its line breaks live in the generator; update those alongside profile data when changing the hero.

## Portrait and layout

The original art is HTML-escaped into a `pre` element in the Markdown file, which keeps every character and line break. Two surrounding `sub` elements reduce the entire portrait's type size, including its line height, so the full supplied art can sit beside the bio. GitHub supplies the monospace font. On narrow screens the table can scroll horizontally.

To replace the art, copy the new text into `assets/portrait.txt`, keep its rows equal in length, and run the generator. Do not resize, resample or regenerate the current portrait.

The contribution status is a verified highlight, not a live counter. Update it manually when choosing a different contribution to feature.
