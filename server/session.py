from utils.utils import get_short_hash
from server.config import GPT3_KEYS, CHATGPT_KEYS, WELM_KEYS, NEWBING_KEYS

from backend.backend import LLMBackend
from prepost.app import app_employ
from prepost.direct.direct import Direct

import json
import time
import random

class Session:
    class Conversations:
        def __init__(self) -> None:
            self.system = ""
            self.history = []
            self.total_len = 0
        def add_conversation(self, user, assistant):
            self.history.append([user, assistant])
            self.total_len += len(user) + len(assistant)
            while self.total_len > 500:
                self.pop_conversation()
        def pop_conversation(self):
            earliest = self.history.pop(0)
            self.total_len -= len(earliest[0]) + len(earliest[1])

    def __init__(self, bot_type, ts, nonce):
        self.bot_type = bot_type
        self.ts = ts
        self.nonce = nonce
        self.app = Direct()

        if bot_type == 'gpt3':
            key = GPT3_KEYS[random.randint(0,len(GPT3_KEYS) - 1)]
            self.bot = LLMBackend(bot_type,api_key = key)
        elif bot_type == 'chatgpt':
            key = CHATGPT_KEYS[random.randint(0,len(CHATGPT_KEYS) - 1)]
            self.bot = LLMBackend(bot_type,api_key = key)
        elif bot_type == 'welm':
            key = WELM_KEYS[random.randint(0,len(WELM_KEYS) - 1)]
            self.bot = LLMBackend(bot_type,api_key = key)
        elif bot_type == 'newbing':
            key = NEWBING_KEYS[random.randint(0,len(NEWBING_KEYS) - 1)]
            self.bot = LLMBackend(bot_type,api_key = key)
        else:
            self.bot = LLMBackend(bot_type)

        self.bot = app_employ(self.bot,self.app)

        info = json.dumps({"bot_type":self.bot_type, "timestamp":self.ts, "nonce":self.nonce})
        self.session_id = get_short_hash(info)
        self.conversations = self.Conversations()
        self.last_use = time.time()

    def get_id(self):
        self.last_use = time.time()
        return self.session_id
    def get_bot(self):
        self.last_use = time.time()
        return self.bot
    def add_conversation(self, user, assistant):
        self.last_use = time.time()
        self.conversations.add_conversation(user, assistant)
    def get_history(self):
        self.last_use = time.time()
        return self.conversations.history
