function reverse(str) {
  return [...str].reverse().join("");
}

// 인덱스로만 접근해서 푸는 방식
function solution(input) {
  let s = input[0];
  let t = input[1];
  let s_len = s.length;
  let t_len = t.length;

  let stack = [[0, t_len - 1, t_len, false]];
  while (stack.length !== 0) {
    let [left, right, len, is_reverse] = stack.pop();
    if (len === s_len) {
      let res = is_reverse
        ? reverse(t.slice(right, left + 1))
        : t.slice(left, right + 1);
      if (res === s) {
        return 1;
      } else {
        continue;
      }
    }

    if (t[right] === "A") {
      let new_left = left;
      let new_right = is_reverse ? right + 1 : right - 1;
      stack.push([new_left, new_right, len - 1, is_reverse]);
    }
    if (t[left] === "B") {
      let new_left = right;
      let new_right = is_reverse ? left - 1 : left + 1;
      stack.push([new_left, new_right, len - 1, !is_reverse]);
    }
  }
  return 0;
}

// 문자열을 매번 편집해서 푸는 방식
function solution(input) {
  let s = input[0];
  let t = input[1];
  let s_len = s.length;
  let t_len = t.length;

  let stack = [[t, t_len]];
  while (stack.length !== 0) {
    let [str, len] = stack.pop();
    if (len === s_len) {
      if (str === s) {
        return 1;
      } else {
        continue;
      }
    }

    if (str[len - 1] === "A") {
      stack.push([str.slice(0, len - 1), len - 1]);
    }
    if (str[0] === "B") {
      stack.push([reverse(str).slice(0, len - 1), len - 1]);
    }
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
    input.push(line);
  })
  .on("close", () => {
    console.log(solution(input));
    process.exit();
  });
