// JS에서 다루는 숫자 범위를 초과한 문제
// Number는 절대값 9007199254740991(Number.MAX_SAFE_INTEGER) 까지만 다룬다
// 대략 2^53 - 1(10 ** 16) 정도
// 이를 초과하는 경우 Bigint로 다루어야 한다

// BigInt는 정수 리터럴의 뒤에 n을 붙이거나(10n) 함수 BigInt()를 호출해 사용
// 단,
// BigInt는 Math 메서드 사용 불가
// 연산의 결과는 언제나 정수값
// Number와 혼합해서 사용 불가
// 따라서 같은 BigInt 데이터 타입으로 변경해서 연산해야 한다

// 그러나,
// Number와 비교 연산은 가능
// 배열에서 Number와 정렬 가능

// BigInt의 경우 값 뒤에 "n"이 붙는다
// ex) 9007199254740992n
// 이를 제거하기 위해 문자열로 변환해서 표현해야 한다

function accu(num) {
  let accu = 0n;
  const bin = num.toString(2);
  const len = BigInt(bin.length);
  for (let i = 0; i < len; i++) {
    const pow = BigInt(len - BigInt(i));
    const div = 2n ** pow;
    const [share, remain] = [(num + 1n) / div, (num + 1n) % div];
    const [shareVal, remainVal] = [share * (div / 2n), remain - div / 2n];
    accu += shareVal + (0n <= remainVal ? remainVal : 0n);
  }
  return accu;
}

function solution(a, b) {
  return String(accu(b) - accu(a - 1n));
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
    const [a, b] = input[0].split(" ").map(BigInt);
    console.log(solution(a, b));
    process.exit();
  });

// Number 범위에서의 풀이
function accu(num) {
  let accu = 0;
  const bin = num.toString(2);
  const len = bin.length;
  for (let i = 0; i < len; i++) {
    const pow = len - i;
    const div = 2 ** pow;
    const [share, remain] = [Math.floor((num + 1) / div), (num + 1) % div];
    const [shareVal, remainVal] = [share * (div / 2), remain - div / 2];
    accu += shareVal + (0 <= remainVal ? remainVal : 0);
  }
  console.log(accu);
  return accu;
}

function solution(a, b) {
  return accu(b) - accu(a - 1);
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
    const [a, b] = input[0].split(" ").map(Number);
    console.log(solution(a, b));
    process.exit();
  });
