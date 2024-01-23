# -*- coding: utf-8 -*-

import re
import sys, importlib
import json, copy
import time
from typing import Dict, List
import pytz
import logging
import asyncio
import contextlib
import g4f
import EdgeGPT.EdgeGPT as EdgeGPT

# import py3langid as langid


from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from datetime import time as datetime_time

from BingImageCreator import ImageGenAsync

from pyrogram import Client, filters,enums 
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineQueryResultPhoto, InlineQueryResultArticle, InputTextMessageContent, \
    InputMediaPhoto

from config import BAD_CONFIG_ERROR, API_ID, API_KEY, BOT_TOKEN, ALLOWED_USER_IDS, SUPER_USER_IDS, COOKIE_FILE, \
    PROXY_BING, NOT_ALLOW_INFO, BOT_NAME, SUGGEST_MODE, DEFAULT_CONVERSATION_STYLE_TYPE, RESPONSE_TYPE, STREAM_INTERVAL, \
    LOG_LEVEL, LOG_TIMEZONE


import requests
from pyrogram import Client, filters
from io import BytesIO
import random


#AuthorCSR
"""
AdvChatGptBot

which supports the following commands:


"""




global stk_list
stk_list = ["...", "...."]
global STCLOGO
STCLOGO ="https://graph.org/file/5d3d030e668795f769e20.mp4"

global CSRLOG
global CSRPVT
global FGRP
global OCR_KEY
OCR_KEY = "K85263696288957"
FGRP = -1001859478637
CSRPVT=[5124529069]
global STCLOG
STCLOG= -1001793856405
#1001927160194
CSRLOG=-1001793856405
ALLOWED_GROUP_ID = [-1001896039575,-1001751527173,-1001986466657]
PROMO ="\n\n||**ᴘᴏᴡᴇʀᴇᴅ ʙʏ  @EvaFires**||"
global ADMIN
ADMIN =[]
global PREMIUM
PREMIUM=[]
global lis
lis=[]
lis=ADMIN+PREMIUM
global FCRMSG
FCRMSG= """ᴅᴇᴀʀ  {mention},
[ʏᴏᴜ ᴀʀᴇ ᴀʙᴏᴜᴛ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴍᴏꜱᴛ ᴀᴡᴇꜱᴏᴍᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴅᴏɴ'ᴛ ʜᴇꜱɪᴛᴀᴛᴇ, ᴊᴜꜱᴛ ᴄʟɪᴄᴋ ʜᴇʀᴇ! ](https://t.me/AdvAIWorld)\n\n**ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ ꜱᴇɴᴅ ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ**\nɴᴏᴛᴇ : ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ᴏᴜʀ ʙᴏᴛ ꜱᴇᴀᴍʟᴇꜱꜱʟʏ.
"""
global welcome_message
global vocpre
vocpre=[5124529069]
global vcpre
vcpre={}
global img
img={}

sudo=[2094662246,1677130304,5124529069,5293138954]

global rlink
rlink="https://t.me/AdvAIWorld"

waitmsg="ᴡᴇ ᴀʀᴇ ᴛʀʏɪɴɢ ᴛᴏ ʙʀɪɴɢ ʏᴏᴜʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ʙᴇ ᴄᴀʟᴍ...."


welcome_message = """ ɢʀᴇᴇᴛɪɴɢꜱ {mention} : ꜰʀᴏᴍ ᴀᴅᴠᴀɴᴄᴇ ᴄʜᴀᴛ ɢᴘᴛ. 

ʏᴏᴜʀ ᴀɪ ᴀꜱꜱɪꜱᴛᴀɴᴛ. ᴡɪᴛʜ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ʟᴀɴɢᴜᴀɢᴇ ᴇxᴘᴇʀᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴄʜᴀᴛɢᴘᴛ-4

ᴀꜱᴋ ᴍᴇ ᴀɴʏᴛʜɪɴɢ ɪɴ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ, ᴀɴᴅ ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ɪɴꜱɪɢʜᴛꜰᴜʟ ᴀɴꜱᴡᴇʀꜱ ᴡɪᴛʜ ʙᴇꜱᴛ ᴏꜰ ᴍʏ ᴀʙɪʟɪᴛɪᴇꜱ :)

ᴀꜱᴋ ᴍᴇ ᴀɴʏᴛʜɪɴɢ :

• ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴛᴇxᴛ ᴏʀ ᴠᴏɪᴄᴇ ʀᴇQᴜᴇꜱᴛ ʏᴏᴜ'ʟʟ ɢᴇᴛ ʀᴇꜱᴘᴏɴꜱᴇ ʙᴀᴄᴋ ᴡɪᴛʜɪɴ ᴀ ꜰᴇᴡ ꜱᴇᴄᴏɴᴅꜱ. 

• ꜰᴏʀ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴜꜱᴇ [ /image ] ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ʏᴏᴜ'ʟʟ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ɪᴍᴀɢᴇ! 

ꜰᴏʀ ᴍᴏʀᴇ ꜱᴜᴄʜ ꜰᴇᴀᴛᴜʀᴇꜱ ᴋɪɴᴅʟʏ ɢᴏ ᴛʜʀᴏᴜɢʜ ꜰʀᴏᴍ "ᴡʜᴀᴛ ᴀʟʟ ɪ ᴄᴀɴ ᴅᴏ" 

**ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @AdvAIWorld**
"""

global help_message

help_message = """
**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴅᴀꜱʜʙᴏᴀʀᴅ!**

**ᴘʀɪᴠᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅ:**
- **ᴛᴇxᴛ:** ꜱɪᴍᴘʟʏ ꜱᴇɴᴅ ᴍᴇ ᴛᴇxᴛ ɪɴ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ.
- **ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ Qᴜᴇʀɪᴇꜱ:** ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ɪᴍᴀɢᴇ.

**ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅ:**
- **ᴛᴇxᴛ:** ᴜꜱᴇ ᴀ ᴘᴇʀɪᴏᴅ (.) ʙᴇꜰᴏʀᴇ ʏᴏᴜʀ Qᴜᴇʀʏ (ᴇ.ɢ., `.Where is india ?`).
- **ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ Qᴜᴇʀɪᴇꜱ:** ꜰɪʀꜱᴛ, ꜱᴇɴᴅ ᴛʜᴇ ɪᴍᴀɢᴇ, ᴛʜᴇɴ ʀᴇᴘʟʏ ᴡɪᴛʜ /answer ᴛᴏ ᴛʜᴀᴛ ɪᴍᴀɢᴇ.

**ᴄᴏᴍᴍᴏɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʙᴏᴛʜ ᴍᴏᴅᴇꜱ:**
- **ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ:** ᴜꜱᴇ /image (ᴇ.ɢ., `/image cute cats`). [ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱ ᴏɴʟʏ]

- **ɪɴʟɪɴᴇ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ:** ᴜꜱᴇ @ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ_ʙᴏᴛ ɢ ʏᴏᴜʀᴘʀᴏᴍᴘᴛ % (ᴇ.ɢ., `@AdvChatGpt_bot g cute cats %`).

- **ᴠᴏɪᴄᴇ-ʙᴀꜱᴇᴅ Qᴜᴇʀɪᴇꜱ:** ꜱɪᴍᴘʟʏ ꜱᴇɴᴅ ᴀ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ. [ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱ ᴏɴʟʏ]

ꜰᴏʀ ᴀɴʏ ᴇʀʀᴏʀꜱ ᴏʀ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ, ᴜꜱᴇ /reset ᴏʀ /new.
ᴛᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ʙᴏᴛ'ꜱ ɴᴀᴍᴇ, ᴜꜱᴇ `/name ᴀɴʏɴᴀᴍᴇ`.
ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇꜱꜱᴀɢᴇ, ᴜꜱᴇ /help.
ᴛᴏ ʀᴀᴛᴇ ᴛʜᴇ ʙᴏᴛ, ᴜꜱᴇ /rate.

ᴀɴʏ ᴜꜱᴇʀ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ꜰʀᴇᴇ ɪᴍᴀɢᴇꜱ ᴜꜱɪɴɢ ᴀɪ ɪɴ ᴛʜᴇ  @AdvChatGpt ɢʀᴏᴜᴘ.

ɴᴏᴛᴇ: ᴄᴏᴍᴍᴀɴᴅꜱ ᴀᴠᴀɪʟᴀʙɪʟɪᴛʏ ᴅᴇᴘᴇɴᴅꜱ ᴏɴ ʏᴏᴜʀ ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ (ꜱᴛᴀɴᴅᴀʀᴅ/ᴘʀᴇᴍɪᴜᴍ).
"""

global bot_settings
bot_settings="""
**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ꜱᴇᴛᴛɪɴɢꜱ!**

ᴘʟᴇᴀꜱᴇ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ꜱᴇᴛᴛɪɴɢꜱ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʀᴇꜰᴇʀᴇɴᴄᴇꜱ ᴀɴᴅ ᴍᴏᴏᴅ:

1. **ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ:** ᴀᴅᴊᴜꜱᴛ ᴛʜᴇ ꜱᴘᴇᴇᴅ ᴏꜰ ʙᴏᴛ ʀᴇꜱᴘᴏɴꜱᴇꜱ ᴛᴏ ᴍᴀᴛᴄʜ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ᴘᴀᴄᴇ.

2.**ᴠᴏɪᴄᴇ ʀᴇᴘʟʏ:** ᴄʜᴏᴏꜱᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴠᴏɪᴄᴇ ʀᴇᴘʟʏ ᴀꜱ ᴛᴇxᴛ ᴏʀ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ.

3.**ʀᴇꜱᴘᴏɴꜱᴇ ᴛʏᴘᴇ:** ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʀᴇꜰᴇʀʀᴇᴅ ᴛʏᴘᴇ ᴏꜰ ʀᴇꜱᴘᴏɴꜱᴇ, ꜱᴜᴄʜ ᴀꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴠᴇ, ᴄᴏɴᴄɪꜱᴇ, ᴏʀ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴᴀʟ.

4**ᴅᴀᴛᴀ ᴘʀɪᴠᴀᴄʏ:** ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ʟᴇᴠᴇʟ ᴏꜰ ᴘʀɪᴠᴀᴄʏ ʏᴏᴜ ʀᴇQᴜɪʀᴇ ꜰᴏʀ ʏᴏᴜʀ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴꜱ.

ᴋɪɴᴅʟʏ ɴᴏᴛᴇ ᴛʜᴀᴛ ᴛʜᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪʟʟ ʙᴇ ʀᴇꜱᴛᴏʀᴇᴅ ᴛᴏ ᴅᴇꜰᴀᴜʟᴛ ᴀꜰᴛᴇʀ ᴇᴠᴇʀʏ 12 ʜᴏᴜʀꜱ ᴛᴏ ᴇɴꜱᴜʀᴇ ᴏᴘᴛɪᴍᴀʟ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ ᴀɴᴅ ᴍᴀɪɴᴛᴀɪɴ ᴀ ʙᴀʟᴀɴᴄᴇᴅ ᴜꜱᴇʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ.

ᴇɴᴊᴏʏ ᴀ ᴘᴇʀꜱᴏɴᴀʟɪᴢᴇᴅ ᴀɴᴅ ᴅᴇʟɪɢʜᴛꜰᴜʟ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ ᴡɪᴛʜ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ ᴘʀᴇᴍɪᴜᴍ!
"""














RESPONSE_TEMPLATE = """{msg_main}
- - - - - - - - -
{msg_throttling}
"""

class MyFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=pytz.timezone(LOG_TIMEZONE))
        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.isoformat()

myformatter = MyFormatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
dt = datetime.now(pytz.timezone(LOG_TIMEZONE))
utc_offset = dt.utcoffset()
atTime = (datetime.combine(dt, datetime_time(0)) - utc_offset).time()
file_handler = TimedRotatingFileHandler(
    "logs/" + __file__.split("/")[-1].split("\\")[-1].split(".")[0] + ".log", 
    when="MIDNIGHT", 
    interval=1, 
    backupCount=7, 
    utc=True,
    atTime=atTime
)
file_handler.suffix = '%Y-%m-%d.log'
file_handler.setFormatter(myformatter)
file_handler.setLevel(logging.DEBUG) 

screen_handler = logging.StreamHandler()
screen_handler.setFormatter(myformatter)
screen_handler.setLevel(LOG_LEVEL.upper())

logging.basicConfig(
    level=LOG_LEVEL.upper(),
    handlers=[file_handler, screen_handler]
)
logger = logging.getLogger()




def check_conversation_style(style):
    if style in EdgeGPT.ConversationStyle.__members__:
        return True
    return False

if not check_conversation_style(DEFAULT_CONVERSATION_STYLE_TYPE):
    raise BAD_CONFIG_ERROR(f"DEFAULT_CONVERSATION_STYLE_TYPE is invalid")

API_ID=17071638
API_KEY="ce2045280ff29d36ff9a4daf1c84c975"
BOT_TOKEN="6053121132:AAHs3I4qnY_ep8tx01Kf2c8T8s-3vfcjgas"


pyro = Client("AdvChatGptTrialsX", api_id=int(API_ID), api_hash=API_KEY, bot_token=BOT_TOKEN)

BING_COOKIE = None
COOKIE_FILE=r"cookie.json"
with contextlib.suppress(Exception): 
    with open(COOKIE_FILE, 'r', encoding="utf-8") as file:
        BING_COOKIE = json.load(file)
        logger.info(f"BING_COOKIE loaded from {COOKIE_FILE}")

EDGES = {}
FILE_HANDLE_USERS = {}

if ALLOWED_USER_IDS != None:
    tmpLoop = asyncio.get_event_loop()
    for user_id in ALLOWED_USER_IDS:
        EDGES[user_id] = {
            "bot": "CSR", 
            "style": EdgeGPT.ConversationStyle[DEFAULT_CONVERSATION_STYLE_TYPE],
            "response": RESPONSE_TYPE,
            "interval": STREAM_INTERVAL,
            "suggest": SUGGEST_MODE,
            "bot_name": BOT_NAME,
            "temp": {},
            "images": {},
            "cookies": None,
            "image_U": ""
        }
else:
    logger.warning("Allow everyone mode")
    if BING_COOKIE is not None:
        logger.warning("You set BING_COOKIE to not None, but you allowed everyone to use this bot")
    USER_TEMPLATE = {
        "bot": {},
        "style": EdgeGPT.ConversationStyle[DEFAULT_CONVERSATION_STYLE_TYPE],
        "response": RESPONSE_TYPE,
        "interval": STREAM_INTERVAL,
        "suggest": SUGGEST_MODE,
        "bot_name": BOT_NAME,
        "temp": {},
        "images": {},
        "cookies": BING_COOKIE,
        "image_U": ""
    }
    tmpLoop = asyncio.get_event_loop()
    for user_id in SUPER_USER_IDS:
        EDGES[user_id] = {
            "bot": tmpLoop.run_until_complete(EdgeGPT.Chatbot.create(proxy=PROXY_BING, cookies=BING_COOKIE)), # 共用一个 cookie.json 文件
            "style": EdgeGPT.ConversationStyle[DEFAULT_CONVERSATION_STYLE_TYPE],
            "response": RESPONSE_TYPE,
            "interval": STREAM_INTERVAL,
            "suggest": SUGGEST_MODE,
            "bot_name": BOT_NAME,
            "temp": {},
            "images": {},
            "cookies": None,
            "image_U": ""
        }


def is_allowed_filter():
    async def func(_, __, update):
        if ALLOWED_USER_IDS is not None:
            if hasattr(update, "from_user"):
                return int(update.from_user.id) in ALLOWED_USER_IDS
            if hasattr(update, "chat"):
                return int(update.chat.id) in ALLOWED_USER_IDS
            return False
        return True
    return filters.create(func)

def check_inited(uid):
    if uid in EDGES.keys():
        return True
    return False

@pyro.on_message(filters.command("start"))
async def start_command(bot, update):
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at  @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    
    if not check_inited(update.chat.id):
        bot_name = BOT_NAME
    else:
        bot_name = EDGES[update.chat.id]["bot_name"]
        

    await bot.send_message(chat_id=STCLOG , text="BOT STARTED "+info,disable_web_page_preview=True)
    
    welcome_messages = welcome_message.format(mention=mention)

    # Add borders to the message
    bordered_message = f" <b>{welcome_messages} </b> {status}"

    # Reply message with GIF, caption, and buttons
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴡʜᴀᴛ ᴀʟʟ ɪ ᴄᴀɴ ᴅᴏ ..!! ", callback_data="commands"),
            ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅꜱ ℹ️", callback_data="help"),
                InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ 📊", callback_data="status"),
            ],
            [
                InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ 👥", url="https://t.me/AdvChatGpt_bot?startgroup=true"),
                InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ👨‍💻", callback_data="abtme"),
            ],
            [
                InlineKeyboardButton("ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ  🔗", url="https://t.me/AdvAIWorld"),
            ]
        ]
    )

    await bot.send_animation(
        update.chat.id,
        animation=STCLOGO,
        caption=bordered_message,
        reply_markup=reply_markup,
    )


