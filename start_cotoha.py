import json
import requests

# https://api.ce-cotoha.com/home の
# Client ID って書いてあるところにあるやつ
client_id     = 'nfefVuEGdhtGAr0GeNrWB3ZGSbr2xiJo'
# Client Secret って書いてあるところにあるやつ
client_secret = 'bKyVYZKDt5iMMnoE'

# Access Token Publish URL って書いてあるところにあるやつ
url = 'https://api.ce-cotoha.com/v1/oauth/accesstokens'
# https://api.ce-cotoha.com/contents/reference.html の
# リファレンスにあるやつ。でも面倒だから書きたくないよね。
headers = {
    'Content-Type': 'application/json'
}
data = json.dumps({
    'grantType'   : 'client_credentials',
    'clientId'    : client_id,
    'clientSecret': client_secret
})
with requests.post(url, headers=headers, data=data) as req:
    response = req.json()

access_token = response['access_token']