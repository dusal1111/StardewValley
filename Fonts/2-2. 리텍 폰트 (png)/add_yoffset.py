import re

path = "Korean.xml"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

def repl(m):
    return f'yoffset="{int(m.group(1)) + 4}"'

text = re.sub(r'yoffset="(-?\d+)"', repl, text)

with open("Korean_modified.xml", "w", encoding="utf-8") as f:
    f.write(text)