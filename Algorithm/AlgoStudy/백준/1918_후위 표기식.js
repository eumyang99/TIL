const plus_set = new Set(["+", "-"]);
const multi_set = new Set(["*", "/"]);
const bracket_set = new Set(["(", ")"]);

// 문자 종류 분류
function which_char_case(char) {
  if (plus_set.has(char)) return "plus";
  if (multi_set.has(char)) return "multi";
  if (bracket_set.has(char)) return "bracket";
  return "alpha";
}

// "+" or "-" 인 경우
// "("가 나오기 전까지 스택에서 pop하고 res에 추가
// 이후 현재 기호 stack에 추가
function plus_case(char) {
  while (stack.length !== 0) {
    if (which_char_case(stack[stack.length - 1]) === "bracket") break;
    res.push(stack.pop());
  }
  stack.push(char);
}

// "*" or "/" 인 경우
// 스택 마지막에 "*" or "/" 가 있으면 스택에서 pop하고 res에 추가
// "*" or "/"가 아닌게 나오면 break
function multi_case(char) {
  while (stack.length !== 0) {
    if (which_char_case(stack[stack.length - 1]) === "multi") {
      res.push(stack.pop());
      continue;
    }
    break;
  }
  stack.push(char);
}

// "(" or ")" 인 경우
// 1.
// "(" 라면 stack에 추가
// 2.
// ")" 라면 "("가 나올 때까지 스택에서 pop하고 res에 추가, 마지막에 "(" 도 pop하고 break
function bracket_case(char) {
  if (char === "(") {
    stack.push(char);
    return;
  }
  while (stack.length !== 0) {
    if (which_char_case(stack[stack.length - 1]) === "bracket") {
      stack.pop();
      break;
    }
    res.push(stack.pop());
  }
}

let res = [];
let stack = [];

function solution(input) {
  // 문자를 순회하며 주어진 케이스에 따라 처리
  for (let char of input) {
    let char_case = which_char_case(char);
    switch (char_case) {
      case "plus":
        plus_case(char);
        break;

      case "multi":
        multi_case(char);
        break;

      case "bracket":
        bracket_case(char);
        break;

      case "alpha":
        res.push(char);
    }
  }

  // 모든 문자를 처리하고
  // "("를 제외한 스택에 남은 기호를 거꾸로 res에 추가
  for (let i = stack.length - 1; 0 <= i; i--) {
    if (which_char_case(stack[i]) === "bracket") continue;
    res.push(stack[i]);
  }

  return res.join("");
}

let input;
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    input = line.split("");
  })
  .on("close", () => {
    console.log(solution(input));
    process.exit();
  });
