"""Contains all important classes"""
import json
import random
from github import Github, GithubException
import discord
from discord.ext import commands
from colorama import Fore

class Resources:
    def __init__(self, github: Github) -> None:
        self.github: Github = github
        self.help: dict[str, str | list] = json.loads(self.getFile("help"))
        self.permissions: list[str] = json.loads(self.getFile("permissions"))
        self.program: list[str] = json.loads(self.getFile("program"))
        self.reseni: list[str] = json.loads(self.getFile("reseni"))
        self.snowglobe: dict[str, int] = json.loads(self.getFile("snowglobe"))
        self.stav: list[str] = json.loads(self.getFile("stav"))

    def getFile(self, fileName:str) -> str:
        """Gets file from Github repository and returns a ``str``"""
        repo = self.github.get_repo(f"{self.github.get_user().login}/kun_prevalsky")
        contents = repo.get_contents(f"new_resources/{fileName}.json")
        print(Fore.LIGHTBLUE_EX + "Downloaded:", Fore.RED + fileName + Fore.WHITE)
        return contents.decoded_content.decode()

    def updateFile(self, fileName:str) -> bool:
        """Updates file back to Github"""
        dumped = json.dumps(getattr(self,fileName, None), ensure_ascii=False, indent=2)
        repo = self.github.get_repo(f"{self.github.get_user().login}/kun_prevalsky")
        contents = repo.get_contents(f"new_resources/{fileName}.json")
        try:
            repo.update_file(f"new_resources/{fileName}.json", "Add files via upload", dumped, sha=contents.sha, branch="main")
            return True
        except GithubException:
            return False

class MyBot(commands.Bot):
    def __init__(self):
        intents: discord.Intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix='/', intents=intents)
        self.activity = discord.Activity(type=discord.ActivityType.playing, name="si s dalšími koňmi ve stáji")

    async def on_ready(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.user} is now running!'+ Fore.WHITE)
        await self.change_presence(activity=self.activity)
        if not await self.sync():
            print("Nepodařilo se synchronizovat všechny slash commandy!")

    async def setup_hook(self) -> None:
        """Adds all commads and cogs to bot"""
        self.remove_command("help")
        await self.load_extension("discordCommands")
        #await self.load_extension("musicCog")

    async def sync(self) -> bool:
        try:
            await self.tree.sync()
            return True
        except Exception as e:
            print(e)
            return False

    async def on_command_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Špatný příkaz!**")

class Snowglobe:
    def __init__(self, tanks: dict[str, int]) -> None:
        self.tanks: dict[str, int] = tanks
        self.all: list[str] = []
        for tank,possibility in tanks.items():
            self.all += [tank for _ in range(possibility)]

    def gamble(self):
        return random.choice(self.all)

class Klaudie_simulator:
    def __init__(self, text:str) -> None:
        self.text = text

    def scramble(self) -> str:
        """Returns deformed word"""
        #CHANCES
        u_all: int = 4 #probability of missclick of ALL
        u_radky: int = 10 #probability of missclick to different keyboard line
        klaves: list = [["q","w","e","r","t","z","u","i","o","p"],["a","s","d","f","g","h","j","k","l"],["y","x","c","v","b","n","m"]]
        returning_word: str = "" #returning value
        for letter in self.text:
            if random.randint(1,u_all) == 1: #probability of missclick of ALL (1/4)
                seznam: list = [] #saves all possible letters

                #very usual letters of missclick
                if letter == "a":
                    seznam.append("q")
                elif letter=="e":
                    seznam.append("w")
                elif letter == "p":
                    seznam.append("o")

                #1st line on keyboard
                elif letter in klaves[0]:
                    #left
                    if klaves[0].index(letter) != 0:
                        for _ in range(u_radky):
                            seznam.append(klaves[0][klaves[0].index(letter)-1])
                    #right
                    if letter != klaves[0][-1]:
                        for _ in range(u_radky):
                            seznam.append(klaves[0][klaves[0].index(letter)+1])
                    #down
                    try:
                        seznam.append(klaves[1][klaves[0].index(letter)])
                    except IndexError:
                        pass

                #2nd line on keyboard
                elif letter in klaves[1]:
                    #left
                    if klaves[1].index(letter) != 0:
                        for _ in range(u_radky):
                            seznam.append(klaves[1][klaves[1].index(letter)-1])
                    #right
                    if letter != klaves[1][-1]:
                        for _ in range(u_radky):
                            seznam.append(klaves[1][klaves[1].index(letter)+1])
                    #down
                    try:
                        seznam.append(klaves[2][klaves[1].index(letter)])
                    except IndexError:
                        pass
                    #up
                    try:
                        seznam.append(klaves[0][klaves[1].index(letter)])
                    except IndexError:
                        pass

                #3rd line on keyboard
                elif letter in klaves[2]:
                    #left
                    if klaves[2].index(letter) != 0:
                        for _ in range(u_radky):
                            seznam.append(klaves[2][klaves[2].index(letter)-1])
                    #right
                    if letter != klaves[2][-1]:
                        for _ in range(u_radky):
                            seznam.append(klaves[2][klaves[2].index(letter)+1])
                    #up
                    try:
                        seznam.append(klaves[1][klaves[2].index(letter)])
                    except IndexError:
                        pass

                #if the letter is not on keyboard => stays same
                else:
                    seznam.append(letter)

                #chooses one letter of all possibilities
                returning_word+=str(random.choice(seznam))

            #letter stays same
            else:
                returning_word+=str(letter)
        return returning_word
