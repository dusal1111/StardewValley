import json
import os

path = "SmallFont.ko-KR.json"

Y_OFFSET = 4 # 여기를 수정

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

cropping = data["content"]["cropping"]

for crop in cropping:
    crop["y"] += Y_OFFSET

name, ext = os.path.splitext(path)
output_path = name + f"_y+{Y_OFFSET}" + ext

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"완료: {output_path}")