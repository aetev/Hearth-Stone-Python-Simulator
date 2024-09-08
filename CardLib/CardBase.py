from abc import ABC, abstractmethod
import json


def get_card_info(card_name):
    with open("card/sets/core/core_dict.json", "r") as file:
        minion_info = json.load(file)
        return minion_info.get(card_name)


class CardSuperClass(ABC):
    def __init__(self):
        name = type(self).__name__
        card_info = get_card_info(name)
        self.name = card_info["name"]  # Name of the card
        self.manaCost = card_info["manaCost"]
        self.base_health = card_info["health"]
        self.base_attack = card_info["attack"]
        self.health = self.base_health
        self.attack = self.base_attack
        self.classId = card_info["classId"]
        self.spellSchoolId = card_info["spellSchoolId"]
        self.cardTypeId = card_info["cardTypeId"]
        self.rarityId = card_info["rarityId"]
        self.text = card_info["text"]
        self.selected = False



