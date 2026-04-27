.PHONY: index audit search lesson exam polish-md

index:
	python3 pipeline/utils/更新索引.py --verbose

audit:
	python3 pipeline/utils/更新索引.py --verbose

search:
	python3 pipeline/utils/检索.py "$(keyword)"

lesson:
	python3 pipeline/build/备课.py --book "$(book)" --chapter "$(chapter)" --output "$(output)"

exam:
	python3 pipeline/build/组卷.py --知识点 "$(topic)" --数量 "$(count)" --输出 "$(output)"

polish-md:
	python3 pipeline/build/润色试卷MD.py --input "$(input)" --output "$(output)"
