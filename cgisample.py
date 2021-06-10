#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'フォームデータ処理サンプルプログラム'

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['mymail', 'passcode',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(入力なし)'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
  <h1 style="color:red">{title}</h1>
  <dl>
    <dt>メールアドレス</dt><dd>{res1}</dd>
    <dt>パスコード</dt><dd>{res2}</dd>
  </body>
</html>
'''[1:-1].format(title=title_str,res1=r['mymail'],res2=r['passcode']))