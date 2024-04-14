// 정보 관리
// visited : 방문 여부 visited array
// board : 전등 on 여부 array
// light : 갈 수 있는 후보지 set

// que에 현재 도착한 위치 담고
// 각각의 현재 위치에서 켤 수 있는 전등을 모두 킨다
// 단, 이미 켜져 있는 곳이면 continue
// 꺼져 있는 곳이면 board에 1을 기록하고 light에 추가한다
// que의 모든 위치에서 전등을 다 켰으면
// 전등이 켜져 있는 곳(다음 후보지)을 모두 순회하며 해당 전등의 4 방향에 visited가 있는지 확인
// visited가 있으면 해당 위치로 갈 수 있는 경로가 있는 것
// 이 경우, 후보지를 que에 추가, light에서 제거, visited에 방문처리를 한다

// 한 depth씩 처리하는 bfs 방식 사용

const [dx, dy] = [
  [0, 1, 0, -1],
  [1, 0, -1, 0],
];

function solution(n, m, btn) {
  let answer = 1;
  const edges = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => [])
  );
  const light = new Set();
  const board = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
  const visited = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
  for (let [x, y, a, b] of btn) {
    edges[x][y].push([a, b]);
  }

  const que = [[1, 1]];
  board[1][1] = 1;
  visited[1][1] = 1;

  function canGo(nx, ny) {
    if (0 < nx && nx <= n && 0 < ny && ny <= n && visited[nx][ny]) return true;
    return false;
  }

  while (que.length) {
    while (que.length) {
      const [x, y] = que.shift();
      for (let [lx, ly] of edges[x][y]) {
        if (board[lx][ly]) continue;
        board[lx][ly] = 1;
        light.add([lx, ly]);
        answer++;
      }
    }

    light.forEach((nextLight) => {
      const [nlx, nly] = nextLight;
      for (let i = 0; i < 4; i++) {
        const [nx, ny] = [nlx + dx[i], nly + dy[i]];
        if (canGo(nx, ny)) {
          light.delete(nextLight);
          visited[nlx][nly] = 1;
          que.push([nlx, nly]);
          return;
        }
      }
    });
  }

  return answer;
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
    const [n, m] = input[0];
    const btn = input.slice(1);
    console.log(solution(n, m, btn));
    process.exit();
  });
