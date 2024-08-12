import os

API_ID = API_ID = 25218674,

API_HASH = os.environ.get("API_HASH", "87c231f0e8704795b8239d06965b4351")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7198600769:AAHfVi7qTaMw20HbpvPrF-fnP77-sWdOthI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "1713924419"))

LOG = -1002154281532,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1713924419").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


