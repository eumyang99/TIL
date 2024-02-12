// 풀이 참조
// 문자열의 가운데서부터 양쪽으로 확장하며 팰린드롬 확인
// for문 하나로 확인 가능해서 시간 소요가 대폭 줄어듬
// 단, 팰린드롬 문자열의 길이가 짝수일 수 있기 때문에
// for문의 인덱스 조절이 필요했음

function solution(input) {
  input = "0" + input;
  const len = input.length;
  const memo = Array.from({ length: len }, (_, idx) => idx);

  // mid가 정수일 때, 홀수개의 문자열 확인
  // ex) mid = 5일 때, [left, right] = [5, 5] [4, 6] [3, 7]...
  // mid가 유리수일 때, 짝수개의 문자열 확인
  // ex) mid = 5.5일 때, [left, right] = [5, 6] [4, 7] [3, 8]...
  for (let mid = 1; mid < len; mid += 0.5) {
    let [left, right] = [mid, mid];
    if (mid % 1) [left, right] = [mid - 0.5, mid + 0.5];

    while (0 < left && right < len && input[left] === input[right]) {
      if (memo[left - 1] + 1 < memo[right]) memo[right] = memo[left - 1] + 1;
      left--;
      right++;
    }
  }

  return memo.at(-1);
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
    console.log(solution(input[0]));
    process.exit();
  });

// 나의 풀이
// 팰린드롬을 양쪽 끝부터 확인하는 방법
// 양쪽 끝의 인덱스를 파악하기 위해 이중 for문 사용
// 시간이 굉장히 오래 걸림

// function solution(input) {
//   input = [0].concat(input);
//   const len = input.length;
//   const memo = Array.from({ length: len }, (_, idx) => idx);
//   const palindromeCheck = Array(len * 2).fill(false);
//   const alphaMap = {};
//   for (let i = len - 1; 1 <= i; i--) {
//     if (alphaMap[input[i]]) alphaMap[input[i]].push(i);
//     else alphaMap[input[i]] = [i];
//   }

//   function isPalindrome(left, right) {
//     if (palindromeCheck[left + right]) return true;
//     if (left === right) return true;
//     while (left < right) {
//       if (input[left] != input[right]) return false;
//       left++;
//       right--;
//     }
//     palindromeCheck[left + right] = true;
//     return true;
//   }

//   for (let start = 1; start < len; start++) {
//     const startAlpha = input[start];
//     for (let i of alphaMap[startAlpha]) {
//       if (i < start) break;
//       if (input[start] === input[i]) {
//         if (isPalindrome(start, i)) {
//           if (memo[start - 1] < memo[i]) memo[i] = memo[start - 1] + 1;
//         }
//       }
//     }
//   }
//   return memo.at(-1);
// }

// let input = [];
// const readline = require("readline").createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });
// readline
//   .on("line", (line) => {
//     input.push(line.split(""));
//   })
//   .on("close", () => {
//     console.log(solution(input[0]));
//     process.exit();
//   });
