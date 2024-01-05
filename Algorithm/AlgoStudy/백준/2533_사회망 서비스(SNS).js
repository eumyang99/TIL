// 발상
// 시작 노드는 어느 곳에서 하든 상관 없음(사이클이 없는 그래프이기 때문)
// 특정 노드가 얼리어댑터인 경우, 다음 노드는 (얼리어댑터, 비 얼리어댑터) 모두 가능
// 특정 노드가 얼리어댑터가 아닌 경우, 얼리어댑터만 가능

// 따라서 A 노드가 얼리어댑터인 경우
// 다음 노드 B가 (얼리어댑터인 경우, 비 얼리어댑터인 경우) 중 작은 값을 채택하고
// 자기 자신이 어리어댑터이기 때문에 +1 한다

// A 노드가 비 얼리어댑터인 경우
// 다음 노드 B가 얼리어댑터인 경우의 값을 물려 받는다

// A가 (얼리어댑터인 경우, 비 얼리어댑터인 경우) 중 작은 값을 채택하여 이전 노드에 활용한다

// 이 과정을 반복하며 특정 노드의 값을 dp[node][비 얼리어댑터, 얼리어댑터] 에 저장하여 재사용 한다

function solution(n, dic) {
  let dp = Array.from({ length: n + 1 }, () => [0, 0]);
  let visited = Array(n + 1).fill(0);

  function SNS(node) {
    // 이미 방문한 상위 depth의 노드를 방문하지 않기 위한 방문 처리
    visited[node] = 1;

    // 현재 노드와 연결된 노드를 순회하며
    for (let next_node of dic[node]) {
      // 연결된 노드가 상위 노드면 넘어가고
      if (visited[next_node]) continue;
      // 하위 노드이면 재귀함수로 들어감
      SNS(next_node);
      // 재귀가 끝다면 자식 노드의 값이 정해진 상황
      // 현재 노드가 얼리어댑터인 경우 자식 노드가 (얼리어댑터인 경우, 비 얼리어댑터인 경우) 중 작은 값을 채택
      dp[node][1] += Math.min(...dp[next_node]);
      // 현재 노드가 비 얼리어댑터인 경우 자식노드가 얼리어댑터인 경우를 채택
      dp[node][0] += dp[next_node][1];
    }

    // 1) 일반적 case
    // 현재 노드가 얼리어댑터인 경우에는 자기 자신도 카운팅해야 하기 때문에 +1

    // 2) base case
    // 만약 말단 노드인 경우 위 for문을 거치지 못함
    // 연결된 노드는 상위 노드 하나인데 방문처리 되어서 재귀함수로 들어갈 수 없음
    // 따라서 말단 노드가 얼리어댑터인 경우(dp[node][1])에는 +1을 하고 얼리어댑터가 아닌 경우(dp[node][0])는 기존 초기값인 0으로 놔둠
    dp[node][1]++;
  }

  SNS(n);
  return Math.min(...dp[n]);
}

let n;
let dic = new Object();
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    let input = line.split(" ").map(Number);
    if (input.length === 1) {
      n = input[0];
      return;
    }
    if (dic[input[0]]) {
      dic[input[0]].push(input[1]);
    } else {
      dic[input[0]] = [input[1]];
    }
    if (dic[input[1]]) {
      dic[input[1]].push(input[0]);
    } else {
      dic[input[1]] = [input[0]];
    }
  })
  .on("close", () => {
    console.log(solution(n, dic));
    process.exit();
  });
