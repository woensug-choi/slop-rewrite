# 한국어

This branch defaults to `ko`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## 한국어: review guidance

- 문서의 기존 높임 수준과 종결형을 유지한다. 해요체·합니다체·한다체를 이유 없이 섞지 않는다.
- 조사와 서술어의 호응, 의존 명사와 보조 용언의 띄어쓰기를 문맥으로 확인한다.
- 영어식 무생물 주어, 피동의 중복, 명사 나열을 줄이되 행위자가 불명확하면 지어 넣지 않는다.
- 군더더기 접속어를 덜고 절차의 순서와 조건을 드러낸다. 필요한 기술 용어는 쉬운 말로 무리하게 바꾸지 않는다.
- 가능·필수·권고·예정·미지원 및 부정 범위를 유지한다. “할 수 있다”를 사실 단정으로 바꾸지 않는다.
- 숫자·단위·코드·영문 식별자를 보존한다. 전문 문서의 명사형 목록은 장르에 맞으면 유지한다.
- 기존 한국어 검사기는 선택한 한국어 가이드에만 추가로 사용한다. 다른 언어에 한국어 규칙을 적용하지 않는다.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

이 기능은 혁신적인 방식으로 20개 표본을 기록합니다.

## Clear example

이 기능은 표본 20개를 기록합니다.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
