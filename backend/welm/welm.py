import json
from backend.bot import Bot
import requests

def _make_welm_post(key, content):
    url = "https://welm.weixin.qq.com/v1/completions"
    try:
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {key}'
        }
        data = { "prompt":content, "model":"xl", "max_tokens":64, "temperature":0.8, "top_p":0.0, "top_k":10, "n":1, "echo":False, "stop":"。"}
        res = requests.post(url, headers=headers,data = json.dumps(data))
        rep = res.json()
        return rep
    except Exception:
        return None


class BotWelm(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'api_key' in kwargs:
            self.api_key = kwargs['api_key']
        self.status = "open"
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        try:
            res = _make_welm_post(self.api_key,prompt)
            if res is not None:
                rep = (res['choices'][0]['text'])
                return rep
            else:
                return None
        except Exception:
            return None

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

