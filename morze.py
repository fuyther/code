def to_morze(string):
    alphabet = {
        "А": "· −", "Б": "− · · ·", "В": "· − −", "Г": "− − ·", "Д": "− · ·", "Е": "·", "Ж": "· · · −", "З": "− − · ·",
        "И": "· ·", "Й": "· − − −", "К": "− · −", "Л": "· − · ·", "М": "− −", "Н": "− ·", "О": "− − −", "П": "· − − ·",
        "Р": "· − ·", "С": "· · ·", "Т": "−", "У": "· · −", "Ф": "· · − ·", "Х": "· · · ·", "Ц": "	− · − ·",
        "Ч": "	− − − ·", "Ш": "− − − −", "Щ": "− − · −", "Ъ": "− − · − −", "Ы": "− · − −", "Ь": "− · · −",
        "Э": "	· · − · ·", "Ю": "	· · − −", "Я": "· − · −", "1": "· − − − −", "2": "· · − − −", "3": "· · · − −",
        "4": "· · · · −", "5": "· · · · ·", "6": "	− · · · ·", "7": "− − · · ·", "8": "− − − · ·", "9": "− − − − ·",
        "0": "− − − − −", ".": "· · · · · ·", ",": "· − · − · −", ":": "− − − · · ·", "(": "	− · − − · −",
        '"': "	· − · · − ·", ";": "− · − · − ·", "'": "	· − − − − ·	", "-": "− · · · · −", "/": "− · · − ·",
        "?": "· · − − · ·", "!": "− − · · − −", "error": "· · · · · · · ·"
    }
    en_to_ru = {
        "A": "А", "B": "Б", "W": "В", "G": "Г", "D": "Д", "E": "Е", "V": "Ж", "Z": "З",
        "I": "И", "J": "Й", "K": "К", "L": "Л", "M": "М", "N": "Н", "O": "О", "P": "П",
        "R": "Р", "S": "С", "T": "Т", "U": "У", "F": "Ф", "H": "Х", "C": "Ц",
        "Q": "Щ", "Y": "Ы", "X": "Ь"
    }
    result = ""
    for symbol in string:
        symbol = symbol.upper()
        if symbol in en_to_ru.keys():
            symbol = en_to_ru[symbol]
        if symbol != " ":
            result += alphabet[symbol] + "  "
        else:
            result += "  "
    return result


print(to_morze(input()))
