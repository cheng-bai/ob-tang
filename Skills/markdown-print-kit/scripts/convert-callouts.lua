-- convert-callouts.lua - Pandoc Lua 过滤器
-- 从 callout 中提取行数，添加到 data-lines 属性

local function extract_lines(el)
  local lines = 3  -- 默认行数
  if el.t == "BulletList" then
    for _, listitem in ipairs(el.content) do
      for _, para in ipairs(listitem.content) do
        local text = pandoc.utils.stringify(para)
        if text:match("^行数：([0-9]+)") then
          lines = tonumber(text:match("^行数：([0-9]+)")) or lines
        end
      end
    end
  end
  return lines
end

function Div(el)
  if el.classes:includes("blank") then
    local lines = 3
    for _, item in ipairs(el.content) do
      lines = extract_lines(item)
    end
    el.attributes["data-lines"] = tostring(lines)
    return el
  end
  return nil
end
