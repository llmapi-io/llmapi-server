from fastapi import FastAPI
from starlette.requests import Request

from utils.utils import get_logger

from server.config import SupportBotTyps
from server.errcode import StatusCode as sc
from server.api_msgs import *
from server.session import Session

import time
import asyncio
import logging

app = FastAPI()
sessions = {}
logger = get_logger('api_server',"logs/api_server.log",logging.INFO)

@app.post("/v1/chat/start")
async def _chat_start(msg:MsgChatStart, request:Request):
    bottype = msg.bot_type
    logger.info(f"chat start, ip:{request.client.host}, bot:{bottype}")
    if bottype not in SupportBotTyps:
        logger.error(f"bot type {bottype} not support")
        return {"code":sc.BOT_TYPE_INVALID.code,"msg":sc.BOT_TYPE_INVALID.msg}

    system = None
    model = None
    if msg.settings is not None:
        if 'system' in msg.settings:
            system = msg.settings['system']
            logger.info(f"system:{system}")
        if 'model' in msg.settings:
            model = msg.settings['model']
            logger.info(f"model:{model}")

    session = Session(bottype, model = model, system = system)
    sessions[session.get_id()] = session

    logger.info(f"get session {session.get_id()}")
    return {"code":sc.OK.code,"msg":sc.OK.msg,"session":f"{session.get_id()}"}

@app.post("/v1/chat/end")
async def _chat_end(msg:MsgChatEnd, request:Request):
    session_id = msg.session
    logger.info(f"chat end, ip:{request.client.host}, session:{session_id}")

    if session_id not in sessions:
        logger.error(f"session {session_id} not exist")
        return {"code":sc.SESSION_INVALID.code,"msg":sc.SESSION_INVALID.msg}

    del sessions[session_id]
    logger.info(f"del session {session_id}")
    return {"code":sc.OK.code,"msg":sc.OK.msg}


@app.post("/v1/chat/ask")
async def _chat_ask(msg:MsgChatAsk, request:Request):
    session_id = msg.session
    to = msg.timeout
    prompt = msg.content
    logger.info(f"chat ask, ip:{request.client.host}, session:{session_id}, timeout:{to}")
    if type(to) is int:
        to = 5 if to < 5 else to
        to = 120 if to > 120 else to
    else:
        to = 10
    to = time.time() + to

    if session_id not in sessions:
        logger.error(f"session {session_id} not exist")
        return {"code":sc.SESSION_INVALID.code,"msg":sc.SESSION_INVALID.msg}

    session = sessions[session_id]

    bot = session.get_bot()
    if bot is None:
        logger.error(f"chat ask,ip:{request.client.host},bot none")
        return {"code":sc.ERROR.code,"msg":sc.ERROR.msg}

    st = bot.input(prompt, history = session.get_history())
    if type(st) is not str:
        logger.warn(f"chat ask,ip:{request.client.host},sensitive")
        return {"code":sc.OK.code,"msg":sc.OK.msg,"reply":f"{st['sensitive']}","timestamp":time.time()}

    reply = bot.output(stub=st)
    while reply is None and time.time() < to:
        await asyncio.sleep(0.1)
        reply = bot.output(stub=st)

    if reply is None:
        logger.warn(f"chat ask,ip:{request.client.host},reply timeout")
        return {"code":sc.REPLY_TIMEOUT.code,"msg":sc.REPLY_TIMEOUT.msg}

    session.add_conversation(prompt, reply)
    resp = {"code":sc.OK.code,"msg":sc.OK.msg,"reply":f"{reply}","timestamp":time.time()}

    return resp

