import customtkinter as ctk
import threading
import requests
import itertools

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window setup
root = ctk.CTk()
root.title("LLM Chat")
root.geometry("380x500")
root.configure(bg="#242526")
root.resizable(False, False)

# Chat container (scrollable area)
chat_container = ctk.CTkScrollableFrame(root, fg_color="#242526")
chat_container.pack(fill="both", expand=True, padx=5, pady=5)

# Chat frame for messages
chat_frame = ctk.CTkFrame(chat_container, fg_color="#242526")
chat_frame.pack(fill="both", expand=True)

# Input area
input_frame = ctk.CTkFrame(root, height=40, fg_color="#3A3B3C", corner_radius=20)
input_frame.pack(fill="x", padx=5, pady=5)

input_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Type a message...",
    border_width=0,
    corner_radius=20,
    fg_color="#4E4F50",
    text_color="white",
    width=300
)
input_entry.pack(side="left", fill="x", expand=True, padx=10, pady=5)

send_btn = ctk.CTkButton(
    input_frame,
    text="➤",
    width=35,
    corner_radius=20,
    fg_color="#0084FF",
    text_color="white",
    command=lambda: generate_response()
)
send_btn.pack(side="right", padx=10, pady=5)

# Handle Enter key to send messages
def handle_enter(event):
    generate_response()
input_entry.bind("<Return>", handle_enter)

# Function to send user input to Ollama
def send_to_ollama(prompt):
    data = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()
        response_json = response.json()
        full_response = response_json.get("response", "No response found")

        if "<think>" in full_response:
            return full_response.split("</think>")[-1].strip()
        return full_response.strip()

        
        return full_response.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to add messages to UI
def add_message(sender, text, is_typing=False):
    align = "e" if sender == "You" else "w"
    bubble_color = "#0084FF" if sender == "You" else "#3A3B3C"
    text_color = "white"

    message_frame = ctk.CTkFrame(chat_frame, fg_color="transparent")
    message_frame.pack(anchor=align, padx=10, pady=3, fill="x")

    message_bubble = ctk.CTkFrame(message_frame, fg_color=bubble_color, corner_radius=20)
    message_bubble.pack(anchor=align, padx=10, pady=2)

    msg_label = ctk.CTkLabel(
        message_bubble, 
        text=text if not is_typing else "...",
        wraplength=260,
        justify="left",
        fg_color="transparent",
        text_color=text_color,
        padx=12,
        pady=8
    )
    msg_label.pack()
    
    return msg_label if is_typing else None

# Typing Animation
def typing_animation(label,is_typing):
    if is_typing:
        dots = itertools.cycle([".", "..", "..."])
        def animate():
            if label.winfo_exists():
                label.configure(text=next(dots))
                label.after(500, animate)
        animate()

# Generate response with typing animation
def generate_response():
    user_input = input_entry.get().strip()
    if not user_input: return

    add_message("You", user_input)
    input_entry.delete(0, ctk.END)

    typing_label = add_message("AI", "", is_typing=True)
    typing_animation(typing_label,True)

    def fetch_response():
        response = send_to_ollama(user_input)
        chat_frame.after(1000, lambda: typing_label.destroy())
        chat_frame.after(1000, lambda: add_message("AI", response))

    threading.Thread(target=fetch_response, daemon=True).start()

root.mainloop()
