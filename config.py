"""Configures all important constants"""
import sys
import os
from colorama import Fore
from tkinter.filedialog import askopenfilename
from github import Github, BadCredentialsException
from cryptography.fernet import Fernet
from classes import Resources


def getToken(token_path:str, key_path: str) -> str:
    """Gets token from encrypted file"""
    try:
        with open(token_path, "rb") as decrypted_file:
            decrypted_token = decrypted_file.read()
        key: Fernet = Fernet(getKey(key_path))
        print(Fore.GREEN + "Token was loaded!")
        return key.decrypt(decrypted_token).decode()
    except FileNotFoundError:
        print("File not found!")
        return ""

def getKey(key_path: str) -> str:
    """Gets key to encrypt tokens from resources"""
    try:
        with open(key_path,'rb') as unlock:
            return unlock.read()
    except FileNotFoundError:
        print(Fore.GREEN + "Token not loaded!")
        return ""

def getDiscordTokenPath() -> str:
    """Gets path of Discord token"""
    defaultPath: str = r"D:\Honza\Škola\SEPTIMA\IVT\Python\Kůň Převalský\token.key"
    if not os.path.isfile(defaultPath):
        defaultPath: str = askopenfilename(title="Vyber Discord TOKEN",
                                                defaultextension=".key",
                                                filetypes=(("Zašifrované soubory","*.key"), ("Všechny soubory", "*.*")))
    return defaultPath

def getGithubTokenPath() -> str:
    """Gets path of Github token"""
    defaultPath = r"D:\Honza\Škola\SEPTIMA\IVT\Python\Kůň Převalský\access_token.key"
    if not os.path.isfile(defaultPath):
        defaultPath: str = askopenfilename(title="Vyber Github TOKEN",
                                                defaultextension=".key",
                                                filetypes=(("Zašifrované soubory","*.key"), ("Všechny soubory", "*.*")))
    return defaultPath

def getKeyPath() -> str:
    """Gets path of the main key"""
    defaultPath:str = r"D:\Honza\Škola\SEPTIMA\IVT\Python\Kůň Převalský\key.key"
    if not os.path.isfile(defaultPath):
        defaultPath:str = askopenfilename(title="Vyber klíč k odšifrování",
                                    defaultextension=".key",
                                    filetypes=(("Zašifrované soubory","*.key"), ("Všechny soubory", "*.*")))
    return defaultPath

key_path: str = getKeyPath()
DISCORD_TOKEN: str = getToken(getDiscordTokenPath(), key_path=key_path)
GITHUB_TOKEN: str = getToken(getGithubTokenPath(), key_path=key_path)

#TESTING
if DISCORD_TOKEN == "" or GITHUB_TOKEN == "":
    print("Nenašel jsem token, brrrr!")
    input()
    sys.exit()
try:
    print(Fore.LIGHTBLUE_EX + "Downloading resources...")
    RESOURCES: Resources = Resources(github=Github(GITHUB_TOKEN))
except BadCredentialsException:
    print("Špatný github token, brrrr!")
    input()
    sys.exit()
