# coding=utf-8
import os
# Define the application directory
from os.path import abspath, realpath, dirname
from dotenv import load_dotenv
load_dotenv()

# Define the application directory
from os.path import abspath, dirname

BASE_DIR = abspath(dirname(__file__))

# Statement for enabling the development environment
DEBUG = os.getenv('DEBUG')
ENV = os.getenv('ENV')
TESTING = os.getenv('TESTING')

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = os.getenv('THREADS_PER_PAGE')

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = os.getenv('CSRF_ENABLED')

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

# Secret key for signing cookies
SECRET_KEY = os.getenv('SECRET_KEY')

# App config
PREFIX = os.getenv('PREFIX')
VERSION = os.getenv('VERSION')


# MongoDB config
from pymongo import MongoClient
from urllib.parse import quote

DB_NAME = os.getenv('DB_NAME')
MONGO_USER = quote(os.getenv('MONGO_USER'))
MONGO_PASS = quote(os.getenv('MONGO_PASS'))

client = MongoClient("mongodb+srv://{}:{}@cluster0.fyiw5.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_USER, MONGO_PASS, DB_NAME))
db = client[DB_NAME]
