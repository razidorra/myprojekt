let eingabe;
while (true) {
  eingabe = prompt("Bitte gib eine positive Zahl ein:");
  if (eingabe > 0) break;
  alert(" Ungültige Eingabe. Die Zahl muss größer als 0 sein.");
}
alert(`Du hast die Zahl ${eingabe} eingegeben.`);
