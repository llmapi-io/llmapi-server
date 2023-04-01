from backend.bot import Bot
import time

class BotMock(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = "open"
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        time.sleep(1)
        return "Mock reply for your prompt:" + prompt

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"

