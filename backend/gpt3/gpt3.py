from backend.bot import Bot

import openai

class BotGPT3(Bot):
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
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
   	        temperature=0.7,
   	        max_tokens=512,
   	        top_p=1.0,
   	        frequency_penalty=0.0,
   	        presence_penalty=0.0
                )
            rep = (response['choices'][0]['text'])
        except Exception:
            return None
        else:
            return rep

    def _image(self, prompt):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=4,
                size="512x512"
                )
            rep = (response['data'])
        except Exception:
            return None
        else:
            return rep
    
    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

