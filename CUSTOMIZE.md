# Maintaining this profile

This is the profile repository for `Sampoornnagpal`. GitHub shows the root `README.md` on the account profile while this repository is public.

## Edit the card

1. Edit `profile.json` to change the bio, stack or project descriptions.
2. Run `python3 scripts/build_profile.py` from this repository.
3. Commit both `profile.json` and the regenerated `assets/profile.svg`.

The generator uses only Python's standard library. Text is XML-escaped. Keep values within the existing line lengths so they fit the card. Project links and the accessible text version are maintained in `README.md` separately.

`assets/portrait.txt` is real ASCII text derived from the supplied portrait. The SVG renders it as text on a fixed grid. The original photo is not required to display or regenerate the card.

The card needs no external image service, JavaScript, API key or scheduled workflow. The profile is intentionally static; it does not display live GitHub counts.
