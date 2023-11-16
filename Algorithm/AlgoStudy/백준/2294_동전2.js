// 발상
// 길이 k개의 dp array를 만들고 infinity로 초기화
// 0부터 k까지 dp값을 할당해 나감

// 만약 dp의 해당 idx값과 같은 동전이 있다면 해당 idx에는 1을 할당
// 그렇지 않다면 해당 idx를 만들 수 있는 이전 값들을 조회하며 최소값으로 할당
// ex) target이 5일 경우
// dp[0] + dp[5], dp[1] + dp[4], dp[2] + dp[3] 중 작은 값으로 할당

// dp의 할당이 완료되면
// dp[k]가 여전히 infinity라면 만들 수 없는 값, -1 출력
// 그렇지 않다면 dp[k] 출력

function solution(input) {
  let [n, k] = input[0].split(" ").map((el) => parseInt(el));
  let arr = input.slice(1).map((el) => parseInt(el));

  let dp = Array(k + 1).fill(Infinity);

  for (let target = 0; target < k + 1; target++) {
    if (arr.includes(target)) {
      dp[target] = 1;
      continue;
    }

    for (let coin = 0; coin * 2 <= target; coin++) {
      if (dp[coin] + dp[target - coin] < dp[target]) {
        dp[target] = dp[coin] + dp[target - coin];
      }
    }
  }

  if (dp[k] === Infinity) {
    return -1;
  }

  return dp[k];
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
