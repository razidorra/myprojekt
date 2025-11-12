const trigger = document.querySelector("#trigger");
const name = document.querySelector("#name");

trigger.addEventListener("click", () => {
  const generatedname = generate();
  console.log(generatedname);
  name.innerText = generatedname;
});

function generate() {
  const names = ["Sama", "Eva", "Sam", "Ava", "Eli "];
  const randomIndex = Math.floor(Math.random() * names.length);
  return names[randomIndex];

  return names;
}
