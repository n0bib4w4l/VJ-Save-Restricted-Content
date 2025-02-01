import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7370607519:AAFG7NB2noic-svLUEedSCRCcj3P1bU6cHY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23439358"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ef7fbd454fd8a9456bbe76ee0d14ae11")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7302286857"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://alialgsnsvqei1237:eXgFhcVNcwXPIYtD@cluster0.464pm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
