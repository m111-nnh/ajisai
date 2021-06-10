#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import start_cotoha as c
#from pprint import pp

# 解析させる文
sentence = '今日も空は美しいでちゅ'

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
  {jsondata}
  </pre>
  </body>
</html>
'''[1:-1].format(title="たいとる",jsondata=response))