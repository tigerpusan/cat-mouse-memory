from pathlib import Path
s=Path('www/index.html').read_text()
assert '<h1>고양이퍼즐</h1>' in s
assert '쥐를 모두 찾아라. 폭탄은 안돼.' in s
assert '숨은 쥐' in s and '찾은 쥐' in s and '기억 시작' in s
assert '타이머' in s or '남은 시간' in s
assert 'cheese' in s and '🧀' in s
assert 'bombs:3' in s and 'bombs:22' in s
assert '{grid:5' in s and '{grid:6' in s and '{grid:7' in s and '{grid:8' in s
assert 'timeLimit:12' in s
assert 'playTone' in s
assert '다시하기' in s and '다음 스테이지' in s
assert '난이도 높은 데모' not in s
assert '보너스' not in s
print('verification passed')