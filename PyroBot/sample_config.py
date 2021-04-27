import os


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")
    ENV = os.environ.get("ENV", True)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
