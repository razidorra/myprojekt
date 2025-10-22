const ticketPreis = 2.5;
let alter = prompt("Bitte gib dein Alter ein.");
let student =
  prompt("Hast du einen gültigen Studentausweis? (ja/nein)").toLowerCase() ===
  "ja";

let preis = ticketPreis;

if (alter < 6) {
  preis = 0;
} else if (student && ater < 27) {
  preis = ticketPreis * 0.5;
} else if (alter > 65) {
  preis = ticketPreis * 0.75;
}
alert(`Dein Fahrpreis beträgt: €${preis.toFixed(2)}`);
