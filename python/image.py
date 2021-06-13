#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cv2, cgi, sys, io

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['food_img',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(入力なし)'

##### img = cv2.imread("C:/Users/Owner/Downloads/shiru1.jpeg")
# 「upload_img.html」から受け取った画像データ「food_img」を読み込み、img変数に格納
img = cv2.imread(r['food_img'])

# img変数に格納した画像データを指定したディレクトリに出力
img_name = "sample1.jpeg"
cv2.imwrite("image/{img_name}".format(img_name="img_name"), img)

print('''
Content-type: text/html

<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>画像アップロード完了</title>
</head>

<body>
<h1>画像を{img_name}の名前で保存しました。</h1>
</body>
</html>
'''[1:-1].format(img_name=img_name))