import re,random
from colorama import Fore, Style, init
init(autoreset=True)

destination= {"beaches":["Bali","Pondycherry","Goa"],
              "mountains":["himalayas","black forest","alps mountain"],
              "cities":["stuttgart","frankfurt","chennai"]}
Jokes=["why do programmers not like forest areas?, too much bugs!",
       "why was six afraid of seven?,seven ate(eight)nine!",
       "the waiter asked:Are you comfortable?,customer replied:no, i come for food.(come for table)"]
def recomend():
    print(f"{Fore.RED}Travel bot: which type of place do you want to visit? beaches,mountain,cities?")
    preference=input(Fore.YELLOW+"you:")
    if preference in destination:
        suggestion=random.choice(destination[preference])
        print(f"{Fore.RED}Travel bot: how about {suggestion}?")
        print(f"{Fore.RED}Did you like the destination?(yes/no)")
        answer=input(Fore.YELLOW+"you:")
        if answer=="yes":
            print(f"{Fore.RED}Travel bot: Enjoy your suggestion!{suggestion}")
        elif answer=="no":
            print(f"{Fore.RED}Travel bot: let's try another")
            recomend()
        else:
            print(f"{Fore.RED}Travel bot: I will suggest again")
            recomend()
    else:
        print(f"{Fore.RED}Travel bot: Sorry I dont have that type of destination")
    show_help()
def joke():
    print(f"{Fore.YELLOW}{random.choice(Jokes)}")
def show_help():
    print(f"{Fore.MAGENTA}Travel bot: I can suggest travel spots(say'recomend')")
    print(f"{Fore.MAGENTA}Travel bot: I can tell you a joke(say'joke')")
    print(f"{Fore.CYAN}Travel bot: type'exit'or'bye'to end")
def chat():
    print(f"{Fore.GREEN}Travel bot:hi im travel bot!")
    name=input("enter your name: ")
    print(f"{Fore.CYAN}Travel bot:nice to meet you",name)
    show_help()
    while True:
        userinput=input()
        if "recomend" in userinput or "suggest" in userinput:
            recomend()
        elif "joke" in userinput:
            joke()
        elif "exit" in userinput:
            print(f"{Fore.CYAN}Travel bot:")
        else:
            print("could you rephrase it?")
if __name__=="__main__":
    chat()