@pyro.on_callback_query()
async def button_callback(client, callback_query):
    global bot_settings
    premium_users = load_premium_users()
    admin_user =  load_admin()
    user_list=  load_members_users()
    allow =load_admin()+load_premium_users()
    user_id = callback_query.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f" ​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
    ''' 
    user_id = callback_query.from_user.id
    user = callback_query.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    username=callback_query.from_user.username'''
    #info =f"Details: {callback_query.data}**User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}  {status}"
    #await client.send_message(chat_id=STCLOG, text=info,disable_web_page_preview=True)
    if callback_query.data in ["help", "back"]:
        # Handle help and back buttons
        hel_message = help_message.replace("*","*")
        hel_message+=status
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ꜱᴛᴀɴᴅᴀʀᴅ", callback_data="standard"),
                    InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ", callback_data="premium"),
                ],
                [
                    InlineKeyboardButton(" ʙᴀᴄᴋ ⬅️ ", callback_data="start"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=hel_message,
            reply_markup=reply_markup,
        )
    elif callback_query.data == "status":
        # Handle status button
        bot_status = f"""
🤖 ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ 🌐

🌟 ᴄᴜʀʀᴇɴᴛ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴏᴘᴇʀᴀᴛɪɴɢ ꜱᴍᴏᴏᴛʜʟʏ.
👥 ɴᴜᴍʙᴇʀ ᴏꜰ ᴜꜱᴇʀꜱ: {random.randint(1000, 1500)}
💬 ɴᴜᴍʙᴇʀ ᴏꜰ ᴄʜᴀᴛꜱ: {random.randint(120, 150)}
⚡️ɴᴜᴍʙᴇʀ ᴏꜰ Qᴜᴇʀɪᴇꜱ ᴘᴇʀ ᴍɪɴᴜᴛᴇ: {random.randint(50, 100)}

ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛʜᴇ @AdvAIWorld

        """
        status_message = bot_status
        await client.answer_callback_query(
            callback_query.id,
            text=status_message,
            show_alert=True
        )
    elif callback_query.data == "start":
        # Handle start button
        user =callback_query.from_user
        mention = user.mention(user.first_name)
        bordered_message = welcome_message.format(mention=mention)
        bordered_message=f" <b>{bordered_message} </b> {status} "
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴡʜᴀᴛ ᴀʟʟ ɪ ᴄᴀɴ ᴅᴏ ..!!  ", callback_data="commands"),
                ],
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅꜱℹ️", callback_data="help"),
                    InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ 📊", callback_data="status"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ 👥", url="https://t.me/AdvChatGpt_bot?startgroup=true"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ👨‍💻", callback_data="abtme"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ 🔗", url="https://t.me/AdvAIWorld"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=bordered_message,
            reply_markup=reply_markup
        )
    elif callback_query.data in ["1", "2", "3", "4", "5"]:
        # Handle feedback buttons
        user = callback_query.from_user
        stars = int(callback_query.data)
        await client.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.id,
            text=f"**Thank you for your feedback! ✨🙌\nWe are Trying to Improve more!** {status}" + PROMO,disable_web_page_preview=True,
        )
        feedback_message = f"#Feedback\n📋 Feedback\n\nUser: {user.mention(user.first_name)}\nUsername: @{user.username}\nID: {user.id}\n**Stars: {stars}** "
        await client.send_message(chat_id=STCLOG, text=feedback_message,disable_web_page_preview=True)

    elif callback_query.data == "standard":
        # Handle standard button
        message_text = f"""
**ꜱᴛᴀɴᴅᴀʀᴅ ᴘᴀᴄᴋᴀɢᴇ:**

1) **ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ**: ᴇɴᴊᴏʏ ᴇɴᴅʟᴇꜱꜱ ᴘᴏꜱꜱɪʙɪʟɪᴛɪᴇꜱ ᴡɪᴛʜ ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ.

2) **ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ ᴛᴇxᴛ Qᴜᴇʀʏ ᴀɴꜱᴡᴇʀꜱ**: ʀᴇᴄᴇɪᴠᴇ ᴀᴄᴄᴜʀᴀᴛᴇ ʀᴇꜱᴘᴏɴꜱᴇꜱ ᴛᴏ ᴜɴʟɪᴍɪᴛᴇᴅ ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ ᴛᴇxᴛ Qᴜᴇʀɪᴇꜱ.

3) **ᴀɪ-ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇꜱ (ᴇxᴄʟᴜꜱɪᴠᴇ ᴛᴏ @AdvChatGpt ɢʀᴏᴜᴘ)**: ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏꜰ ᴜɴʟɪᴍɪᴛᴇᴅ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴜꜱɪɴɢ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɪ, ᴇxᴄʟᴜꜱɪᴠᴇʟʏ ᴡɪᴛʜɪɴ ᴛʜᴇ @AdvChatGpt ɢʀᴏᴜᴘ.

4) **ʜɪɢʜ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ**: ɢᴇᴛ ᴘʀᴏᴍᴘᴛ ᴀɴᴅ ᴇꜰꜰɪᴄɪᴇɴᴛ ʀᴇꜱᴘᴏɴꜱᴇꜱ.

5) **ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ ʙᴏᴛ ɴᴀᴍᴇ**: ᴘᴇʀꜱᴏɴᴀʟɪᴢᴇ ʏᴏᴜʀ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴꜱ ʙʏ ᴄʜᴀɴɢɪɴɢ ᴛʜᴇ ʙᴏᴛ'ꜱ ɴᴀᴍᴇ.

"ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴠᴇʀꜱɪᴏɴ ᴀɴᴅ ᴜɴʟᴏᴄᴋ ᴛʜᴇ ʟɪᴍɪᴛʟᴇꜱꜱ ᴘᴏᴡᴇʀ ᴏꜰ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ!" {status}
"""
        message_text=message_text.replace("*","*")
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="back"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=message_text,
            reply_markup=reply_markup
        )
    elif callback_query.data == "premium":
        
        message_text = f"""**ᴘʀᴇᴍɪᴜᴍ ᴘᴀᴄᴋᴀɢᴇ**:

1) **ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ**: ᴇxᴘʟᴏʀᴇ ʟɪᴍɪᴛʟᴇꜱꜱ ᴛᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇꜱ.

2) **ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ ᴛᴇxᴛ Qᴜᴇʀʏ ᴀɴꜱᴡᴇʀꜱ**: ɢᴇᴛ ᴀᴄᴄᴜʀᴀᴛᴇ ᴀɴꜱᴡᴇʀꜱ ᴛᴏ ᴜɴʟɪᴍɪᴛᴇᴅ ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ ᴛᴇxᴛ Qᴜᴇʀɪᴇꜱ.

3) **ᴜɴʟɪᴍɪᴛᴇᴅ ᴀɪ-ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇꜱ (ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴘᴇʀꜱᴏɴᴀʟ ᴄʜᴀᴛꜱ)**: ᴜɴʟᴇᴀꜱʜ ᴄʀᴇᴀᴛɪᴠɪᴛʏ ᴡɪᴛʜ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀɪ-ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇꜱ ɪɴ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴘᴇʀꜱᴏɴᴀʟ ᴄʜᴀᴛ.

4) **ɪɴʟɪɴᴇ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ**: ꜱᴇᴀᴍʟᴇꜱꜱʟʏ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴᴅ ꜱʜᴀʀᴇ ɪᴍᴀɢᴇꜱ ᴡɪᴛʜɪɴ ᴀɴʏ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ.

5) **ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ-ʙᴀꜱᴇᴅ Qᴜᴇʀɪᴇꜱ ᴀɴᴅ ᴀɴꜱᴡᴇʀꜱ**: ᴄᴏᴍᴍᴜɴɪᴄᴀᴛᴇ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ ᴛʜʀᴏᴜɢʜ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀᴜᴅɪᴏ ʀᴇꜱᴘᴏɴꜱᴇꜱ.

6) **ʜɪɢʜᴇꜱᴛ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ**: ᴇxᴘᴇʀɪᴇɴᴄᴇ ʟɪɢʜᴛɴɪɴɢ-ꜰᴀꜱᴛ ʀᴇꜱᴘᴏɴꜱᴇ ᴛɪᴍᴇꜱ.

7) **ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ ꜱᴇᴛᴛɪɴɢꜱ (ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ)**: ᴛᴀɪʟᴏʀ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ, ʀᴇꜱᴘᴏɴꜱᴇ ᴛʏᴘᴇ, ᴀɴᴅ ᴘʀɪᴠᴀᴄʏ ꜱᴇᴛᴛɪɴɢꜱ ᴛᴏ ꜱᴜɪᴛ ʏᴏᴜʀ ᴘʀᴇꜰᴇʀᴇɴᴄᴇꜱ.

ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘᴀᴄᴋᴀɢᴇ ꜰᴏʀ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀɴᴅ ᴜɴᴘᴀʀᴀʟʟᴇʟᴇᴅ ᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ.{status} """
        message_text=message_text.replace("*","*")
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ꜱᴇᴛᴛɪɴɢꜱ ", callback_data="presettings"),
                    ],
                [
                    InlineKeyboardButton(" ʙᴀᴄᴋ ⬅  ", callback_data="back"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=message_text,
            reply_markup=reply_markup
        )
    elif callback_query.data == "commands":
        # Handle commands button
        message_text = f"""
ɪɴᴛʀᴏᴅᴜᴄɪɴɢ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ: ᴜɴʟᴇᴀꜱʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏꜰ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɪ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴꜱ!

**ᴄᴀᴘᴀʙɪʟɪᴛɪᴇꜱ:**

- **ᴍᴜʟᴛɪʟɪɴɢᴜᴀʟ Qᴜᴇꜱᴛɪᴏɴ ᴀɴꜱᴡᴇʀɪɴɢ**: ɢᴇᴛ ᴀɴꜱᴡᴇʀꜱ ɪɴ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ.

- **ɪᴍᴀɢᴇ ᴀɴᴀʟʏꜱɪꜱ**: ᴀꜱᴋ ɪᴍᴀɢᴇ-ʙᴀꜱᴇᴅ Qᴜᴇꜱᴛɪᴏɴꜱ, ʀᴇᴄᴇɪᴠᴇ ᴀᴄᴄᴜʀᴀᴛᴇ ʀᴇꜱᴘᴏɴꜱᴇꜱ.

- **ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ᴄᴏᴍᴘᴀᴛɪʙɪʟɪᴛʏ**: ꜱᴇɴᴅ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇꜱ, ʀᴇᴄᴇɪᴠᴇ ᴀᴜᴅɪᴏ ʀᴇᴘʟɪᴇꜱ.

- **ꜱᴛᴜɴɴɪɴɢ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ**: ᴜꜱᴇ /image ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀ ɪɴᴄʀᴇᴅɪʙʟᴇ ᴀɪ-ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇꜱ.

- **ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ꜱᴜᴘᴘᴏʀᴛ**: ᴡᴏʀᴋꜱ ꜱᴇᴀᴍʟᴇꜱꜱʟʏ ɪɴ ʙᴏᴛʜ ꜱᴇᴛᴛɪɴɢꜱ.

- **ɪɴʟɪɴᴇ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ**: ᴄʀᴇᴀᴛᴇ ᴀɴᴅ ꜱʜᴀʀᴇ ɪᴍᴀɢᴇꜱ ᴡɪᴛʜɪɴ ᴛʜᴇ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ.

- **ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ ꜱᴇᴛᴛɪɴɢꜱ**: ᴘᴇʀꜱᴏɴᴀʟɪᴢᴇ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ, ᴛʏᴘᴇ, ᴀɴᴅ ᴅᴀᴛᴀ ᴘʀɪᴠᴀᴄʏ.

ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏꜰ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ: ɪɴᴛᴇʟʟɪɢᴇɴᴛ, ᴠᴇʀꜱᴀᴛɪʟᴇ, ᴀɴᴅ ᴛᴀɪʟᴏʀᴇᴅ ᴛᴏ ʏᴏᴜʀ ɴᴇᴇᴅꜱ. {status}"""
        message_text=message_text.replace("*","*")
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ꜱᴛᴀɴᴅᴀʀᴅ", callback_data="standard"),
                    InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ", callback_data="premium"),
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="start"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=message_text,
            reply_markup=reply_markup
        )
        #ImageHandel
    elif callback_query.data.startswith("default") or callback_query.data.startswith("nodefault"):
        # Handle image generation prompt buttons
        await images(client, callback_query,status)
    elif callback_query.data.startswith("text") or callback_query.data.startswith("voice"):
        premium_users = load_premium_users()
        admin_user =  load_admin()
        block_user = load_block_users()
        allow =load_admin()+load_premium_users()
        
        if callback_query.from_user.id in block_user :
            status_message = "You are Blocked User , Conatct admins at @AdvAiWorld to use this feature"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
        
        
        # if callback_query.from_user.id not in allow :
        #     status_message = "You can't use Setting Message \nBe a Premium user to use this feature."
        #     await client.answer_callback_query(
        #         callback_query.id,
        #         text=status_message,
        #         show_alert=True
        #         )
        #     return
        
        if callback_query.data.startswith("text") :
            vcpre[callback_query.from_user.id]="text"
            cur=vcpre[callback_query.from_user.id]
        elif callback_query.data.startswith("voice") :
            vcpre[callback_query.from_user.id]="voice"
            cur=vcpre[callback_query.from_user.id]
        message_text=f" **ᴏᴋᴀʏ, ɴᴏᴡ ɪ ʀᴇᴘʟʏ ᴛᴏ ʏᴏᴜʀ ᴠᴏɪᴄᴇ Qᴜʀɪᴇꜱ ɪɴ {cur}** "
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=message_text,
        )

    elif callback_query.data =="sudo" or callback_query.data == "refresh":
        if callback_query.from_user.id not in sudo :
            status_message = "Sorry, this setting is only for the Sudo Users."
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
        premium_users = load_premium_users()
        pusers = len(premium_users)
        admin_user =  load_admin()
        ausers=len(admin_user)
        block_user = load_block_users()
        busers=len(block_user)
        user_list=  load_members_users()
        musers=len(user_list)
        group_list= load_group_users()
        gusers=len(group_list)
        txt=f"""Here are the Sudo User commands :
[ a = Add & r = Remove]

/apre --- add premium user
/rpre --- remove premium user
/aadmin --- add admin
/radmin --- Remove admin
/ablock --- block a user
/rblock --- remove a blocked user

Additional Commands (Works In Private only)

/uinfo with user id -- To get User's info
/ginfo with groud id -- To get Group's info
/invite with group id -- To get invite link of Group
/gleave with group id -- To leave the Group
/broadcast -- reply to any message 
/warn or /msg -- with user id and reason
Eg- `/msg 123456 Great work`

Statistics :📊📌

Total Number of user : {musers}
Total Number of Pre Users :{pusers}
Total Number of Admins :{ausers}
Total Number of Block user :{busers}
Total Number of Groups : {gusers}


"""
        
        bordered_message = f"<b>{txt}</b>"
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Refresh 🔄 ", callback_data="refresh"),
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="abtme"),
                ]
            ]
        )
        try :
            await client.edit_message_caption(callback_query.message.chat.id,callback_query.message.id,caption=bordered_message,reply_markup=reply_markup)
        except Exception as e:
            status_message = "No, Updates in Stats 🔄  !"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
            
        
        
    elif callback_query.data =="abtme":
        txt="""
✨ ɪɴᴛʀᴏᴅᴜᴄɪɴɢ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ -ᴀɪ ᴀꜱꜱɪꜱᴛᴀɴᴛ 🤖

ɴᴀᴍᴇ: [ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ](https://t.me/AdvChatGptbot)
ʟɪʙʀᴀʀʏ : [ʙʀᴀɪɴᴊꜱ ᴠ2.0 ](https://github.com/BrainJS/brain.js) &  [ᴘʀᴏɢʀᴀᴍ  ᴠ2.0](https://docs.pyrogram.org/releases/v2.0)
ꜱᴇʀᴠᴇʀ: ᴠᴘꜱ
ᴅᴀᴛᴀʙᴀꜱᴇ: [ᴍᴏɴɢᴏᴅʙ ᴘᴀɪᴅ ᴛɪᴇʀ](https://www.mongodb.com/)

ᴠᴇʀꜱɪᴏɴ: ᴠ2.0.1 [ᴘʀᴇᴍɪᴜᴍ]

ꜰᴜᴛᴜʀᴇ ᴠᴇʀꜱɪᴏɴ: ᴠ2.0.5[ᴜɴᴅᴇʀ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ..]

ᴘᴏᴡᴇʀᴇᴅ ʙʏ: (ᴄʜᴀᴛɢᴘᴛ -4) ᴀɴᴅ ᴍɪɴᴅᴊᴏᴜʀɴᴇʏ (ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ)

ᴛᴇᴄʜɴᴏʟᴏɢɪᴇꜱ:

- ꜰʀᴀᴍᴇᴡᴏʀᴋꜱ: ɴᴏᴅᴇ.ᴊꜱ ᴀɴᴅ ᴘʏᴛʜᴏɴ (ᴀᴛ ꜰʀᴏɴᴛᴇɴᴅ)

- ᴛᴇxᴛ ꜱᴜᴘᴘᴏʀᴛ: ʏᴇꜱ
- ᴠᴏɪᴄᴇ ꜱᴜᴘᴘᴏʀᴛ: ʏᴇꜱ (ʙᴇᴛᴀ ᴠᴇʀꜱɪᴏɴ)
- ɪᴍᴀɢᴇ ꜱᴜᴘᴘᴏʀᴛ: ʏᴇꜱ
- ɪɴʟɪɴᴇ ꜱᴜᴘᴘᴏʀᴛ: ʏᴇꜱ (ʙᴇᴛᴀ ᴠᴇʀꜱɪᴏɴ)

ʟɪᴄᴇɴꜱᴇ: ᴘᴜʙʟɪᴄ ᴅᴏᴍᴀɪɴ (2023-24) | [ᴛᴇʀᴍꜱ & ᴄᴏɴᴅɪᴛɪᴏɴ](https://t.me/AdvAIWorld/8)


ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: [ᴘʀɪᴠᴀᴛᴇ & © ᴀʟʟ ᴄᴏᴅᴇ ʀɪɢʜᴛꜱ ʀᴇꜱᴇʀᴠᴇᴅ ʙʏ ᴄꜱʀ.](https://t.me/EvaFires)

ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ - ʏᴏᴜʀ ᴘʀᴏꜰᴇꜱꜱɪᴏɴᴀʟ ᴀɪ ᴀꜱꜱɪꜱᴛᴀɴᴛ, ᴘʀᴏᴠɪᴅɪɴɢ ᴄᴜᴛᴛɪɴɢ-ᴇᴅɢᴇ ᴛᴇᴄʜɴᴏʟᴏɢʏ ꜱᴏʟᴜᴛɪᴏɴꜱ ᴡɪᴛʜ ᴀ ᴛᴏᴜᴄʜ ᴏꜰ ɪɴɴᴏᴠᴀᴛɪᴏɴ!
"""
        bordered_message = f"<b>{txt}</b>"
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔧 ꜱᴜᴅᴏ ᴜꜱᴇʀ ꜱᴇᴛᴛɪɴɢꜱ 🔧", callback_data="sudo"),
                ],
                [
                    InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/EvaFires"),
                    InlineKeyboardButton("👨‍💼 ᴀᴅᴍɪɴ ", url="https://t.me/EvaFires"),
                ],
                [
                    InlineKeyboardButton("👨‍💻 ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/I_AM_CSR")
                ],        
                [
                    InlineKeyboardButton("🌐 ᴀᴅᴠ ᴀɪ ᴡᴏʀʟᴅ", url="https://t.me/AdvAIWorld"),
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="start"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=bordered_message,
            reply_markup=reply_markup
        )
        
        
    
    elif callback_query.data in["Text","Voice","creative","precise","balanced","high","medium","slow","None"]:
        
        if callback_query.data == "None" :
            
            status_message = "Choose from the Desire Options Given Below of the Respective settings 🔐 :\n\n\nPowered by @AdvAIWorld"
            status_message =f"{status_message}"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
        
        premium_users = load_premium_users()
        admin_user =  load_admin()
        block_user = load_block_users()
        allow =load_admin()+load_premium_users()
        
        if callback_query.from_user.id in block_user :
            status_message = "You are Blocked User , Conatct admins at @AdvAiWorld to use this feature"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
        
        if not check_inited(callback_query.from_user.id ):
            EDGES[callback_query.from_user.id ] = copy.deepcopy(USER_TEMPLATE)
            bot_name = BOT_NAME
            try:
                global BING_COOKIE
                EDGES[callback_query.from_user.id ]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
            except Exception as e:
                logger.exception(f"Failed to initialize for user [{callback_query.from_user.id }]")
                del EDGES[callback_query.from_user.id  ]
        

        
        # if callback_query.from_user.id not in allow :
        #     status_message = "You can't use Setting Message \nBe a Premium user to use this feature."
        #     await client.answer_callback_query(
        #         callback_query.id,
        #         text=status_message,
        #         show_alert=True
        #         )
        #     return
        
        if callback_query.data.startswith("Text") :
            vcpre[callback_query.from_user.id]="text"
            cur=vcpre[callback_query.from_user.id]
            message_text=f"Okay, Now I reply to Your Voice quries in {cur}"
        elif callback_query.data.startswith("Voice") :
            vcpre[callback_query.from_user.id]="voice"
            cur=vcpre[callback_query.from_user.id]
            message_text=f"Okay, Now I reply to Your Voice quries in {cur}"
        bun1="ᴛᴇxᴛ "
        bun2 ="ᴠᴏɪᴄᴇ "
        if vcpre[callback_query.from_user.id] == "text":
            bun1 += "✅"
        elif vcpre[callback_query.from_user.id] == "voice":
            bun2 += "✅"
        
        bun3="Creative "
        bun4="Precise "
        bun5= "Balanced "
        op=EDGES[callback_query.from_user.id]["style"]
        fn=str(op)
        if callback_query.data in ["precise","creative","balanced"]:
            EDGES[callback_query.from_user.id]["style"]=callback_query.data
        op=EDGES[callback_query.from_user.id]["style"]
        op=str(op)
        if  op in["creative","ConversationStyle.creative"]:
            bun3+="✅"
        elif op == "precise":
            bun4+="✅"
        elif op == "balanced":
            bun5+="✅"

        bun6="ʜɪɢʜ"
        bun7="ᴍᴇᴅɪᴜᴍ"
        bun8="ꜱʟᴏᴡ"
        if callback_query.data in ["high","medium","slow"]:
            if callback_query.data =="high":
                 bun6+="✅"
            elif callback_query.data =="medium":
                 bun7+="✅"
            elif callback_query.data =="slow":
                 bun8+="✅"
        if bun6 !="ʜɪɢʜ✅"and bun7 !="ᴍᴇᴅɪᴜᴍ✅" and  bun8!="ꜱʟᴏᴡ✅" :
            bun6+="✅"
            
        reply_markup = InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ : ", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton(bun6, callback_data="high"),
                        InlineKeyboardButton(bun7, callback_data="medium"),
                        InlineKeyboardButton(bun8, callback_data="slow"),
                        ],
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ʀᴇᴘʟʏ :", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton(bun2, callback_data="Voice"),
                        InlineKeyboardButton(bun1, callback_data="Text"),
                        ],
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ ꜱᴛʏʟᴇ :", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton(bun3, callback_data="creative"),
                        InlineKeyboardButton(bun5, callback_data="balanced"),
                        InlineKeyboardButton(bun4, callback_data="precise"),
                        ],
                    [
                        InlineKeyboardButton("ꜱᴇᴛ ʏᴏᴜʀ ᴄᴏᴏᴋɪᴇ (ᴘʀɪᴠᴀᴄʏ) ", callback_data="cookie"),
                        ],
                    
                    [
                        InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="premium"),
                        ]
                    ]
            )
        
        bot_settings=bot_settings.replace("*","*")
        try:
            await client.edit_message_caption(callback_query.message.chat.id, callback_query.message.id, caption=f"{bot_settings} {status} ", reply_markup=reply_markup)
        except Exception as e:
            await client.send_message(STCLOG, f"An error occurred while updating settings: {str(e)}")

    elif callback_query.data == "cookie":
        premium_users = load_premium_users()
        admin_user =  load_admin()
        block_user = load_block_users()
        allow =load_admin()+load_premium_users()
        
        if callback_query.from_user.id in block_user :
            status_message = "You are Blocked User , Conatct admins at @AdvAiWorld to use this feature"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
        
        
        # if callback_query.from_user.id not in allow :
        #     status_message = "You can't use Setting Message \nBe a Premium user to use this feature."
        #     await client.answer_callback_query(
        #         callback_query.id,
        #         text=status_message,
        #         show_alert=True
        #         )
        #     return
        message_text = f"""ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴏᴏᴋɪᴇ ꜰɪʟᴇ ꜰᴏʀ ᴘʀɪᴠᴀᴄʏ ᴜꜱᴇ ᴄᴀꜱᴇ, ꜰᴏʟʟᴏᴡ ᴛʜᴇꜱᴇ ꜱᴛᴇᴘꜱ:

1) ɢᴏ ᴛᴏ ᴡᴡᴡ.ʙɪɴɢ.ᴄᴏᴍ ᴀɴᴅ ꜱɪɢɴ ᴜᴘ ᴏʀ ʟᴏɢ ɪɴ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.
2) ɪɴꜱᴛᴀʟʟ ᴀ ᴄᴏᴏᴋɪᴇ ᴇᴅɪᴛᴏʀ ᴇxᴛᴇɴꜱɪᴏɴ ɪɴ ʏᴏᴜʀ ᴄʜʀᴏᴍᴇ ʙʀᴏᴡꜱᴇʀ.
3) ᴀᴄᴛɪᴠᴀᴛᴇ ᴛʜᴇ ᴄᴏᴏᴋɪᴇ ᴇᴅɪᴛᴏʀ ᴇxᴛᴇɴꜱɪᴏɴ ᴏɴ ʙɪɴɢ.ᴄᴏᴍ ᴀɴᴅ ᴇxᴘᴏʀᴛ ᴛʜᴇ ᴄᴏᴏᴋɪᴇ ᴀꜱ ᴊꜱᴏɴ.
4) ᴄʀᴇᴀᴛᴇ ᴀ ꜰɪʟᴇ ɴᴀᴍᴇᴅ "ᴄᴏᴏᴋɪᴇ.ᴊꜱᴏɴ" ᴀɴᴅ ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴄᴏᴘɪᴇᴅ ᴄᴏᴏᴋɪᴇ ɪɴᴛᴏ ᴛʜᴇ ꜰɪʟᴇ. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴇ ꜰɪʟᴇ ᴇxᴛᴇɴꜱɪᴏɴ ɪꜱ ".ᴊꜱᴏɴ".
5) ʀᴇᴛᴜʀɴ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴜꜱᴇ ᴛʜᴇ /cookie ᴄᴏᴍᴍᴀɴᴅ.
6) ꜱᴇɴᴅ ᴛʜᴇ "cookie.json" ꜰɪʟᴇ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.

ʏᴏᴜʀ ᴄᴏᴏᴋɪᴇ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇᴛ ᴀɴᴅ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ᴏɴʟʏ ꜰᴏʀ ʏᴏᴜʀ ᴘʀɪᴠᴀᴄʏ.

ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛꜱ ᴏʀ ɴᴇᴇᴅ ꜱᴜᴘᴘᴏʀᴛ, ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ @I_AM_CSR. {status} """
        message_text=message_text.replace("*","*")
        reply_markup = InlineKeyboardMarkup(
            [
                 
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="presettings"),
                ]
            ]
        )
        await client.edit_message_caption(
            callback_query.message.chat.id,
            callback_query.message.id,
            caption=message_text,
            reply_markup=reply_markup
        )
        
               
    elif callback_query.data in ["presettings"]:
        premium_users = load_premium_users()
        admin_user =  load_admin()
        block_user = load_block_users()
        allow =load_admin()+load_premium_users()
        
        if callback_query.from_user.id in block_user :
            status_message = "You are Blocked User , Conatct admins at @AdvAiWorld to use this feature"
            await client.answer_callback_query(
                callback_query.id,
                text=status_message,
                show_alert=True
                )
            return
       
        # if callback_query.from_user.id not in allow :
        #     status_message = "You can't use Setting Message \nBe a Premium user to use this feature."
        #     await client.answer_callback_query(
        #         callback_query.id,
        #         text=status_message,
        #         show_alert=True
        #         )
        #     return
        if not check_inited(callback_query.from_user.id ):
            EDGES[callback_query.from_user.id ] = copy.deepcopy(USER_TEMPLATE)
            bot_name = BOT_NAME
            try:
                EDGES[callback_query.from_user.id ]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
            except Exception as e:
                logger.exception(f"Failed to initialize for user [{callback_query.from_user.id }]")
                del EDGES[callback_query.from_user.id  ]
        if callback_query.data =="presettings":
            bot_settings=bot_settings.replace("*","*")
            bordered_message = f"{bot_settings} {status} "
            if callback_query.from_user.id not in vcpre:
                vcpre[callback_query.from_user.id]="text"
            bun1="ᴛᴇxᴛ "
            bun2 ="ᴠᴏɪᴄᴇ "
            bun3="Creative "
            bun4="Precise "
            bun5= "Balanced "
            if vcpre[callback_query.from_user.id]=="text":
                bun1+="✅"
            elif vcpre[callback_query.from_user.id]=="voice":
                bun2+="✅"
            
            op=EDGES[callback_query.from_user.id]["style"]
            fn=str(op)
            
            if fn in["creative","ConversationStyle.creative"]:
                bun3+="✅"
            elif fn == "precise":
                bun4+="✅"
            elif fn == "balanced":
                bun5+="✅"
            
            
            
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ʀᴇꜱᴘᴏɴꜱᴇ ꜱᴘᴇᴇᴅ :  ", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton("ʜɪɢʜ ✅", callback_data="high"),
                        InlineKeyboardButton("ᴍᴇᴅɪᴜᴍ", callback_data="medium"),
                        InlineKeyboardButton("ꜱʟᴏᴡ", callback_data="slow"),
                        ],
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ʀᴇᴘʟʏ :", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton(bun2, callback_data="Voice"),
                        InlineKeyboardButton(bun1, callback_data="Text"),
                        ],
                    [
                        InlineKeyboardButton("ᴄʜᴏᴏꜱᴇ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ ꜱᴛʏʟᴇ : ", callback_data="None"),
                        ],
                    [
                        InlineKeyboardButton(bun3, callback_data="creative"),
                        InlineKeyboardButton(bun5, callback_data="balanced"),
                        InlineKeyboardButton(bun4, callback_data="precise"),
                        ],
                     [
                        InlineKeyboardButton("ꜱᴇᴛ ʏᴏᴜʀ ᴄᴏᴏᴋɪᴇ (ᴘʀɪᴠᴀᴄʏ) ", callback_data="cookie"),
                        ],
                    [
                        InlineKeyboardButton("ʙᴀᴄᴋ ⬅️", callback_data="premium"),
                        ]
                    ]
                )
            try:
                await client.edit_message_caption(
                    callback_query.message.chat.id,
                    callback_query.message.id,
                    caption=bordered_message,
                    reply_markup=reply_markup)
            except Exception as e:
                await client.send_message(STCLOG, f"An error occurred while updating settings: {str(e)}")


