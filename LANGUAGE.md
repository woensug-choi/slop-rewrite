# 中文

This branch defaults to `zh`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## 中文: review guidance

- 保留原文的简体或繁体及地区用词，不自动转换字形。
- 检查主谓搭配、量词、指代和长定语的位置，避免照搬英语句法。
- 删除空泛的引导语、重复说明和没有依据的宣传语，保留必要的技术术语。
- 区分可以、必须、建议、预计、尚未支持及否定范围，不把可能性改成承诺。
- 中文标点与原文保持一致；代码、路径、公式、数值和 API 标识符不做全角或半角替换。
- 保持主题衔接，不为每句话机械添加主语或连接词。
- 不按空格数判断词数或句长；在不破坏条件、步骤和因果关系的前提下拆分长句。

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

值得注意的是，求解器会记录20个样本。

## Clear example

求解器会记录20个样本。

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
