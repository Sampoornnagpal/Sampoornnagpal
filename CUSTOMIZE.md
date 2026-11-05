# Maintaining this profile

The portrait and terminal-style bio are actual text inside a fenced code block in `README.md`. There are no image embeds, SVGs, external widgets, custom fonts or runtime services.

## Change the profile details

1. Edit `profile.json`.
2. Run `python3 scripts/build_readme.py`.
3. Commit `profile.json` and the regenerated `README.md` together.

The generator uses only Python's standard library. It enforces a 96-character line limit and reads the portrait from `assets/portrait.txt`. Project links and the accessible text section are defined in the generator.

## Portrait

`assets/portrait.txt` contains ordinary printable ASCII characters and spaces. It was derived from Sampoorn's supplied photograph using a close face crop, local contrast adjustment, and character densities calibrated to a monospace font. The original photograph is not stored in this repository.

To change the art, edit `assets/portrait.txt` and run the generator again. Its rows must stay aligned; use a monospace editor and spaces instead of tabs. The current portrait is 63 columns by 36 rows.

GitHub renders the code block as selectable text in its own monospace font. The exact appearance varies slightly with the viewer's operating system and theme. On narrow mobile screens the code block can scroll horizontally.
