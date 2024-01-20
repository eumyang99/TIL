let [dx, dy] = [
  [-1, 0, 1, 0],
  [0, 1, 0, -1],
];

function solution(n, m, board) {
  let answer = 0;
  // 외부 공기는 2로 처리
  function mark_air(stack) {
    while (stack.length !== 0) {
      let [x, y] = stack.pop();
      board[x][y] = 2;
      for (let i = 0; i < 4; i++) {
        let [nx, ny] = [x + dx[i], y + dy[i]];
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 0) {
          board[nx][ny] = 2;
          stack.push([nx, ny]);
        }
      }
    }
  }

  // 치즈 개수
  let cheeze = [];
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (board[x][y]) {
        cheeze.push([x, y]);
      }
    }
  }
  let cheeze_cnt = cheeze.length;

  // 치즈 없애기
  let new_space = [[0, 0]];
  let remove_cheeze = [];
  while (cheeze_cnt) {
    mark_air(new_space);
    new_space = [];

    cheeze.forEach(([x, y]) => {
      if (board[x][y] === 2) return;
      let around_air_cnt = 0;
      let space = [];
      for (let i = 0; i < 4; i++) {
        let [nx, ny] = [x + dx[i], y + dy[i]];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
          if (board[nx][ny] === 2) around_air_cnt++;
          else if (board[nx][ny] === 0) space.push([nx, ny]);
        }
      }
      if (2 <= around_air_cnt) {
        remove_cheeze.push([x, y]);
        new_space = new_space.concat(space);
      }
    });

    while (remove_cheeze.length !== 0) {
      let [x, y] = remove_cheeze.pop();
      board[x][y] = 2;
      cheeze_cnt--;
    }

    answer++;
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
    input.push(line);
  })
  .on("close", () => {
    const [n, m] = input[0].split(" ").map(Number);
    const board = input.slice(1).map((el) => el.split(" ").map(Number));
    console.log(solution(n, m, board));
    process.exit();
  });
// let [dx, dy] = [
//   [-1, 0, 1, 0],
//   [0, 1, 0, -1],
// ];

// function solution(n, m, board) {
//   let answer = 0;
//   // 외부 공기는 2로 처리
//   function mark_air(stack) {
//     while (stack.length !== 0) {
//       let [x, y] = stack.pop();
//       board[x][y] = 2;
//       for (let i = 0; i < 4; i++) {
//         let [nx, ny] = [x + dx[i], y + dy[i]];
//         if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 0) {
//           board[nx][ny] = 2;
//           stack.push([nx, ny]);
//         }
//       }
//     }
//   }

//   // 치즈 개수
//   let cheeze_cnt = 0;
//   for (let x = 0; x < n; x++) {
//     for (let y = 0; y < m; y++) {
//       if (board[x][y]) cheeze_cnt++;
//     }
//   }

//   // 치즈 없애기
//   let new_space = [[0, 0]];
//   let remove_cheeze = [];
//   while (cheeze_cnt) {
//     mark_air(new_space);
//     new_space = [];
//     for (let x = 0; x < n; x++) {
//       for (let y = 0; y < m; y++) {
//         if (board[x][y] !== 1) continue;
//         let around_air_cnt = 0;
//         let space = [];
//         for (let i = 0; i < 4; i++) {
//           let [nx, ny] = [x + dx[i], y + dy[i]];
//           if (0 <= nx && nx < n && 0 <= ny && ny < m) {
//             if (board[nx][ny] === 2) around_air_cnt++;
//             else if (board[nx][ny] === 0) space.push([nx, ny]);
//           }
//         }
//         if (2 <= around_air_cnt) {
//           remove_cheeze.push([x, y]);
//           new_space = new_space.concat(space);
//         }
//       }
//     }

//     while (remove_cheeze.length !== 0) {
//       let [x, y] = remove_cheeze.pop();
//       board[x][y] = 2;
//       cheeze_cnt--;
//     }

//     answer++;
//   }
//   return answer;
// }

// let input = [];
// const readline = require("readline").createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });
// readline
//   .on("line", (line) => {
//     input.push(line);
//   })
//   .on("close", () => {
//     const [n, m] = input[0].split(" ").map(Number);
//     const board = input.slice(1).map((el) => el.split(" ").map(Number));
//     console.log(solution(n, m, board));
//     process.exit();
//   });
