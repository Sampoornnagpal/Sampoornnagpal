# Updating this profile

The portrait in `README.md` is literal ASCII text, derived from the supplied portrait. Its background characters have been removed and its framing focuses on the head and shoulders. No portrait PNG, SVG, remote card or image embed is used.

## Change the profile

1. Edit `profile.json` to update project descriptions, links and the contribution highlight.
2. Run `python3 scripts/build_readme.py`.
3. Commit `profile.json` and the regenerated `README.md` together.

The generator uses only Python's standard library. The short hero copy and its line breaks live in the generator; update those alongside profile data when changing the hero.

## Portrait and layout

`assets/portrait.txt` stores the cleaned 79-column, 32-row portrait. The face and hair use characters from the supplied ASCII art. Background characters were replaced with spaces, and the view was cropped to the head and shoulders. Repeated shading rows were omitted to compensate for GitHub's tall monospace line spacing and keep the face's proportions closer to the photo.

The art is HTML-escaped into a bold `pre` element at GitHub's native code size. Keep each line the same width and use spaces rather than tabs when editing. Run the generator after changing the art. On narrow screens the table can scroll horizontally.

The contribution status is a verified highlight, not a live counter. Update it manually when choosing a different contribution to feature.
