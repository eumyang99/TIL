function horizonCalc(multi) {
  if (multi === 1) return 5;
  return horizonCalc(multi / 2) * 2 + 1;
}

function solution(n) {
  const multi = n / 3;
  const horizon = horizonCalc(multi);
  const table = Array.from({ length: n }, () =>
    Array.from({ length: horizon }, () => " ")
  );

  let nextStartEnd = [-1, horizon + 1];
  let temp = [];
  for (let row = n - 1; 0 < row; row -= 3) {
    for (let i = 0; i < nextStartEnd.length; i += 2) {
      makeTree(nextStartEnd[i], nextStartEnd[i + 1], row);
    }
    nextStartEnd = temp;
    temp = [];
  }

  function makeTree(start_idx, end_idx, row) {
    let cnt = 1;
    for (let i = start_idx + 1; i <= end_idx - 1; i++) {
      // 6의 배수에서 점찍기 패스
      if (cnt % 6 === 0) {
        cnt = 1;
        continue;
      }

      // cnt가 짝수일 때 2개 점 찍기
      if (cnt % 2 === 0) table[row - 1][i] = "*";

      // cnt가 3일 때 1개 점찍기
      // 다음 5찍기 범위 저장
      if (cnt === 3) {
        table[row - 2][i] = "*";
        temp.push(i);
      }

      // 5찍기
      table[row][i] = "*";
      cnt++;
    }
  }

  table.forEach((row) => {
    console.log(row.join(""));
  });
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
    solution(input[0]);
    process.exit();
  });
