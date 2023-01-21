"""All functions"""
import random
import os
import json
from cryptography.fernet import Fernet
from github import Github

#GET
def get(file_name:str):
    """Gets resource file from github"""
    git = Github(get_access_token())
    repo = git.get_repo(f"{git.get_user().login}/kun_prevalsky")
    contents = repo.get_contents(f"resources/{file_name}.json")
    return json.loads(contents.decoded_content.decode())

#UPDATE
def update(file_name:str, file):
    """Updates file on github"""
    dumped_file = json.dumps(file, ensure_ascii=False, indent=2)
    git = Github(get_access_token())
    repo = git.get_repo(f"{git.get_user().login}/kun_prevalsky")
    contents = repo.get_contents(f"resources/{file_name}.json")
    repo.update_file(f"resources/{file_name}.json", "Add files via upload", dumped_file, sha=contents.sha, branch="main")

# ADD
def add(file_name:str, new_item:str) -> str:
    """Adds item to specific list and then updates it on Github using update()"""
    file: list = get(file_name)
    if new_item in file:
        return f"**{new_item}** už je na seznamu *{file_name}*, brrrr!"
    file.append(new_item)
    update(file_name, file)
    return f"**{new_item}** přidáno na seznam *{file_name}*."

#REMOVE
def remove(file_name:str, index:str) -> str:
    """Removes item from specific list and then updates it on Github using update()"""
    if int_try_parse(index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    index = int(index)
    file: list = get(file_name)
    if index >= len(file):
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    del file[index]
    update(file_name, file)
    return f"Index **{index}** odebrán ze seznamu *{file_name}*."

# LIST
def list_(file_name:str) -> str:
    """Returns list of items with indexes"""
    choices: list = [str(f"{index}. {line}") for index,line in enumerate(get(file_name))]
    return "\n".join(choices)

#LEN
def len_(file_name:str) -> str:
    """Returns number of choices in specific list."""
    return f"Eviduju **{len(get(file_name))}** možností."

#ROZVRH
def rozvrh(rozvrh_index = None) -> str:
    """Returns random choice from rozvrh."""
    if rozvrh_index is None:
        return random.choice(get("rozvrh"))
    if int_try_parse(rozvrh_index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    try:
        return get("rozvrh")[int(rozvrh_index)]
    except IndexError:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"

#STAV
def stav(stav_index = None, reseni_index = None) -> str:
    """Returns random choice from stav."""
    if stav_index is None and reseni_index is None:
        return f"Mám se zle, protože {random.choice(get('stav'))}. {random.choice(get('reseni'))}"
    if reseni_index is None:
        if int_try_parse(stav_index) is False:
            return "Musíš napsat číslo indexu, brrrr!"
        try:
            return f"Mám se zle, protože {get('stav')[int(stav_index)]}. {random.choice(get('reseni'))}"
        except IndexError:
            return "Musíš napsat číslo ve správném rozsahu, brrrr!"
    if int_try_parse(stav_index) is False or int_try_parse(reseni_index) is False:
        return "Musíš napsat číslo indexu, brrrr!"
    try:
        return f"Mám se zle, protože {get('stav')[int(stav_index)]}. {get('reseni')[int(stav_index)]}"
    except IndexError:
        return "Musíš napsat číslo ve správném rozsahu, brrrr!"

#PERMISSION CHECKER
def check_permission(id_: str, username: str) -> bool:
    """Return True, if user has admin permission - otherwise False."""
    if f"{id_} {username}" == "417328107939299329 dzendys_#0258":
        return True
    permissions: list = get("permissions")
    if [id_, username] in permissions:
        return True
    return False

#TRY PARSE
def int_try_parse(value:str) -> bool:
    """Returns True, if value can be converted to integer - otherwise False."""
    try:
        value = int(value)
        return True
    except ValueError:
        return False

#VTIPY
def vtip() -> str:
    """Returns random joke from list of vtip."""
    return random.choice(random.choice(get("vtipy")))

#GET TOKEN
def get_token(token_file_name:str) -> str:
    """Gets token from encrypted file in Documents"""
    try:
        path:str = os.path.join(os.path.expanduser("~"), "Documents", token_file_name)
        with open(path, "rb") as decrypted_file:
            decrypted_token = decrypted_file.read()
        key = Fernet(get_key())
        print(f"{token_file_name} found in documents:",path)
        return key.decrypt(decrypted_token).decode()
    except FileNotFoundError:
        print(f"{token_file_name} not found in documents:",path)
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), token_file_name)
            with open(path, "rb") as decrypted_file:
                decrypted_token = decrypted_file.read()
            key = Fernet(get_key())
            print(f"{token_file_name} found in directory:",path)
            return key.decrypt(decrypted_token).decode()
        except FileNotFoundError:
            print(f"{token_file_name} not found in directory:",path)
            try:
                path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), token_file_name)
                with open(path, "rb") as decrypted_file:
                    decrypted_token = decrypted_file.read()
                key = Fernet(get_key())
                print(f"{token_file_name} found in outer directory:",path)
                return key.decrypt(decrypted_token).decode()
            except FileNotFoundError:
                print(f"{token_file_name} not found in outer directory:",path)
                return ""

#ACCESS TOKEN
def get_access_token() -> str:
    """Returns access token for github"""
    key: str = get_key()
    with open("access_token.key", "rb") as decrypted_file:
        decrypted_access_token = decrypted_file.read()
    key = Fernet(get_key())
    return key.decrypt(decrypted_access_token).decode()

#GET KEY
def get_key() -> str:
    """Gets key to encrypt token from resources"""
    with open('key.key','rb') as unlock:
        return unlock.read()
