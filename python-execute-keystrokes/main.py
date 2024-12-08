from pynput.keyboard import Controller, Key
import json
import time 

input_file = "recorded_keystrokes.json"
                                        
keyboard = Controller()

def load_events():
    """Load recorded keyboard events from the file."""
    try:
        with open(input_file, "r") as file:
            events = json.load(file)
        print(f"Loaded {len(events)} events.")
        return events
    except Exception as e:
        print(f"Error loading events: {e}")
        return []

def replay_events(events):
    """Replay the loaded keyboard events."""
    print("Replaying keyboard events...")
    for event in events:
        try:
            event_type = event["type"]
            key = event["key"]
 
            if key.startswith("Key."):
                key_obj = getattr(Key, key.split(".")[1], None)
            else:
                key_obj = key.strip("'")  
            
            if event_type == "press" and key_obj:
                keyboard.press(key_obj)
                print(f"Pressed: {key}")
            elif event_type == "release" and key_obj:
                keyboard.release(key_obj)
                print(f"Released: {key}")
            
            time.sleep(0.05)
        except Exception as e:
            print(f"Error replaying event {event}: {e}")

def main():
    print("Starting replay...")
    time.sleep(2)
    events = load_events()
    if events: 
        replay_events(events)
    else:
        print("No events to replay.")

if __name__ == "__main__":
    main()
import pyautogui
import time
import json

def handle_paste(text):
    for char in text:
        if char == '\n':
            pyautogui.press('enter')  
        else:
            pyautogui.write(char)  
        time.sleep(0.05)  

def execute_actions_from_file(file_path):
    with open(file_path, 'r') as f:
        actions = json.load(f) 

    for action in actions:
        if action['type'] == 'press':
            pyautogui.press(action['key'])  
        elif action['type'] == 'paste':
            handle_paste(action['text'])  
        time.sleep(0.5)  

    print("Actions executed successfully.")

execute_actions_from_file('recorded_keystrokes.json')
