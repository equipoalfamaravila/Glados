import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response 

class ChatbotInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)

        self.user_input = tk.StringVar()
        self.entry_box = tk.Entry(self.root, textvariable=self.user_input, width=40)
        self.entry_box.pack(padx=10, pady=10, side=tk.LEFT)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10, side=tk.RIGHT)

        self.root.bind('<Return>', lambda event: self.send_message())
    
    def send_message(self):
        user_message = self.user_input.get()
        if user_message.strip():
            self.display_message("User", user_message)
            self.user_input.set("")
            bot_response = get_response(user_message)
            self.display_message("Glados", bot_response)

    def display_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = ChatbotInterface(root)
    root.mainloop()
