from __future__ import unicode_literals

import os
import sys
import psycopg2
import redis
import re
from flask import Flask, request, abort, render_template
import requests 
import json 
import decimal
from argparse import ArgumentParser



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
