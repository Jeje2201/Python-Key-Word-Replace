import keyboard

# Define word replacements
word_replacements = {
    "(joy)": "😂",
    "(sob)": "😭",
    "(angel)": "😇"
}

current_word = ""  # Initialize an empty string to keep track of the current word being typed

def on_key_press(event):
    global current_word

    if event.name == "backspace":  # Check if the backspace key is pressed
        current_word = current_word[:-1]  # Remove the last character from the current word
    elif event.name == "space":  # Check if the space key is pressed
        current_word = ""  # Reset the current word when a space is typed
    elif event.name not in ["up", "ctrl", "left", "right", "down"]:  # Check if it's not a navigation key
        current_word += event.name  # Append the pressed key to the current word
        if current_word in word_replacements:  # Check if the current word matches any replacement string
            num_backspaces = len(current_word)  # Calculate the number of backspaces needed to delete the current word
            # Send backspaces to delete the word
            for _ in range(num_backspaces):
                keyboard.press_and_release('backspace')
            replaced_text = word_replacements[current_word]  # Get the replacement text for the current word
            keyboard.write(replaced_text)  # Write the replacement text
            current_word = ""  # Reset the current word after replacement

# Register the on_key_press function to handle key presses
keyboard.on_press(on_key_press)
# Wait for the alt+p key to be pressed to exit the program
keyboard.wait("alt+p")