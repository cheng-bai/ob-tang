-- Pandoc Lua filter: render :::space ... ::: as writing lines in LaTeX output.

local function repeat_lines(n)
  local out = {}
  for _ = 1, n do
    table.insert(out, "\\noindent\\rule{\\linewidth}{0.2pt}\\\\[7.8mm]")
  end
  return table.concat(out, "\n")
end

function Div(el)
  if not el.classes:includes("space") then
    return nil
  end

  local lines = tonumber(el.attributes["data-lines"] or "3") or 3
  local latex = "\\vspace{1mm}\n" .. repeat_lines(lines) .. "\n\\vspace{1mm}\n"
  return pandoc.RawBlock("latex", latex)
end

