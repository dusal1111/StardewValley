# StardewValley

스타듀밸리 리텍

## 폰트

폰트 적용 방법: https://naver.me/xnOAcNS1

1. 폰트 다운로드
    - **Neo둥근**: https://neodgm.dalgona.dev/index.html
    - 
2. bitmap font generator 다운로드
    - https://www.angelcode.com/products/bmfont/
    - Neo둥근 폰트 선택
    - `Korean.fnt`: 30px, 모두 선택, 1024*976으로 함 (여러장)
    - `SpriteFont1.ko-KR.fnt`: 30px, KS1001.txt로 선택, 1024*1780 (1장)
    - `SmallFont.ko-KR.fnt`: 26px, KS1001.txt로 선택(2499개), 1024*1340 (1장)

3. 위의 카페 글에서 font parser 다운로드
    - 하라는대로 파일들 넣어서 변환 -> output에 결과물 나옴
    - xml 파일 열어서 연결된 파일명들 Korean_0x.xnb 로 바꾸기 (제로패딩 필요)

4. xnb <-> png 변환 프로그램 다운로드
    - https://github.com/LeonBlade/xnbcli/releases
    - 변환된 파일들 모두 unpacked에 넣어서 `pake.bat` 돌리면 packed에 결과물 나옴
    - Korean_x.xnb 파일들은 Korean_0x.xnb로 바꾸기 (제로패딩)

## 초상화