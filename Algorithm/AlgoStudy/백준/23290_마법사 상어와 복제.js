const fishDir = [
  null,
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
];
const sharkDir = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
];

function solution(m, s, fish, shark) {
  let res = m;

  // 3차원 배열 초기화 : [x][y][물고기 방향들]
  let originalBoard = Array.from({ length: 5 }, () =>
    Array.from({ length: 5 }, () => new Array())
  );
  let movedBoard = Array.from({ length: 5 }, () =>
    Array.from({ length: 5 }, () => new Array())
  );
  const smell = Array.from({ length: 5 }, () => Array(5).fill(0));

  for (let [x, y, dir] of fish) {
    originalBoard[x][y].push(dir);
  }

  // board 범위 체크
  function inBoard(dx, dy) {
    if (1 <= dx && dx < 5 && 1 <= dy && dy < 5) {
      return true;
    }
    return false;
  }

  // 물고기 움직임
  function fishMove(x, y, dir) {
    for (let i = dir + 8; dir < i; i--) {
      const [dx, dy] = [x + fishDir[i][0], y + fishDir[i][1]];
      if (
        inBoard(dx, dy) &&
        JSON.stringify([dx, dy]) != JSON.stringify(shark) &&
        !smell[dx][dy]
      ) {
        movedBoard[dx][dy].push(i % 8 ? i % 8 : 8);
        return;
      }
    }
    movedBoard[x][y].push(dir);
  }

  // 상어 움직임
  function sharkMove(shark) {
    let maxHunt = -1;
    let route;

    function makeSharkPermu(x, y, accu, arr, eachRoute) {
      if (arr.length === 3) {
        if (maxHunt < accu) {
          maxHunt = accu;
          route = eachRoute.slice();
        }
        return;
      }

      for (let i = 0; i < 4; i++) {
        const [dx, dy] = [x + sharkDir[i][0], y + sharkDir[i][1]];
        if (!inBoard(dx, dy)) continue;
        arr.push(i);
        if (
          eachRoute.some(
            (spot) => JSON.stringify(spot) === JSON.stringify([dx, dy])
          )
        ) {
          eachRoute.push([dx, dy]);
          makeSharkPermu(dx, dy, accu, arr, eachRoute);
        } else {
          eachRoute.push([dx, dy]);
          makeSharkPermu(
            dx,
            dy,
            accu + movedBoard[dx][dy].length,
            arr,
            eachRoute
          );
        }
        arr.pop();
        eachRoute.pop();
      }
    }

    makeSharkPermu(shark[0], shark[1], 0, [], []);
    for (let [dx, dy] of route) {
      if (movedBoard[dx][dy].length) {
        smell[dx][dy] = 3;
        movedBoard[dx][dy] = [];
      }
    }
    return [maxHunt, route.at(-1)];
  }

  // 냄새 제거
  function smellDiscount() {
    for (let x = 1; x < 5; x++) {
      for (let y = 1; y < 5; y++) {
        if (smell[x][y]) smell[x][y]--;
      }
    }
  }

  // 게임
  for (let i = 0; i < s; i++) {
    res *= 2;
    movedBoard = Array.from({ length: 5 }, () =>
      Array.from({ length: 5 }, () => new Array())
    );
    for (let x = 1; x < 5; x++) {
      for (let y = 1; y < 5; y++) {
        originalBoard[x][y].forEach((dir) => {
          fishMove(x, y, dir);
        });
      }
    }

    const [huntingCnt, newShark] = sharkMove(shark);
    res -= huntingCnt;
    shark = newShark;

    for (let x = 1; x < 5; x++) {
      for (let y = 1; y < 5; y++) {
        originalBoard[x][y].push(...movedBoard[x][y]);
      }
    }
    smellDiscount();
  }

  return res;
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
    const [m, s] = input[0];
    const fish = input.slice(1, m + 1);
    const shark = input.at(-1);
    console.log(solution(m, s, fish, shark));
    process.exit();
  });
