import json
import tkinter as tk

class VideoGameCharacterGUI:
    def __init__(self, root, data_dict):
        self.root = root
        self.root.title("Character Profile")
        self.root.geometry("650x750")


        self.name = data_dict["name"]
        self.character_class = data_dict["characterClass"]
        self.level = data_dict["level"]
        self.health = data_dict["stats"]["health"]
        self.max_health = data_dict["stats"]["health"]
        self.mana = data_dict["stats"]["mana"]
        self.abilities =  data_dict["abilities"]
        self.image_path = data_dict.get("image_path", "")

        self.title_label = tk.Label(root, text=f"{self.name} the {self.character_class}", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        try:
            self.char_image = tk.PhotoImage(file=self.image_path)
            self.image_label = tk.Label(root, image=self.char_image)
            self.image_label.pack(pady=10)
        except Exception:
            self.image_label = tk.Label(root, text=["Image Not Found"], fg="grey")
            self.image_label.pack(pady=10)

        self.stats_label = tk.Label(root, text=f"Level: {self.level}\nhealth: {self.health}/{self.max_health}\nMana: {self.mana}", font=("Arial", 12), justify="left")
        self.stats_label.pack(pady=10)

        self.console_label = tk.Label(root, text=f"Ready to play!", fg="blue", font=("Arial", 10, "italic"))
        self.console_label.pack(pady=15)

        if self.abilities:
            ability_name = self.abilities[0]["name"]
            self.action_btn = tk.Button(root, text=f"Cast {ability_name}", command=self.use_ability)
            self.action_btn.pack(pady=5)

    # def display_status_bar(self):
    #     bar_length = 10
    #     filled_length = int(round(bar_length * self.health / self.max_health))
    #     bar = '*' * filled_length + '-' * (bar_length - filled_length)
    #     print(f"\n~ {self.name} the {self.character_class} (Level {self.level})")
    #     print(f"health:    [{bar}] {self.health}/{self.max_health}")
    #     print(f"mana: {self.mana}")

    # def cast_ability(self, ability_index):
    #     if 0 <= ability_index < len(self.abilities):
    #         ability = self.abilities[ability_index]
    #         print(f"\n {self.name} casts {ability['name']}!")
    #         print(f"Deal {ability['power']} points of {ability['type']} effect!")
    #     else:
    #         print("Invalid ability")

    def use_ability(self):
        ability = self.abilities[0]
        action_text = f"{self.name} casts {ability['name']}!\nDeals {ability['power']} {ability['type']} damage!"
        self.console_label.config(text=action_text, fg="red")
    
with open("vulpix.json", "r") as file:
    character_data = json.load(file)

# my_character = VideoGameCharacter(character_data)

# my_character.display_status_bar()

# my_character.cast_ability(0)

window = tk.Tk()
app = VideoGameCharacterGUI(window, character_data)
window.mainloop()

    