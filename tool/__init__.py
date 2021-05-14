# dependencies
from flask import Flask
from werkzeug.utils import secure_filename
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
# creating app
app = Flask(__name__)

UPLOAD_FOLDER = 'tool/uploads/'
# Flask Env Variables
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from tool import routes