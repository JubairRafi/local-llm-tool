from pynput import keyboard
import subprocess
import sys
import os

def on_activate():
    """
    Launches the GUI script when the hotkey is pressed.
    """
    # Get the path to the Python interpreter in the virtual environment
    python_path = sys.executable

    # Get the path to the GUI script
    gui_script_path = os.path.join(os.path.dirname(__file__), "llm_tool_gui.py")

    # Launch the GUI script using the correct Python interpreter
    subprocess.Popen([python_path, gui_script_path])

def for_canonical(f):
    """
    Helper function to normalize key events.
    """
    return lambda k: f(listener.canonical(k))

# Define the hotkey (Ctrl+Shift+L)
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<shift>+l'),
    on_activate
)

# Set up the keyboard listener
with keyboard.Listener(
    on_press=lambda k: hotkey.press(listener.canonical(k)),
    on_release=lambda k: hotkey.release(listener.canonical(k))
) as listener:
    listener.join()