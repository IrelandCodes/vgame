#vgame

# 🎮 Playing Around with Python & GUIs
Started as a fun weekend project where I am playing around with Python, JSON, and desktop GUIs! I wanted to see if I could build the start of a video game character engine using a clean visual interface instead of just printing plain text to the standard terminal.

# 🛠️ What I'm Experimenting With
 - Python & Tkinter: Using Python's built-in tkinter library to break out of the terminal and open an actual, interactive desktop app window on my screen.
 - JSON Data Configurations: Playing around with JSON files (characters.json) to store all the character data—like names, stats, levels, and moves.
 - Decoupling Logic: The Python script handles the heavy lifting (the GUI window and button clicks), while the JSON file handles the data. This means I can completely change the character or their stats in the JSON file without breaking my Python code.
 - Event Handling: Setting up interactive buttons so that clicking a move like "Cast Flash Fire" instantly triggers an action and dynamically updates the text on screen.
 - Basic Error Fallbacks: Added a quick try-except safeguard so that if the character's image file goes missing, the app doesn't completely crash—it just displays a friendly Image Not Found message instead.

# 📂 Project Setup
  ```text
vgame/
  ├── game.py              # The Python script running the GUI and app logic
  └── characters.json      # The JSON file holding our character's stats and moves
```

# 🚀 How to Run It
Since this uses standard Python libraries, you don't need to install any external dependencies or packages.

Clone or download this repo.

Open your terminal, navigate to this project directory, and run:
  ```text
  python3 game.py
```

