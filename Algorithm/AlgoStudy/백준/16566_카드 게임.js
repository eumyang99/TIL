function solution(n, m, k, minsu, suggest) {
  minsu = minsu.sort((a, b) => a - b);

  // 카드 값의 인덱스 저장
  const idx_arr = Array(n + 1);
  // parent 저장
  // 없는 카드는 참조하지 않아야 함
  const left_parent = Array(n + 1);
  const right_parent = Array(n + 1);
  for (let i = 0; i < m; i++) {
    idx_arr[minsu[i]] = i;
    left_parent[minsu[i]] = minsu[i];
    right_parent[minsu[i]] = minsu[i];
  }

  const find = (card, parent) => {
    if (parent[card] === card) return card;
    parent[card] = find(parent[card], parent);
    return parent[card];
  };

  for (const target of suggest) {
    // 민수 카드 arr의 인덱스
    // 가장 "작은" 카드의 "오른쪽 부모 카드"를 찾고 그 카드의 idx를 찾음
    let l_idx = idx_arr[find(minsu[0], right_parent)];
    // 가장 "큰" 카드의 "왼쪽 부모 카드"를 찾고 그 카드의 idx를 찾음
    let r_idx = idx_arr[find(minsu.at(-1), left_parent)];
    while (l_idx < r_idx) {
      // 중간 카드의 idx
      const m_idx = Math.floor((l_idx + r_idx) / 2);
      // 이 카드가 사용된 카드일 때
      if (
        left_parent[minsu[m_idx]] !== minsu[m_idx] ||
        right_parent[minsu[m_idx]] !== minsu[m_idx]
      ) {
        // 찾아야 하는 값보다 작거나 같으면
        if (minsu[m_idx] <= target) {
          // 오른쪽 부모를 l_idx로 바꿈
          l_idx = idx_arr[find(minsu[m_idx], right_parent)];
          continue;
        }

        // 찾아야 하는 값보다 크면
        if (target < minsu[m_idx]) {
          // 그 카드보다 작은 카드의 인덱스를 r_idx로
          new_r_idx = idx_arr[find(minsu[m_idx], left_parent)];

          // 그 때 r_idx가 될 카드의 값이 target보다 작거나 같으면
          if (minsu[new_r_idx] <= target) {
            // l_idx를 높이고
            l_idx = idx_arr[find(minsu[m_idx], right_parent)];
            continue;
          }

          // r_idx가 될 카드의 값이 유효한 값이면
          if (target < minsu[new_r_idx]) {
            // r_idx를 갱신
            r_idx = new_r_idx;
          }
        }
      }

      // 사용할 수 있는 카드일 때
      // 카드가 target 보다 작거나 같으면
      if (minsu[m_idx] <= target) {
        // 오른쪽 카드의 최종 부모를 l_idx로 갱신
        l_idx = idx_arr[find(minsu[m_idx + 1], right_parent)];
        continue;
      }

      // 유효한 카드면
      if (target < minsu[m_idx]) {
        // m_idx를 r_idx로 갱신
        r_idx = m_idx;
      }
    }

    // 제출할 카드 출력
    console.log(minsu[l_idx]);

    // 사용한 카드의 parent 조정
    left_parent[minsu[l_idx]] = minsu[l_idx - 1];
    right_parent[minsu[l_idx]] = minsu[l_idx + 1];
  }
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
    const [n, m, k] = input[0].split(" ").map(Number);
    const minsu = input[1].split(" ").map(Number);
    const suggest = input[2].split(" ").map(Number);
    solution(n, m, k, minsu, suggest);
    process.exit();
  });
