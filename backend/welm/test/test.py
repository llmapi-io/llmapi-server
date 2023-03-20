import json
import requests

def _make_post(url,content):
    try:
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer cfe7mpr2fperuifn5p8g'
        }
        res = requests.post(url, headers=headers,data = json.dumps(content))
        rep = res.json()
        return rep
    except Exception:
        return {'code':-1,'msg':'request failed'}


url = "https://welm.weixin.qq.com/v1/completions"
data = { "prompt":"你是谁", "model":"xl", "max_tokens":16, "temperature":0.8, "top_p":0.0, "top_k":10, "n":1, "echo":False, "stop":"。"}

res = _make_post(url,data)
print(res)
print(res['choices'][0]['text'])
