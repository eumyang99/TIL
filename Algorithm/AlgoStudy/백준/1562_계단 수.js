// bottom-up DP & 비트마스킹
// 계단수만 체크하면 DP로 풀리지만
// 0 ~ 9까지 모든 숫자가 포함되어 있어야 하기 때문에 비트마스킹 사용

// 로직
// ex) 1100110101(2)
// 각 자리수가 1이면 해당 자리수는 사용함
// 0이면 해당 자리수는 사용하지 않음

// 만약 숫자가 254로 진행되었다면 그 다음 숫자는 3이나 5
// 비트마스킹을 사용하지 않으면
// 1234까지 진행된 상황과 구분할 수 없음
// 따라서 254의 경우 0000110100(2)
// 1234의 경우 0000011110(2)

// 254는 [2543, 0000111100(2)]와 [2545, 0000110100(2)]의 경우의 수의 합
// 이를 dp 점화식으로 표현하면
// dp[자리수][사용된 숫자][사용된 숫자들 마킹(2진수)]
// = dp[자리수+1][사용된 숫자-1][(사용된 숫자-1)을 마킹한 2진수]
// + dp[자리수+1][사용된 숫자+1][(사용된 숫자+1)을 마킹한 2진수]
// 따라서 dp[3][4][0000110100(2)] = dp[4][3][0000111100(2)] + dp[4][5][0000110100(2)]

// 베이스 케이스
// 자리수가 n과 같으면서 모든 숫자를 사용한 경우는 원하는 계단수이기 때문에 1을 리턴
// 그렇지 않은 경우 0을 리턴

function solution(n) {
  if (n < 10) return 0;

  let answer = 0;
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: 10 }, () => Array(1 << 10).fill(0))
  );

  function recur(dep, num, used) {
    if (dep === n) {
      if (used === (1 << 10) - 1) return 1;
      else return 0;
    }

    if (dp[dep][num][used]) return dp[dep][num][used];

    const [low, high] = [num - 1, num + 1];
    if (0 <= low)
      dp[dep][num][used] += recur(dep + 1, low, used | (1 << (num - 1)));
    if (high <= 9)
      dp[dep][num][used] += recur(dep + 1, high, used | (1 << (num + 1)));

    dp[dep][num][used] %= 1000000000;
    return dp[dep][num][used];
  }

  for (let num = 1; num < 10; num++) {
    answer += recur(1, num, 1 << num);
  }

  return (answer %= 1000000000);
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
    console.log(solution(n));
    process.exit();
  });
