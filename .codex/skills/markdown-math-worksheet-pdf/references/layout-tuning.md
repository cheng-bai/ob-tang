# Layout Tuning

## Common Tweaks

- Increase worksheet looseness: raise `\baselinestretch` and `\parskip` in `assets/header.tex`.
- Increase writable area: increase `lines` in `:::space ...` blocks.
- Reduce page count: reduce `lines` values and heading paddings.

## Font Strategy

- Primary CJK text font defaults to `Songti SC`.
- If unavailable or glyph warnings appear, switch `\setCJKmainfont` in `assets/header.tex`.

## Pagination

- Use `\Needspace` before `\subsection` to reduce ugly breaks.
- Keep question headings compact and visually distinct.
