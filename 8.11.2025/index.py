
alter = 16
if alter >= 19:
   print ("Du bist volljährig")
else:
   print("Was machst du hier?")


   for zahl in [1, 2, 3, 4, 5]:
       print(zahl)

       
for i in range(8):
          print (i)
          if i == 3:
             break
          


for i in range(10):
    if i == 5:
        continue
    print(i)


temperatur = int(input("Wie viel Grad hat es draußen?"))

if temperatur > 30:
  print("Es ist heiß draußen")
elif temperatur >= 18:
    print("Es ist angenehm")
else:
    print("Es ist kalt draußen")


alter = int(input("Wie alt bist du?"))

if alter < 14:
   print ("Du bist ein Kind")
elif alter < 18:
    print("Du bist ein Teenager")
else:
    print("Du bist ein Erwachsener")

for zahl in range (1, 11):
 print(zahl)

 fruechte = ["Apfel", "Banane", "Kirsche", "Orange"]

for frucht in fruechte:
    print(frucht)

for zahl in range(5, 16, 2):
    print(zahl)


eingabe = 0
while eingabe != 7:
    eingabe = int(input("Gib eine Zahl ein: "))
    print(f"Du hast {eingabe} eingegeben.")


zahlen = [5, 12, -3, 18, 0, 25, 100, 7]

for zahl in zahlen:
    if zahl <= 0:
        continue        
    if zahl == 100:
        break           
    if zahl > 10:
        print(zahl)
