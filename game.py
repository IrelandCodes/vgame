import json

class VideoGameCharacter:
    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.character_class = data_dict["characterClass"]
        self.level = data_dict["level"]
        self.health = data_dict["stats"]["health"]
        self.max_health = data_dict["stats"]["health"]
        self.mana = data_dict["stats"]["mana"]
        self.abilities =  data_dict["abilities"]

    def display_status_bar(self):
        bar_length = 10
        filled_length = int(round(bar_length * self.health / self.max_health))
        bar = '*' * filled_length + '-' * (bar_length - filled_length)
        print(f"\n~ {self.name} the {self.character_class} (Level {self.level})")
        print(f"health:    [{bar}] {self.health}/{self.max_health}")
        print(f"mana: {self.mana}")

    def cast_ability(self, ability_index):
        if 0 <= ability_index < len(self.abilities):
            ability = self.abilities[ability_index]
            print(f"\n {self.name} casts {ability['name']}!")
            print(f"Deal {ability['power']} points of {ability['type']} effect!")
        else:
            print("Invalid ability")
    
with open("vulpix.json", "r") as file:
    character_data = json.load(file)

my_character = VideoGameCharacter(character_data)

my_character.display_status_bar()

my_character.cast_ability(0)

    