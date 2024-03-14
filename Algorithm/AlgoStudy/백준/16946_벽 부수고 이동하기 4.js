// 1. 이동 공간의 그룹에 각각 그룹 사이즈를 기재하자
// 1.1 새로운 배열에 저장
// 2. 위에 저장된 정보를 가지고 각 벽마다 4방향을 탐색, 모두 더해서 값을 구하자

// 그룹 개수 배열 : 최대 1000*1000 1차원 배열
// 0을 만나면 최대한 탐색하며 new board에 해당 주소값을 기재, 총 몇개까지 갔는지 cnt세서 탐색 주소값에 cnt 기재

const [dx, dy] = [
  [0, 1, 0, -1],
  [1, 0, -1, 0],
];

function dfs(startX, startY, board, groupNum, n, m) {
  board[startX][startY] = -groupNum;
  let size = 1;
  const stack = [[startX, startY]];

  while (stack.length) {
    const [x, y] = stack.pop();
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (0 <= nx && nx < n && 0 <= ny && ny < m && !board[nx][ny]) {
        board[nx][ny] = -groupNum;
        size++;
        stack.push([nx, ny]);
      }
    }
    size %= 10;
  }

  return size;
}

function solution(n, m, board) {
  const groupSizeArr = [0];

  let groupNum = 1;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (board[x][y]) continue;
      const groupSize = dfs(x, y, board, groupNum, n, m);
      groupSizeArr.push(groupSize);
      groupNum++;
    }
  }

  const res = Array.from({ length: n }, () => Array(m).fill(0));
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (board[x][y] !== 1) continue;
      let val = 1;
      let visitedGourp = [];
      for (let i = 0; i < 4; i++) {
        const [nx, ny] = [x + dx[i], y + dy[i]];
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] !== 1) {
          const groupNum = -board[nx][ny];
          if (visitedGourp.includes(groupNum)) continue;
          val += groupSizeArr[groupNum];
          visitedGourp.push(groupNum);
        }
      }
      res[x][y] = val % 10;
    }
  }

  res.forEach((row) => {
    console.log(row.join(""));
  });
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
    const board = input.slice(1).map((el) => el.split("").map(Number));
    solution(n, m, board);
    process.exit();
  });