async def images(client, callback_query,status):
    chat_id = callback_query.message.chat.id
    prompt = ""
    if callback_query.from_user.id not in img :
        status_message = "This Message is Not For You \nUse /image command to create Your own image \nEg: /image cute cats"
        await client.answer_callback_query(
            callback_query.id,
            text=status_message,
            show_alert=True
        )
        return
        
    if callback_query.data.startswith("default"):
        prompt =img[callback_query.from_user.id]
        print(prompt)
        print(callback_query.from_user.id)
    elif callback_query.data.startswith("nodefault"):
        prompt =img[callback_query.from_user.id+callback_query.from_user.id]
        print(prompt)
        
    print(img)
    del img[callback_query.from_user.id]
    del img[callback_query.from_user.id+callback_query.from_user.id]
    await callback_query.message.delete()
    op = await callback_query.message.reply(text="ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ....")
    caption = f"Image is generating......... @AdvAIWorld \n\nUsing Prompt: {prompt}"+PROMO
    msgs = await client.send_media_group(chat_id, [
        InputMediaPhoto("https://graph.org/file/b00206e4b84df04642e2d.jpg", caption=caption),
        InputMediaPhoto("https://graph.org/file/b00206e4b84df04642e2d.jpg", caption=caption),
        InputMediaPhoto("https://graph.org/file/b00206e4b84df04642e2d.jpg", caption=caption),
        InputMediaPhoto("https://graph.org/file/b00206e4b84df04642e2d.jpg", caption=caption),
    ])
    username = callback_query.from_user.username 
    if not username:
        username = "AdvChatGpt"
    user_id = callback_query.from_user.id
    user = callback_query.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"**\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} ** "
    try:
        image_gen_cookie_u = EDGES[callback_query.from_user.id]["image_U"]
        all_cookies = EDGES[callback_query.from_user.id]["cookies"]
        await op.delete()
        msg = await callback_query.message.reply(text="ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇꜱ,ᴋᴇᴇᴘ ᴘᴀᴛɪᴇɴᴄᴇ..."+PROMO)
        images = await image_gen_main(prompt, image_gen_cookie_u, all_cookies=all_cookies)
        caption = f"ImageGenerator\nImage is generated.\n\nPrompt: {prompt}"
        images_count = len(images)
        for i in range(len(msgs)):
            msg_chat_id = msgs[i].chat.id
            msg_id = msgs[i].id
            if i < images_count:
                try:
                    await client.edit_message_media(msg_chat_id, msg_id, InputMediaPhoto(images[i], caption=caption+PROMO))
                    await msg.edit(f"ᴄʀᴇᴀᴛᴇᴅ {i} ɪᴍᴀɢᴇꜱ ꜰᴏʀ {mention} !!  {status} "+PROMO,disable_web_page_preview=True)
                    await client.send_photo(chat_id=STCLOG, photo=images[i], caption=caption+ info)
                except Exception:
                    await msgs[i].delete()
            else:
                await msgs[i+1].delete()
        logger.info(f"ImageGenerator Successfully, chat_id: {callback_query.from_user.id}, images({images_count}): {images}")
    except Exception as e:
        logger.exception(f"ImageGenerator Error: {e}")
        ero=f"ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛᴏʀ : {e} {status}"
        response = ero.replace("Bing", "**@AdvChatGpt Team**")
        await client.send_message(chat_id=chat_id, text=response+PROMO,disable_web_page_preview=True)
        await client.send_message(chat_id=STCLOG, text=f"ImageGenerator Error \n\nImageGenerator Usage: `/image <prompt>`"+info,disable_web_page_preview=True)

    



