# -*- coding: utf-8 -*-

import json

from flask import Flask

FILE_IMPORT = "candidates.json"


def data_import(file_json):
    with open(file_json, encoding="utf-8") as f:
        candidates_list = json.load(f)
    return candidates_list

app = Flask(__name__)

@app.route("/")
def page_index(candidates_list):

    return "Главная страница"

app.run()
