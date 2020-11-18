from flask import Flask, request
from flask_compress import Compress

app = Flask(__name__)

Compress(app)

from server import routes
