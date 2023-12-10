// 발상
// 나눠야할 전체 금액이 홀수이면 나눌 수 없음 : 최소 동전은 1원이기 때문
// 전체 금액이 짝수일 경우
// 한 사람이 받을 금액(target) : 전체 금액 / 2
// 길이 target+1의 memo_arr를 만들어 0으로 초기화
// 0이면 만들 수 없는 금액, 1이면 만들 수 있는 금액
// x원은 만들 수 있는 금액일 때, memo_arr의 (x원 + 현재 동전으로 만들 수 있는 금액)의 인덱스를 1로 할당
// 모든 동전을 순회하며 target idx가 1이 되었는지 확인

function solution(input) {
  n = input[0];
  let coins = input.slice(1);

  let total = coins.reduce((accu, cur_item) => {
    return accu + cur_item[0] * cur_item[1];
  }, 0);

  if (total % 2) return 0;

  let target = total / 2;
  let memo = Array(target + 1).fill(0);
  memo[0] = 1;

  for (let [coin, cnt] of coins) {
    for (let val = target; coin <= val; val--) {
      if (memo[val - coin]) {
        for (let i = 0; i < cnt; i++) {
          let new_val = val + coin * i;
          if (new_val <= target) memo[new_val] = 1;
          else break;
        }
      }
    }
    if (memo[target]) return 1;
  }

  return 0;
}

let input = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    let parsed_line = line.split(" ").map(Number);
    if (parsed_line.length === 1 && input.length !== 0) {
      console.log(solution(input));
      input = [];
    }
    input.push(parsed_line);
  })
  .on("close", () => {
    console.log(solution(input));
    process.exit();
  });
