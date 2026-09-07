from pathlib import Path
s=Path('www/index.html').read_text()
assert '<h1>고양이퍼즐</h1>' in s
assert '쥐를 모두 찾아라. 폭탄은 안돼.' in s
assert '숨은 쥐' in s and '찾은 쥐' in s and '기억 시작' in s
assert '난이도 높은 데모' not in s
assert '격자' not in s and '남은 오답' not in s
assert '치즈' not in s and '보너스' not in s
assert '다시하기' in s and '다음 스테이지' in s
assert 'STAGES' in s and '{grid:5,mice:3,bombs:1' in s
print('verification passed')
