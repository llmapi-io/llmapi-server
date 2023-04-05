from backend.bot import Bot

import openai

class BotChatGPT(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.support_models = ["gpt-3.5-turbo"]
        if 'api_key' in kwargs:
            openai.api_key = kwargs['api_key']
        if 'system' in kwargs and kwargs['system'] is not None:
            self.system = kwargs['system']
        else:
            self.system = 'You are a helpful assistant.'

        if 'model' in kwargs and kwargs['model'] is not None:
            self.model = kwargs['model']
        else:
            self.model = "gpt-3.5-turbo"
        if self.model not in self.support_models:
            self.model = "gpt-3.5-turbo"

        self.status = "open"
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        try:
            messages=[]
            messages.append({'role': 'system', 'content': self.system})
            for h in history:
                messages.append({'role': 'user', 'content': h[0]})
                messages.append({'role': 'assistant', 'content': h[1]})
            messages.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(model=self.model, messages=messages)
            rep = (response['choices'][0]['message']['content'])
        except Exception as e:
            print(e)
            return None
        else:
            return rep

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

