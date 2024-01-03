// 발상
// union-find 활용
// 모든 도시에 대해 union을 시키고
// 여행 경로에 있는 모든 도시들이 같은 조상을 갖고 있는지 확인

function solution(n, m, edges, route) {
  let parent = Array.from({ length: n }, (_, idx) => idx);

  function find(x) {
    if (x === parent[x]) return x;
    parent[x] = find(parent[x]);
    return parent[x];
  }

  // union 과정
  for (let city = 0; city < n; city++) {
    let city_parent = find(city);
    for (let next_city = 0; next_city < n; next_city++) {
      if (edges[city][next_city]) {
        let next_city_parent = find(next_city);
        if (city_parent === next_city_parent) continue;
        parent[next_city_parent] = city_parent;
      }
    }
  }

  // 여행 경로 도시들의 조상 비교
  const route_parent = find(route[0]);
  for (let city_idx = 1; city_idx < m; city_idx++) {
    let city_parent = find(route[city_idx]);
    if (route_parent === find(city_parent)) continue;
    return "NO";
  }

  return "YES";
}

let input = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    input.push(line.split(" ").map(Number));
  })
  .on("close", () => {
    const n = input[0][0];
    const m = input[1][0];
    const edges = input.slice(2, n + 2);
    const route = input[n + 2].map((el) => el - 1);
    console.log(solution(n, m, edges, route));
    process.exit();
  });
