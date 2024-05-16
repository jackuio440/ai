import os
import sys
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def chat():
    print("你好！我是聊天機器人。你可以隨時與我交流。輸入 '退出' 來結束對話。")
    
    while True:
        user_input = input("你: ")
        
        if user_input.lower() == "退出":
            print("再見")
            break
        

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                    
                }
            ],
            model="llama3-8b-8192",
        )
        
        response = chat_completion.choices[0].message.content
        print("groq:", response)


if __name__ == "__main__":
    chat()
