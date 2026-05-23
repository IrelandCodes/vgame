import json
import tkinter as tk

class VideoGameCharacterGUI:
    def __init__(self, root, all_character_data):
        self.root = root
        self.root.title("Character Selection")
        self.root.geometry("900x750")

        self.all_characters = all_character_data

        self.current_widgets = []

        self.menu_images = {}

        self.show_selection_menu()

    def clear_screen(self):
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets = []

    def show_selection_menu(self):
        self.clear_screen()
        self.root.title("Charater Selection")

        menu_title = tk.Label(self.root, text="Choose Your Character", font=("Arial", 20, "bold"))
        menu_title.pack(pady=30)
        self.current_widgets.append(menu_title)

        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=10)
        self.current_widgets.append(grid_frame)

        columns_limit = 3
        current_row = 0
        current_col = 0

        for char_name, data in self.all_characters.items():
            cell_frame = tk.Frame(grid_frame, padx=15, pady=15)
            cell_frame.grid(row=current_row, column=current_col)

            image_path = data.get("image_path", "")

            try:
                full_photo = tk.PhotoImage(file=image_path)
                photo = full_photo.subsample(2,2)
                self.menu_images[char_name] = photo

                img_btn = tk.Button(
                    cell_frame, 
                    image=photo, 
                    command=lambda name=char_name: self.show_character_profile(name),
                    bd=1, relief="groove"
                )
            except Exception:
                img_btn = tk.Button(
                    cell_frame, 
                    text="No Image\nFound", 
                    font=("Arial", 11, "italic"),
                    width=12, height=6, fg="grey",
                    command=lambda name=char_name: self.show_character_profile(name)
                )

            img_btn.pack()

            name_label = tk.Label(cell_frame, text=char_name, font=("Arial", 12, "bold"), pady=5)
            name_label.pack()

            current_col += 1
            if current_col >= columns_limit:
                current_col = 0
                current_row += 1

            # btn = tk.Button(
            #     self.root,
            #     text=char_name,
            #     font=("Arial", 14),
            #     width=20, padx=10, pady=5,
            #     command=lambda name=char_name: self.show_character_profile(name)
            # )
            # btn.pack(pady=10)
            # self.current_widgets.append(btn)

    def show_character_profile(self, character_name):
        self.clear_screen()

        data_dict = self.all_characters[character_name]
        self.root.title(f"{data_dict['name']}'s Profile")

        self.name = data_dict["name"]
        self.character_class = data_dict["characterClass"]
        self.level = data_dict["level"]
        self.health = data_dict["stats"]["health"]
        self.max_health = data_dict["stats"]["health"]
        self.mana = data_dict["stats"]["mana"]
        self.abilities =  data_dict["abilities"]
        self.image_path = data_dict.get("image_path", "")

        back_btn = tk.Button(self.root, text="<- Back to Menu", command=self.show_selection_menu)
        back_btn.pack(anchor="nw", padx=10, pady=10)
        self.current_widgets.append(back_btn)
        
        title_label = tk.Label(self.root, text=f"{self.name} the {self.character_class}", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        self.current_widgets.append(title_label)

        try:
            self.full_char_image = tk.PhotoImage(file=self.image_path)
            self.char_image = self.full_char_image.subsample(2,2)
            image_label = tk.Label(self.root, image=self.char_image)
            image_label.pack(pady=10)
        except Exception:
            image_label = tk.Label(self.root, text="Image Not Found", fg="grey")
            image_label.pack(pady=10)
        self.current_widgets.append(image_label)

        stats_label = tk.Label(self.root, text=f"Level: {self.level}\nhealth: {self.health}/{self.max_health}\nMana: {self.mana}", font=("Arial", 12), justify="left")
        stats_label.pack(pady=15)
        self.current_widgets.append(stats_label)

        self.console_label = tk.Label(self.root, text=f"Ready to play!", fg="blue", font=("Arial", 10, "italic"))
        self.console_label.pack(pady=20)
        self.current_widgets.append(self.console_label)

        if self.abilities:
            ability_name = self.abilities[0]["name"]
            action_btn = tk.Button(self.root, text=f"Cast {ability_name}", command=self.use_ability)
            action_btn.pack(pady=5)
            self.current_widgets.append(action_btn)

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
    
with open("characters.json", "r") as file:
    all_character_data = json.load(file)

# my_character = VideoGameCharacter(character_data)

# my_character.display_status_bar()

# my_character.cast_ability(0)

window = tk.Tk()
app = VideoGameCharacterGUI(window, all_character_data)
window.mainloop()

    