# meine_funktionen.py

def begruesse_user(name):
    """Gibt eine personalisierte Begrüßung zurück."""
    return f"Hallo {name}, willkommen im Programm!"

def dividiere(a, b):
    """Teilt zwei Zahlen und behandelt Division durch Null."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Fehler: Division durch Null ist nicht erlaubt!"
