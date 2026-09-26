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
    - `Korean.fnt`
        - 폰트 사이즈: 30px
        - 적용 폰트: 모두 선택
        - 이미지 사이즈: 1024*740 (12장)
        - **이미지 사이즈 조절해서 딱 12장을 만들어야함**
    - `SmallFont.ko-KR.fnt`
        - 폰트 사이즈: 26px
        - 적용 폰트: 한글모두+라틴기본+일반문장부호
        - 이미지 사이즈: 4096*2048 (1장)
    - `SpriteFont1.ko-KR.fnt`
        - 폰트 사이즈: 30px
        - 적용 폰트: 한글모두+라틴기본+일반문장부호
        - 이미지 사이즈: 4096*2048 (1장)

3. 위의 카페 글에서 font parser 다운로드
    - 하라는대로 파일들 넣어서 변환 -> output에 결과물 나옴
    - **SmallFont 랑 SpriteFont .json 파일 열어서 `hidef:true` 로 변경**
    - **파이썬 파일 돌려서 Korean의 yoffset +4 해주기**

4. xnb <-> png 변환 프로그램 다운로드
    - https://github.com/LeonBlade/xnbcli/releases
    - 변환된 파일들 모두 unpacked에 넣어서 `pack.bat` 돌리면 packed에 결과물 나옴

## 초상화