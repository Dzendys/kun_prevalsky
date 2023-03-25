"""Returns responses"""
import sys
import random
import Klaudie_simulator
import Snowglobe
import functions

#MAIN FUNC
def get_response(message, user_message: str) -> str:
    """Returns responses using functions in functions.py"""
    p_message:str = user_message.strip() #gets message
    admin_permission: bool = functions.check_permission(str(message.author.id),str(message.author.name) + "#" + str(message.author.discriminator))
    permission_deny_message: str = "You **don't** have permission to do that, brrrr!"
    items: list = ["rozvrh", "stav", "reseni", "permissions"]

    #ASLEEP
    if random.randint(1,25) == 1:
        return "Zzzzz 😴"

    #HELP
    if p_message.startswith("help"):
        #HELP
        if p_message == 'help':
            return functions.get(file_name="help")

        #HELP STAFF
        if p_message == 'help_staff':
            if not admin_permission:
                return permission_deny_message
            return functions.get(file_name="help_staff")

    #ROZVRH
    if p_message.startswith("rozvrh"):
        if len(p_message) > len("rozvrh"):
            rozvrh_index: str = p_message[6:].strip()
            return functions.rozvrh(rozvrh_index=rozvrh_index)
        return functions.rozvrh()
    
    #STAV
    if p_message.startswith("stav"):
        if len(p_message) > len("stav"):
            if len(p_message[4:].strip().split(" ", 1)) == 2:
                stav_index: str = p_message[4:].strip().split(" ", 1)[0]
                reseni_index: str = p_message[4:].strip().split(" ", 1)[1]
                return functions.stav(stav_index, reseni_index)
            stav_index: str = p_message[4:].strip()
            return functions.stav(stav_index)
        return functions.stav()

    #ADD
    if p_message.startswith("add_"):
        if not admin_permission: #check permission
            return permission_deny_message
        file_name: str = p_message[4:].strip().split(" ")[0]
        if file_name not in items: #check valid list
            return f"Seznam **{file_name}** neeviduju, brrrr!"
        if len(p_message) <= len(f"add_{file_name}"): #check empty
            return "Zapomněl jsi, cos chtěl přidat, brrrr!"
        if file_name == "rozvrh":
            new_choice: str = p_message[10:].strip()
            if new_choice[0].islower():
                new_choice = new_choice[0].upper() + new_choice[1:]
            if new_choice[-1]!=".":
                new_choice +="."
        elif file_name == "stav":
            new_choice: str = p_message[8:].strip()
            if new_choice.startswith("Mám se zle, protože "):
                new_choice = new_choice[20:]
            if new_choice[0].isupper():
                new_choice = new_choice[0].lower() + new_choice[1:]
            if new_choice[-1] == ".":
                new_choice = new_choice[:-1]
        elif file_name == "reseni":
            new_choice: str = p_message[10:].strip()
            if new_choice[0].islower():
                new_choice = new_choice[0].upper() + new_choice[1:]
            if new_choice[-1] != ".":
                new_choice = new_choice+"."
        elif file_name == "permissions":
            new_choice: str = p_message[15:].strip()
        return functions.add(file_name=file_name,new_item=new_choice)

    #REMOVE
    if p_message.startswith("remove_"):
        if not admin_permission:
            return permission_deny_message
        file_name: str = p_message[7:].strip().split(" ")[0]
        if file_name not in items: #check valid list
            return f"Seznam **{file_name}** neeviduju, brrrr!"
        if file_name == "rozvrh":
            index: str = p_message[13:].strip()
        elif file_name == "stav":
            index: str = p_message[8:].strip()
        elif file_name == "reseni":
            index: str = p_message[10:].strip()
        elif file_name == "permissions":
            index: str = p_message[18:].strip()
        return functions.remove(file_name=file_name, index=index)

    #LEN
    if p_message.startswith("len_"):
        if not admin_permission: #check permission
            return permission_deny_message
        file_name: str = p_message[4:].strip()
        if file_name not in items: #check valid list
            return f"Seznam **{file_name}** neeviduju, brrrr!"
        return functions.len_(file_name=file_name)

    #LIST
    if p_message.startswith("list_"):
        if not admin_permission: #check permission
            return permission_deny_message
        file_name: str = p_message[5:].strip()
        if file_name not in items or file_name == "snowglobe": #check valid list
            return f"Seznam **{file_name}** neeviduju, brrrr!"
        return functions.list_(file_name=file_name)

    #ADMIN PERMISSION
    if p_message == "admin_permission":
        if not admin_permission:
            return "**Nemáš** *vyšší* pravomoce."
        return "**Máš** *vyšší* pravomoce."

    #EXIT
    if p_message == "exit":
        sys.exit()

    #EASTER EGG
    if p_message == '🐴':
        return "To jsem já, jsem ti k službám, brrrrrr!🐴"

    #:)
    if p_message == "sex":
        return "Až po svatbě, brrrr!"

    #VTIP
    if p_message == "vtip":
        return functions.vtip()

    #SNOWGLOBE
    if p_message == "snowglobe":
        return Snowglobe.snowglobe()

    #GITHUB
    if p_message == "github":
        return "https://github.com/Dzendys/kun_prevalsky"

    #KLAUDIE SIMULATOR
    if random.randint(1,15) != 1:
        return Klaudie_simulator.klaudie_simulator(p_message)
    return "lol ne 😂😂😂😂"