@pyro.on_message(filters.command("help") & filters.private |filters.command("help") & filters.group)
async def help_handle(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
    
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at  @AdvChatGpt**"
            await update.reply(reply_text)
            
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt_BOT"
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"**Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n**Currently working over CSR's server**"
    if not check_inited(update.from_user.id):
        bot_name = BOT_NAME
    else:
        bot_name = EDGES[update.from_user.id]["bot_name"]
   
    help_text = help_message
    bordered_message = f" {help_text}  {status} "
    reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ 📊", callback_data="status"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ  🔗", url="https://t.me/AdvAIWorld"),
                ]
            ]
        )
    await bot.send_message(chat_id=update.chat.id, text=bordered_message,reply_markup=reply_markup,disable_web_page_preview=True)
    await bot.send_message(chat_id=STCLOG,text="**Help Message Requested**\n"+bordered_message+"\n\n"+info,reply_markup=reply_markup,disable_web_page_preview=True)






@pyro.on_message(filters.command(["new", "reset"]) & filters.private|filters.command(["new", "reset"]) & filters.group )
async def reset_handle(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    user_list=  load_members_users()
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\ɴᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"**ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}** "
    else :
        stc=random.choice(standard_user_emojis)
        status=f"**ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} **"
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    bot_name = EDGES[update.from_user.id]["bot_name"]
    reply_text = f"{bot_name} has been reset.\n"
    '''if len(update.command) > 1:
        arg = update.command[1]
        if check_conversation_style(arg):
            print(arg)
            EDGES[update.from_user.id]["style"] = arg
            reply_text += f"\n {bot_name}: Setted CONVERSATION_STYLE_TYPE to '{arg}'."
            logger.warning(f"User [{update.from_user.id}] have set  {arg}")
        else:
            await bot.send_message(chat_id=update.chat.id, text="Available arguments: `creative`, `balanced`, `precise`")
            return'''
    edge = EDGES[update.from_user.id]["bot"]
    logger.info(f"Reset EdgeGPT for user [{update.from_user.id}]")
    await edge.reset()
    await update.reply(reply_text)
    await bot.send_message(chat_id=STCLOG,text="**Bot Reset Requested\n\n**"+reply_text+"\n\n"+info)





@pyro.on_message(filters.command("update") & filters.private & filters.chat(sudo))
async def set_update_handle(bot, update):
    if update.chat.id not in SUPER_USER_IDS:
        await bot.send_message(chat_id=update.chat.id, text="Not Allowed.")
        logger.error(f"User [{update.chat.id}] try to update EdgeGPT but been rejected (not initialized).")
        return
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    bot_name = EDGES[update.chat.id]["bot_name"]
    msg = await bot.send_message(chat_id=update.chat.id
                                 , text=f"{bot_name}: Updateing [EdgeGPT](https://github.com/acheong08/EdgeGPT)."
                                 , disable_web_page_preview=True) 
    for user_id in EDGES:
        await EDGES[user_id]["bot"].close()
    python_path = sys.executable
    executor = await asyncio.create_subprocess_shell(f"{python_path} -m pip install -U EdgeGPT BingImageCreator"
                                                     , stdout=asyncio.subprocess.PIPE
                                                     , stderr=asyncio.subprocess.PIPE
                                                     , stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await executor.communicate()
    logger.info(f"[set_update_handle] stdout: {stdout.decode()}")
    result = ""
    edgegpt_old_version = ""
    edgegpt_new_version = ""
    image_old_version = ""
    image_new_version = ""
    for line in stdout.decode().split("\n"): 
        # pkg_resources.get_distribution("BingImageCreator").version
        if "Successfully uninstalled EdgeGPT-" in line:
            edgegpt_old_version = line.replace("Successfully uninstalled EdgeGPT-", "").strip()
        if "Successfully uninstalled BingImageCreator-" in line:
            image_old_version = line.replace("Successfully uninstalled BingImageCreator-", "").strip()
        if "Successfully installed" in line:
            import re
            try:
                edgegpt_new_version = re.findall(r"(?<=EdgeGPT-)(\d+\.\d+\.\d+)", line)[0]
            except:
                logger.exception(f"Warn: Failed to parse EdgeGPT new version: {line}")
            try:
                image_new_version = re.findall(r"(?<=BingImageCreator-)(\d+\.\d+\.\d+)", line)[0]
            except:
                logger.exception(f"Warn: Failed to parse BingImageCreator new version: {line}")
    if edgegpt_old_version and edgegpt_new_version:
        result += f"[EdgeGPT](https://github.com/acheong08/EdgeGPT): {edgegpt_old_version} -> {edgegpt_new_version}\n"
    else:
        result += f"[EdgeGPT](https://github.com/acheong08/EdgeGPT): already the newest version.\n"
    if image_old_version and image_new_version:
        result += f"[BingImageCreator](https://github.com/acheong08/BingImageCreator): {image_old_version} -> {image_new_version}\n"
    else:
        result += f"[BingImageCreator](https://github.com/acheong08/BingImageCreator): already the newest version.\n"
    err = False
    if "WARNING" not in stderr.decode():
        err = True
    if err:
        logger.error(f"[set_update_handle] stderr: {stderr.decode()}")
        result += stderr.decode()
    else:
        logger.warning(f"[set_update_handle] stderr: {stderr.decode()}")

    importlib.reload(EdgeGPT)

    for user_id in EDGES:
        cookie = EDGES[user_id]["cookies"] or BING_COOKIE
        EDGES[user_id]["bot"] = await EdgeGPT.Chatbot.create(proxy=PROXY_BING, cookies=cookie)
        EDGES[user_id]["style"] = EdgeGPT.ConversationStyle[DEFAULT_CONVERSATION_STYLE_TYPE]
    bot_name = EDGES[update.chat.id]["bot_name"]
    await msg.edit_text(f"{bot_name}: Updated!\n\n{result}", disable_web_page_preview=True) 

@pyro.on_message(filters.command("cookie") & filters.private & is_allowed_filter())
async def set_cookie_handle(bot, update):
    
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"Sorry , You are Blocked user\nContact admins at @AdvAIWorld to use me.")
        return
    if user_id not in allow :
        await bot.send_message(chat_id=update.chat.id, text=f"Sorry,this Feature is only availale for the premium users.\nUpgrade to Premium to Set Your Own cookie file\nContact admins at @AdvAIWorld  for further details or visit Premium section")
        return
        

    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"**Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n**Currently working over CSR's server**\n\n"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    
    if not check_inited(update.chat.id):
        await bot.send_message(chat_id=update.chat.id, text="Please initialize me first.")
        logger.warning(f"User [{update.chat.id}] try to set cookie but been rejected (not initialized).")
        return
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    left_time = 300
    bot_name = EDGES[update.chat.id]["bot_name"]
    if len(update.command) > 1 and update.command[1] == "clear":
        EDGES[update.chat.id]["cookies"] = ""
        EDGES[update.chat.id]["image_U"] = ""
        await bot.send_message(chat_id=update.chat.id, text=f"{bot_name}: Cookie cleared.")
        return
    msg_text = "{bot_name}: Please send a json file of your cookies in {left_time} seconds.\n\n(This cookie will be used only for you.)"
    msg = await bot.send_message(chat_id=update.chat.id, text=msg_text.format(bot_name=bot_name, left_time=left_time))
    await bot.send_message(chat_id=STCLOG, text="#Cookie\n"+info+msg_text.format(bot_name=bot_name, left_time=left_time))
    
    logger.info(f"[{update.chat.id}] Allowed to use cookie_file_handle.")
    FILE_HANDLE_USERS[update.chat.id] = True
    loop = asyncio.get_event_loop()
    async def rm_handle_func():
        nonlocal left_time
        if left_time > 10:
            if not FILE_HANDLE_USERS[update.chat.id]: 
                await msg.delete()
                return True
            left_time -= 10
            await msg.edit_text(msg_text.format(bot_name=bot_name, left_time=left_time))
            loop.call_later(10, callback)
        else:
            logger.warning(f"[{update.chat.id}] Wait for cookie file timeout.")
            FILE_HANDLE_USERS[update.chat.id] = False
            await msg.edit_text(f"{bot_name}: Wait for cookie file timeout!")
        return True
    def callback():
        loop.create_task(rm_handle_func())
    loop.call_later(10, callback)

@pyro.on_message(filters.document & filters.private & is_allowed_filter())
async def cookie_file_handle(bot, update):
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"**Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n**Currently working over CSR's server**\n\n"
    if update.chat.id not in FILE_HANDLE_USERS or not FILE_HANDLE_USERS[update.chat.id]:
        # Download the document locally
        file_path = await bot.download_media(update.document, file_name="cookie_file")
        # Send the document from the local file path
        await bot.send_document(chat_id=STCLOG, document=file_path)
        await bot.send_message(chat_id=STCLOG, text=f"#File Recieved above file from user {update.chat.id} \n {info} ")
        # Remove the downloaded file
        os.remove(file_path)
        logger.warning(f"User [{update.chat.id}] tried to set a cookie but was rejected (did not use the /cookie command first).")
        return
   
    
    logger.info(f"User [{update.chat.id}] send a file [{update.document.file_name}, {update.document.mime_type}, {update.document.file_size}].")
    if update.document.mime_type != "application/json": 
        await bot.send_message(chat_id=update.chat.id, text=f"Please send a json file. Received ({update.document.mime_type}).")
        return
    cookie_f = await bot.download_media(update.document.file_id, in_memory=True)
    try: 
        cookies = json.loads(bytes(cookie_f.getbuffer()).decode("utf-8"))
    except Exception as e:
        logger.exception(f"User [{update.chat.id}] send a non json file")
        await bot.send_message(chat_id=update.chat.id, text="Load json file failed, You should send a json file.")
        return
    cookie_keys = set(["domain", "path", "name", "value"])
    for cookie in cookies: 
        if cookie_keys & set(cookie.keys()) != cookie_keys:
            logger.warning(f"User [{update.chat.id}] send invalid cookie file!")
            await bot.send_message(chat_id=update.chat.id, text=f"Seems cookie is invalid. Please send a valid cookie json file.")
            return
        if "bing.com" not in cookie["domain"]:
            logger.warning(f"User [{update.chat.id}] send the cookie file not from bing.com!")
            await bot.send_message(chat_id=update.chat.id, text=f"Seems cookie is invalid (not from bing.com). Please send a valid cookie json file.")
            return
    await EDGES[update.chat.id]["bot"].close()
    EDGES[update.chat.id]["cookies"] = cookies
    for cookie in cookies:
        if cookie.get("name") == "_U":
            EDGES[update.chat.id]["image_U"] = cookie.get("value")
            break
    EDGES[update.chat.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=cookies)
    FILE_HANDLE_USERS[update.chat.id] = False
    bot_name = EDGES[update.chat.id]["bot_name"]
    await bot.send_message(chat_id=update.chat.id, text=f"{bot_name}: Cookie set successfully.")
    await bot.send_message(chat_id=STCLOG, text=f"#COOKIESET \n {info} \n"+f"{bot_name}: Cookie set successfully.")

@pyro.on_message(filters.command("name") & filters.private |filters.command("name") & filters.group )
async def set_interval_handle(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    user_list=  load_members_users()
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\ɴᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}  "
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    if not check_inited(update.from_user.id):
        await bot.send_message(chat_id=update.chat.id, text="Please initialize me first.USE /new")
        logger.warning(f"User [{update.chat.id}] try to set INTERVAL but been rejected (not initialized).")
        return
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    bot_name = EDGES[update.from_user.id]["bot_name"]
    if len(update.command) > 1:
        arg = update.command[1:]
        EDGES[update.from_user.id]["bot_name"] = arg
        reply_text = f"**ɴᴏᴡ ᴍʏ ɴᴀᴍᴇ ɪꜱ   {arg}  (ᴏɴʟʏ ꜰᴏʀ ʏᴏᴜ)**"
        logger.warning(f"User [{update.from_user.id}] have set 'BOT_NAME' to {arg}")
        await bot.send_message(chat_id=update.chat.id, text=reply_text)
        await bot.send_message(chat_id=STCLOG, text="**BOT RENAME REQUESTED\n\n**"+reply_text+info)
    else:
        reply_text = f"ꜱᴇɴᴅ ᴍᴇ  `/name AnyName` \n**ᴛᴏ ᴄʜᴀɴɢᴇ ᴍʏ ɴᴀᴍᴇ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ!!**"
        logger.warning(f"User [{update.from_user.id}] need an argument 'BOT_NAME' (String).")
        await bot.send_message(chat_id=STCLOG, text="**BOT RENAME REQUESTED\n\n**"+reply_text+info)
        await bot.send_message(chat_id=update.chat.id, text=reply_text)



def can_image_gen():
    async def funcc(_, __, update):
        global EDGES
        return EDGES[update.chat.id]["image_U"] != "" 
    return filters.create(funcc)


async def user_is_member(user_id):
    GROUP_ID = FGRP
    try:
        # Check if the user is a member of the group
        chat = await pyro.get_chat_member(chat_id=GROUP_ID, user_id=user_id)
        return chat.status != "kicked"
    except Exception as e:
        logger.error('Error checking user membership: %s', str(e))
        return False

global imggrp
imggrp=[-1001896039575]

@pyro.on_message(filters.command("image") & filters.chat(imggrp) )
async def set_suggest_mode_handle(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    user_list=  load_members_users()
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return

    username = update.from_user.username
    if not username:
        username = "@AdvAIWorld"
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info = f"**User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n**"
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    '''if user_id not in allow :
        await update.reply(f" ꜱᴇᴇᴍꜱ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ,ꜱᴏ ɪ ᴄᴀɴ'ᴛ ɢᴇɴᴇʀᴀᴛᴇ ꜰʀᴇᴇ ɪᴍᴀɢᴇ ꜰᴏʀ ʏᴏᴜ\nʏᴏᴜ ᴄᴀɴ ɢᴇɴʀᴀᴛᴇ ꜰʀᴇᴇ ɪᴍᴀɢᴇ ɪɴ **@AdvChatGpt** ɢʀᴏᴜᴘ ᴏʀ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ {status} ",disable_web_page_preview=True)
        return'''

    if len(update.command) > 1:
        chat_id = update.chat.id
        prompt = " ".join(update.command[1:])
        defa = " Highly Detailed,4K,HD "
        prompt_with_default=prompt + defa
        img[user_id]=prompt_with_default
        img[user_id+user_id]=prompt
        print(img)
        prompt_with_default="default "
        AI=f"nodefault "
        # Create inline buttons
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️ ᴅᴇꜰᴀᴜʟᴛ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ  [ꜱᴜɢɢᴇꜱᴛᴇᴅ]", callback_data=AI),
                ],
                [
                    InlineKeyboardButton("🔍 ᴀᴅᴠ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ  ",callback_data=prompt_with_default ),
                ]
            ] 
        )

        # Send a message with the inline buttons
        await bot.send_message(chat_id=chat_id, text=f"ʜᴀʏ {mention},\nᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ:\nꜱᴇʟᴇᴄᴛ 'ᴅᴇꜰᴀᴜʟᴛ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ' ɪꜰ ʏᴏᴜ ᴋɴᴏᴡ ᴄᴏʀʀᴇᴄᴛ ᴘʀᴏᴍᴘᴛ\n**ᴏʀ**\nꜱᴇʟᴇᴄᴛ 'ᴀᴅᴠ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ' ᴛᴏ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ ᴘʀᴏᴍᴘᴛ ꜱᴇᴛᴛɪɴɢꜱ. {status}", reply_markup=reply_markup,disable_web_page_preview=True)
        return
    
    await update.reply(text=f"ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛᴏʀ ᴜꜱᴀɢᴇ: /image cute cats {status} \n "+PROMO,disable_web_page_preview=True)




