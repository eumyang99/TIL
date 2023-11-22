let [dx, dy] = [
  [0, 1],
  [1, 0],
];
function solution(m, n, puddles) {
  let memo = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
  for (let puddle of puddles) {
    memo[puddle[1]][puddle[0]] = -1;
  }
  memo[1][1] = 1;

  for (let x = 1; x <= n; x++) {
    for (let y = 1; y <= m; y++) {
      if (memo[x][y] === -1) continue;
      if (0 < memo[x - 1][y]) {
        memo[x][y] += memo[x - 1][y];
      }
      if (0 < memo[x][y - 1]) {
        memo[x][y] += memo[x][y - 1];
      }
      memo[x][y] %= 1000000007;
    }
  }
  return memo[n][m];
}
