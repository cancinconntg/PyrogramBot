import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if bool(os.environ.get("ENV", False)):
    from PyroBot.sample_config import Config
else:
    from PyroBot.config import Development as Config


LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
COMMAND_HAND_LER = Config.COMMAND_HAND_LER

if not os.path.isdir(TMP_DIR):
    os.makedirs(TMP_DIR)
