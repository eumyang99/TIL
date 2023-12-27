// 각 요소를 사용하는 것과 사용하지 않는 것을 다룰 때,
// 또한 그 조합의 크기가 매우 클 때,
// 배낭 문제 개념을 사용하면 좋겠다

// 발상 : 배낭 문제
// 현재 위치를 기준으로 왼쪽 방향, 오른쪽 방향으로 가는 것을 나누어 판단
// 각 방향에 대해
// 만들 수 있는 인원수(index)에 가장 작은 소요 시간(value)을 기록하는 array를 생성

// 만들어야 하는 인원수 = 왼쪽 방향에서 만든 수 + 오른쪽 방향에서 만든 수
// 따라서 각 방향에서의 소요시간을 계산하여 제한 시간보다 작으면 가능

function solution(n, m, t, arr, p) {
  // 처음 속한 그룹의 크기
  let start_group_size = arr[p - 1];
  // 처음 속한 그룹은 무조건 사용하기 때문에
  // 만들어야 하는 인원 - 처음 속한 그룹 크기 = 왼쪽 인원 + 오른쪽 인원 = 타겟 사이즈
  let target_size = m - start_group_size;

  // 만약 애초에 만들 수 없다면 종료
  if (target_size < 0) return "NO";

  // 왼쪽, 오른쪽 memo array 초기화
  let left_memo = Array(target_size + 1).fill(Infinity);
  let right_memo = Array(target_size + 1).fill(Infinity);
  left_memo[0] = 0;
  right_memo[0] = 0;

  // 오른쪽 방향 탐색
  for (
    // 초기 그룹 인덱스 = 처음 속한 그룹의 오른쪽 그룹 인덱스
    // 초기 시간 = 1초
    let group_idx = p, sec = 1;
    // 그룹 인덱스가 n보다 작으면서
    // 시간이 제한 시간보다 작을 때까지만 탐색
    group_idx < n && sec <= t;
    // 오른쪽 방향이기 때문에 그룹 인덱스 증가, 시간 증가
    group_idx++, sec++
  ) {
    // 현재 탐색하는 그룹의 사이즈
    let group_size = arr[group_idx];
    // right_memo의 마지막 인덱스부터 0번째 인덱스까지 순회하며
    for (let size = target_size; 0 <= size; size--) {
      // 값이 Infinity(아직 만들 수 없는 인원수)라면 continue
      if (right_memo[size] === Infinity) continue;

      // 이전에 만들 수 있는 사이즈라면
      // 현재 그룹의 사이즈를 더했을 때
      let sum_size = size + group_size;
      // 그 값이 타겟 사이즈 보다 크면 continue
      if (target_size < sum_size) continue;

      // 그렇지 않다면
      // 해당 사이즈를 만들기 위한 소요 시간을 최소값으로 갱신
      if (sec < right_memo[sum_size]) {
        right_memo[sum_size] = sec;
      }
    }
  }

  // 왼쪽 방향 탐색
  // 로직은 위와 동일
  for (
    let group_idx = p - 2, sec = 1;
    0 <= group_idx && sec <= t;
    group_idx--, sec++
  ) {
    let group_size = arr[group_idx];
    for (let size = target_size; 0 <= size; size--) {
      if (left_memo[size] === Infinity) continue;
      let sum_size = size + group_size;
      if (target_size < sum_size) continue;
      if (sec < left_memo[sum_size]) {
        left_memo[sum_size] = sec;
      }
    }
  }

  // 위에서 만든 right_memo와 left_memo를 활용하여 가불가 여부 확인
  // 왼쪽에서 만든 인원수를 0부터 타겟 사이즈까지 증가
  // 오른쪽에서 만든 인원수는 타겟 사이즈부터 0까지 감소
  for (let left_val = 0; left_val <= target_size; left_val++) {
    let right_val = target_size - left_val;

    // 만약 둘 중에 하나라도 만들 수 없다면 해당 좌우 조합은 continue
    if (left_memo[left_val] === Infinity || right_memo[right_val] === Infinity)
      continue;

    // 양쪽 다 만들 수 있다면 각각의 소요 시간을 확인
    let [left_sec, right_sec] = [left_memo[left_val], right_memo[right_val]];
    // 최소한의 시간으로 해당 인원수를 맞추도록 해야 하기 때문에
    // 소요 시간이 짧은(시작 그룹으로부터 가까운) 방향으로 먼저 갔다가 반대 방향으로 가야 함
    // 따라서 (짧은 방향의 소요 시간 * 2) + (긴 방향의 소요 시간)으로 계산
    // 이 값이 제한 시간보다 작다면 제한 시간 내에 원하는 인원수를 만들 수 있음
    if (left_sec < right_sec) {
      if (left_sec * 2 + right_sec <= t) {
        return "YES";
      }
    } else {
      if (left_sec + right_sec * 2 <= t) {
        return "YES";
      }
    }
  }

  // 위 for문에서 return 되지 않았다면 원하는 인원수를 만들지 못했다는 것
  return "NO";
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
    let [n, m, t] = input[0].split(" ").map(Number);
    let arr = input[1].split(" ").map(Number);
    let p = Number(input[2]);
    console.log(solution(n, m, t, arr, p));
    process.exit();
  });
