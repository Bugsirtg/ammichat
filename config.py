from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 23181468))
API_HASH = getenv("API_HASH", "139146f6e5d20550ba60988a7e867235")
OWNER_ID = int(getenv("OWNER_ID", "6571408029"))
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "ammichatt")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ammichatt")
OWNER_USERNAME = getenv("OWNER_USERNAME", "bugadam")

# Random Start Images
IMG = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


# Random Stickers
STICKER = [
    "",
    "",
    "",
]


EMOJIOS = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
