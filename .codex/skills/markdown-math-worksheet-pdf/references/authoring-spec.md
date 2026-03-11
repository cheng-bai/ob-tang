# Authoring Spec

## Question Block Contract

Use this sequence under each `### 例 x.x` heading:

1. `**题目**：...`
2. Optional choices as four vertical lines:
A. ...
B. ...
C. ...
D. ...
3. Space marker block:
`:::space type=<mc|fill|solve> level=<A|B|C> lines=<n>`
`:::`
4. Hidden solution block:
`<!-- **答案**：...`
`**解析**：... -->`

## Space Mapping

- `mc`: A=2, B=3, C=3
- `fill`: A=2, B=3, C=4
- `solve`: A=6, B=8, C=10

## Content Hygiene

- Keep choices vertical; avoid inline A/B/C/D.
- Avoid extra blank lines inside a question block.
- Keep formulas in `$...$` or `$$...$$`.
