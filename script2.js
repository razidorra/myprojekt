let temperatur = prompt("Bitte gib die aktuelle Raumtemperatur in °C ein.");

if (temperatur < 16) {
  alert("Die Temperatur ist zu kalt.");
} else if (temperatur <= 22) {
  alert("Die Temperatur ist angenehm.");
} else {
  alert("Die Temperatur ist zu warm.");
}
