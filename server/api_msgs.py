from pydantic import BaseModel

class MsgChatStart(BaseModel):
    bot_type:str
    settings:dict = None
    """
    setting is optional for advanced use:
    example:
    {
        "system": "you are a helpful assiant",  // field for chatgpt
        "model": "text-embedding-ada-002" // field for gpt embedding
    }

    """

class MsgChatEnd(BaseModel):
    session:str

class MsgChatAsk(BaseModel):
    session:str
    content:str
    timeout:int = 30 # [5,120]
