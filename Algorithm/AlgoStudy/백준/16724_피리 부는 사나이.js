// 1.
// 특정 노드를 타고 들어가면서
// 보드 외부로 나가거나 이미 지나온 노드를 만나면 res += 1

// 2.
// 과거 탐색했던 부분을 만나면(node가 number)
// res += 1
// unionCnt += 1

// 3.
// 최종적으로 res - unionCnt 를 출력

// [2.] 에서도 res를 증가시키는 이유는 과거와 현재, 미래의 탐색 루트를 구분하기 위해서.
// 대신 unionCnt로 루트들이 몇번 합쳐졌는지 카운팅해서 마지막에 차감함

const delta = {
  R: [0, 1],
  D: [1, 0],
  L: [0, -1],
  U: [-1, 0],
};

function solution(n, m, board) {
  let res = 0;
  let unionCnt = 0;
  for (let startX = 0; startX < n; startX++) {
    for (let startY = 0; startY < m; startY++) {
      if (typeof board[startX][startY] === "number") continue;

      let [x, y] = [startX, startY];
      while (true) {
        if (!((0 <= x) & (x < n) & (0 <= y) & (y < m)) || board[x][y] === res) {
          res++;
          break;
        }
        if (typeof board[x][y] === "number") {
          res++;
          unionCnt++;
          break;
        }
        const direction = board[x][y];
        board[x][y] = res;
        x += delta[direction][0];
        y += delta[direction][1];
      }
    }
  }
  return res - unionCnt;
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
    const [n, m] = input[0].split(" ").map(Number);
    const board = input.slice(1).map((el) => el.split(""));
    console.log(solution(n, m, board));
    process.exit();
  });