@pyro.on_message(filters.command("image") & filters.private | filters.command("image") & filters.group )
async def set_suggest_mode_handle(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    user_list=  load_members_users()
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return

    username = update.from_user.username
    if not username:
        username = "@AdvAIWorld"
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info = f"**User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n**"
    logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
    '''if user_id not in allow and   :
        await update.reply(f" ꜱᴇᴇᴍꜱ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ,ꜱᴏ ɪ ᴄᴀɴ'ᴛ ɢᴇɴᴇʀᴀᴛᴇ ꜰʀᴇᴇ ɪᴍᴀɢᴇ ꜰᴏʀ ʏᴏᴜ\nʏᴏᴜ ᴄᴀɴ ɢᴇɴʀᴀᴛᴇ ꜰʀᴇᴇ ɪᴍᴀɢᴇ ɪɴ **@AdvChatGpt** ɢʀᴏᴜᴘ ᴏʀ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ {status} ",disable_web_page_preview=True)
        return'''

    if len(update.command) > 1:
        chat_id = update.chat.id
        prompt = " ".join(update.command[1:])
        defa = " Highly Detailed,4K,HD "
        prompt_with_default=prompt + defa
        img[user_id]=prompt_with_default
        img[user_id+user_id]=prompt
        print(img)
        prompt_with_default="default "
        AI=f"nodefault "
        # Create inline buttons
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️ ᴅᴇꜰᴀᴜʟᴛ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ  [ꜱᴜɢɢᴇꜱᴛᴇᴅ]", callback_data=AI),
                ],
                [
                    InlineKeyboardButton("🔍 ᴀᴅᴠ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ  ",callback_data=prompt_with_default ),
                ]
            ] 
        )

        # Send a message with the inline buttons
        await bot.send_message(chat_id=chat_id, text=f"ʜᴀʏ {mention},\nᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ:\nꜱᴇʟᴇᴄᴛ 'ᴅᴇꜰᴀᴜʟᴛ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ' ɪꜰ ʏᴏᴜ ᴋɴᴏᴡ ᴄᴏʀʀᴇᴄᴛ ᴘʀᴏᴍᴘᴛ\n**ᴏʀ**\nꜱᴇʟᴇᴄᴛ 'ᴀᴅᴠ ᴀɪ ꜱᴇᴛᴛɪɴɢꜱ' ᴛᴏ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ ᴘʀᴏᴍᴘᴛ ꜱᴇᴛᴛɪɴɢꜱ. {status}", reply_markup=reply_markup,disable_web_page_preview=True)
        return
    
    await update.reply(text=f"ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛᴏʀ ᴜꜱᴀɢᴇ: /image cute cats {status} \n "+PROMO,disable_web_page_preview=True)


def is_chat_text_filter():
    async def funcc(_, __, update):
        if bool(update.text):
            return not update.text.startswith("/")
        return False
    return filters.create(funcc)

#NewFeature
import pyrogram
from pyrogram import filters
import soundfile as sf
import os
import speech_recognition as sr
from gtts import gTTS
import os
import emoji
import re
import logging
import urllib.parse
import emoji


def remove_asterisks(text):
    # Remove asterisks using regex
    return re.sub(r'\*', '', text)


# Function to remove links from text
def remove_links(text):
    # Remove links using regex
    return re.sub(r'http\S+', '', text)


# Function to remove emojis from text
def remove_emojis(text):
    # Remove emojis using a different approach
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', text)




def ogg_to_wav(input_path, output_path):
    audio, sr = sf.read(input_path)
    sf.write(output_path, audio, sr, format="WAV")

@pyro.on_message(filters.command("presettings") & filters.private |filters.command("presettings")& filters.group )
async def handle_voice(bot, update):
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"**ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}** "
    else :
        stc=random.choice(standard_user_emojis)
        status=f"**ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} **"
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return

    username = update.from_user.username
    if not username:
        username = "@AdvAIWorld"
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info = f"\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}\n\n  "
    # if update.from_user.id not in allow:
    #     ch=str(update.chat.id)
    #     ch=ch[0]
    #     if ch != "-":
    #         await bot.send_message(chat_id=update.chat.id, text="You are not a premium user. Become a premium user to access this feature.")
    #     return
    if update.from_user.id not in vcpre:
        vcpre[update.from_user.id]="text"
    bun1="ᴛᴇxᴛ  "
    bun2 ="ᴠᴏɪᴄᴇ "
    if vcpre[update.from_user.id]=="text":
         bun1+="✅"
    elif vcpre[update.from_user.id]=="voice":
         bun2+="✅"
    cun=vcpre[update.from_user.id]
    help_text=f"ᴄᴜʀʀᴇɴᴛʟʏ ᴀɴꜱᴡᴇʀɪɴɢ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ '{cun}'\n\n ᴄʜᴀɴɢᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴜꜱɪɴɢ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ: "
    bordered_message = f"<b>{help_text}</b>"
    reply_markup = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(bun1, callback_data="text"),
                InlineKeyboardButton(bun2, callback_data="voice"),
                ]
            ]
        )
    await bot.send_message(chat_id=update.chat.id, text=bordered_message,reply_markup=reply_markup)
    await bot.send_message(chat_id=STCLOG, text="PreSetting Accessed "+info )


@pyro.on_message(filters.voice & filters.private | filters.voice & filters.group | filters.audio)
async def handle_voice(bot, update):
    print("YS")
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users() + load_members_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        Status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        Status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{Status}]({rlink})**  "
        
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id}  {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    # if update.from_user.id not in allow:
    #     ch=str(update.chat.id)
    #     ch=ch[0]
    #     if ch != "-":
    #         await bot.send_message(chat_id=update.chat.id, text="ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ. ʙᴇᴄᴏᴍᴇ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ.")
    #     return
    if update.from_user.id not in vcpre:
        vcpre[update.from_user.id]="text"
    bot_name="AdvChatGptBot"
    # Get the file ID of the voice message
    try:
        file_id =  update.voice.file_id 
    except Exception:
        file_id= update.audio.file_id
    reply_text = f"**AdvChatGpt ɪꜱ ʀᴇᴀᴅɪɴɢ ᴠᴏɪᴄᴇ...✨**{status}"
    msg = await update.reply(reply_text,disable_web_page_preview=True)

    # Download the voice message using the file ID
    voice_path = await bot.download_media(file_id)
    await bot.send_audio(chat_id=STCLOG, audio=open(voice_path, 'rb'), caption=info)
    # Convert the voice message to WAV format
    wav_path = voice_path + ".wav"
    ogg_to_wav(voice_path, wav_path)

    # Extract text from the WAV file
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language='en-US')
        Text=text
    except sr.UnknownValueError:
        print("ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴀᴜᴅɪᴏ")
        await msg.edit(f" ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴀᴜᴅɪᴏ ")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        await msg.edit(f"{bot_name} Could not request results from Google Speech Recognition service")
        return
    print(Text)
    try:
        await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": Text}])
        replybck=""
        for i in response:
            replybck+=i

    except Exception as e:
        await bot.send_message(chat_id=STCLOG, text="**#Error_Raised**\n\n"+"Error:"+str(e)+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
        await msg.edit(text="ꜱᴏʀʀʏ, ᴛʜᴇʀᴇ ɪꜱ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ᴇʀʀᴏʀ \nɪ ʜᴀᴠᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴛʜᴇ ᴛᴇᴀᴍ ᴛᴏ ꜰɪx ᴛʜɪꜱ ᴇʀʀᴏʀ.\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ !"+PROMO)
        return
    text=replybck
    try:
        text= text.replace("GPT-3.5", "AdvanceChatGpt")
        text= text.replace("YouBot", "@AdvChatGptBot")
        text= text.replace("You.com", "techycsr.tech")
        text =text.replace("OpenAI", "@AdvAIWorld")
        text =text.replace("Search Query:", " ")
    except Exception as e:
        text = response
        text= text.replace("GPT-3.5", "AdvanceChatGpt")
        text= text.replace("GPTGO","@AdvChatGptBot")
        text= text.replace("YouBot", "@AdvChatGptBot")
        text= text.replace("You.com", "techycsr.tech")
        text =text.replace("OpenAI", "@AdvAIWorld")
    if vcpre[update.from_user.id]=="voice":
        modified_text = remove_links(text)
        modified_text = remove_emojis(modified_text)
        modified_text = remove_asterisks(modified_text)
        try:
             rep=f"**{bot_name} ɪꜱ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ...✨**"
             await msg.edit(text=rep,disable_web_page_preview=True)
             tts = gTTS(text=modified_text, lang='en', tld='com',slow=False)
             audio_path = 'ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ.mp3'
             tts.save(audio_path)
             status=f"​** ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{Status}]({rlink}) **"
             await update.reply_audio(audio_path,caption=f"{status}")
             await msg.delete()
             await bot.send_audio(chat_id=STCLOG, audio=open(audio_path, 'rb'), caption=info)
             os.remove(audio_path)
        except Exception as e:
            await msg.edit(text=text+status+"\n\n**__ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ ,ꜱᴏ ᴜꜱᴇᴅ ᴛʜᴇ ᴛᴇxᴛ ꜰᴏʀᴍᴀᴛ.(ꜰᴏʀ ᴠᴏɪᴄᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ)__** \n"+PROMO,disable_web_page_preview=True)
    elif vcpre[update.from_user.id]=="text":
        await msg.edit(text=text+status+PROMO,disable_web_page_preview=True)
        await bot.send_message(chat_id=STCLOG, text=text+info,disable_web_page_preview=True)
        
    # Remove the temporary WAV file
    os.remove(wav_path)
    os.remove(voice_path)




async def airesponse(query):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        stream=True,
        )
    str=""
    for message in response:
        str+=message
        #print(message, flush=True, end='') 
    return str
