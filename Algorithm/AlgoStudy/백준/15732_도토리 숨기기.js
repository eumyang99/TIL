function solution(input) {
  let [n, k, d] = input[0].split(" ").map((el) => parseInt(el));
  let arr = [];
  for (let i = 1; i <= k; i++) {
    arr.push(input[i].split(" ").map((el) => parseInt(el)));
  }

  let [left, right] = [0, n];
  while (left < right) {
    let mid = Math.floor((right + left) / 2);
    let corn_cnt = 0;
    for (let i = 0; i < k; i++) {
      let [start, last, gap] = arr[i];
      if (mid < start) continue;
      let end = Math.min(mid, last);
      corn_cnt += Math.floor((end - start) / gap) + 1;
    }

    if (corn_cnt < d) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
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
    console.log(solution(input));
    process.exit();
  });
