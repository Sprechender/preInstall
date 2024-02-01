import os
import requests # shit to download stuff
import sys # idk
import questionary # questions
from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

# config file
config_object["SETTINGS"] = {
    "1": "c",
    "2": "b",
    "3": "a"
}

config_object["TESTING"] = {
    "debugMode": "true",
    "ignoreOS": "false"
}

def clean():
    os.system('cls') # clear terminal

def quitApp():
    # maybe when debug dont clear
    

    clean()
    quit()
    exit()

def greet():
    print("WELCOME TO PREINSTALL!\n")

def checkCompatibility():
    if os.name != 'nt':
        print("ERROR:\n    Is not Windows.\n    preInstall is only supported on Windows!")
        exit()

def loadConfFile():
    
    #try:
    #    #Read config.ini file
    #    config_object = ConfigParser()
    #    config_object.read("config.ini")
    #except:
        #Write the above sections to config.ini file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)
        return;
def initApp():
    loadConfFile() # tries to load config

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
            choices=["Updates", "Default Repo", "Misc", "Back"],
        ).ask()
        
        clean()
        match q__optionsMenu:
            case "Updates":
                q__optionsMenu__updates = questionary.select(
                    message="Do you want automatic updates",
                    choices=["Yes", "No"],
            ).ask()
                   
                match q__optionsMenu__updates:
                    case "Yes":
                        print("true")
                        return
                    case "No":
                        print("false")
                        return
                return
            case "Default Repo":
                q__optionsMenu__defaultRepo = questionary.select(
                    message="From which repo do you want to request instructions",
                    choices=["Official", "Untested", "Custom"],
                ).ask()
                match q__optionsMenu__defaultRepo:
                    case "Official":
                        print("official")
                        return
                    case "Untested":
                        print("untested")
                        return
                    case "Custom":
                        print("custom")
                        return
                return        
            case "Misc":
                q__optionsMenu__misc = questionary.select(
                    message="Some miscellaneous options",
                    choices=["Auto Install", "Export Instruction groups", "Logs", "Create config file"],
                ).ask()
            
                match q__optionsMenu__misc:
                    case "Auto Install":
                        print("auto install")
                        return
                    case "Export Instruction groups":
                        print("export instruction groups")
                        return
                    case "Logs":
                        print("logs")
                        return
                    case "Create config file":
                        print("create config file")
                        return
                print("misc")
                return

    loadOptionsMenu()

    print("saving...")

def installMenu():
    # brauche unbedingt besseren namen als instruction server

    whichInstructionFileSys = questionary.select(
        message="Select instruction file",
        choices=["Official (Online)", "Custom (Online)", "Local (Offline)"],
    ).ask()
    
    match whichInstructionFileSys:
        case "Official (Online)":
            print("apfel")
            return
        case "Custom (Online)":
            print(whichInstructionFileSys)
            return
        case "Local (Offline)":
            print(whichInstructionFileSys)
            return

def start():
    startIOHA = questionary.select(
    message="Select an action",
    choices=["Install", "Options", "About", "Exit"],
).ask()

    match startIOHA:
        case "Install":
            # prepare Function
            prepFunction()

            # call installMenu function
            installMenu()
            return
        case "Options":
            # prepare Function
            prepFunction()
            optionsMenu()
            initApp()
            return;
        case "About":
            # prepare Function
            prepFunction()

            # call about function
            aboutMenu()

            initApp() # reset
            return
        case "Exit":
            # prepare Function
            prepFunction()
            exit()
            # ALTERNATIVE EXIT
            # return;

initApp()
    # whichInstructionFileSys = questionary.checkbox(
    #     "Select instruction file", choices=["Official (Online)", "Custom (Online)", "Local (Offline)"]
    #).ask()