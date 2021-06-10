import start_cotoha as c
from pprint import pp

# 解析させる文
sentence = 'あの、えっと、今日も空は美しいです。そう、ほんとに、うん。'

url = 'https://api.ce-cotoha.com/api/dev/nlp/beta/remove_filler'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': f'Bearer {c.access_token}'
}
data = c.json.dumps({
    'text': sentence
})
with c.requests.post(url, headers=headers, data=data) as req:
    response = req.json()

# 辞書を見やすく整形して出力
pp(response)