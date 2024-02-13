// 발상
// 주어지는 신호의 idx에서 밟고 있는 버튼 조합의 값을 메모하여 재사용함으로써
// 불필요한 재귀를 방지

function cost(here, next) {
  // 제자리
  if (here === next) return 1;
  // 0에서 출발
  if (here === 0) return 2;
  // 옆
  if ((here + next) % 2) return 3;
  // 맞은 편
  return 4;
}

function solution(input) {
  const len = input.length;
  // 3차원 배열, [idx][왼발][오른발]
  const memo = Array.from({ length: len }, () =>
    Array.from({ length: 5 }, () => Array(5).fill(0))
  );

  function recur(left, right, idx) {
    // 이번에 밟아야 할 숫자
    const num = input[idx];
    // base case
    if (num === 0) return 0;
    // 이번 idx에 left, right 발 조합이 메모되어 있으면 사용
    if (memo[idx][left][right]) return memo[idx][left][right];

    // 양발을 같이 둬야 하면 infinity 할당하면서 재귀 경로 삭제
    // 현재 서 있는 각 발에 대해 [발을 움직이는 비용 + 그 발을 움직였을 때 발생할 미래의 총 비용]을 계산
    const accu1 =
      left === num ? Infinity : recur(left, num, idx + 1) + cost(right, num);
    const accu2 =
      right === num ? Infinity : recur(right, num, idx + 1) + cost(left, num);

    // 비용이 작은 쪽을 선택해서 메모
    memo[idx][left][right] = accu1 < accu2 ? accu1 : accu2;
    // 사실상 [왼발 : 1, 오른발 : 2] === [왼발 : 2, 오른발 : 1] 상황은 같은 상황
    memo[idx][right][left] = memo[idx][left][right];
    return memo[idx][left][right];
  }
  return recur(0, 0, 0);
}

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    console.log(solution(line.split(" ").map(Number)));
  })
  .on("close", () => {
    process.exit();
  });
