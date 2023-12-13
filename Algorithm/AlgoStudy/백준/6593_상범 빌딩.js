// 발상 : 전형적인 BFS

let [dh, dx, dy] = [
  [-1, 0, 0, 0, 0, 1],
  [0, -1, 0, 1, 0, 0],
  [0, 0, 1, 0, -1, 0],
];

function range_check(nh, nx, ny, L, R, C) {
  if (0 <= nh && nh < L && 0 <= nx && nx < R && 0 <= ny && ny < C) return true;
  else return false;
}

function solution(input) {
  let [L, R, C] = input[0];
  let building = input.slice(1);
  let start, end;
  for (let h = 0; h < L; h++) {
    for (let x = 0; x < R; x++) {
      for (let y = 0; y < C; y++) {
        if (building[h][x][y] === "S") start = [h, x, y];
        else if (building[h][x][y] === "E") end = [h, x, y];
      }
    }
  }

  let visited = Array.from({ length: L }, () =>
    Array.from({ length: R }, () => Array(C).fill(0))
  );
  visited[start[0]][start[1]][start[2]] = 1;
  let que = [[0, ...start]];
  let que_length = 1;
  while (que_length) {
    let [cnt, h, x, y] = que.shift();
    if (building[h][x][y] === "E") {
      return `Escaped in ${cnt} minute(s).`;
    }
    que_length--;
    for (let i = 0; i < 6; i++) {
      let [nh, nx, ny] = [h + dh[i], x + dx[i], y + dy[i]];
      if (
        range_check(nh, nx, ny, L, R, C) &&
        building[nh][nx][ny] !== "#" &&
        !visited[nh][nx][ny]
      ) {
        que.push([cnt + 1, nh, nx, ny]);
        visited[nh][nx][ny] = 1;
        que_length++;
      }
    }
  }

  return "Trapped!";
}

let input = [];
let floor = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    if (Number.isInteger(parseInt(line[0])) && input.length !== 0) {
      console.log(solution(input));
      input = [line.split(" ").map(Number)];
    } else if (line.length === 0) {
      input.push(floor);
      floor = [];
    } else if (Number.isInteger(parseInt(line[0])))
      input.push(line.split(" ").map(Number));
    else floor.push(line.split(""));
  })
  .on("close", () => {
    process.exit();
  });
