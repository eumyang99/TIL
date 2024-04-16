// a번째의 최대값 = dp[a] = max(dp[a-2], dp[a-3]) + moeny[a]

function solution(money) {
  const dp_1 = [0, money[0], 0];
  const dp_2 = [0, 0, money[1]];

  for (let i = 2; i < money.length; i++) {
    dp_1.push(money[i] + Math.max(dp_1[i - 2], dp_1[i - 1]));
    dp_2.push(money[i] + Math.max(dp_2[i - 2], dp_2[i - 1]));
  }

  max_dp_1 = Math.max(dp_1.at(-2), dp_1.at(-3));
  max_dp_2 = Math.max(dp_2.at(-1), dp_2.at(-2));

  return Math.max(max_dp_1, max_dp_2);
}
