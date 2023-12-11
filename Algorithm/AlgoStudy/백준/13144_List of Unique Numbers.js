// 발상 : set과 투포인터
// 1.
// left_idx(연속된 수열의 가장 왼쪽)를 기준으로 right_idx의 값이 set에 없다면 추가해 나감
// 2.
// right_idx 값이 set에 있다면 현재 set의 길이를 res에 추가
// 이후 left_idx의 값을 set에서 제거하고
// left_idx를 1 증가
// ex) set = {1, 2, 3, 4} 일 때,
// {1} / {1, 2} / {1, 2, 3} / {1, 2, 3, 4} left_idx를 기준으로 4개의 경우가 가능하기 때문
// left_idx의 값이 1인 경우의 모든 값을 구했으니
// 다음 left_idx의 값이 2인 경우의 값을 구하기 위해 left_idx++

// left_idx가 마지막 인덱스까지 탐색하되
// right_idx가 마지막 인덱스를 넘어서면 더 이상 중복될 가능성이 없기 때문에 break
// break된 경우 set에 담겨 있는 길이만큼 (시그마 k 공식)으로 따로 계산해서 res에 추가하면 됨
// ex) set = {1, 2, 3}일 때,
// left_idx가 1인 경우 3개
// 2인 경우 2개
// 3인 경우 1개

function solution(input) {
  let n = input[0][0];
  let arr = input[1];
  let res = 0;
  let set = new Set();
  let set_length = 0;
  let [left_idx, right_idx] = [0, 0];
  while (left_idx < n) {
    if (right_idx === n) break;
    if (!set.has(arr[right_idx])) {
      set.add(arr[right_idx]);
      set_length++;
      right_idx++;
      continue;
    }
    res += set_length;
    set.delete(arr[left_idx]);
    set_length--;
    left_idx++;
  }
  res += (set_length * (set_length + 1)) / 2;

  return res;
}

let input = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    let new_line = line.split(" ").map(Number);
    input.push(new_line);
  })
  .on("close", () => {
    console.log(solution(input));
    process.exit();
  });
