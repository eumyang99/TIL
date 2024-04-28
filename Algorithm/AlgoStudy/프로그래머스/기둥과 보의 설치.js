function build_pillar(x, y, board) {
  // 바닥일 때
  if (y === 0) return true;
  // 이전 기둥이 있을 때
  if (board[x][y - 1][0]) return true;
  // 보가 있을 때
  if ((0 <= x - 1 && board[x - 1][y][1]) || board[x][y][1]) return true;
  return false;
}

function build_beam(x, y, board) {
  // 한쪽 끝 부분이 기둥일 때
  if (board[x][y - 1][0]) return true;
  if (board[x + 1][y - 1][0]) return true;
  // 양쪽에 보가 있을 때
  if (0 <= x - 1 && board[x - 1][y][1] && board[x + 1][y][1]) return true;
  return false;
}

function delete_pillar(x, y, board) {
  // 위에 기둥이 있는데 위에 기둥이 불가능할 때
  if (board[x][y + 1][0] && !build_pillar(x, y + 1, board)) return false;
  // 양쪽 보의 설치가 불가능할 때
  if (0 <= x - 1 && board[x - 1][y + 1][1] && !build_beam(x - 1, y + 1, board))
    return false;
  if (board[x][y + 1][1] && !build_beam(x, y + 1, board)) return false;
  return true;
}

function delete_beam(x, y, board) {
  // 보 위에 쌓인 기둥들이 있을 때 해당 기둥이 불가능할 때
  if (board[x][y][0] && !build_pillar(x, y, board)) return false;
  if (board[x + 1][y][0] && !build_pillar(x + 1, y, board)) return false;
  // 보의 좌우에 보가 있을 때 해당 보가 불가능할 때
  if (0 <= x - 1 && board[x - 1][y][1] && !build_beam(x - 1, y, board))
    return false;
  if (board[x + 1][y][1] && !build_beam(x + 1, y, board)) return false;
  return true;
}

function solution(n, build_frame) {
  const answer = [];
  // [[[기둥, 보]]]
  const board = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => Array(2).fill(0))
  );
  // [x, y, 종류, 설치/삭제]
  for (let [x, y, obj, order] of build_frame) {
    if (obj === 0) {
      // 기둥 설치
      if (order === 1) {
        if (board[x][y][0]) continue;
        if (build_pillar(x, y, board)) board[x][y][0] = 1;
        // 기둥 삭제
      } else {
        if (!board[x][y][0]) continue;
        board[x][y][0] = 0;
        if (!delete_pillar(x, y, board)) board[x][y][0] = 1;
      }
    } else {
      // 보 설치
      if (order === 1) {
        if (board[x][y][1]) continue;
        if (build_beam(x, y, board)) board[x][y][1] = 1;
        // 보 삭제
      } else {
        if (!board[x][y][1]) continue;
        board[x][y][1] = 0;
        if (!delete_beam(x, y, board)) board[x][y][1] = 1;
      }
    }
  }

  for (let x = 0; x < n + 1; x++) {
    for (let y = 0; y < n + 1; y++) {
      for (let type = 0; type < 2; type++) {
        if (board[x][y][type]) answer.push([x, y, type]);
      }
    }
  }
  return answer;
}
