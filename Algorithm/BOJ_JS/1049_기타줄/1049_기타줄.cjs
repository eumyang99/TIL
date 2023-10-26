const fs = require("fs");
const input = fs
  .readFileSync("1049_기타줄\\input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((el) => {
    const [a, b] = el.split(" ").map((el) => parseInt(el));
    return [a, b];
  });

const [n, m] = input[0];
const arr = input.slice(1);

let minPack = arr[0][0];
let minEach = arr[0][1];

for (i = 1; i < m; i++) {
  if (arr[i][0] < minPack) {
    minPack = arr[i][0];
  }
  if (arr[i][1] < minEach) {
    minEach = arr[i][1];
  }
}

const res = (minPack, minEach) => {
  // 낱개가 더 쌀 때
  if (minEach * 6 <= minPack) {
    return console.log(minEach * n);
  }

  // 패키지가 더 싸지만 n이 6보다 작을 때
  if (n <= 6) {
    if (minEach * n <= minPack) {
      return console.log(minEach * n);
    } else {
      return console.log(minPack);
    }
  }

  // 패키지가 더 싸지만 n이 6보다 클 때
  const packCost = Math.floor(n / 6) * minPack;
  const eachCost = (n % 6) * minEach;
  if (packCost + minPack < packCost + eachCost) {
    return console.log(packCost + minPack);
  } else {
    return console.log(packCost + eachCost);
  }
};

res(minPack, minEach);
