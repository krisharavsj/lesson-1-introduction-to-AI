import colorama
from colorama import Fore ,Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.LIGHTCYAN_EX}Welcome to sentiment spy{Style.RESET_ALL}")
user_name=input(f"{Fore.LIGHTBLUE_EX}enter your name: {Style.RESET_ALL}")
if not user_name:
    user_name="mystery agent"
conversation_history=[]
print(f"{Fore.GREEN}Hello agent",user_name)