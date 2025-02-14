#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24798261"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fef280037f5759eccc540c6d7a279a14")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002280514367"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6155478725"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rajeshpro123321:Vs9n8R90yUtCIyu4@clonestore1.w51yrrp.mongodb.net/?retryWrites=true&w=majority&appName=clonestore1")
DB_NAME = os.environ.get("DATABASE_NAME", "clonestore1")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001678918073"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://www.imghippo.com/i/rNu5704kiQ.jpg")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI Am 𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™ 😊store bot You will get here Study Material by links🔗 which will be provided in channels✅⭐️.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5347709348").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋Hello {first}\n\n<b>🪴You need to join in my official channel😊 to get lectures📽️\n\n🎀Kindly Please join Channel\n\n📍And Click on try again or go on post link again\n\nThankyou💕🪴\n\n📍𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™~</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly Dm here if u have any problem @HKOWNER0 !"

ADMINS.append(6155478725)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
