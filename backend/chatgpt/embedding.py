from backend.bot import Bot

import json
import openai

class BotGPTEmbedding(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.support_models = ["text-embedding-ada-001","text-embedding-ada-002"]
        if 'api_key' in kwargs:
            openai.api_key = kwargs['api_key']
        if 'model' in kwargs and kwargs['model'] is not None:
            self.model = kwargs['model']
        else:
            self.model = "text-embedding-ada-002"
        if self.model not in self.support_models:
            self.model = "text-embedding-ada-002"

        self.status = "open"
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        try:
            prompt = prompt.replace("\n", " ")
            response = openai.Embedding.create(model=self.model, input=prompt)
            rep = json.dumps(response['data'][0]['embedding'])
        except Exception as e:
            print(e)
            return None
        else:
            return rep

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

