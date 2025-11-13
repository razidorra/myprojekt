
try:
    zahl = int(input("Bitte gib eine Zahl ein: "))
    print(f"Die Zahl ist: {zahl}")
except ValueError:
    print("Fehler: Das ist keine gültige Zahl! Bitte versuche es erneut.")

    # Beispiel: Division zweier Zahlen

try:
    a = float(input("Zähler: "))
    b = float(input("Nenner: "))
    ergebnis = a / b
    print(f"Ergebnis: {ergebnis}")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt!")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


# Beispiel mit else und finally

try:
    x = int(input("Zahl: "))
    y = int(input("Teiler: "))
    ergebnis = x / y
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
else:
    # Wird nur ausgeführt, wenn kein Fehler auftritt
    print(f"Ergebnis: {ergebnis}")
finally:
    # Wird IMMER ausgeführt
    print("Programmende – danke fürs Benutzen!")



dateiname = "nicht_existierende_datei.txt"

try:
    with open(dateiname, "r") as datei:
        print(datei.read())
except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden!")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
else:
    print("Datei wurde erfolgreich gelesen.")
finally:
    print("Dateizugriff beendet.")


def parse_numbers(data_string):
    
    try:
        
        teile = data_string.split(",")
        
       
        zahlen = [float(teil.strip()) for teil in teile]
        
        return zahlen
    
    except ValueError:
        print("Fehler: Die Eingabe enthält keine gültigen Zahlen!")
        return []

# --- Testbeispiele ---
print(parse_numbers("10, 20, 30"))     
print(parse_numbers("5, -3.5, 7.2"))    
print(parse_numbers("a, 2, 3"))  