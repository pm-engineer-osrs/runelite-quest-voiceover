import hashlib

def str_to_md5(text: str) -> str:
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

replacements = {"[player name]": "Hero", 
                "[1-19]": "", 
                "[boy/girl]": "boy", 
                "[#]": "", 
                "[ball/balls]": "", 
                "[lad/lass]": "lad"}

def remove_special_characters(line: str) -> str:
    for pattern, replacement in replacements.items():
        line = line.replace(pattern,replacement)
    return line

def escape_single_quotes(text):
    return text.replace("'", "''")
