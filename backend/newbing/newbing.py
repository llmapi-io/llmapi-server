import asyncio
import json
from backend.bot import Bot

from EdgeGPT import Chatbot, ConversationStyle

class BotNewBing(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(kwargs['api_key'], 'r') as f:
            cookies = json.load(f)
        self.client = Chatbot(cookies=cookies)
        self.status = "open"

    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        try:
            rep = asyncio.run(self.client.ask(prompt=prompt, conversation_style=ConversationStyle.precise))
            rep = rep['item']['messages'][-1]['text']
        except Exception:
            return None
        else:
            return rep

    def reset(self, **kwargs):
        self.client.reset()

    def close(self, **kwargs):
        asyncio.run(self.client.close())
        self.status = "close"

