function solution(edges) {
  var answer = [0, 0, 0, 0];
  let start_check = Array(1000001).fill(true);
  let edges_map = new Object();

  // 노드 개수 구하기와 단방향 그래프
  let last_node = 0;
  edges.forEach(([s, e]) => {
    last_node = Math.max(Math.max(s, e), last_node);
    if (start_check[e]) start_check[e] = false;
    edges_map[s] ? edges_map[s].push(e) : (edges_map[s] = [e]);
  });

  // 추가된 노드 찾기
  let start_node;
  for (let i = 1; i <= last_node; i++) {
    if (start_check[i] && 1 < edges_map[i].length) {
      start_node = i;
      answer[0] = i;
      break;
    }
  }

  // 추가된 노드로부터 갈 수 있는 노드들을 순회
  let visited = Array(last_node + 1).fill(false);
  edges_map[start_node].forEach((group_start_node) => {
    // type 1 = 도넛
    // type 2 = 막대
    // type 3 = 8자
    let which_type = 1;
    let node = group_start_node;
    while (!visited[node]) {
      // 노드 방문처리
      visited[node] = true;
      if (which_type === 1) {
        // 이 노드로부터 출발하는 간선의 개수가 없으면 막대 확정
        if (!edges_map[node]) {
          which_type = 2;
          break;
        }
        // 이 노드로부터 출발하는 간선의 개수가 2개면 8자 확정
        if (edges_map[node].length === 2) {
          which_type = 3;
          break;
        }
      }
      // 위 조건에서 while문이 끝나지 않았으면 연결된 다음 노드 탐색
      node = edges_map[node][0];
    }
    // type에 맞는 개수 추가
    answer[which_type]++;
  });

  return answer;
}
