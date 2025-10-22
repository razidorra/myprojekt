function toUpperClassic(text) {
  return text.toUpperCase();
}

const toUpperArrow = (text) => {
  return text.toUpperCase();
};

console.log(toUpperClassic("hallo"));
console.log(toUpperArrow("welt"));

const namen = ["Razieh", "Anna", "Sara"];

const grossNamen = namen.map((name) => name.toUpperCase());

console.log(grossNamen);

const person = {
  name: "Razieh",
  sagHallo: function () {
    console.log("Hallo, ich bin " + this.name);
  },
};

person.sagHallo();
