import requests

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma:2b",
            "messages": messages,
            "stream": False
        }
    )

    bot_reply = response.json()["message"]["content"]
    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})