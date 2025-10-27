// COUNTER LOGIC
let count = 0;
const countLabel = document.getElementById("countLabel");
const decreaseBtn = document.getElementById("decreasebtn");
const resetBtn = document.getElementById("resetbtn");
const increaseBtn = document.getElementById("increasebtn");

decreaseBtn.onclick = () => {
  count--;
  countLabel.textContent = count;
};

resetBtn.onclick = () => {
  count = 0;
  countLabel.textContent = count;
};

increaseBtn.onclick = () => {
  count++;
  countLabel.textContent = count;
};

// CALCULATOR LOGIC
const display = document.getElementById("display");
const buttons = document.querySelectorAll(".calc-btn");

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const value = btn.textContent;

    if (value === "C") {
      display.value = "";
    } else if (value === "=") {
      try {
        display.value = eval(display.value) || "";
      } catch {
        display.value = "Error";
      }
    } else {
      display.value += value;
    }
  });
});
