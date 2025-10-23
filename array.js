// const color = ["weiss", "schwarz", "blau", "rot", "gelb"];
// color[0];
// console.log(color[0]);
// color.forEach((color) => {
//   console.log("ich mag " + color);
// });

// const color = ["weiss", "schwarz", "blau", "rot", "gelb"];

// const uppercolor = color.map((color) => color.toUpperCase());
// console.log(uppercolor);

let user = {
  username: "razieh",
  age: 25,
  city: "Hamburg",
};

let user1 = {
  username: "sam",
  age: 22,
  city: "berlin",
};
let user2 = {
  username: "khaliq",
  age: 33,
  city: "essen",
};
// Add a new property (occupation) to each user
user.occupation = "Web Developer";
user1.occupation = "Designer";
user2.occupation = "Engineer";

delete user.city;
// // console.log(user);
// console.log("age:", user.age);
// console.log("city:", user.city);
// Put all users in one array
const users = [user, user1, user2];

// Loop through each user and print their data
users.forEach((person, index) => {
  console.log(`User ${index + 1}:`);
  for (let key in person) {
    // console.log(`${key}: ${person[key]}`);
    console.log(key + ": " + person[key]); // alternative way
  }
  console.log("-------------"); // separator line
});

// Test-Kommentar zum Ändern der Datei
