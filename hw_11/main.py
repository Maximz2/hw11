# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import utils

app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    """
    Выводит список всех кандидатов
    :return: Список кандидатов
    """
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:uid>/")
def page_candidate(uid):
    """
    Выводит данные кандидата по id
    :param uid: id кандидата
    :return: Данные кандидата
    """
    candidate = utils.get_candidate(uid)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>/")
def search_candidate_name(candidate_name):
    """
    Выводит кандидатов по заданному имени
    :param candidate_name: Имя кандидата
    :return: Список кандидатов с заданным именем
    """
    candidates = utils.get_candidates_by_name(candidate_name)
    count = len(candidates)
    return render_template("search.html", candidates=candidates, count=count)


@app.route("/skill/<skill_name>/", methods=['GET'])
def page_skill(skill_name):
    """
    Выводит кандидатов с заданным навыком
    :param skill_name: Навык
    :return: Список кандидатов с навыком
    """
    candidates = utils.get_candidates_by_skill(skill_name)
    count = len(candidates)
    limit = int(request.args.get('limit', count))
    candidates = candidates[:limit]
    return render_template("skill.html", candidates=candidates, count=count, skill=skill_name)


if __name__ == "__main__":
    app.run()
