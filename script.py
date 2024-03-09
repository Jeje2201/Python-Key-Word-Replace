import keyboard

# Define word replacements
word_replacements = {
    "(joy)": "😂",
    "(sob)": "😭",
    "(angel)": "😇"
}

current_word = ""

def on_key_press(event):
    global current_word

    if event.name == "backspace":  # Check if allowed character
        current_word = current_word[:-1]
    elif event.name == "space":  # Check if allowed character
        current_word = ""
    elif event.name not in ["haut", "ctrl","gauche","droite", "bas"]:
        current_word += event.name
        print(current_word)
        if current_word in word_replacements:
            num_backspaces = len(current_word)
            # Send backspaces to delete the word
            for _ in range(num_backspaces):
                keyboard.press_and_release('backspace')
            replaced_text = word_replacements[current_word]
            print("Replaced:", current_word, "->", replaced_text)
            keyboard.write(replaced_text)
            current_word = ""  # Reset after replacement

keyboard.on_press(on_key_press)
keyboard.wait("esc")