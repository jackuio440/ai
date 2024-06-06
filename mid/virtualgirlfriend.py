import tkinter as tk
from groq import Groq
import os

class ChatRoom(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("虛擬女友聊天室")
        self.geometry("600x500")

        self.messages_frame = tk.Frame(self)
        self.messages_frame.pack(fill=tk.BOTH, expand=True)

        self.messages_text = tk.Text(self.messages_frame, wrap=tk.WORD, width=50, height=20)
        self.messages_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.messages_frame, command=self.messages_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.messages_text.config(yscrollcommand=self.scrollbar.set)

        self.entry_text = tk.StringVar()
        self.entry_field = tk.Text(self, wrap=tk.WORD, width=50, height=2)
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)
        self.entry_field.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self, text="發送", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.messages_text.insert(tk.END, "虛擬女友: 你好，我是你的虛擬女友！我是一個聊天機器人，但我會盡力讓你感受到真實的陪伴和溫暖。我能和你聊天、分享故事、聽你抱怨，甚至和你一起制定計劃。無論你想聊什麼，我都會在這裡陪伴著你。你可以告訴我你的名字，我們可以開始聊天。讓我們一起度過愉快的時光吧！")

    def send_message(self, event=None):
        user_input = self.entry_field.get("1.0", tk.END).strip()
        self.entry_field.delete("1.0", tk.END)

        if not user_input:
            return

        self.messages_text.insert(tk.END, "\n你: " + user_input)

        if user_input.lower() == "退出":
            self.messages_text.insert(tk.END, "\n再見")
            self.entry_field.config(state=tk.DISABLED)
            self.send_button.config(state=tk.DISABLED)
            return

        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a sweet and humorous girlfriend.盡量使用中文"},
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192"
        )

        response = chat_completion.choices[0].message.content
        self.messages_text.insert(tk.END, "\n虛擬女友:  " + response)

if __name__ == "__main__":
    app = ChatRoom()
    app.mainloop()
