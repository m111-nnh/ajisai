import start_cotoha as c
from pprint import pp

# 解析させる文
sentence = '今日も空は美しいです。'

url = 'https://api.ce-cotoha.com/api/dev/nlp/v1/sentiment'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': f'Bearer {c.access_token}'
}
data = c.json.dumps({
    'sentence': sentence
})
with c.requests.post(url, headers=headers, data=data) as req:
    response = req.json()

# 辞書を見やすく整形して出力
pp(response)