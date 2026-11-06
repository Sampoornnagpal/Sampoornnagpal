# Updating this profile

The portrait in `README.md` is literal ASCII text, derived from the supplied portrait. Only the background characters have been replaced with spaces; the original framing and character positions are preserved. No portrait PNG, SVG, remote card or image embed is used.

## Change the profile

1. Edit `profile.json` to update project descriptions, links and the contribution highlight.
2. Run `python3 scripts/build_readme.py`.
3. Commit `profile.json` and the regenerated `README.md` together.

The generator uses only Python's standard library. The short hero copy and its line breaks live in the generator; update those alongside profile data when changing the hero.

## Portrait and layout

`assets/portrait.txt` keeps the supplied 140-column, 70-row grid. Only background characters were replaced with spaces. No rows were skipped, no columns were cropped, and no retained subject characters were changed or moved.

The art is HTML-escaped into a plain `pre` element, with the two surrounding `sub` elements restoring the display size used before the bold/crop edit. No bold styling is applied to the portrait. Keep each line the same width and use spaces rather than tabs when editing. Run the generator after changing the art. On narrow screens the table can scroll horizontally.

The contribution status is a verified highlight, not a live counter. Update it manually when choosing a different contribution to feature.
