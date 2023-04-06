import asyncio

from backend.chatgpt.chatgpt import BotChatGPT
from backend.gpt3.gpt3 import BotGPT3
from backend.mock.mock import BotMock
from backend.welm.welm import BotWelm
from backend.newbing.newbing import BotNewBing
from backend.chatgpt.embedding import BotGPTEmbedding
from backend.dalle.dalle import BotDALLE

class LLMBackend():
    def __init__(self, bottype = 'mock', **kwargs):
        if bottype == 'chatgpt':
            self.bot = BotChatGPT(**kwargs)
        elif bottype == 'gpt3':
            self.bot = BotGPT3(**kwargs)
        elif bottype == 'welm':
            self.bot = BotWelm(**kwargs)
        elif bottype == 'newbing':
            self.bot = BotNewBing(**kwargs)
        elif bottype == 'gpt-embedding':
            self.bot = BotGPTEmbedding(**kwargs)
        elif bottype == 'dall-e':
            self.bot = BotDALLE(**kwargs)
        else:
            self.bot = BotMock(**kwargs)

        self.bot_type = bottype

    def open(self, **kwargs):
        self.bot.open(**kwargs)
    def input(self, prompt, **kwargs):
        return self.bot.input(prompt=prompt, **kwargs)
    def output(self, **kwargs):
        return self.bot.output(**kwargs)
    def reset(self, **kwargs):
        self.bot.reset(**kwargs)
    def close(self, **kwargs):
        self.bot.close(**kwargs)
