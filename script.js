let alter = parseInt(prompt("Bitte gib dein Alter ein:"));
let mitgliedschaftEingabe = prompt(
  "Hast du eine aktive Jahresmitgliedschaft? (ja/nein)"
);
let mitgliedschaft = mitgliedschaftEingabe === "ja";

if (alter >= 18 && mitgliedschaft) {
  alert("Scön das du da bist");
} else {
  alert("Du darfst nicht rein!");
}

if (alter >= 18 && !mitgliedschaft) {
  alert("Grund: Du bist unter 18 und hast keine aktive Mitgliedschaft.");
} else if (alter < 18) {
  alert("Grund: Du bist unter 18 Jahre alte.");
} else if (!mitgliedschaft) {
  alert("Grund: Du hast keine aktive mitgliedschaft.");
}
