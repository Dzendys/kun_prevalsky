"""Backup"""
import os
import shutil
import datetime

def export() -> str:
    """Exports resources to zip."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    docs:str = os.path.join(os.path.expanduser("~"), "Documents")
    backup_name: str = "Export resources"
    time_format: str = str(datetime.datetime.now())[:19].replace(":","-")
    dirname: str= f"{backup_name} {time_format}"
    print(os.getcwd())
    shutil.make_archive(dirname, format="zip",root_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources"))
    shutil.move(dirname+".zip",docs)
    return "Soubory byly úspěšně extrahovány."

def import_() -> str:
    """Imports zip resources."""
    dir_name = "resources.zip"
    path = os.path.dirname(os.path.abspath(__file__))
    docs:str = os.path.join(os.path.expanduser("~"), "Documents")
    os.chdir(docs)
    if dir_name not in os.listdir():
        return f"Nemohl jsem najít **{dir_name}** v adresáři, brrrr!"
    shutil.move(dir_name, os.path.join(path, "resources"))
    os.chdir(os.path.join(path, "resources"))
    shutil.unpack_archive(dir_name,os.path.join(path, "resources"))
    os.remove("resources.zip")
    if len(os.listdir()) > 8:
        resources: list = ["help_staff.txt", "help.txt", "permissions.txt", "reseni.txt", "rozvrh.txt", "snowglobe.txt", "stav.txt", "vtipy.txt"]
        for file in os.listdir():
            if file not in resources:
                os.remove(file)
    return "Soubory byly úspěšně importovány."

#LIST FILES
def list_files() -> str:
    """Returns list of resources."""
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources"))
    files:list = [f"{index}. {file}" for index,file in enumerate(os.listdir())]
    return "\n".join(files)

#LEN FILES
def len_files() -> str:
    """Returns the number of resource files."""
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources"))
    return f"Eviduju **{len(os.listdir())}** souborů."
