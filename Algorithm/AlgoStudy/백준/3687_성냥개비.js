// 발상
// 최대값 : 그리디
// 최소값 : DP

// 최대값 : 자리수를 최대로 높이는 방법
// 최대값은 스스로 찾았다.
// target이 홀수 or 짝수인지 확인하고
// 짝수일 경우 1(성냥개비 2개)로 채우고
// 홀수일 경우 7(성냥개비 3개) 하나와 나머지 1(성냥개비 2개)로 채운다

// 최소값 : 최소한 숫자 한 자리만 늘리도록 함
// 성냥개비가 8개 이상 늘면 자리수가 2자리 추가된다.
// 따라서 성냥개비 7개를 기준으로 이전 dp값을 활용하여 숫자를 추가한다
// ex) 성냥개비 17개
// (15 + 2), (14 + 3), (13 + 4), (12 + 5), (11 + 6), (10 + 7)
// 15개로 만들 수 있는 최소값에 2개로 만들 수 있는 최소값을 마지막 자리로 추가하고 dp[17]과 비교하여 작은 값으로 갱신한다.
// 14개로 만들 수 있는 최소값에 3개로 만들 수 있는 최소값을 마지막 자리로 추가하고 dp[17]과 비교하여 작은 값으로 갱신한다.
// ...

const cost = [0, 0, 1, 7, 4, 2, 0, 8, 10];

function solution(input) {
  const n = parseInt(input[0]);
  const arr = input.slice(1).map((el) => parseInt(el));

  for (let idx = 0; idx < n; idx++) {
    let target = arr[idx];

    // 최소값
    let dp = [0, 0, 1, 7, 4, 2, 6, 8, 10];
    dp[6] = 6;

    for (let i = 9; i <= target; i++) {
      dp.push(Infinity);
      for (let j = 2; j < 8; j++) {
        dp[i] = Math.min(dp[i], dp[i - j] * 10 + cost[j]);
      }
    }

    // 최대값
    let max_res = [];
    let quotient = Math.floor(target / 2);
    let remainder = target % 2;
    if (remainder) {
      max_res.push("7");
      max_res.push(...Array(quotient - 1).fill("1"));
    } else {
      max_res.push(...Array(quotient).fill("1"));
    }

    console.log(dp[target], max_res.join(""));
  }
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
    solution(input);
    process.exit();
  });
