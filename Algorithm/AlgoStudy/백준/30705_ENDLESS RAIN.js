// 발상
// union-find(분리 집합) 사용

// 주어지는 배열에서 각 날짜마다
// 그날 설치할 수 있는 파라솔의 의미로 remain(여분)에 1씩 추가하고
// 그날 필요한 파라솔의 개수(need)는 0으로 초기화
// 이후 아래의 과정을 while문으로 반복
// left_parent(왼쪽 빌딩의 조상)을 right_parent(오른쪽 빌딩의 조상)과 연결
// 연결할 때마다 해당 날짜에서 미리 필요한 파라솔의 개수를 1씩 추가
// 이후 left_parent의 바로 다음 빌딩(left_parent + 1)의 조상 빌딩을 left_parent로 갱신
// left_parent < right_parent 조건에서 반복

// 만약 그날 필요한 파라솔의 개수가 없다면 remain은 1씩 커짐
// 1) 여분(remain)이 필요한 파라솔(need) 보다 많으면
//    여분에서 필요한 파라솔을 차감
//        remain -= need
// 2) 여분(remain)이 필요한 파라솔(need) 보다 작거나 같으면
//    필요한 파라솔에서 여분을 차감한 값을 res에 추가
//        res += (need - remain)
//    여분은 모두 사용했으므로 0으로 초기화
//        remain = 0

function solution(n, m, arr) {
  let res = 0;
  let parent = Array.from({ length: n + 1 }, (_, i) => i);

  function find(s, e) {
    if (s !== parent[s]) {
      parent[s] = find(parent[s]);
      return parent[s];
    }
    return s;
  }

  let remain = 0;
  for (let [left, right] of arr) {
    remain++;
    let need = 0;
    let left_parent = find(left);
    let right_parent = find(right);

    while (left_parent < right_parent) {
      parent[left_parent] = right_parent;
      need++;
      left_parent = find(left_parent + 1);
    }

    if (remain <= need) {
      res += need - remain;
      remain = 0;
    } else {
      remain -= need;
    }
  }

  return res;
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
    let [n, m] = input[0].split(" ").map(Number);
    let arr = input.slice(1).map((el) => el.split(" ").map(Number));
    console.log(solution(n, m, arr));
    process.exit();
  });
