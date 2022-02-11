# -*- coding: utf-8 -*-

import json

from flask import Flask

FILE_IMPORT = "candidates.json"


app = Flask(__name__)


@app.route("/")
def page_main():
    stroka = ''
    for i in range(len(candidates)):
        stroka += f"<pre>{candidates[i]['name']}\n" \
                  f"{candidates[i]['position']}\n" \
                  f"{candidates[i]['skills']}</pre>\n"
    return stroka


@app.route("/candidate/<int:index>")
def page_candidate(index):
    stroka = f"<img src='{candidates[index]['picture']}'>\n" \
             f"<pre>{candidates[index]['name']}\n" \
             f"{candidates[index]['position']}\n" \
             f"{candidates[index]['skills']}</pre>\n"
    return stroka


@app.route("/skills/<skill>")
def page_skill(skill):
    stroka = ''
    for i in range(len(candidates)):
        if skill in candidates[i]['skills'].lower():
            stroka += f"<pre>{candidates[i]['name']}\n" \
                      f"{candidates[i]['position']}\n" \
                      f"{candidates[i]['skills']}</pre>\n"
    return stroka


if __name__ == '__main__':
    with open(FILE_IMPORT, encoding="utf-8") as f:
        candidates = json.load(f)
    app.run()
