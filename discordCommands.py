"""All discord (application) commands"""
import random
import discord
from discord.ext import commands
from discord import app_commands
from classes import Snowglobe, Klaudie_simulator
from config import RESOURCES

class BasicCommands(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot

    @app_commands.command(name = "help")
    async def help_(self, interaction: discord.Interaction) -> None:
        """Informace o příkazech"""
        embed: discord.Embed = discord.Embed(
                title=RESOURCES.help["title"],
                color=discord.Colour.red(),
                description=RESOURCES.help["description"],
            )
        for name,value in dict(RESOURCES.help["commands"]).items():
            embed.add_field(name=name, value=value, inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "stav")
    @app_commands.describe(index_stavu = "index stavu", index_reseni = "idex řešení")
    async def stav(self, interaction: discord.Interaction, index_stavu:int = None, index_reseni:int = None) -> None:
        """Jak se mám v tuto chvíli?"""
        if index_reseni is None and index_reseni is None:
            await interaction.response.send_message(f"{random.choice(RESOURCES.stav)} {random.choice(RESOURCES.reseni)}")
            return
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        if index_stavu is not None and index_reseni is None and index_stavu < len(RESOURCES.stav):
            await interaction.response.send_message(f"{RESOURCES.stav[index_stavu]} {random.choice(RESOURCES.reseni)}")
            return
        if index_reseni is not None and index_stavu is None and index_reseni < len(RESOURCES.reseni):
            await interaction.response.send_message(f"{random.choice(RESOURCES.stav)} {RESOURCES.reseni[index_reseni]}")
            return
        if index_stavu is not None and index_reseni is not None and index_stavu < len(RESOURCES.stav) and index_reseni < len(RESOURCES.reseni):
            await interaction.response.send_message(f"{RESOURCES.stav[index_stavu]} {RESOURCES.reseni[index_reseni]}")
            return
        await interaction.response.send_message("**Špatný index!**")

    @app_commands.command(name = "program")
    @app_commands.describe(index = "index programu")
    async def program(self, interaction: discord.Interaction, index:int = None) -> None:
        """Co mám dneska na programu?"""
        if index is None:
            await interaction.response.send_message(random.choice(RESOURCES.program))
            return
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        if index is not None and index < len(RESOURCES.program):
            await interaction.response.send_message(RESOURCES.program[index])
            return
        await interaction.response.send_message("**Špatný index!**")

    @app_commands.command(name="snowglobe")
    async def snowglobe(self, interaction: discord.Interaction) -> None:
        """Zagambli si o tank jako o Vánocích ve WoT Bliz!"""
        globe: Snowglobe = Snowglobe(RESOURCES.snowglobe)
        await interaction.response.send_message(f"Gratuluji! Vyhrál jsi: **{globe.gamble()}**")

    @app_commands.command(name="list")
    @app_commands.describe(filename = "název příkazu")
    @app_commands.choices(filename = [
        discord.app_commands.Choice(name="permissions", value=1),
        discord.app_commands.Choice(name="program", value=2),
        discord.app_commands.Choice(name="reseni", value=3),
        discord.app_commands.Choice(name="stav", value=4)
    ])
    async def list_(self, interaction: discord.Interaction, filename:discord.app_commands.Choice[int]) -> None:
        """Vypíše všechny položky příkazu"""
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        attribute:list = getattr(RESOURCES,filename.name, None)
        embed: discord.Embed = discord.Embed(
            title=f"Obsah: {filename.name}",
            color=discord.Colour.red(),
            description= "\n".join([f"**{index}**: {i}" for index, i  in enumerate(attribute)])
        )
        await interaction.response.send_message(embed=embed)


    @app_commands.command()
    @app_commands.describe(filename = "název příkazu", arg = "obsah")
    @app_commands.choices(filename = [
        discord.app_commands.Choice(name="permissions", value=1),
        discord.app_commands.Choice(name="program", value=2),
        discord.app_commands.Choice(name="reseni", value=3),
        discord.app_commands.Choice(name="stav", value=4)
    ])
    async def add(self, interaction: discord.Interaction, filename:discord.app_commands.Choice[int], arg: str) -> None:
        """Přidá položku do vybraného příkazu"""
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        attribute:list = getattr(RESOURCES,filename.name, None)
        if arg in attribute:
            await interaction.response.send_message("**Nepřidáno!** Jedná se o duplicitní položku.")
            return
        attribute.append(arg)
        await interaction.response.send_message(f"**'{arg}'** přidáno do {filename.name}!")

    @app_commands.command(name="remove")
    @app_commands.describe(filename = "název příkazu", index = "index")
    @app_commands.choices(filename = [
        discord.app_commands.Choice(name="permissions", value=1),
        discord.app_commands.Choice(name="program", value=2),
        discord.app_commands.Choice(name="reseni", value=3),
        discord.app_commands.Choice(name="stav", value=4)
    ])
    async def remove(self, interaction: discord.Interaction, filename:discord.app_commands.Choice[int], index:int) -> None:
        """Odebere položku na vybraném indexu z příkazu"""
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        attribute:list = getattr(RESOURCES,filename.name, None)
        if index >= len(attribute):
            await interaction.response.send_message("**Špatný index!**")
            return
        del attribute[index]
        await interaction.response.send_message("Úspěšně **odstraněno**!")

    @app_commands.command(name="update")
    @app_commands.describe(filename = "název příkazu")
    @app_commands.choices(filename = [
        discord.app_commands.Choice(name="permissions", value=1),
        discord.app_commands.Choice(name="program", value=2),
        discord.app_commands.Choice(name="reseni", value=3),
        discord.app_commands.Choice(name="stav", value=4)
    ])
    async def update(self, interaction: discord.Interaction, filename:discord.app_commands.Choice[int]) -> None:
        """Synchronizuje vybraný příkaz na github"""
        if interaction.user.mention not in RESOURCES.permissions:
            await interaction.response.send_message("K tomuto příkazu **nemáš** práva!")
            return
        if RESOURCES.updateFile(filename.name):
            await interaction.response.send_message("Aktualizace proběhla **úspěšně**!")
            return
        await interaction.response.send_message("Aktualizace bohužel **neproběhla**! Zkontroluj, zda jsi napsal příkaz správně.")

    @app_commands.command()
    async def github(self, interaction: discord.Interaction) -> None:
        """Odkaz na stránku githubs s projektem"""
        await interaction.response.send_message("https://github.com/Dzendys/kun_prevalsky/")

    @app_commands.command()
    async def sex(self, interaction: discord.Interaction) -> None:
        """Easter egg"""
        await interaction.response.send_message("Až po svatbě, brrr!")

    @app_commands.command(name="ks")
    @app_commands.describe(arg = "text")
    async def ks(self, interaction: discord.Interaction, arg:str) -> None:
        """Klaudie simulátor"""
        await interaction.response.send_message(Klaudie_simulator(text=arg).scramble())

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BasicCommands(bot))
