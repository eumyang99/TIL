// 발상
// 5원을 만들기 위해 2원짜리를 사용한다는 것은
// 5원을 만드는 경우의 수에 3원을 만들 수 있는 경우의 수를 더하는 것과 같음
// 3원을 만드는 경우의 수들에 +2원을 하면 5원을 만드는 경우의 수이기 때문

function solution(n, money) {
  const dp = Array(n + 1).fill(0);
  for (let m of money) {
    dp[m] += 1;
    for (let size = m + 1; size <= n; size++) {
      dp[size] += dp[size - m];
      dp[size] %= 1000000007;
    }
  }
  return dp.at(-1) % 1000000007;
}
