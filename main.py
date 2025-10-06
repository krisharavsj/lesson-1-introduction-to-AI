print("hi, i am an AI bot!, what is your name?")
name=input()
print(f"nice to meet you,{name}!")
print("how are you feeling today? good/bad")
mood=input().lower()
if mood=='bad':
    print("i'm so sorry to hear that..")
elif mood=='good':
    print("it's glad to hear that!")
else:
    print("its fine if you dont want to say...")
print(f"it was nice meeting you,{name},")