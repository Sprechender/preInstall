import os
import questionary

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For macOS and Linux
    else:
        _ = os.system('clear')

def greet():
    print("WELCOME TO PREINSTALL!\n")

def initApp():
    clean() # clears the terminal
    
    greet() # greets the user (ex. " welcome to preInstall")
    start() # starts IOHA menu

def prepFunction():
    clean() # clears the terminal

def aboutMenu():
    print("Hey there! 👋 I'm Sprechender, the developer behind this python script.")
    print("This Script helps you with the automated installion of multiple programs.")
    aboutE = questionary.select(
        message="Go back",
        instruction="(press enter)",
        choices=["back"],
    ).ask()
    initApp()

def installMenu():
    # brauche unbedingt besseren namen als instruction server

    whichInstructionFileSys = questionary.select(
        message="Select instruction file",
        choices=["Official (Online)", "Custom (Online)", "Local (Offline)"],
    ).ask()

    if whichInstructionFileSys == "Official (Online)":
        print("test")

    if whichInstructionFileSys == "Custom (Online)":
        print(whichInstructionFileSys)

    if whichInstructionFileSys == "Local (Offline)":
        print(whichInstructionFileSys)

def start():
    startIOHA = questionary.select(
    message="Select an action",
    choices=["Install", "Options", "About", "Exit"],
).ask()

    if startIOHA == "Install":
        # prepare Function
        prepFunction()

        # call installMenu function
        installMenu()
    if startIOHA == "Options":
        # prepare Function
        prepFunction()

        print("test")
        initApp()

    if startIOHA == "About":
        # prepare Function
        prepFunction()

        # call about function
        aboutMenu()

    if startIOHA == "Exit":
        # prepare Function
        prepFunction()

        exit()
        # ALTERNATIVE EXIT
        # return;

initApp()
    # whichInstructionFileSys = questionary.checkbox(
    #     "Select instruction file", choices=["Official (Online)", "Custom (Online)", "Local (Offline)"]
    #).ask()