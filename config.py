"""
Configuration module for the bot status checker.

This module loads environment variables required for the bot to function,
such as bot token, API ID and API HASH.
It also sets up the necessary configuration settings.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID", "22270544"))
    API_HASH = getenv("12fd6c5d681c662e28da50bbcb8ebd06")
    BOT_TOKEN = getenv("7269795660:AAGC8oFnwWCPQMwdMETSTCdgQK3fA4yOerA")
    