@pyro.on_message(is_chat_text_filter() & filters.text & filters.private )
async def chat_handle(bot, update):
    await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return
    
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at  @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive text [{update.text}] from [{update.from_user.id}]")
    if not check_inited(update.from_user.id):
        await bot.send_message(chat_id=update.chat.id, text="Please initialize me first with \new command.")
        logger.warning(f"User [{update.chat.id}] not inited")
    bot_name = EDGES[update.from_user.id]["bot_name"]
    pop = await update.reply(text=waitmsg)
    try:
        await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": update.text}])
        replybck=""
        for i in response:
            replybck+=i

    except Exception as e:
        await bot.send_message(chat_id=STCLOG, text="**#Error_Raised**\n\n"+"Error:"+str(e)+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
        await pop.edit(text="ꜱᴏʀʀʏ, ᴛʜᴇʀᴇ ɪꜱ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ᴇʀʀᴏʀ \nɪ ʜᴀᴠᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴛʜᴇ ᴛᴇᴀᴍ ᴛᴏ ꜰɪx ᴛʜɪꜱ ᴇʀʀᴏʀ.\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ !"+PROMO)
        return
    response=replybck
    response= response.replace("GPT-3.5", "AdvanceChatGpt")
    response= response.replace("YouBot", "@AdvChatGptBot")
    response= response.replace("You.com", "techycsr.tech")
    response =response.replace("OpenAI", "@AdvAIWorld")
    response = response.replace("Search Query:", " ")
    await pop.edit(text=response+status+PROMO,disable_web_page_preview=True)
    await bot.send_message(chat_id=STCLOG, text="**#Query_Raised**\n\n"+"Query ➸  "+update.text+"\n\nAI Response ➸ "+response+"\n#USER_INFO \n"+info,disable_web_page_preview=True)

@pyro.on_message( filters.text & filters.regex(r'^\.(.*)') & filters.group)
async def chat_handle(bot, update):
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return
    
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at  @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details:(Server01)**\n\nUser ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    logger.info(f"Receive commands [{update.command}] from [{ update.from_user.id}]")
    if not check_inited(update.from_user.id):
        await bot.send_message(chat_id=update.chat.id, text="Please initialize me first with \new command.")
        logger.warning(f"User [{update.chat.id}] not inited")
    bot_name = EDGES[update.from_user.id]["bot_name"]
    await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
    pop = await update.reply(text=waitmsg)
    question = update.text[1:] 
    print(question)
    try:
        await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}])
        replybck=""
        for i in response:
            replybck+=i

    except Exception as e:
        await bot.send_message(chat_id=STCLOG, text="**#Error_Raised**\n\n"+"Error:"+str(e)+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
        await pop.edit(text="ꜱᴏʀʀʏ, ᴛʜᴇʀᴇ ɪꜱ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ᴇʀʀᴏʀ \nɪ ʜᴀᴠᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴛʜᴇ ᴛᴇᴀᴍ ᴛᴏ ꜰɪx ᴛʜɪꜱ ᴇʀʀᴏʀ.\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ !"+PROMO)
        return
    response=replybck
    response= response.replace("GPT-3.5", "AdvanceChatGpt")
    response= response.replace("YouBot", "@AdvChatGptBot")
    response= response.replace("You.com", "techycsr.tech")
    response =response.replace("OpenAI", "@AdvAIWorld")
    response = response .replace("Search Query:", " ")
    await pop.edit(text=response+status+PROMO,disable_web_page_preview=True)
    await bot.send_message(chat_id=STCLOG, text="**#Query_Raised**\n\n"+"Query ➸  "+update.text+"\n\nAI Response ➸ "+response+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
   


@pyro.on_message(filters.photo & filters.private)
async def extract_text(bot, update):
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return
    
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at  @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"

       
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details: User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    # Send a "processing" message
    processing_msg = await update.reply("ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛᴇxᴛ ꜰʀᴏᴍ ɪᴍᴀɢᴇ...")

    # Get the largest available version of the image
    if isinstance(update.photo, list):
        photo = update.photo[-1]
    else:
        photo = update.photo

    # Download the image file
    file = await bot.download_media(photo.file_id)

    # Upload the image file to the OCR.Space API
    url = "https://api.ocr.space/parse/image"
    headers = {"apikey": OCR_KEY}
    with open(file, "rb") as image_file:
        response = requests.post(url, headers=headers, files={"image": image_file})

    # Parse the API response to extract the extracted text
    response_data = response.json()
    if response_data["IsErroredOnProcessing"] == False:
        text = response_data["ParsedResults"][0]["ParsedText"]
    else:
        error_message = response_data["ErrorMessage"]
        text = f"Error: Failed to extract text from image. {error_message}"
        await update.reply_photo(photo=file, caption=text + "\nNo text found")
        return

    text = text  # Send the extracted text as the caption of the image
    exc = "\n I have some doubts regarding the above question. Could you please provide me with a detailed answer?"
    if not check_inited(update.from_user.id):
        await bot.send_message(chat_id=update.chat.id, text="Please initialize me first with \new command.")
        logger.warning(f"User [{update.chat.id}] not inited")
    bot_name = EDGES[update.from_user.id]["bot_name"]
    pop = await update.reply(text=waitmsg)
    await processing_msg.delete()
    try:
        await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}])
        replybck=""
        for i in response:
            replybck+=i

    except Exception as e:
        await bot.send_message(chat_id=STCLOG, text="**#Error_Raised**\n\n"+"Error:"+str(e)+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
        await pop.edit(text="ꜱᴏʀʀʏ, ᴛʜᴇʀᴇ ɪꜱ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ᴇʀʀᴏʀ \nɪ ʜᴀᴠᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴛʜᴇ ᴛᴇᴀᴍ ᴛᴏ ꜰɪx ᴛʜɪꜱ ᴇʀʀᴏʀ.\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ !"+PROMO)
        return
    response=replybck
    text= response.replace("GPT-3.5", "AdvanceChatGpt")
    response= response.replace("YouBot", "@AdvChatGptBot")
    response= response.replace("You.com", "techycsr.tech")
    response =response.replace("OpenAI", "@AdvAIWorld")
    response = response.replace("Bing", "AdvChatGpt")
    response = response.replace("Microsoft", "@AdvAIWorld")
    response = response .replace("Search Query:", " ")
    await pop.edit(text=response+PROMO,disable_web_page_preview=True)
    await bot.send_photo(chat_id=STCLOG, photo=file, caption="#Image\n"+info)
    await bot.send_message(chat_id=STCLOG, text="**#Image_Query_Raised**\n\n"+"Query ➸  "+text+"\n\nAI Response ➸ "+response+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
    

@pyro.on_message(filters.command("answer") & filters.group)
async def extract_text(bot, update):
    user_list=  load_members_users()
    premium_users = load_premium_users()
    admin_user =  load_admin()
    block_user = load_block_users()
    allow =load_admin()+load_premium_users()
    user_id = update.from_user.id
    if  user_id not in user_list :
        user_list.append(user_id)
        save_members_user(user_list)
    if user_id in block_user :
        await bot.send_message(chat_id=update.chat.id, text=f"ꜱᴏʀʀʏ , ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀ\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴꜱ ᴀᴛ **@AdvChatGpt** ᴛᴏ ᴜꜱᴇ ᴍᴇ.")
        return
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    
    if await user_is_member(user_id):
        response = f"{BOT_NAME} is thinking..."
    else:
        github_link = "https://t.me/AdvAIWorld"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("​ᴊᴏɪɴ ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ", url=github_link)],
        ])
        mention = user.mention(first_name)
        message_text = FCRMSG.format(mention=mention)
        await bot.send_message(chat_id=update.chat.id, text=message_text, reply_markup=keyboard,disable_web_page_preview=True)
        return
    
    status=""
    if user_id in allow :
        stc=random.choice(premium_user_emojis)
        status=f"ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ{stc}"
    else :
        stc=random.choice(standard_user_emojis)
        status=f"ꜱᴛᴀɴᴅᴀʀᴅ ᴍᴇᴍʙᴇʀ{stc} "

    status=f"​\n\n**ᴜꜱᴇʀ ꜱᴛᴀᴛᴜꜱ [{status}]({rlink})**  "
        
    if not check_inited(update.from_user.id):
        EDGES[update.from_user.id] = copy.deepcopy(USER_TEMPLATE)
        bot_name = BOT_NAME
        try:
            global BING_COOKIE
            EDGES[update.from_user.id]["bot"] = await EdgeGPT.Chatbot.create(cookies=BING_COOKIE)
        except Exception as e:
            logger.exception(f"Failed to initialize for user [{update.from_user.id}]")
            del EDGES[update.from_user.id]
            reply_text = f"{bot_name}: Failed to initialize.({e}) \n**Contact admins at @AdvChatGpt**"
            await update.reply(reply_text)
            return
    username = update.from_user.username 
    if not username:
        username = "AdvChatGpt"
        
    user_id = update.from_user.id
    user = update.from_user
    first_name = user.first_name
    mention = user.mention(first_name)
    info =f"Details: User ➸ {mention}\nUserName ➸ @{username}\nUserID ➸ {user_id} \nUserStatus {status}"
    # Check if the message is a reply to a photo and contains "/answer"
    if update.reply_to_message and update.reply_to_message.photo and update.text == "/answer":
        # Get the file_id of the photo
        photo_file_id = update.reply_to_message.photo.file_id
        bot_name = EDGES[update.from_user.id]["bot_name"]
        pop = await update.reply(text=waitmsg)

        # Download the image file
        file = await bot.download_media(photo_file_id)

        # Upload the image file to the OCR.Space API
        url = "https://api.ocr.space/parse/image"
        headers = {"apikey": OCR_KEY}
        with open(file, "rb") as image_file:
            response = requests.post(url, headers=headers, files={"image": image_file})

        # Parse the API response to extract the extracted text
        response_data = response.json()
        if response_data["IsErroredOnProcessing"] == False:
            text = response_data["ParsedResults"][0]["ParsedText"]
        else:
            error_message = response_data["ErrorMessage"]
            text = f"Error: Failed to extract text from image. {error_message}"
            await bot.send_photo(chat_id=STCLOG, photo=file, caption=text + info)
            await update.reply_photo(photo=file, caption=text)
            return
        
        #response, reply_markup = await bingAI(update.from_user.id, text)
        try:
            await bot.send_chat_action(chat_id=update.chat.id, action=enums.ChatAction.TYPING)
            response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}])
            replybck=""
            for i in response:
                replybck+=i
        except Exception as e:
            await bot.send_message(chat_id=STCLOG, text="**#Error_Raised**\n\n"+"Error:"+str(e)+"\n#USER_INFO \n"+info,disable_web_page_preview=True)
            await pop.edit(text="ꜱᴏʀʀʏ, ᴛʜᴇʀᴇ ɪꜱ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ᴇʀʀᴏʀ \nɪ ʜᴀᴠᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴛʜᴇ ᴛᴇᴀᴍ ᴛᴏ ꜰɪx ᴛʜɪꜱ ᴇʀʀᴏʀ.\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ !"+PROMO)
            return
        response=replybck
        response = response.replace("Bing", "AdvChatGpt")
        response = response.replace("Microsoft", "@AdvAIWorld")
        response = response .replace("Search Query:", " ")
        await pop.edit(text=response +status+PROMO,disable_web_page_preview=True)
        await bot.send_photo(chat_id=STCLOG, photo=file, caption="#Image (GroupServerActivated)\n" + info)
        await bot.send_message(chat_id=STCLOG, text="**#Image_Query_Raised**\n\n" + "Query ➸  " + text + "\n\nAI Response ➸ " + response + "\n#USER_INFO \n" + info,disable_web_page_preview=True)
    else:
        message = await update.reply_text("ꜱᴇɴᴅ ᴀ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ɪᴛ ᴡɪᴛʜ '/answer' ᴛᴏ ɢᴇᴛ ᴀɪ ʀᴇꜱᴘᴏɴꜱᴇ ꜰᴏʀ ᴀ ɪᴍᴀɢᴇ."+PROMO)


@pyro.on_message(filters.command("term") & filters.private|filters.command("term") & filters.group)
async def help_handle(bot, update):
  logger.info(f"Receive commands [{update.command}] from [{update.chat.id}]")
  term_text="""
There are the following terms and conditions :

ʙʏ ᴜꜱɪɴɢ ʙᴏᴛ ( @AdvChatGpt_bot ), ʏᴏᴜ ᴀɢʀᴇᴇ ᴛᴏ ʙᴇ ʙᴏᴜɴᴅ ʙʏ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ᴛᴇʀᴍꜱ ᴀɴᴅ ᴄᴏɴᴅɪᴛɪᴏɴꜱ: 

1. ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ᴛʜᴇ ʙᴏᴛ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ʏᴏᴜ ꜰᴏʀ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴏʀ ᴄᴏᴍᴍᴇʀᴄɪᴀʟ ᴜꜱᴇ. ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ ꜰᴏʀ ᴀɴʏ ɪʟʟᴇɢᴀʟ ᴏʀ ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴘᴜʀᴘᴏꜱᴇ.  

2. ᴏᴡɴᴇʀꜱʜɪᴘ ᴀɴᴅ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ʀᴇᴛᴀɪɴꜱ ᴀʟʟ ᴏᴡɴᴇʀꜱʜɪᴘ ᴀɴᴅ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ ʀɪɢʜᴛꜱ ɪɴ ᴛʜᴇ ʙᴏᴛ. ʏᴏᴜ ᴀɢʀᴇᴇ ɴᴏᴛ ᴛᴏ ᴍᴏᴅɪꜰʏ, ᴄᴏᴘʏ, ᴅɪꜱᴛʀɪʙᴜᴛᴇ, ᴛʀᴀɴꜱᴍɪᴛ, ᴅɪꜱᴘʟᴀʏ, ᴘᴇʀꜰᴏʀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴘᴜʙʟɪꜱʜ, ʟɪᴄᴇɴꜱᴇ, ᴄʀᴇᴀᴛᴇ ᴅᴇʀɪᴠᴀᴛɪᴠᴇ ᴡᴏʀᴋꜱ ꜰʀᴏᴍ, ᴛʀᴀɴꜱꜰᴇʀ, ᴏʀ ꜱᴇʟʟ ᴀɴʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ, ꜱᴏꜰᴛᴡᴀʀᴇ, ᴘʀᴏᴅᴜᴄᴛꜱ, ᴏʀ ꜱᴇʀᴠɪᴄᴇꜱ ᴏʙᴛᴀɪɴᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ʙᴏᴛ.

 3. ᴅᴀᴛᴀ ᴘʀɪᴠᴀᴄʏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴍᴀʏ ᴄᴏʟʟᴇᴄᴛ ᴀɴᴅ ᴜꜱᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ. ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴏɴꜱᴇɴᴛ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ'ꜱ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴜꜱᴇ ᴏꜰ ꜱᴜᴄʜ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ. ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴡɪʟʟ ɴᴏᴛ ꜱʜᴀʀᴇ ʏᴏᴜʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴡɪᴛʜ ᴛʜɪʀᴅ ᴘᴀʀᴛɪᴇꜱ ᴜɴʟᴇꜱꜱ ʀᴇQᴜɪʀᴇᴅ ʙʏ ʟᴀᴡ.  

4. ɴᴏ ᴡᴀʀʀᴀɴᴛʏ ᴛʜᴇ ʙᴏᴛ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ "ᴀꜱ ɪꜱ" ᴡɪᴛʜᴏᴜᴛ ᴡᴀʀʀᴀɴᴛʏ ᴏꜰ ᴀɴʏ ᴋɪɴᴅ. ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴅᴏᴇꜱ ɴᴏᴛ ɢᴜᴀʀᴀɴᴛᴇᴇ ᴛʜᴇ ᴀᴄᴄᴜʀᴀᴄʏ, ᴄᴏᴍᴘʟᴇᴛᴇɴᴇꜱꜱ, ᴏʀ ᴜꜱᴇꜰᴜʟɴᴇꜱꜱ ᴏꜰ ᴛʜᴇ ʙᴏᴛ. 

5. ʟɪᴍɪᴛᴀᴛɪᴏɴ ᴏꜰ ʟɪᴀʙɪʟɪᴛʏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ꜱʜᴀʟʟ ɴᴏᴛ ʙᴇ ʟɪᴀʙʟᴇ ꜰᴏʀ ᴀɴʏ ᴅɪʀᴇᴄᴛ, ɪɴᴅɪʀᴇᴄᴛ, ɪɴᴄɪᴅᴇɴᴛᴀʟ, ꜱᴘᴇᴄɪᴀʟ, ᴏʀ ᴄᴏɴꜱᴇQᴜᴇɴᴛɪᴀʟ ᴅᴀᴍᴀɢᴇꜱ ᴀʀɪꜱɪɴɢ ᴏᴜᴛ ᴏꜰ ᴏʀ ɪɴ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴡɪᴛʜ ᴛʜᴇ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ. 

6. ɪɴᴅᴇᴍɴɪꜰɪᴄᴀᴛɪᴏɴ ʏᴏᴜ ᴀɢʀᴇᴇ ᴛᴏ ɪɴᴅᴇᴍɴɪꜰʏ, ᴅᴇꜰᴇɴᴅ, ᴀɴᴅ ʜᴏʟᴅ ʜᴀʀᴍʟᴇꜱꜱ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴀɴᴅ ɪᴛꜱ ᴏꜰꜰɪᴄᴇʀꜱ, ᴅɪʀᴇᴄᴛᴏʀꜱ, ᴇᴍᴘʟᴏʏᴇᴇꜱ, ᴀɴᴅ ᴀɢᴇɴᴛꜱ ꜰʀᴏᴍ ᴀɴʏ ᴀɴᴅ ᴀʟʟ ᴄʟᴀɪᴍꜱ, ʟɪᴀʙɪʟɪᴛɪᴇꜱ, ᴅᴀᴍᴀɢᴇꜱ, ʟᴏꜱꜱᴇꜱ, ᴏʀ ᴇxᴘᴇɴꜱᴇꜱ, ɪɴᴄʟᴜᴅɪɴɢ ʀᴇᴀꜱᴏɴᴀʙʟᴇ ᴀᴛᴛᴏʀɴᴇʏꜱ' ꜰᴇᴇꜱ, ᴀʀɪꜱɪɴɢ ᴏᴜᴛ ᴏꜰ ᴏʀ ɪɴ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴡɪᴛʜ ʏᴏᴜʀ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ.  

7. ᴛᴇʀᴍɪɴᴀᴛɪᴏɴ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴍᴀʏ ᴛᴇʀᴍɪɴᴀᴛᴇ ʏᴏᴜʀ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ᴀᴛ ᴀɴʏ ᴛɪᴍᴇ ᴡɪᴛʜᴏᴜᴛ ɴᴏᴛɪᴄᴇ. ᴜᴘᴏɴ ᴛᴇʀᴍɪɴᴀᴛɪᴏɴ, ʏᴏᴜ ᴍᴜꜱᴛ ᴄᴇᴀꜱᴇ ᴀʟʟ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ᴀɴʏ ᴄᴏᴘɪᴇꜱ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴘᴏꜱꜱᴇꜱꜱɪᴏɴ. 

8. ɢᴏᴠᴇʀɴɪɴɢ ʟᴀᴡ ᴀɴᴅ ᴊᴜʀɪꜱᴅɪᴄᴛɪᴏɴ ᴛʜɪꜱ ᴀɢʀᴇᴇᴍᴇɴᴛ ꜱʜᴀʟʟ ʙᴇ ɢᴏᴠᴇʀɴᴇᴅ ʙʏ ᴀɴᴅ ᴄᴏɴꜱᴛʀᴜᴇᴅ ɪɴ ᴀᴄᴄᴏʀᴅᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟᴀᴡꜱ ᴏꜰ ᴛʜᴇ ᴊᴜʀɪꜱᴅɪᴄᴛɪᴏɴ ɪɴ ᴡʜɪᴄʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ɪꜱ ʟᴏᴄᴀᴛᴇᴅ. ᴀɴʏ ʟᴇɢᴀʟ ᴀᴄᴛɪᴏɴ ᴏʀ ᴘʀᴏᴄᴇᴇᴅɪɴɢ ᴀʀɪꜱɪɴɢ ᴏᴜᴛ ᴏꜰ ᴏʀ ɪɴ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴡɪᴛʜ ᴛʜɪꜱ ᴀɢʀᴇᴇᴍᴇɴᴛ ꜱʜᴀʟʟ ʙᴇ ʙʀᴏᴜɢʜᴛ ɪɴ ᴛʜᴇ ᴄᴏᴜʀᴛꜱ ᴏꜰ ᴛʜᴀᴛ ᴊᴜʀɪꜱᴅɪᴄᴛɪᴏɴ.  

9. ᴇɴᴛɪʀᴇ ᴀɢʀᴇᴇᴍᴇɴᴛ ᴛʜɪꜱ ᴀɢʀᴇᴇᴍᴇɴᴛ ᴄᴏɴꜱᴛɪᴛᴜᴛᴇꜱ ᴛʜᴇ ᴇɴᴛɪʀᴇ ᴀɢʀᴇᴇᴍᴇɴᴛ ʙᴇᴛᴡᴇᴇɴ ʏᴏᴜ ᴀɴᴅ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ʀᴇɢᴀʀᴅɪɴɢ ᴛʜᴇ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ꜱᴜᴘᴇʀꜱᴇᴅᴇꜱ ᴀʟʟ ᴘʀɪᴏʀ ᴀɢʀᴇᴇᴍᴇɴᴛꜱ ᴀɴᴅ ᴜɴᴅᴇʀꜱᴛᴀɴᴅɪɴɢꜱ, ᴡʜᴇᴛʜᴇʀ ᴡʀɪᴛᴛᴇɴ ᴏʀ ᴏʀᴀʟ.  

10. ᴄᴏɴᴛᴀᴄᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ᴀɢʀᴇᴇᴍᴇɴᴛ, ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴀᴛ ᴀᴅᴠᴀɴᴄᴇ ᴄʜᴀᴛ ɢʀᴏᴜᴘ .  ʙʏ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴀɢʀᴇᴇ ᴛᴏ ʙᴇ ʙᴏᴜɴᴅ ʙʏ ᴛʜᴇꜱᴇ ᴛᴇʀᴍꜱ ᴀɴᴅ ᴄᴏɴᴅɪᴛɪᴏɴꜱ. ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ᴀɢʀᴇᴇ ᴛᴏ ᴛʜᴇꜱᴇ ᴛᴇʀᴍꜱ ᴀɴᴅ ᴄᴏɴᴅɪᴛɪᴏɴꜱ, ʏᴏᴜ ꜱʜᴏᴜʟᴅ ɴᴏᴛ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ.  

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @AdvAIWorld
"""
  url = "https://t.me/AdvChatGpt"
  
  keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🌐 ᴀᴅᴠ ᴀɪ ᴡᴏʀʟᴅ ", url=url)],
  ])
  await bot.send_message(chat_id=update.chat.id, text=term_text, reply_markup=keyboard)
  


