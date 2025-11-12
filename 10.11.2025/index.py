# def greet(text):
#     print(text)

# greet("Hallo, ILP Teilnehmer!")



# def greetPerson(name):
#     print(f"Hallo {name}!")

# greetPerson("Yasaswi")
# greetPerson("Khaliq")
# greetPerson("Ronak")
# greetPerson("Dora")

# # Definiere eine Funktion, die zwei Zahlen multipliziert
# def berechne_produkt(zahl1, zahl2):
#     return zahl1 * zahl2

# # Rufe die Funktion auf und speichere das Ergebnis in einer Variablen
# ergebnis = berechne_produkt(4, 7)

# # Gib das Ergebnis aus
# print(f"Das Produkt ist: {ergebnis}")



# hauptprogramm.py

# Modul importieren
import meine_funktionen

# Begrüßung testen
begruessung = meine_funktionen.begruesse_user("Sofia")
print(begruessung)

# Division testen
ergebnis1 = meine_funktionen.dividiere(10, 2)
print(f"Ergebnis der Division: {ergebnis1}")

# Division durch Null testen
ergebnis2 = meine_funktionen.dividiere(10, 0)
print(f"Ergebnis der Division: {ergebnis2}")
