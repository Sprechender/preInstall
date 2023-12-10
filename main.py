import os
import requests # shit to download stuff
import sys # idk
import questionary # questions

def clean():
        os.system('cls') # clear terminal

def greet():
    print("WELCOME TO PREINSTALL!\n")

def checkCompatibility():
    if os.name != 'nt':
        print("ERROR:\n    Is not Windows.\n    preInstall is only supported on Windows!")
        exit()

def initApp():
    clean() # clears the terminal
    greet() # greets the user (ex. " welcome to preInstall")
    checkCompatibility() # checks if system is compatible
    start() # starts IOHA menu

def prepFunction():
    clean() # clears the terminal

def aboutMenu():
    print("Hey there! 👋 I'm Sprechender, the developer behind this python script.") # blablabla
    print("This Script helps you with the automated installion of multiple programs.") # more blablabla
    aboutE = questionary.select( # go back question
        message="Go back",
        instruction="(press enter)",
        choices=["back"],
    ).ask()
    
    return; # return to main


# config.preinstall

def optionsMenu():
    def loadOptionsMenu():
        q__optionsMenu = questionary.select(
            message="Select an option you want to edit",
            choices=["Updates", "Default Repo", "Misc"],
        ).ask()
        
        clean()
    
        if q__optionsMenu == "Updates":
            q__optionsMenu__updates = questionary.select(
                message="Do you want automatic updates",
                choices=["Yes", "No"],
            ).ask()
            if q__optionsMenu__updates == "Yes":
                print("true")
            elif q__optionsMenu__updates == "No":
                print("false")
        
        elif q__optionsMenu == "Default Repo":
            q__optionsMenu__defaultRepo = questionary.select(
                message="From which repo do you want to request instructions",
                choices=["Official", "Untested", "Custom"],
            ).ask()

            if q__optionsMenu__defaultRepo == "Official":
                print("official")
            
            elif q__optionsMenu__defaultRepo == "Untested":
                print("untested")
            
            elif q__optionsMenu__defaultRepo == "Custom":
                print("custom")
            
            print("default repo")

        elif q__optionsMenu == "Misc":
            q__optionsMenu__misc = questionary.select(
                message="Some miscellaneous options",
                choices=["Auto Install", "Export Instruction groups", "Logs", "Create config file"],
            ).ask()
            
            if q__optionsMenu__misc == "Auto Install":
                print("auto install")
            
            elif q__optionsMenu__misc == "Export Instruction groups":
                print("export instruction groups")
            
            elif q__optionsMenu__misc == "Logs":
                print("logs")
            
            elif q__optionsMenu__misc == "Create config file":
                print("create config file")

        print("misc")

    loadOptionsMenu()

    print("saving...")

def installMenu():
    # brauche unbedingt besseren namen als instruction server

    whichInstructionFileSys = questionary.select(
        message="Select instruction file",
        choices=["Official (Online)", "Custom (Online)", "Local (Offline)"],
    ).ask()
    
    if whichInstructionFileSys == "Official (Online)":
        print("apfel")

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

        optionsMenu()

        initApp()

    if startIOHA == "About":
        # prepare Function
        prepFunction()

        # call about function
        aboutMenu()

        initApp() # reset

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