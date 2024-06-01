#!/usr/bin/env python

from groq import Groq

client = Groq(
    api_key="put in your api code in here between the quotes"
)

def main():
    print("")
    dict = {"role": "user","content": ""}
    continue_chat = True
    while continue_chat== True:
        question = input("> ")
        if question.lower() == "quit":
            continue_chat = False
            dict["content"] = "Say goodby to the user"
            chat_completion =client.chat.completions.create(messages=[dict], model="llama3-8b-8192",)
            print("")
            print(chat_completion.choices[0].message.content)
            print("")
                  
        else:
            dict["content"] = question
            chat_completion =client.chat.completions.create(messages=[dict], model="llama3-8b-8192",)
            print("")
            print(chat_completion.choices[0].message.content)
            print("")
    
main()
