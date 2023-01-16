"""Returns responses"""
import sys
import random
import Klaudie_simulator
import Snowglobe
import functions
import backup

#MAIN FUNC
def get_response(message, user_message: str) -> str:
    """Returns responses using functions in functions.py"""
    p_message:str = user_message.strip() #gets message
    admin_permission: bool = functions.check_permission(str(message.author.id),str(message.author.name), str(message.author.discriminator))
    permission_deny_message: str = "You **don't** have permission to do that, brrrr!"

    #ASLEEP
    if random.randint(1,25) == 1:
        return "Zzzzz 😴"


    #HELP
    ###
    #HELP
    if p_message == 'help':
        return functions.help_()

    #HELP STAFF
    if p_message == 'help_staff':
        if not admin_permission:
            return permission_deny_message
        return functions.help_staff()
    ###


    #ROZVRH
    ###
    #ROZVRH
    if p_message == 'rozvrh':
        return functions.rozvrh()

    #ROZVRH RIGGED
    if p_message.startswith("rozvrh") and len(p_message) > len("rozvrh"):
        if not admin_permission:
            return permission_deny_message
        rozvrh_index: str = p_message[6:].strip()
        return functions.rozvrh_rigged(rozvrh_index)

    #ADD ROZVRH
    if p_message.startswith("add_rozvrh") and len(p_message) > len("add_rozvrh"):
        if not admin_permission:
            return permission_deny_message
        rozvrh_add: str = p_message[10:].strip()
        return functions.add_rozvrh(rozvrh_add)

    #REMOVE ROZVRH
    if p_message.startswith("remove_rozvrh") and len(p_message) > len("remove_rozvrh"):
        if not admin_permission:
            return permission_deny_message
        rozvrh_remove: str = p_message[13:].strip()
        return functions.remove_rozvrh(rozvrh_remove)

    #LIST ROZVRH
    if p_message == "list_rozvrh":
        if not admin_permission:
            return permission_deny_message
        return functions.list_rozvrh()

    #LEN ROZVRH
    if p_message == "len_rozvrh":
        return functions.len_rozvrh()
    ###


    #STAV + RESENI
    ###
    #STAV
    if p_message == "stav":
        return functions.stav()

    #STAV RIGGED
    if p_message.startswith("stav") and len(p_message.strip()) > len("stav"):
        if not admin_permission:
            return permission_deny_message
        indexes: list = functions.valid_stav_rigged(p_message[4:].strip())
        if len(indexes) == 2:
            return functions.stav_reseni_rigged(indexes[0], indexes[1])
        if len(indexes) == 1:
            return functions.stav_rigged(indexes[0])
        return "Musíš napsat číslo indexu, brrrr!"

    #ADD STAV
    if p_message.startswith("add_stav") and len(p_message) > len("add_stav"):
        if not admin_permission:
            return permission_deny_message
        return functions.add_stav(p_message[8:].strip())

    #ADD RESENI
    if p_message.startswith("add_reseni") and len(p_message) > len("add_reseni"):
        if not admin_permission:
            return permission_deny_message
        return functions.add_reseni(p_message[10:].strip())

    #REMOVE STAV
    if p_message.startswith("remove_stav") and len(p_message) > len("remove_stav"):
        if not admin_permission:
            return permission_deny_message
        return functions.remove_stav(p_message[11:].strip())

    #REMOVE RESENI
    if p_message.startswith("remove_reseni") and len(p_message) > len("remove_reseni"):
        if not admin_permission:
            return permission_deny_message
        return functions.remove_reseni(p_message[13:].strip())

    #LIST STAV
    if p_message == "list_stav":
        if not admin_permission:
            return permission_deny_message
        return functions.list_stav()

    #LEN STAV
    if p_message == "len_stav":
        if not admin_permission:
            return permission_deny_message
        return functions.len_stav()

    #LIST RESENI
    if p_message == "list_reseni":
        if not admin_permission:
            return permission_deny_message
        return functions.list_reseni()

    #LEN RESENI
    if p_message == "len_reseni":
        if not admin_permission:
            return permission_deny_message
        return functions.len_reseni()
    ###


    #PERMISSIONS
    ###
    #ADMIN PERMISSION
    if p_message == "admin_permission":
        if not admin_permission:
            return "**Nemáš** *vyšší* pravomoce."
        return "**Máš** *vyšší* pravomoce."

    #ADD PERMISSION
    if p_message.startswith("add_permission") and len(p_message) > len("add_permission"):
        if not admin_permission:
            return permission_deny_message
        user: list = functions.valid_user(p_message[14:])
        if user: #empty list "is" False
            return functions.add_permission(user[0], user[1], user[2])
        return "Špatný syntax, brrrr!"

    #REMOVE PERMISSION
    if p_message.startswith("remove_permission") and len(p_message) > len("remove_permission"):
        if not admin_permission:
            return permission_deny_message
        user: list = functions.valid_user(p_message[17:])
        if user: #empty list "is" False
            return functions.remove_permission(user[0], user[1], user[2])
        return "Špatný syntax, brrrr!"

    #LIST PERMISSIONS
    if p_message == "list_permissions":
        return functions.list_permissions()

    # LEN PERMISSIONS
    if p_message == "len_permissions":
        return functions.len_permissions()
    ###

    #FILES
    ###
    #IMPORT
    if p_message == "import":
        if not admin_permission:
            return permission_deny_message
        return_value: str = backup.import_()
        if return_value != "Nemohl jsem najít **resources.zip** v adresáři, brrrr!":
            sys.exit()
        return return_value

    #EXPORT
    if p_message == "export":
        if not admin_permission:
            return permission_deny_message
        backup.export()
        sys.exit()

    #EXIT
    if p_message == "exit":
        sys.exit()

    #LEN FILES
    if p_message == "len_files":
        if not admin_permission:
            return permission_deny_message
        return backup.len_files()

    #LIST FILES
    if p_message == "list_files":
        if not admin_permission:
            return permission_deny_message
        return backup.list_files()
    ###


    #OTHER
    ###
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

    #LIST SNOWGLOBE
    if p_message == "list_snowglobe":
        if not admin_permission:
            return permission_deny_message
        with open("resources/snowglobe.txt","r",encoding="utf8") as file:
            return file.read()

    #GITHUB
    if p_message == "github":
        return "https://github.com/Dzendys/kun_prevalsky"

    #KLAUDIE SIMULATOR
    else:
        if random.randint(1,15) != 1:
            return Klaudie_simulator.klaudie_simulator(p_message)
        return "lol ne 😂😂😂😂"
    ###
