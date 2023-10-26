const fs = require("fs");
// const arr = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const arr = fs.readFileSync("1008\\input.txt").toString().trim().split(" ");
console.log(arr[0] / arr[1]);
