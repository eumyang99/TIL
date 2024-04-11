// DP bottom-up
// DP bottom-up을 구현할 때, 현재 데이터를 통해 미리 이후 데이터를 구성하는 방법도 있지만(a + b = c)
// 현재 데이터를 이전 데이터를 참조하여 구성하는 방법도 고려해야 함(c = a + b)

function solution(n, m, board) {
  let answer = 0;
  const dp = [Array(m + 1).fill(0), ...board.map((el) => [0, ...el])];
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (!dp[i][j]) continue;
      dp[i][j] += Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
      if (answer < dp[i][j]) answer = dp[i][j];
    }
  }
  return answer ** 2;
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
    const [n, m] = input[0].split(" ").map(Number);
    const board = input.slice(1).map((el) => el.split("").map(Number));
    console.log(solution(n, m, board));
    process.exit();
  });
