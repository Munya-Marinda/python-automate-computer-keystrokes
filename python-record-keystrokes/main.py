from pynput import keyboard
from pynput.keyboard import Key, Listener
import json
import os
import datetime


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
filename = f"file_{formatted_datetime}.txt"

output_file = 'recorded_keystrokes.json'
  
 
keyboard_events = []

 
def on_key_press(key):
    """Record key press."""
    try:
        keyboard_events.append({"type": "press", "key": str(key)})
        print(f"Key pressed: {key}")   
    except Exception as e:
        print(f"Error recording key press: {e}")

def on_key_release(key):
    """Record key release."""
    try:
        keyboard_events.append({"type": "release", "key": str(key)})
        print(f"Key released: {key}")   

         
        if key == Key.esc:
            print("Exiting and saving events...")
            save_events()
            return False
    except Exception as e:
        print(f"Error recording key release: {e}")

 
def save_events():
    """Save recorded keyboard events to a file."""
    try:
        with open(output_file, "w") as file:
            json.dump(keyboard_events, file, indent=4)
        print(f"Keyboard events saved to {output_file}")
    except Exception as e:
        print(f"Error saving events: {e}")

 
def main():
    print("Starting keyboard tracking... Press 'Esc' to stop.")
    if os.path.exists(output_file):
        os.remove(output_file)   
 
    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()