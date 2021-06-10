#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import start_cotoha as c
#from pprint import pp

sentence = '今日も天気が良いですね。'

# 解析させる文
url = 'https://api.ce-cotoha.com/api/dev/nlp/beta/user_attribute'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': f'Bearer {c.access_token}'
}
data = c.json.dumps({
    'document': sentence
})
with c.requests.post(url, headers=headers, data=data) as req:
    response = req.json()

# 辞書を見やすく整形して出力
#pp(response)

res = {}
for k in ['age','civilstatus']:
  if k in response['result'].keys():
    res[k] = response['result'][k]
  else:
    res[k] = ''

civil = '未婚'

print('''
Content-type: text/html

<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
  <h1 style="color:red">{title}</h1>
  <pre>
  あなたはこんな人ですか？
  年齢：{age}
  結婚歴：{civil}
  </pre>
  </body>
</html>
'''[1:-1].format(title="たいとる",age=res['age'], civil=res['civilstatus']))