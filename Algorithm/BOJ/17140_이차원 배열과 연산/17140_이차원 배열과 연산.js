// 무조건 각 행의 개수로 정렬
// 아래의 경우 배열을 그대로 재귀함수에 넘김
// - 배열의 세로가 가로보다 클 때
// - 배열이 뒤집히지 않은 상태에서 가로와 세로가 같을 때

// 아래의 경우 배열을 뒤집어서 재귀함수에 넘김
// - 배열의 가로가 세로보다 클 때
// - 배열이 뒤집힌 상태에서 가로와 세로가 같을 때

// 각 행의 숫자 카운팅은 hashmap 사용
// 정렬은 cntArr.sort((a, b) => a[1] - b[1] || a[0] - b[0])
// 이후 flat 메소드로 배열의 차원을 낮춤

function check(answer, r, c, k, reversed, board) {
  // answer가 100이 넘으면 -1 반환
  if (100 < answer) return -1;

  // 전달 받은 board의 크기
  const [r_size, c_size] = [board.length, board[0].length];
  // 타겟을 찾으면 answer 반환
  if (r < r_size && board[r][c] === k) return answer;

  // 다음 재귀로 넘길 board
  let nextBoard = [];
  // board의 가로 최대 길이
  let maxLength = 0;
  // 각 행에 대하여
  for (let row = 0; row < r_size; row++) {
    // count = {등장하는 숫자 : 빈도}
    let count = new Map();
    // 각 열에 대해 빈도 누적
    for (let col = 0; col < c_size; col++) {
      if (board[row][col] === 0) continue;
      const [key, val] = [board[row][col], count.get(board[row][col])];
      count.has(key) ? count.set(key, val + 1) : count.set(key, 1);
    }
    // [숫자, 빈도]를 담는 배열
    let cntArr = [];
    for (let item of count) {
      cntArr.push(item);
    }

    // 빈도 오름차순 & 숫자 오름차순 정렬
    cntArr.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
    // 그 다음 flat 이후 100개만 추림
    cntArr = cntArr.flat().slice(0, 100);
    // board의 최대 가로 길이 갱신
    maxLength = Math.max(maxLength, cntArr.length);
    // board에 행 추가
    nextBoard.push(cntArr);
  }

  // 가로 최대 길이에 맞추어 각 행에 "0" 추가
  nextBoard = nextBoard.map((row) => [
    ...row,
    ...Array(maxLength - row.length).fill(0),
  ]);
  // 전달 받은 board가 뒤집히지 않았으면서 여전히 세로 길이가 가로 길이보다 크거나 같으면
  if (!reversed && maxLength <= r_size)
    return check(answer + 1, r, c, k, reversed, nextBoard);
  // 혹은 전달 받은 board가 뒤집혀 있으면서 세로 길이가 가로 길이보다 크면
  if (reversed && maxLength < r_size)
    // reversed 상태와 r, c를 그대로 넘김
    return check(answer + 1, r, c, k, reversed, nextBoard);

  // 뒤집힌 board 초기화
  const reversedBoard = Array.from({ length: maxLength }, () =>
    Array(r_size).fill(0)
  );
  // i, j 값을 바꾸어 뒤집힌 board에 기록
  for (let i = 0; i < nextBoard.length; i++) {
    for (let j = 0; j < maxLength; j++) {
      if (nextBoard[i][j] === 0) break;
      reversedBoard[j][i] = nextBoard[i][j];
    }
  }
  // reversed 상태를 바꾸고 r, c => c, r로 바꾸어 전달
  return check(answer + 1, c, r, k, !reversed, reversedBoard);
}

function solution(r, c, k, initBoard) {
  return check(0, r, c, k, false, initBoard);
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
    const [r, c, k] = input[0];
    const initBoard = input.slice(1);
    console.log(solution(r - 1, c - 1, k, initBoard));
    process.exit();
  });
