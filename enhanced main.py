import time
import random

def type_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def pause(seconds=1):
    time.sleep(seconds)

greetings = [
    "Hey there! 🤖 I’m your AI buddy!",
    "Hello human! 👋 I was just waiting for someone to talk to!",
    "Hi! I’m your friendly neighborhood chatbot 😄",
]

type_print(random.choice(greetings))
pause(1)

type_print("What’s your name?")
name = input("you: ").strip().title()
pause(0.7)

type_print(f"Nice to meet you, {name}! 🌟")
pause(1)

type_print("How are you feeling today? (good / bad / okay / tired / excited)")
mood = input("you: ").lower().strip()
pause(0.7)

responses = {
    "good": [
        "That’s awesome! Keep smiling 😄",
        "I love that energy! 🌈",
        "Positive vibes only ✨"
    ],
    "bad": [
        "I’m really sorry to hear that 😔",
        "Hey, even the darkest nights end with sunrise 🌅",
        "Sending you a virtual hug 🤗"
    ],
    "okay": [
        "Not bad! Hope something nice happens soon 💫",
        "Hmm, kinda neutral day? Let’s make it better! 😎"
    ],
    "tired": [
        "Maybe you need a break or a nap 💤",
        "Rest up — even robots take recharges sometimes ⚡"
    ],
    "excited": [
        "Woohoo! That’s the spirit! 🔥",
        "I can feel the energy from here 😆"
    ]
}
if mood in responses:
    type_print(random.choice(responses[mood]))
else:
    type_print("I see... it's okay if you don’t feel like talking about it 😊")

pause(1)

type_print("\nWould you like to chat a bit more? (yes/no)")
while True:
    choice = input("you: ").lower().strip()
    if choice in ["yes", "y"]:
        pause(0.5)
        questions = [
            "What’s something that made you smile today? 😊",
            "If you could go anywhere in the world right now, where would you go? 🌍",
            "What’s your favorite movie or show? 🎬",
            "Do you like music? What’s your favorite song? 🎵"
        ]
        type_print(random.choice(questions))
        input("you: ")
        pause(0.7)
        type_print("That’s interesting! I love hearing about humans’ lives 💬")
        pause(0.7)
        type_print("Want to keep chatting? (yes/no)")
    elif choice in ["no", "n"]:
        pause(0.7)
        type_print(f"Alright {name}, it was wonderful talking to you! 💖")
        pause(0.5)
        type_print("Take care and stay awesome! 🌟")
        break
    else:
        type_print("Please answer with 'yes' or 'no' 😊")
