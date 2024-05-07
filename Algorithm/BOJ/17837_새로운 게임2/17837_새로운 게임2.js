// 구현 문제
// 주어진 조건을 꼼꼼히 적용해야 함

// 우, 좌, 상, 하
const [dx, dy] = [
  [0, 0, 0, -1, 1],
  [0, 1, -1, 0, 0],
];
// 파란색일 때 반대 방향의 dx, dy idx
// 따로 조건문을 사용할 필요가 없어서 좋은 방법임
const opposite = [0, 2, 1, 4, 3];

function solution(n, k, color, pieces) {
  let answer = 1;
  // board : 각 위치에 체스말의 번호를 순서를 반영하여 저장
  const board = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => [])
  );
  // board에 체스말 초기화
  pieces.forEach(([x, y, dir], idx) => board[x][y].push(idx));

  // 다음 갈 곳의 색을 구분하는 함수
  const order = (x, y) => {
    if (!(0 < x && x <= n && 0 < y && y <= n)) return "B";
    if (color[x][y] === 0) return "W";
    if (color[x][y] === 1) return "R";
    if (color[x][y] === 2) return "B";
  };

  // 다음 갈 곳이 흰색이나 빨간색일 때
  const notBlue = (x, y, nx, ny, num, step) => {
    // 현재 좌표에서 이동할 말의 idx를 확인
    const cutIdx = board[x][y].indexOf(num);
    // 이동할 말보다 idx가 큰 말들을 잘라냄
    // 빨간색이면 arr를 뒤집음
    const moveArr =
      step === "W"
        ? board[x][y].slice(cutIdx)
        : board[x][y].slice(cutIdx).reverse();

    // 현재 좌표에서 이동할 말들을 제거
    board[x][y] = board[x][y].slice(0, cutIdx);
    // 이동할 좌표에 말들을 추가
    board[nx][ny] = [...board[nx][ny], ...moveArr];
    // 이동한 말들의 좌표 정보를 모두 변경
    for (const p of moveArr) {
      pieces[p][0] = nx;
      pieces[p][1] = ny;
    }
  };

  // 다음 갈 곳이 파란색일 때
  const blue = (x, y, dir, num) => {
    // 이동할 말의 방향 정보를 변경
    pieces[num][2] = opposite[dir];
    // 반대 방향으로 이동할 곳의 좌표
    const [nx, ny] = [x + dx[opposite[dir]], y + dy[opposite[dir]]];
    // step : 이동할 곳의 색깔
    const step = order(nx, ny);
    // 이동할 곳의 색의 파란색이면 현재 위치 반환
    if (step === "B") return [x, y];
    // 파란색이 아니면 말들을 옮김
    notBlue(x, y, nx, ny, num, step);
    // 옮겨진 위치 반환
    return [nx, ny];
  };

  // 각 턴에서
  while (answer <= 1000) {
    // 모든 말을 순회하며 옮김
    for (let num = 0; num < k; num++) {
      // 현재 말의 좌표
      const [x, y, dir] = pieces[num];
      // 이동할 곳의 좌표
      let [nx, ny] = [x + dx[dir], y + dy[dir]];
      // step : 이동할 곳의 색깔
      const step = order(nx, ny);
      // 이동할 곳이 파란색이 아닐 때
      if (step !== "B") notBlue(x, y, nx, ny, num, step);
      // 이동할 곳이 파란색일 때
      // 말을 옮기고 이동한 좌표를 받음
      else if (step === "B") [nx, ny] = blue(x, y, dir, num);

      // 이동한 좌표의 말 개수 확인
      if (4 <= board[nx][ny].length) return answer;
    }
    // 모든 말을 옮긴 후 턴 증가
    answer++;
  }

  // 1000턴이 넘으면 -1 반환
  return -1;
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
    const [n, k] = input[0];
    const color = [
      Array(n + 1).fill(0),
      ...input.slice(1, n + 1).map((el) => [0, ...el]),
    ];
    const pieces = input.slice(n + 1);
    console.log(solution(n, k, color, pieces));
    process.exit();
  });
