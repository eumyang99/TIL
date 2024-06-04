function solution(board) {
  const empty = [];
  for (let x = 0; x < 9; x++) {
    for (let y = 0; y < 9; y++) {
      if (board[x][y]) continue;
      empty.push([x, y]);
    }
  }

  const check_window = (val, x, y) => {
    const [win_top, win_left] = [Math.floor(x / 3) * 3, Math.floor(y / 3) * 3];
    for (let i = win_top; i < win_top + 3; i++) {
      for (let j = win_left; j < win_left + 3; j++) {
        if (board[i][j] === val) return false;
      }
    }
    return true;
  };

  const check_row = (val, x) => {
    if (board[x].includes(val)) return false;
    return true;
  };

  const check_col = (val, y) => {
    for (let i = 0; i < 9; i++) {
      if (board[i][y] === val) return false;
    }
    return true;
  };

  let flag = false;

  const dfs = (idx) => {
    if (flag) return;
    if (idx === empty.length) {
      flag = true;
      for (let row = 0; row < 9; row++) {
        console.log(board[row].map(String).join(""));
      }
      return;
    }
    const [x, y] = empty[idx];
    for (let val = 1; val <= 9; val++) {
      if (!check_window(val, x, y)) continue;
      if (!check_row(val, x)) continue;
      if (!check_col(val, y)) continue;
      board[x][y] = val;
      dfs(idx + 1);
      board[x][y] = 0;
    }
  };

  dfs(0);
}

let board = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline
  .on("line", (line) => {
    board.push(line);
  })
  .on("close", () => {
    board = board.map((row) => row.split("").map(Number));
    solution(board);
    process.exit();
  });
