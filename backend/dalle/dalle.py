from backend.bot import Bot

import json
import openai

class BotDALLE(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'api_key' in kwargs:
            openai.api_key = kwargs['api_key']

        self.status = "open"
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        try:
            response = openai.Image.create( prompt=prompt, n=1, size="1024x1024")
            rep = response['data'][0]['url']
        except Exception as e:
            print(e)
            return None
        else:
            return rep

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

