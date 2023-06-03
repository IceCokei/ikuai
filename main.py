import base64
import json
import logging
import sys
import requests
import time
import asyncio
from hashlib import md5
from telegram import Bot


import configparser
from ikuai import * 


if __name__ == "__main__":
    asyncio.run(switch())