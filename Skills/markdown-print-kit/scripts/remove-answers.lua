-- remove-answers.lua - Pandoc Lua 过滤器
-- 移除 <!-- Answer ... --> 注释块中的内容

local in_answer = false

function Comment(el)
  -- 检查是否是答案块的开始或结束
  if el:match("^%s*Answer") then
    in_answer = true
    return {}  -- 移除 Answer 标记本身
  end
  if el:match("^%s*/Answer") then
    in_answer = false
    return {}  -- 移除 /Answer 标记本身
  end
  
  -- 如果在答案块内，移除所有注释
  if in_answer then
    return {}
  end
  
  -- 其他注释保留
  return el
end

function RawBlock(el)
  -- 处理 raw HTML 注释
  if el.format == "html" then
    local text = el.text
    if text:match("^%s*<!--%s*Answer") then
      in_answer = true
      return {}
    end
    if text:match("^%s*<!--%s*/Answer") then
      in_answer = false
      return {}
    end
    if in_answer then
      return {}
    end
  end
  return el
end
