function solution(input) {
  let [r, c] = input[0].split(" ").map((el) => parseInt(el));
  let board = input.slice(1).map((el) => el.split(""));
  let jihoon = [];
  let fires = [];
  let res = 0;
  for (let x = 0; x < r; x++) {
    for (let y = 0; y < c; y++) {
      if (board[x][y] === "J") {
        jihoon.push([x, y]);
      }
      if (board[x][y] === "F") {
        fires.push([x, y]);
      }
    }
  }

  const [dx, dy] = [
    [-1, 0, 1, 0],
    [0, 1, 0, -1],
  ];
  bfs(0, jihoon, fires);
  return res ? res : "IMPOSSIBLE";

  function bfs(cnt, jihoon, fires) {
    let new_fires = [];
    let new_jihoon = [];

    fires.forEach(([fx, fy]) => {
      for (let i = 0; i < 4; i++) {
        let [nfx, nfy] = [fx + dx[i], fy + dy[i]];
        if (0 <= nfx && nfx < r && 0 <= nfy && nfy < c) {
          if (board[nfx][nfy] === "." || board[nfx][nfy] === "J") {
            board[nfx][nfy] = "F";
            new_fires.push([nfx, nfy]);
          }
        }
      }
    });

    jihoon.forEach(([jx, jy]) => {
      for (let i = 0; i < 4; i++) {
        let [njx, njy] = [jx + dx[i], jy + dy[i]];
        if (0 <= njx && njx < r && 0 <= njy && njy < c) {
          if (board[njx][njy] === ".") {
            board[njx][njy] = "J";
            new_jihoon.push([njx, njy]);
          }
        } else {
          res = cnt + 1;
          return;
        }
      }
    });

    if (res || new_jihoon.length === 0) {
      return;
    }

    bfs(cnt + 1, new_jihoon, new_fires);
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
    console.log(solution(input));
    process.exit();
  });