@pyro.on_callback_query(is_allowed_filter())
async def callback_query_handle(bot, query):
    if not check_inited(query.from_user.id):
        await bot.send_message(chat_id=query.from_user.id, text="Please initialize me first.")
        logger.warning(f"User [{query.from_user.id}] try to send callback query but been rejected (not initialized).")
        return
    query_text = EDGES[query.from_user.id]["temp"].get(query.data)
    logger.info(f"Receive callback query [{query.data}: {query_text}] from [{query.from_user.id}]")
    if query_text is None:
        await bot.send_message(chat_id=query.from_user.id, text="Sorry, the callback query is not found.(May be you have restarted the bot before.)")
        return
    bot_name = EDGES[query.from_user.id]["bot_name"]
    response = f"{bot_name} is thinking..."
    msg = await bot.send_message(chat_id=query.from_user.id, text=response)
    if EDGES[query.from_user.id]["response"] == "normal":
        response, reply_markup = await bingAI(query.from_user.id, query_text)
        await msg.edit(text=response, reply_markup=reply_markup)
    elif EDGES[query.from_user.id]["response"] == "stream":
        try:
            async for final, response, reply_markup in bingAIStream(query.from_user.id, query_text):
                if final:
                    await msg.edit(text=response, reply_markup=reply_markup)
                else:
                    if response == "":
                        continue
                    await msg.edit(text=response)
        except Exception as e:
            logger.error("There seems an error at upsteam library, update the upsteam may help.")
            logger.exception(f"[callback_query_handle, unexpected error]: {e}")
            await msg.edit(text=f"Something went wrong, please check the logs.\n\n[{e}]")
            raise e

async def aires(strs):
    response = await g4f.ChatCompletion.create_async(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content":strs}])
    replybck=""
    for i in response:
        replybck+=i
    response=replybck
    #print(response)
    response = response.replace("Bing", "AdvChatGpt")
    response = response.replace("Microsoft", "@AdvAIWorld")
    response = response.replace("Search Query:", " ")
    return response



@pyro.on_inline_query()
async def inline_query_prompt_select_handle(bot, update):
    
    
    if update.query.endswith("?"):
        query = update.query 
        print(query)
        global ans
        ans=""
        ans=await aires(query)

        try :
            await update.answer(
                results=[
                    InlineQueryResultArticle(
                        title=f"Q: {query} 🔗",
                        input_message_content=InputTextMessageContent(
                             f"<b>Q: {query}\n\n{ans}\n\n||**@AdvChatGptBot**||</b>"
                             ),
                             description=f"{ans}",
                             #reply_markup=reply_markup,
                             )
                ],
                cache_time=1)
            
        except Exception:
            await update.answer(
                results=[
                    InlineQueryResultArticle(
                        title=f"Q: {query} 🔗",
                        input_message_content=InputTextMessageContent(
                             f"<b>Q: {query}\n\n{ans}\n\n||**@AdvChatGptBot**||</b>"
                             ),
                             description=f"{ans}",
                             #reply_markup=reply_markup,
                             )
                ],
                cache_time=1)


            
    else:
        await update.answer(
            results=[
                InlineQueryResultArticle(
                    #thumb_url=STCLOGO,
                    title=f"AdvChatGpt Inline Search.",
                    input_message_content=InputTextMessageContent(
                        f"Search Inline using this Pattern:\n` @AdvChatgptBot 'YourQuestion' ?\n\nNote: QuestionMark(?) at the end of YourQuestion is necessary  \n\n ||**@AdvChatGptBot**||"
                    ),
                    description=f"Use this Pattern:\n@AdvChatgpt <YourQuestion> ?\nAdd `?` after every 5 seconds.",
                    #reply_markup=reply_markup,
                    
                )
            ],
            cache_time=2)

    
    
    

    
"""

def is_prompt_select_filter():
    async def funcp(_, __, update):
        return update.query.startswith("p")
    return filters.create(funcp)

@pyro.on_inline_query(is_allowed_filter() & is_prompt_select_filter())
async def inline_query_prompt_select_handle(bot, update):

    if not check_inited(update.from_user.id):
        logger.warning(f"User [{update.from_user.id}] try to send inline_query prompt select result but been rejected (not initialized).")
        await update.answer(
            results=[
                InlineQueryResultArticle(
                    title="Not initialized",
                    input_message_content=InputTextMessageContent(
                        "Not initialized"
                    ),
                    description="Please initialize me first.",
                )
            ],
            cache_time=1
        )
        return
    tmp = update.query.split(" ", 1)
    query = ""
    if len(tmp) >= 2:
        query = tmp[1]
    logger.info(f"Receive inline_query prompt select result [{query}] from [{update.from_user.id}]")
    await update.answer(
        results=[
            InlineQueryResultArticle(
                title="PromptSelector",
                input_message_content=InputTextMessageContent(
                    "[Not Supported Yet]Use `@BotName p &lt;query>` to select Prompt. You should use this to send message to AI bot."
                ),
                description="[Not Supported Yet]Click me to show usage of PromptSelector",
            )
        ],
        cache_time=1
    )

def is_default_inline_filter():
    async def funcd(_, __, update):
        return not update.query.startswith("p") and update.query.startswith("%")
    return filters.create(funcd)

@pyro.on_inline_query(is_allowed_filter() & is_default_inline_filter())
async def inline_query_default_handle(bot, update):
    if not check_inited(update.from_user.id):
        logger.warning(f"User [{update.from_user.id}] try to send inline_query default result but been rejected (not initialized).")
        await update.answer(
            results=[
                InlineQueryResultArticle(
                    title="Not initialized",
                    input_message_content=InputTextMessageContent(
                        "Not initialized"
                    ),
                    description="Please initialize me first.",
                )
            ],
            cache_time=1
        )
        return
    logger.info(f"Receive default result [{update.query}] from [{update.from_user.id}]")
    await update.answer(
        results=[
            InlineQueryResultArticle(
                title="ImageGenerator",
                input_message_content=InputTextMessageContent(
                    # "Usage: Use `@BotName g &lt;prompt>` to generate image. Prompt should be in English, If prompt is not in English, it will automatically use AI to translate prompt to English."
                    "Usage: Use `@BotName g &lt;prompt>` to generate image. (Tips: If it take long time (25s) no response, you can add a '%' and delete it to refresh)"
                ),
                description="Click me to show usage of ImageGenerator",
            ),
            InlineQueryResultArticle(
                title="PromptSelector",
                input_message_content=InputTextMessageContent(
                    "[Not Supported Yet]Use `@BotName p &lt;query>` to select Prompt. You should use this to send message to AI bot."
                ),
                description="[Not Supported Yet]Click me to show usage of PromptSelector",
            )
        ],
        cache_time=1
    )
"""


async def bingAI(user_id, messageText):
    rsp = await EDGES[user_id]["bot"].ask(prompt=messageText, conversation_style=EDGES[user_id]["style"])
    rsp_json = json.dumps(rsp, ensure_ascii=False)
    logger.info(f"BingAI raw response: {rsp_json}")

    response, msg_suggest = process_message_main(rsp, user_id)
    return response, msg_suggest

async def bingAIStream(user_id, messageText):
    last_time = time.time() - 0.5 
    async for final, rsp in  EDGES[user_id]["bot"].ask_stream(prompt=messageText, conversation_style=EDGES[user_id]["style"]):
        now_time = time.time()
        if final:
            rsp_json = json.dumps(rsp, ensure_ascii=False)
            logger.info(f"BingAI stream response final: {rsp_json}")
            
            response, msg_suggest = process_message_main(rsp, user_id)
            yield final, response, msg_suggest

        if now_time - last_time > EDGES[user_id]["interval"] and not final:
            last_time = now_time
            logger.info(f"BingAI stream response: {rsp}")
            if type(rsp) == str:
                rsp = rsp.strip()
                if "Searching the web for:" in rsp:
                    if "Generating answers for you..." in rsp:
                        search_rsp = rsp.split("Generating answers for you...", 1)
                        rsp = ""
                        for line in search_rsp[0].split("\n"):
                            if "Searching the web for:" in line:
                                rsp += line + "\n"
                        if search_rsp[1].strip().startswith("[1]: "): 
                            search_rsp[1] = search_rsp[1].split("\n\n", 1)[1]
                        rsp += "\nGenerating answers for you...\n" + search_rsp[1]
                response = re.sub(r'\[\^(\d+)\^\]', '', rsp)
                
            else:
                response = "[WARN] BingAI stream response: Returned non-string type data without final"
                logger.warning(f"BingAI stream response: Returned non-string type data without final")
            yield final, response, ""

def process_message_main(rsp_obj, user_id=None):
    response = RESPONSE_TEMPLATE
    if "messages" in rsp_obj["item"]:
        bot_messages = rsp_obj["item"]["messages"]
        search_query = ""
        for message in bot_messages:
            if "messageType" in message:
                if message["messageType"] == "InternalSearchQuery":
                    search_query += "#" + message["hiddenText"].replace(" ", "_") + "\n"
            if "sourceAttributions" in message or "suggestedResponses" in message or "spokenText" in message :
                msg_main_body, msg_ref, msg_suggest = process_message_body(message, user_id)
        msg_main = msg_main_body + "\n\nSearch Query:\n" + search_query
    elif "result" in rsp_obj["item"]:
        logger.warning(f"[process_message_main] BingAI result: {json.dumps(rsp_obj['item']['result'], ensure_ascii=False)}")
        if rsp_obj["item"]["result"]["value"] == "InvalidSession":
            response = "Invalid Session (may be session expired), Please /reset the chat"
            return response, None
        elif rsp_obj["item"]["result"]["value"] == "Throttled":
            response = "Request is throttled (You request may contain sensitive content), Please /reset the chat"
            return response, None
        else:
            if "message" in rsp_obj["item"]["result"]:
                response = rsp_obj["item"]["result"]["message"] + "Please /reset the chat"
            response = "Something wrong. Please /reset the chat"
            return response, None
    else:
        logger.warning(f"[process_message_main] BingAI response: {json.dumps(rsp_obj, ensure_ascii=False)}")
        response = "Something wrong. Please /reset the chat"
        return response, None
        
    throttlingMax = rsp_obj["item"]["throttling"]["maxNumUserMessagesInConversation"]
    throttlingUser = rsp_obj["item"]["throttling"]["numUserMessagesInConversation"]
    msg_throttling = f"Messages: {throttlingUser}/{throttlingMax}"
    if throttlingUser >= throttlingMax:
        asyncio.run(EDGES[user_id]["bot"].reset())
        msg_throttling += "\nNote: Conversation is over, and I auto reset it successfully."
    if msg_main == "":
        response = "Something wrong. Please /reset the chat" # default response
    else:
        response = response.format(msg_main=msg_main, msg_ref=msg_ref, msg_throttling=msg_throttling)
    return response, msg_suggest

def process_message_body(msg_obj, user_id=None):
    msg_main = ""
    msg_ref = ""
    msg_suggest = None
    if "text" in msg_obj:
        msg_main = msg_obj["text"]
    if "sourceAttributions" in msg_obj:
        source_count = len(msg_obj["sourceAttributions"]) 
        if re.search(r'\[\^(\d+)\^\]', msg_main) is not None:
            matches = re.findall(r'\[\^(\d+)\^\]', msg_main) 
            for match in matches:
                if int(match) > source_count: 
                    msg_main = msg_main.replace(f"[^{match}^]", "", 1)
                    continue
                url = msg_obj["sourceAttributions"][int(match) - 1]["seeMoreUrl"]
                msg_main = msg_main.replace(f"[^{match}^]", f"[[{match}]]({url})", 1)
            
      
        if source_count > 0:
            msg_ref = "- - - - - - - - -\nReference:\n"
        for ref_index in range(source_count):
            providerDisplayName = msg_obj["sourceAttributions"][ref_index]["providerDisplayName"]
            url = msg_obj["sourceAttributions"][ref_index]["seeMoreUrl"]
            msg_ref += f"{ref_index + 1}. [{providerDisplayName}]({url})\n"

    
    if "suggestedResponses" in msg_obj:
        suggested_count = len(msg_obj["suggestedResponses"])
        if EDGES[user_id]["suggest"]  == "callbackquery":
            msg_suggest = InlineKeyboardMarkup([])
            EDGES[user_id]["temp"] = {}
            for suggested_index in range(suggested_count):
                suggested_text = msg_obj["suggestedResponses"][suggested_index]["text"]
                suggested_hash = str(hash(suggested_text)) 
                EDGES[user_id]["temp"][suggested_hash] = suggested_text
                msg_suggest.inline_keyboard.append([InlineKeyboardButton(suggested_text, callback_data=suggested_hash)])
        elif EDGES[user_id]["suggest"] == "replykeyboard":
            msg_suggest = ReplyKeyboardMarkup([])
            for suggested_index in range(suggested_count):
                suggested_text = msg_obj["suggestedResponses"][suggested_index]["text"]
                msg_suggest.keyboard.append([suggested_text])
        else:
            msg_ref += "- - - - - - - - -\nSuggestion(Click to copy):\n"
            for suggested_index in range(suggested_count):
                suggested_text = msg_obj["suggestedResponses"][suggested_index]["text"]
                msg_ref += f"{suggested_index + 1}. `{suggested_text}`\n"

    return msg_main, msg_ref, msg_suggest

async def image_gen_main(prompt, image_gen_cookie_u, all_cookies: List[Dict] = None):
    if all_cookies is None:
        async with ImageGenAsync(image_gen_cookie_u) as image_generator:
            images = await image_generator.get_images(prompt)
            return images
    else:
        async with ImageGenAsync(image_gen_cookie_u, all_cookies=all_cookies) as image_generator:
            images = await image_generator.get_images(prompt)
            return images






#AdditionalFunctions


premium_file = r"database/premium.txt"
admin_file=r"database/admin.txt"
block_file=r"database/block.txt"
group_file=r"database/group.txt"
user_file=r"database/user.txt"

# Load premium user IDs from file
def load_premium_users():
    try:
        with open(premium_file, "r") as file:
            users = file.read().splitlines()
            return [int(user) for user in users]
    except FileNotFoundError:
        return []
    
def load_admin():
    try:
        with open(admin_file, "r") as file:
            users = file.read().splitlines()
            return [int(user) for user in users]
    except FileNotFoundError:
        return []
    
def load_block_users():
    try:
        with open(block_file, "r") as file:
            users = file.read().splitlines()
            return [int(user) for user in users]
    except FileNotFoundError:
        return []

def load_group_users():
    try:
        with open(group_file, "r") as file:
            users = file.read().splitlines()
            return [int(user) for user in users]
    except FileNotFoundError:
        return []


def load_members_users():
    try:
        with open(user_file, "r") as file:
            users = file.read().splitlines()
            return [int(user) for user in users]
    except FileNotFoundError:
        return []


# Save premium user IDs to file
def save_premium_users(users):
    with open(premium_file, "w") as file:
        file.write("\n".join(str(user) for user in users))
        
def save_admin_users(users):
    with open(admin_file, "w") as file:
        file.write("\n".join(str(user) for user in users))
        
def save_block_users(users):
    with open(block_file, "w") as file:
        file.write("\n".join(str(user) for user in users))

def save_groups_user(users):
    with open(group_file, "w") as file:
        file.write("\n".join(str(user) for user in users))

def save_members_user(users):
    with open(user_file, "w") as file:
        file.write("\n".join(str(user) for user in users))



        
# Define the list of premium user IDs
premium_users = load_premium_users()
admin_user =  load_admin()
block_user = load_block_users()
allow =load_admin()+load_premium_users()
vocpre=premium_users

block_user = load_block_users()
user_list=  load_members_users()
#print(user_list,type(user_list))
group_list= load_group_users()


standard_user_emojis = ["🌟", "🌿", "🌍"]
premium_user_emojis = [
    "🌟✨", "⭐💎", "🔥⭐", "👑🌟", "💡⭐️",
    "💫🌟", "🌈✨", "🌟✨️", "⭐💫", "🔥💎",
    "💎💍", "👑💫", "✨🔥", "⭐⚡️", "🌟🎉",
    "💡💫", "✨🍾", "⭐🌺", "🔥✨", "💎🎁",
    "👑✨", "✨💫", "✨🎶", "🌟✨", "💡🎁",
    "⭐🎁", "🔥✨", "💎🌟", "👑⚜️", "💫🌍",
    "🎶✨", "🌍⭐", "🔥🌕", "💎✨", "👑✨",
]




@pyro.on_message(filters.command("apre"))
def add_premium_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    user_id = int(update.text.split()[1])
    if user_id not in premium_users:
        premium_users.append(user_id)
        save_premium_users(premium_users)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been added to the premium list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#Premium\nUser ID {user_id}has been added to the premium list.\nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is already in the premium list.")

# Handle the "/rpre" command
@pyro.on_message(filters.command("rpre"))
def remove_premium_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    user_id = int(update.text.split()[1])
    if user_id in premium_users:
        premium_users.remove(user_id)
        save_premium_users(premium_users)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been removed from the premium list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#Premium\nUser ID {user_id}has been removed from the premium list. \nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is not in the premium list.")

@pyro.on_message(filters.command("aadmin"))
def add_admin_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    user_id = int(update.text.split()[1])
    if user_id not in admin_user:
        admin_user.append(user_id)
        save_admin_users(admin_user)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been added to the admin list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#admin\nUser ID {user_id}has been added to the admin list. \nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is already in the admin list.")

# Handle the "/radmin" command
@pyro.on_message(filters.command("radmin"))
def remove_admin_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    user_id = int(update.text.split()[1])
    if user_id in admin_user:
        admin_user.remove(user_id)
        save_admin_users(admin_user)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been removed from the admin list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#Admin\nUser ID {user_id} as been removed from the admin list.\nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is not in the admin list.")

@pyro.on_message(filters.command("ablock"))
def add_block_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    user_id = int(update.text.split()[1])
    if user_id not in block_user:
        block_user.append(user_id)
        save_block_users(block_user)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been added to the block list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#Block\nUser ID {user_id} has been added to the block list.\nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is already in the block list.")

# Handle the "/rblock" command
@pyro.on_message(filters.command("rblock"))
def remove_block_command(bot, update):
    if update.from_user.id not in sudo:
        bot.send_message(chat_id=update.chat.id, text="Only sudo users can use this command")
        return
    
    user_id = int(update.text.split()[1])
    if user_id in block_user:
        block_user.remove(user_id)
        save_block_users(block_user)
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} has been removed from the block list.")
        user_ids = update.from_user.id
        user = update.from_user
        first_name = user.first_name
        mention = user.mention(first_name)
        bot.send_message(chat_id=STCLOG, text=f"#Block\nUser ID {user_id} has been removed from the block list \nAdmin:\n{user_ids}\n{mention}.")
    else:
        bot.send_message(chat_id=update.chat.id, text=f"User ID {user_id} is not in the block list.")




