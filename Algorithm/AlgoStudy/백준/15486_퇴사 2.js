// 내 방법 : bottom up
function solution(n, consults) {
  const dp = Array(n + 1).fill(0);
  let maxi = 0;
  for (let i = 0; i < n; i++) {
    const [t, p] = consults[i];
    const endDay = i + t;
    maxi = Math.max(maxi, dp[i]);
    if (n < endDay) continue;
    dp[endDay] = Math.max(dp[endDay], maxi + p);
  }
  return Math.max(maxi, dp.at(-1));
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
    const n = parseInt(input[0]);
    const consults = input.slice(1).map((el) => el.split(" ").map(Number));
    console.log(solution(n, consults));
    process.exit();
  });
