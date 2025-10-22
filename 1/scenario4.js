const zufallszahl = Math.floor(Math.random() * 10) + 1;
let versuch;
do {
  versuch = parseInt(prompt("🎲 Rate eine Zahl zwischen 1 und 10:"));
  if (versuch < zufallszahl) {
    alert("🔻 Zu niedrig!");
  } else if (versuch > zufallszahl) {
    alert("🔺 Zu hoch!");
  }
} while (versuch !== zufallszahl);

alert(`🎉 Richtig! Die gesuchte Zahl war ${zufallszahl}.`);
