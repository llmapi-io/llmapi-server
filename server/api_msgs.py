from pydantic import BaseModel

class MsgChatStart(BaseModel):
    bot_type:str

class MsgChatEnd(BaseModel):
    session:str

class MsgChatAsk(BaseModel):
    session:str
    content:str
    timeout:int = 30 # [5,120]
