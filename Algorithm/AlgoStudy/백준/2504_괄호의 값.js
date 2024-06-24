// 완전한 하나의 묶음을 찾아서 해당 묶음 내부의 작은 완전한 묶음으로 들어감
// 괄호의 depth 관리를 재귀의 depth로 해결

// 완전한 묶음 내부를 탐색
// 스택으로 내부의 작은 완전한 묶음을 찾으면
// 다시 재귀로 들어감

// 각 재귀는 하나의 완전한 묶음이기 때문에 단일 값을 가짐
// 해당 묶음의 값(partSum)은 하위 재귀가 반환하는 값을 누적
// 재귀의 값을 반환하기 전에 가장 바깥 괄호에 따라 2 or 3 곱해서 반환

// 1. basecase
// 1-1. "()" : 2, "[]" : 3, 다른 것이 나오면 불가능한 경우

// 2. 불가능한 경우
// 2-1. 스택이 비어있는데 닫는 괄호가 나오는 경후
// 2-2. 초기의 완전한 묶음을 탐색을 끝냈는데 stack이 남아 있는 경우

// 3. 입력값 조정
// 3-1. 초기 입력값이 완전한 묶음이 아닐 수 있기 때문에
//      임의로 "(", ")"로 감싸고 답안 제출 시 "2"로 나누어 제출함

// 불가능한 경우 0을 출력 후 종료
const fail = () => {
  console.log(0);
  process.exit();
};

// 괄호의 값
const multi = {
  "(": 2,
  "[": 3,
};

// 닫는 괄호의 짝
const counterBracket = {
  ")": "(",
  "]": "[",
};

function solution(line) {
  // 재귀함수 recur(완전한 묶음의 시작 idx, 끝 idx)
  const recur = (start, end) => {
    // basecase
    // "()" 이면 2, "[]"이면 3, 다른 경우면 불가능
    if (end - start === 1) {
      if (line[start] === "(" && line[end] === ")") return 2;
      if (line[start] === "[" && line[end] === "]") return 3;
      fail();
    }

    // 현재 묶음 내부의 누적값
    let partSum = 0;
    // 현재 묶음 내부의 작은 완전한 묶음의 시작 idx
    let partStart;
    const stack = [];

    // 현재 묶음의 내부 탐색
    for (let i = start + 1; i < end; i++) {
      const bracket = line[i];
      // 여는 괄호인 경우
      if (bracket === "(" || bracket === "[") {
        // 스택이 비어있다면 내부의 새로운 묶음 시작 idx로 설정
        if (stack.length === 0) partStart = i;
        // 스택 추가
        stack.push(bracket);
        continue;
      }

      // 닫는 괄호의 경우
      // 스택이 비어있다면 불가능한 경우
      if (stack.length === 0) fail();

      // 짝이 맞는 괄호라면 stack pop
      if (stack.at(-1) === counterBracket[bracket]) stack.pop();

      // 스택이 비어버리면 완전한 묶음이 완성되었다는 의미
      // partSum에 하위 묶음 값 누적
      if (stack.length === 0) partSum += recur(partStart, i);
    }

    // for문이 끝나도 stack이 남아있다면 불가능한 경우
    if (stack.length !== 0) fail();

    // 내부의 값 * 괄호의 값
    return partSum * multi[line[start]];
  };

  // input값에 임의로 "(", ")"를 추가한 것 조정
  return recur(0, line.length - 1) / 2;
}

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    console.log(solution("(" + line + ")"));
  })
  .on("close", () => {
    process.exit();
  });
