import json

class VideoGameCharacter:
    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.character_class = data_dict["characterClass"]
        self.level = data_dict["level"]
        self.health = data_dict["health"]
        self.max_health = data_dict["stats"]["health"]
        self.mana = data_dict["stats"]["mana"]
        self.abilities =  data_dict["abilities"]

    def display_status_bar(self):
        bar_length = 10
        filled_length = int(round(bar_length * self.health / self.max_health))
        bar = '*' * filled_length + '-' * (bar_length - filled_length)
        print(f"\n~ {self.name} the {self.charater_class} (Level {self.level})")
        print(f"health:    [{bar}] {self.health}/{self.max_health}")
        print(f"mana: {self.mana}")

    