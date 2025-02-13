# Local LLM Tool

A lightweight, local LLM (Large Language Model) tool that allows you to interact with a local AI model using a modern, messenger-like interface. The tool is activated via a hotkey and stays on top of all other windows for easy access.

## Features
- **Hotkey Activation**: Launch the tool using `Ctrl+Shift+L`.
- **Messenger-Like UI**: Modern, chat-based interface with animated typing bubbles.
- **Local LLM Integration**: Uses Ollama and the DeepSeek R1 1.5B model for local AI responses.
- **Floating Window**: The tool stays on top of all other windows for quick access.

## Requirements
- Python 3.8+
- Ollama installed and running locally.
- DeepSeek R1 1.5B model downloaded via Ollama.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/JubairRafi/local-llm-tool.git
   cd llm-tool



## Create a virtual environment:
## bash
python -m venv llm-tool-env
Activate the virtual environment:

## On Windows:
.\llm-tool-env\Scripts\Activate.ps1

## On macOS/Linux:
source llm-tool-env/bin/activate

## Install the dependencies:
pip install -r requirements.txt

Download the DeepSeek R1 1.5B model using Ollama:
ollama pull deepseek-r1:1.5b

## Usage

Start the Ollama server (if not already running):
ollama serve

## Run the hotkey listener:
python hotkey_listener.py

Press Ctrl+Shift+L to launch the Local LLM Tool.

Type your message in the input box and press "Send" or hit Enter.

The AI will respond with animated typing bubbles, simulating a real-time chat experience.

## Customization
1. Change Hotkey: Modify the hotkey in hotkey_listener.py by editing the keyboard.HotKey.parse line.

2. Change Model: Update the model parameter in llm_tool_gui.py to use a different Ollama model.
3. UI Themes: Customize the appearance by changing ctk.set_appearance_mode and ctk.set_default_color_theme in llm_tool_gui.py.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.