from pathlib import Path

html = Path('www/index.html').read_text()
icons = Path('scripts/generate_icons.py').read_text()

# Existing game identity and core flow stay intact.
assert '<h1>고양이퍼즐</h1>' in html
assert '쥐를 모두 찾아라. 폭탄은 안돼.' in html
assert '숨은 쥐' in html and '찾은 쥐' in html and '기억 시작' in html
assert '다시하기' in html and '다음 스테이지' in html

# Regression requirements for this patch.
assert '100dvh' in html
assert 'overflow:hidden' in html
assert 'max-height:100dvh' in html or 'height:100dvh' in html
assert 'MASTER_VOLUME' in html and '0.10' in html
assert 'remove_adaptive_icons' in icons
assert 'mipmap-anydpi-v26' in icons
assert 'ic_launcher.xml' in icons and 'ic_launcher_round.xml' in icons

print('verification passed')