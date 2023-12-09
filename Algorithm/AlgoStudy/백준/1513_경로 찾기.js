function solution(input) {
  let [n, m, c] = input[0].split(" ").map((el) => parseInt(el));
  let board = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
  let game_num = 1;
  for (let game of input.slice(1)) {
    let [x, y] = game.split(" ").map((el) => parseInt(el));
    board[x][y] = game_num;
    game_num++;
  }

  let memo = Array.from(Array(n + 1), () =>
    Array.from(Array(m + 1), () =>
      Array.from(Array(c + 1), () => Array(game_num).fill(0))
    )
  );

  memo[0][1][0][0] = 1;

  for (let x = 1; x <= n; x++) {
    for (let y = 1; y <= m; y++) {
      let this_game = board[x][y];
      // 게임일 때
      if (this_game) {
        for (let cnt = 0; cnt < c; cnt++) {
          for (let game = 0; game < this_game; game++) {
            memo[x][y][cnt + 1][this_game] +=
              memo[x - 1][y][cnt][game] + memo[x][y - 1][cnt][game];
          }
          memo[x][y][cnt + 1][this_game] %= 1000007;
        }
      }

      // 게임 아닐 때
      else {
        for (let cnt = 0; cnt <= c; cnt++) {
          for (let game = 0; game <= c; game++) {
            memo[x][y][cnt][game] =
              memo[x - 1][y][cnt][game] + memo[x][y - 1][cnt][game];
            memo[x][y][cnt][game] %= 1000007;
          }
        }
      }
    }
  }

  res = [];
  memo[n][m].map((arr) => {
    let sum = arr.reduce((accu, val) => {
      return accu + val;
    });
    sum %= 1000007;
    res.push(sum);
  });
  return res.join(" ");
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
