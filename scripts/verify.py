from pathlib import Path

html = Path('www/index.html').read_text()
icons = Path('scripts/generate_icons.py').read_text()

# Game identity and core flow.
assert '<h1>고양이퍼즐</h1>' in html
assert '쥐를 모두 찾아라. 폭탄은 안돼.' in html
assert '숨은 쥐' in html and '찾은 쥐' in html and '기억 시작' in html
assert '다시하기' in html and '게임 단계' in html

# Current UX requirements.
assert '퍼즐 단계' in html
assert '퍼즐이 열릴 때 쥐와 폭탄의 위치를 기억하세요.' in html
assert '다음 단계로 이동합니다.' in html
assert '다음 스테이지' not in html

# Three-puzzle stage progression.
assert '퍼즐맞추기' in html
assert 'PUZZLES_PER_STAGE=3' in html
assert 'puzzleRound' in html
assert '퍼즐맞추기 ${puzzleRound} / ${PUZZLES_PER_STAGE}' in html
assert 'puzzleRound<PUZZLES_PER_STAGE' in html

# Android bottom safe-area / home gesture overlap protection.
assert 'safe-area-inset-bottom' in html
assert 'padding-bottom:calc(' in html

# Regression requirements.
assert '100dvh' in html
assert 'overflow:hidden' in html
assert 'max-height:100dvh' in html or 'height:100dvh' in html
assert 'MASTER_VOLUME' in html and '0.10' in html
assert 'remove_adaptive_icons' in icons
assert 'mipmap-anydpi-v26' in icons
assert 'ic_launcher.xml' in icons and 'ic_launcher_round.xml' in icons

print('verification passed')