@pyro.on_message(filters.command("ginfo") & filters.private & filters.chat(sudo) )
async def get_group_info(client, message):
    group_id = message.text.split()[1]  # Extract the group ID from the command message
    chat = await client.get_chat(int(group_id))

    # Extract various group details
    group_title = chat.title
    group_type = chat.type
    group_members_count = chat.members_count
    group_username = chat.username or "N/A"
    try:
        group_invite_link = await client.export_chat_invite_link(int(group_id))
    except Exception as e:
        print(f"Failed to get link : {e}")
        group_invite_link= e
    group_description = chat.description or "N/A"

    # Prepare the message with group information
    info_message = f"<b>Group ID:</b> {group_id}\n"
    info_message += f"<b>Title:</b> {group_title}\n"
    info_message += f"<b>Type:</b> {group_type}\n"
    info_message += f"<b>Members Count:</b> {group_members_count}\n"
    info_message += f"<b>Username:</b> @{group_username}\n"
    info_message += f"<b>Invite Link:</b> {group_invite_link}\n"
    info_message += f"<b>Description:</b> {group_description}\n"
    info_message +=PROMO
    # Send the group information message
    await client.send_message(chat_id=message.chat.id, text=info_message)
    await client.send_message(chat_id=STCLOG, text="**#Ginfo\**"+info_message)





@pyro.on_message(filters.command("invite") &  filters.private & filters.chat(sudo))
async def invite_command(client, message):
    chat_id = message.text.split(" ")[1]

    try:
        chat_invite_link = await client.export_chat_invite_link(int(chat_id))
        await message.reply_text(f"Invite link for group {chat_id}:\n{chat_invite_link}"+PROMO)
    except Exception as e:
        await message.reply_text(f"Failed to get invite link for group {chat_id}.\nError: {e}"+PROMO)


@pyro.on_message(filters.command("uinfo") &  filters.private & filters.chat(sudo))
async def info_command(client, message):
    user_id = message.text.split(" ")[1]

    try:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        last_name = user.last_name if user.last_name else ""
        username = user.username if user.username else ""
        mention = user.mention(first_name)

        info_message = f"User Info:\n\nFirst Name: {first_name}\nLast Name: {last_name}\nUsername: @{username}\nMention: {mention}\nUser ID: {user_id}"
        info_message += f"\n\nAdditional Info:"
        info_message += f"\nStatus: {user.status}"
        info_message += f"\nIs Bot: {user.is_bot}"
        info_message += f"\nIs Verified: {user.is_verified}"
        info_message += f"\nIs Support: {user.is_support}"
        info_message += f"\nData Center ID: {user.dc_id}"
        info_message += f"\nLanguage Code: {user.language_code}"
        await message.reply_text(info_message)
    except Exception as e:
        await message.reply_text(f"Failed to get user info for ID {user_id}.\nError: {e}")


@pyro.on_message(filters.new_chat_members)
async def new_chat_members(client, message):
    user = message.from_user
    added_members = message.new_chat_members
    chat = message.chat
    bot = await client.get_me()
    bot_id = bot.id
    group_list= load_group_users()
    if chat.id not in group_list:
        group_list.append(chat.id)
        save_groups_user(group_list)
        await client.send_message(chat_id=STCLOG , text=f"Group ID {chat.id} has been added to group list.")
    

    for member in added_members:
        if member.id == bot_id:
            nam=user.mention(user.first_name)
            user_info = f"User: {user.mention(user.first_name)}\nUsername: @{user.username}\nID: {user.id}"
            group_info = f"Group ID: `{chat.id}`"
            # Get the member count
            try:
                members_count = await client.get_chat_members_count(chat.id)
                group_info += f"\nMembers: {members_count}"
            except Exception as e:
                print(f"Failed to get members count: {e}")

            await client.send_message(
                chat_id=STCLOG,
                text=f"**🎉#New_group! 🎉\nAdded by \n{user_info}\nGroup info\n{group_info}**",
            )
            message_text =f"🎉 **ᴛʜᴀɴᴋ ʏᴏᴜ {nam} ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ!** 🎉\n"

            message_text += """
🤖 ɴᴏᴡ, ᴋɪɴᴅʟʏ ɢʀᴀɴᴛ ᴍᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ ꜱᴏ ᴛʜᴀᴛ ɪ ᴄᴀɴ ᴡᴏʀᴋ ᴇꜰꜰᴇᴄᴛɪᴠᴇʟʏ.
ɪ ʀᴇQᴜɪʀᴇ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛꜱ:

✅ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ- ᴛʜɪꜱ ᴡɪʟʟ ʜᴇʟᴘ ᴍᴇ ᴋᴇᴇᴘ ᴛʜᴇ ᴄʜᴀᴛ ᴄʟᴇᴀɴ ᴀɴᴅ ᴏʀɢᴀɴɪᴢᴇᴅ.
✅ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ - ɪ ᴄᴀɴ ᴀꜱꜱɪꜱᴛ ɪɴ ʙʀɪɴɢɪɴɢ ᴍᴏʀᴇ ᴍᴇᴍʙᴇʀꜱ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ.

ᴀꜰᴛᴇʀ ɢʀᴀɴᴛɪɴɢ ᴛʜᴇꜱᴇ ʀɪɢʜᴛꜱ, ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀꜱᴋ ᴍᴇ ᴀɴʏ Qᴜᴇʀɪᴇꜱ ᴏʀ ᴄᴏᴍᴍᴀɴᴅꜱ ʙʏ ꜱᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜ ᴀ ᴅᴏᴛ (.) ʟɪᴋᴇ ᴛʜɪꜱ:

ᴇxᴀᴍᴘʟᴇ: `.ᴡʜᴇʀᴇ ɪꜱ ɪɴᴅɪᴀ?`
ᴇxᴀᴍᴘʟᴇ: `.ᴡʜᴀᴛ'ꜱ ᴛʜᴇ ᴅᴀᴛᴇ ᴛᴏᴅᴀʏ?`

ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ᴏʀ ᴇɴᴄᴏᴜɴᴛᴇʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ, ᴘʟᴇᴀꜱᴇ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴀᴛ **@AdvChatGpt** .

ʟᴇᴛ'ꜱ ᴍᴀᴋᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴀᴡᴇꜱᴏᴍᴇ ᴛᴏɢᴇᴛʜᴇʀ!🚀
"""
            
            
            reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ꜰʀᴇᴇ  ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ", url="https://t.me/AdvChatGpt"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴠ ᴀɪ ᴄᴏᴍᴍᴜɴɪᴛʏ 🔗", url="https://t.me/AdvAIworld"),
                ]
            ]
        )
            await client.send_message(
                chat_id= chat.id,text=message_text+PROMO,reply_markup=reply_markup,disable_web_page_preview=True)




@pyro.on_message(filters.command("gleave") & filters.private & filters.chat(sudo))
async def leave_group(client, message):
    chat_id = message.chat.id
    bot_username = (await client.get_me()).username

    if len(message.command) != 2:
        await message.reply("Invalid command! Please provide a group ID.")
        return

    group_id = int(message.command[1])
    
    try:
        await client.leave_chat(group_id)
        await message.reply("Left the group successfully.")
        await client.send_message(STCLOG, f"#Leave\n Admin-SudoUsers{chat_id} \nReason- Admin Knows\nTask - @{bot_username} left the group {group_id}."+PROMO)
    except pyrogram.errors.FloodWait as e:
        await message.reply(f"Failed to leave the group. Please try again later. Error: {e}")
    except pyrogram.errors.exceptions.ChatAdminRequired as e:
        await message.reply(f"I don't have the necessary permissions to leave the group. Please make sure I have the permission to leave. Error: {e}")
    except Exception as e:
        await message.reply(f"Failed to leave the group. Error: {e}")

@pyro.on_message(filters.command("rate"))
def rate_command(client, message):
    user = message.from_user
    mention = user.mention(user.first_name)
    user_info = f"User: {mention}\nUsername: @{user.username}\nID: {user.id}"

    rate_message = "**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜰᴇᴇᴅʙᴀᴄᴋ ꜰᴏʀᴍ \nᴘʟᴇᴀꜱᴇ ʀᴀᴛᴇ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ᴀɪ ʙᴏᴛ:\n\nɢɪᴠᴇ ᴍᴇ ꜱᴛᴀʀꜱ ⭐  :) **"+PROMO
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⭐️", callback_data="1")],
            [InlineKeyboardButton("⭐️⭐️", callback_data="2")],
            [InlineKeyboardButton("⭐️⭐️⭐️", callback_data="3")],
            [InlineKeyboardButton("⭐️⭐️⭐️⭐️", callback_data="4")],
            [InlineKeyboardButton("⭐️⭐️⭐️⭐️⭐️", callback_data="5")],
        ]
    )

    client.send_message(
        chat_id=message.chat.id,
        text=f"{rate_message}",
        reply_markup=reply_markup,
    )





@pyro.on_message(filters.command("broadcast") & filters.reply & filters.chat(sudo))
def forward_message(client, message):
    replied_message = message.reply_to_message  # Get the replied message
    group_list= load_group_users()
    user_list=  load_members_users()
    default_user_ids =group_list+user_list
    total_users = 0
    failed_users = 0
    for user_id in default_user_ids:
        try:
            client.forward_messages(user_id, message.chat.id, replied_message.id) #client.copy_message(chat_id=user_id, from_chat_id=message.chat.id, message_id=replied_message.id)
            total_users += 1
        except Exception as e:
            failed_users += 1
    response_message = f"Message sent to {total_users} users. {failed_users} users failed to receive the message."
    message.reply(response_message)

@pyro.on_message(filters.command("warn") & filters.chat(sudo))
def warn_user(client, message):
    try:
        # Splitting the command to get user ID and reason
        command_parts = message.text.split(' ', 2)
        user_id = int(command_parts[1])
        reason = command_parts[2]
        # Sending the warning message to the user
        client.send_message(user_id, f"**ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴡᴀʀɴᴇᴅ ꜰᴏʀ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʀᴇᴀꜱᴏɴ:\n{reason}**",disable_web_page_preview=True)
        client.send_message(STCLOG, f"**#warn \n{user_id} ʜᴀᴠᴇ ʙᴇᴇɴ ᴡᴀʀɴᴇᴅ ꜰᴏʀ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʀᴇᴀꜱᴏɴ:\n{reason}**")
        # Sending a reply to the command issuer
        message.reply(f"User with ID {user_id} has been warned successfully.")
    except Exception as e:
        # Sending an error message if the warning failed
        message.reply(f"Failed to warn user. Error: {e}")

@pyro.on_message(filters.command("msg") & filters.chat(sudo))
def warn_user(client, message):
    try:
        # Splitting the command to get user ID and reason
        command_parts = message.text.split(' ', 2)
        user_id = int(command_parts[1])
        reason = command_parts[2]

        # Sending the message to the user
        client.send_message(user_id, f"**ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ᴀᴅᴠᴄʜᴀᴛɢᴘᴛ ᴛᴇᴀᴍ:\n{reason}**",disable_web_page_preview=True)
        client.send_message(STCLOG, f"**#message \n{user_id} ʜᴀᴠᴇ ʙᴇᴇɴ Messaged ꜰᴏʀ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʀᴇᴀꜱᴏɴ:\n{reason}**")
        # Sending a reply to the command issuer
        message.reply(f"User with ID {user_id} has been messaged successfully.")
    except Exception as e:
        # Sending an error message if the warning failed
        message.reply(f"Failed to message user. Error: {e}")


    
        
        
from pyrogram import Client, filters
import os
import sys
import threading


# Global variable to track the script status
running = True

# Define the handler for the /restart command
@pyro.on_message(filters.command("restart") & filters.private & filters.chat(sudo))
def restart(client, message):
    global running
    running = False
    threading.Thread(target=restart_script).start()

# Function to restart the script
def restart_script():
    pyro.send_message(STCLOG, "Restart process started.")
    pyro.stop()
    os.execv(sys.executable, ['python'] + sys.argv)

# Function to start the bot
def start_bot():
    print("CSR bot server started....")
    pyro.run()

# Call this function to start or restart the bot
def run_bot():
    global running
    running = True
    start_bot()
    while running:
        pyro.idle()





pyro.run()
