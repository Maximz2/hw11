# -*- coding: utf-8 -*-

import json


def load_candidates_from_json(path="candidates.json"):
    """
    Возвращает список всех кандидатов
    :param path: файл json
    :return: список кандидатов
    """
    with open(path, encoding="utf-8") as f:
        candidates = json.load(f)
    return candidates


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id: id кандидата
    :return: Кандидат
    """
    list_candidates = load_candidates_from_json()
    for candidate in list_candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    :param candidate_name: Имя
    :return: Список кандидатов с именем
    """
    list_candidates = load_candidates_from_json()
    candidates = []
    for candidate in list_candidates:
        if candidate_name in candidate["name"]:
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    :param skill_name: Навык
    :return: Список квндидатов
    """
    list_candidates = load_candidates_from_json()
    candidates = []
    for candidate in list_candidates:
        if skill_name in candidate["skills"].split(", "):
            candidates.append(candidate)
    return candidates
