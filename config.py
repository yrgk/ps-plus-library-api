import os
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
NAME = os.environ.get("NAME")

ADMIN_KEY = os.environ.get("ADMIN_KEY")