"""All functions"""
import random
import os
from cryptography.fernet import Fernet

#HELP
###
#HELP
def help_() -> str:
    """Returns commands for basic user."""
    with open("resources/help.txt","r",encoding="utf8") as help_file:
        return help_file.read()

#HELP STAFF
def help_staff() -> str:
    """Returns commands for admin users."""
    with open("resources/help_staff.txt","r",encoding="utf8") as help_staff_file:
        return help_staff_file.read()
###


#ROZVRH
###
#GET ROZVRH
def get_rozvrh() -> list:
    """Returns list all types from rozvrh."""
    with open("resources/rozvrh.txt","r",encoding="utf8") as get_rozvrh_file:
        return get_rozvrh_file.read().split("\n")

#UPDATE ROZVRH
def update_rozvrh(lst: list):
    """Updates rozvrh in files."""
    updated_rozvrh: str = "\n".join(lst)
    with open("resources/rozvrh.txt", "w", encoding="utf8") as update_rozvrh_file:
        update_rozvrh_file.write(updated_rozvrh)

#ROZVRH
def rozvrh() -> str:
    """Returns random choice from rozvrh."""
    return random.choice(get_rozvrh())

#ROZVRH RIGGED
def rozvrh_rigged(rozvrh_index: str) -> str:
    """Returns given choice from rozvrh. \n
    index is type of string - we need to test converting to int"""
    rozvrh_len: int = len(get_rozvrh())
    if int_try_parse(rozvrh_index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    rozvrh_index: int = int(rozvrh_index)
    if rozvrh_index >= rozvrh_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    return get_rozvrh()[rozvrh_index]

#ADD ROZVRH
def add_rozvrh(text: str) -> str:
    """Adds new choice to rozvrh."""
    rozvrh_previous_choices: list = get_rozvrh()
    if text[0].islower():
        text = text[0].upper() + text[1:]
    if text[-1]!=".":
        text +="."
    rozvrh_new_choices: list = rozvrh_previous_choices+[text]
    update_rozvrh(rozvrh_new_choices)
    return f"**{text}** přidáno do seznamu *rozvrh*"

#REMOVE ROZVRH
def remove_rozvrh(index:str) -> str:
    """Removes given choice from rozvrh.\n
    index is type of string - we need to test converting to int"""
    rozvrh_previous_choices: list = get_rozvrh()
    rozvrh_len: int = len(rozvrh_previous_choices)
    if int_try_parse(index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    index: int = int(index)
    if index >= rozvrh_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    del rozvrh_previous_choices[index]
    update_rozvrh(rozvrh_previous_choices)
    return f"Index **{index}** odebráno ze seznamu *rozvrh*"

#LIST ROZVRH
def list_rozvrh() -> str:
    """Returns list of all choices in rozvrh."""
    rozvrh_choices: list = [str(f"{index}. {line}") for index,line in enumerate(get_rozvrh())]
    return "\n".join(rozvrh_choices)

#LEN ROZVRH
def len_rozvrh() -> str:
    """Returns length of all choices in rozvrh."""
    len_rozvrh_choices = len(get_rozvrh())
    return f"Aktuálně eviduju **{len_rozvrh_choices}** aktivit."
###


#STAV
###
#GET STAV
def get_stav() -> list:
    """Returns list all types from stav."""
    with open("resources/stav.txt","r",encoding="utf8") as get_stav_file:
        return get_stav_file.read().split("\n")

#GET RESENI
def get_reseni() -> list:
    """Returns list all types from reseni."""
    with open("resources/reseni.txt","r",encoding="utf8") as get_reseni_file:
        return get_reseni_file.read().split("\n")

#STAV
def stav() -> str:
    """Returns random choice from stav."""
    if random.randint(1,50) == 5:
        return "Mám se dobře"
    return f"Mám se zle, protože {random.choice(get_stav())}. {random.choice(get_reseni())}"

#STAV RIGGED
def stav_rigged(stav_index: int) -> str:
    """Returns given choice from stav and random choice from reseni."""
    stav_len: int = len(get_stav())
    if stav_index >= stav_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    return f"Mám se zle, protože {get_stav()[stav_index]}. {random.choice(get_reseni())}"

#STAV RIGGED
def stav_reseni_rigged(stav_index: int, reseni_index: int) -> str:
    """Returns given choice from stav and reseni."""
    stav_len: int = len(get_stav())
    reseni_len: int = len(get_reseni())
    if stav_index >= stav_len or reseni_index >= reseni_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    return f"Mám se zle, protože {get_stav()[stav_index]}. {get_reseni()[reseni_index]}"

#VALID STAV RIGGED
def valid_stav_rigged(text: str) -> list:
    """Returns two, one or zero integers depending to user input.
    text is type of string - raw user input"""
    try:
        indexes: list = [int(num) for num in text.split(" ")]
        if len(indexes) == 2 or len(indexes) == 1:
            return indexes
        return []
    except ValueError:
        return []

#UPDATE STAV
def update_stav(lst: list):
    """Updates stav in files."""
    updated_stav: str = "\n".join(lst)
    with open("resources/stav.txt", "w", encoding="utf8") as update_stav_file:
        update_stav_file.write(updated_stav)

#ADD STAV
def add_stav(text:str) -> str:
    """Adds new choice to stav."""
    stav_previous_choices: list = get_stav()
    if text.startswith("Mám se zle, protože "):
        text = text[20:]
    if text[0].isupper():
        text = text[0].lower() + text[1:]
    if text[-1] == ".":
        text = text[:-1]
    stav_previous_choices.append(text)
    update_stav(stav_previous_choices)
    return f"**{text}** úspěšně přidáno na seznam *stav*"

#UPDATE RESENI
def update_reseni(lst: list):
    """Updates stav in reseni."""
    updated_reseni: str = "\n".join(lst)
    with open("resources/reseni.txt", "w", encoding="utf8") as update_reseni_file:
        update_reseni_file.write(updated_reseni)

#ADD RESENI
def add_reseni(text:str) -> str:
    """Adds new choice to reseni."""
    reseni_previous_choices: list = get_reseni()
    if text[0].islower():
        text = text[0].upper() + text[1:]
    if text[-1] != ".":
        text = text+"."
    reseni_previous_choices.append(text)
    update_reseni(reseni_previous_choices)
    return f"**{text}** úspěšně přidáno na seznam *reseni*"

#REMOVE STAV
def remove_stav(index:str) -> str:
    """Removes given choice from stav.\n
    index is type of string - we need to test converting to int"""
    stav_previous_choices: list = get_stav()
    stav_len: int = len(stav_previous_choices)
    if int_try_parse(index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    index: int = int(index)
    if index >= stav_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    del stav_previous_choices[index]
    update_stav(stav_previous_choices)
    return f"Index **{index}** odebráno ze seznamu *stav*"

#REMOVE STAV
def remove_reseni(index:str) -> str:
    """Removes given choice from reseni.\n
    index is type of string - we need to test converting to int"""
    reseni_previous_choices: list = get_reseni()
    reseni_len: int = len(reseni_previous_choices)
    if int_try_parse(index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    index: int = int(index)
    if index >= reseni_len:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    del reseni_previous_choices[index]
    update_reseni(reseni_previous_choices)
    return f"Index **{index}** odebráno ze seznamu *reseni*"

#LIST STAV
def list_stav() -> str:
    """Returns list of all choices in stav."""
    stav_choices: list = [str(f"{index}. Mám se zle, protože {line}.") for index,line in enumerate(get_stav())]
    return "\n".join(stav_choices)

#LEN STAV
def len_stav() -> str:
    """Returns length of all choices in stav."""
    return f"Eviduju **{len(get_stav())}** stavů."

#LIST RESENI
def list_reseni() -> str:
    """Returns list of all choices in reseni."""
    reseni_choices: list = [str(f"{index}. {line}") for index,line in enumerate(get_reseni())]
    return "\n".join(reseni_choices)

#LEN RESENI
def len_reseni() -> str:
    """Returns length of all choices in reseni."""
    return f"Eviduju **{len(get_reseni())}** řešení."
###

#PERMISSIONS
###
#GET PERMISSIONS
def get_permissions() -> list:
    """Returns all users from permissions."""
    with open("resources/permissions.txt","r",encoding="utf8") as get_permissions_file:
        permissions: list = get_permissions_file.read().split("\n")
        if permissions == [""]:
            return []
        return [[user.split(" ",1)[0], user.split(" ",1)[1][:-5], user.split(" ",1)[1][-4:]] for user in permissions]

#UPDATE PERMISSIONS
def update_permissions(lst: list[list]):
    """Updates permissions in files."""
    updated_permissions: str = "\n".join([f"{user[0]} {user[1]} {user[2]}" for user in lst])
    with open("resources/permissions.txt", "w", encoding="utf8") as update_permissions_file:
        update_permissions_file.write(updated_permissions)

#PERMISSION CHECKER
def check_permission(id_: str,name: str,discriminator: str) -> bool:
    """Return True, if user has admin permission - otherwise False."""
    if f"{id_} {name} {discriminator}" == "417328107939299329 dzendys_ 0258":
        return True
    permissions = get_permissions()
    if [id_,name,discriminator] in permissions:
        return True
    return False

#ADD PERMISSION
def add_permission(id_: str,name: str,discriminator: str) -> str:
    """Adds user to list of permissions."""
    all_permissions: list[list] = get_permissions()
    if [id_,name,discriminator] not in all_permissions:
        all_permissions.append([id_,name,discriminator])
        update_permissions(all_permissions)
        return f"**{name}** přidán na seznam práv."
    return f"**{name}** je již registrován, brrrr!"

#REMOVE PERMISSION
def remove_permission(id_: str,name: str,discriminator: str) -> str:
    """Removes user from list of permissions."""
    all_permissions: list[list] = get_permissions()
    if [id_,name,discriminator] in all_permissions:
        all_permissions.remove([id_,name,discriminator])
        update_permissions(all_permissions)
        return f"**{name}** byl odebrán ze seznamu práv."
    return f"**{name}** není na seznamu práv, brrrr!"

# LIST PERMISSIONS
def list_permissions() -> str:
    """Returns list of all users on permissions list."""
    permissions: list = get_permissions()
    if not permissions:
        return "Nikdo až na **správce** bota není na seznamu práv."
    lst_permissions: list = [f"{line[0]} {line[1]}#{line[2]}" for line in permissions]
    return "\n".join(lst_permissions)

#LEN PERMISSIONS
def len_permissions() -> str:
    """Returns the number of users with admin permissions."""
    return f"Aktuálně eviduju **{len(get_permissions())}** uživatelů na seznamu práv."

#TRY PARSE
def int_try_parse(value:str) -> bool:
    """Returns True, if value can be converted to integer - otherwise False."""
    try:
        value = int(value)
        return True
    except ValueError:
        return False

#VALID USER
def valid_user(text: str) -> list:
    """Returns user type of list in valid format - otherwise empty list"""
    user_id, user_name = text.strip().split(" ", 1)
    if int_try_parse(user_id) is True and user_name[-5] == "#" and int_try_parse(user_name[-4:]) is True:
        return [user_id, user_name[:-5], user_name[-4:]]
    return []
###


#OTHER
###
#VTIPY
def vtip() -> str:
    """Returns random joke from list of vtip."""
    with open("resources/vtipy.txt", "r",encoding="utf8") as vtipy_file:
        vtipy: list= vtipy_file.read().split("\n\n")
    return random.choice(vtipy)
###

#TOKEN
###
#GET TOKEN
def get_token() -> str:
    """Gets token from encrypted file in Documents"""
    try:
        path:str = os.path.join(os.path.expanduser("~"), "Documents", "token.key")
        with open(path, "rb") as decrypted_file:
            decrypted_token = decrypted_file.read()
        key = Fernet(get_key())
        return key.decrypt(decrypted_token).decode()
    except FileNotFoundError:
        print("Token not found in documents:",path)
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "token.key")
            with open(path, "rb") as decrypted_file:
                decrypted_token = decrypted_file.read()
            key = Fernet(get_key())
            return key.decrypt(decrypted_token).decode()
        except FileNotFoundError:
            print("Token not found in directory:",path)
            try:
                path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "token.key")
                with open(path, "rb") as decrypted_file:
                    decrypted_token = decrypted_file.read()
                key = Fernet(get_key())
                return key.decrypt(decrypted_token).decode()
            except FileNotFoundError:
                print("Token not found in outer directory:",path)
                return ""

#GET KEY
def get_key() -> str:
    """Gets key to encrypt token from resources"""
    with open('key.key','rb') as unlock:
        return unlock.read()
###
