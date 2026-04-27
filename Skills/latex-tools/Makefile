# LaTeX 构建系统
# 用法: make [target]

# 配置
LATEX = pdflatex
BIBTEX = bibtex
OUTPUT_DIR = output
SOURCES = $(wildcard *.tex)

# 默认目标
.PHONY: all clean product-pdf product-pdf-all help

all: help

help:
	@echo "LaTeX 构建系统"
	@echo "==================="
	@echo "make product-pdf     - 编译所有专题讲义 tex → pdf"
	@echo "make product-pdf-all - 编译所有 tex 文件"
	@echo "make clean           - 清理编译产物"
	@echo "make help            - 显示帮助"

# 编译单个 tex 文件
%.pdf: %.tex
	@echo "正在编译 $< ..."
	@mkdir -p $(OUTPUT_DIR)
	$(LATEX) -output-directory=$(OUTPUT_DIR) $<
	@echo "✅ 已生成: $(OUTPUT_DIR)/$(basename $<).pdf"

# 编译所有专题讲义
product-pdf:
	@echo "正在编译所有专题讲义 ..."
	@mkdir -p $(OUTPUT_DIR)
	@find ../20-Product/专题讲义/AI生成 -name "*.tex" | while read tex; do \
		cd $$(dirname $$tex) && \
		$(LATEX) -output-directory=../../$(OUTPUT_DIR) $$(basename $$tex) && \
		echo "✅ $$(basename $$tex)"; \
	done
	@echo "✅ 所有专题讲义编译完成!"

# 编译所有 tex 文件
product-pdf-all:
	@echo "正在编译所有 tex 文件 ..."
	@mkdir -p $(OUTPUT_DIR)
	@for tex in $(SOURCES); do \
		echo "正在编译 $$tex ..."; \
		$(LATEX) -output-directory=$(OUTPUT_DIR) $$tex; \
	done
	@echo "✅ 所有文件编译完成!"

# 清理编译产物
clean:
	@echo "正在清理编译产物 ..."
	@rm -rf $(OUTPUT_DIR)
	@rm -f *.aux *.log *.out *.toc *.bbl *.blg
	@echo "✅ 清理完成!"
