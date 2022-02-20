# -*- coding: utf-8 -*-

import json


class CandidateManager:

    def __init__(self, path):
        self.path = path

    def load_candidates_from_json(self, ):
        """
        Возвращает список всех кандидатов
        :return: список кандидатов
        """
        with open(self.path, encoding="utf-8") as f:
            candidates = json.load(f)
        return candidates

    def get_candidate_by_id(self, candidate_id):
        """
        Возвращает одного кандидата по его id
        :param candidate_id: id кандидата
        :return: Кандидат
        """
        list_candidates = self.load_candidates_from_json()
        for candidate in list_candidates:
            if candidate["id"] == candidate_id:
                return candidate

    def get_candidates_by_name(self, candidate_name):
        """
        Возвращает кандидатов по имени
        :param candidate_name: Имя
        :return: Список кандидатов с именем
        """
        list_candidates = self.load_candidates_from_json()
        candidates = []
        for candidate in list_candidates:
            if candidate_name.lower() in candidate["name"].lower():
                candidates.append(candidate)
        return candidates

    def get_candidates_by_skill(self, skill_name):
        """
        Возвращает кандидатов по навыку
        :param skill_name: Навык
        :return: Список квндидатов
        """
        list_candidates = self.load_candidates_from_json()
        candidates = []
        for candidate in list_candidates:
            if skill_name.lower() in candidate["skills"].lower().split(", "):
                candidates.append(candidate)
        return candidates
