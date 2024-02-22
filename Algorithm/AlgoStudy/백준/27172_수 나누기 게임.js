// 에라토네스처럼 숫자들을 증가시키면서 증가된 숫자가 list에 있으면
// res[기준 숫자]++, res[증가된 숫자]--

function solution(n, list) {
  const res = Array(n).fill(0);
  const maxNum = Math.max(...list);
  const table = Array(maxNum + 1).fill(-1);
  for (let i = 0; i < n; i++) table[list[i]] = i;

  for (let num of list) {
    for (let addedNum = num * 2; addedNum <= maxNum; addedNum += num) {
      if (table[addedNum] === -1) continue;
      res[table[num]]++;
      res[table[addedNum]]--;
    }
  }

  console.log(...res);
}

let input = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    const n = Number(input[0]);
    const list = input[1].split(" ").map(Number);
    solution(n, list);
    process.exit();
  });
