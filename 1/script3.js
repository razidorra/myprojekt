let wochentag = prompt(
  "Gib eine zahl für den wochentag ein(1 =Montag,..., 7 =Sonntag"
);
switch (wochentag) {
  case 1:
    alert("Montag: Coding Session");
    break;
  case 2:
    alert("DienstagSport");
    break;
  case 3:
    alert("MittwochLesen");
    break;
  case 4:
    alert("Donnerstag: Kreatives Arbeiten");
    break;
  case 5:
    alert("Freitag: Filmabend");
    break;
  case 6:
    alert("Samstag: Zocken & Entspannen");
    break;
  case 7:
    alert("Sonntag: Freizeit genießen");
    break;
  default:
    alert("Ungültige Eingabe! Bitte gib eine Zahl zwischen 1 und 7 ein.");
}
