import re

path = "Korean.xml"
Y_OFFSET = 7 # 여기 수정 (글씨 내리기)
LINE_HEIGHT = 36 # 여기 수정 (줄간격)

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

def repl(m):
    return f'yoffset="{int(m.group(1)) + Y_OFFSET}"'

text = re.sub(r'yoffset="(-?\d+)"', repl, text)
text = re.sub(r'lineHeight="\d+"', f'lineHeight="{LINE_HEIGHT}"', text, count=1)

with open("Korean_modified.xml", "w", encoding="utf-8") as f:
    f.write(text)
