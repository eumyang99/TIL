// 1. 각 퍼즐 조각과 보드의 빈 공간의 원본을 저장
// 2. 퍼즐 조각의 piece들을 최대한 좌상단으로 옮기고 정렬한다.
// 3. 빈 공간의 원본도 최대한 좌상단으로 옮기고 정렬한다.
// 4. 빈 공간과 퍼즐 조각의 배열이 같은지 확인한다.
// 5. 다르다면 퍼즐 조각을 시계방향으로 돌린다.
//// 각 퍼즐 조각의 piece를 시계방향으로 돌리면 [x, y] => [y, row_size - x]
//// row_size = 퍼즐 조각을 담을 수 있는 가장 작은 직육면체의 세로 길이 - 1
//// 즉, 평행이동한 모든 piece의 x 값 중 가장 큰 값 - 1
// 6. 다시 빈 공간과 퍼즐 조각 배열을 비교한다.

const [dx, dy] = [
  [0, 1, 0, -1],
  [1, 0, -1, 0],
];
// board 크기
let size;
// 퍼즐 면적에 따른 퍼즐 조각 배열을 담을 dic
const dic = {};

function in_board(nx, ny, size) {
  if (0 <= nx && nx < size && 0 <= ny && ny < size) return true;
  return false;
}

// 좌상단으로 옮기는 함수
// 가장 작은 row값이 0이 되고, 가장 작은 col값이 0이 되도록 모든 조각의 좌표를 평행이동
function adjust(block, min_row, min_col) {
  block = block.map((piece) => [piece[0] - min_row, piece[1] - min_col]);
  return block;
}

// row 기준으로 가장 작은 값으로 정렬하되 같은 row값일 경우 col기준으로 정렬
// 이 코드는 아주 유용한 코드!!
function sorting(block) {
  // aX - bX의 값이 다르면 정렬되고 같다면 0이기 때문에 falsy라서 aY - bY 기준으로 정렬됨
  block.sort(([aX, aY], [bX, bY]) => aX - bX || aY - bY);
  return block;
}

// 빈 공간이나 퍼즐 조각의 모양(배열)을 리턴하는 함수
// board에 game_board나 table이 들어감
// board 자체가 참조하는 배열이기 때문에 board의 값을 수정하면 원본 배열의 값이 수정됨
// 이것도 아주 유용한 방법!!
function part(board, i, j) {
  let block = [];
  let [min_row, min_col] = [i, size];
  const stack = [[i, j]];
  board[i][j] = 0;
  while (stack.length) {
    const [x, y] = stack.pop();
    block.push([x, y]);
    if (y < min_col) {
      min_col = y;
    }
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (!in_board(nx, ny, size) || !board[nx][ny]) continue;
      stack.push([nx, ny]);
      board[nx][ny] = 0;
    }
  }
  block = sorting(adjust(block, min_row, min_col));
  return block;
}

// 네 방향으로 돌리면서 빈 공간과 같은 모양인지 확인하는 함수
function correct(space, block) {
  for (let i = 0; i < 4; i++) {
    let is_correct = true;
    for (let j = 0; j < block.length; j++) {
      if (block[j][0] !== space[j][0] || block[j][1] !== space[j][1]) {
        is_correct = false;
        break;
      }
    }
    if (is_correct) return true;
    const row_size = block.at(-1)[0];
    block = sorting(block.map((piece) => [piece[1], row_size - piece[0]]));
  }
  return false;
}

function solution(game_board, table) {
  let res = 0;
  size = table.length;

  // game_board와 table을 part 함수에서 공통으로 사용하기 위해 1과 0을 바꿈
  game_board = game_board.map((row) =>
    row.map((piece) => (piece === 1 ? 0 : 1))
  );

  // 퍼즐 조각을 dic에 저장하는 부분
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (table[i][j]) {
        block = part(table, i, j);
        if (dic[block.length]) dic[block.length].push([0, block]);
        else dic[block.length] = [[0, block]];
      }
    }
  }

  // 빈 공간의 모양을 찾고 해당 모양과 같은 크기의 퍼즐 조각들을 순회하며 일치 여부를 확인하는 부분
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (game_board[i][j]) {
        space = part(game_board, i, j);
        if (!dic[space.length]) continue;
        for (let k = 0; k < dic[space.length].length; k++) {
          if (dic[space.length][k][0]) continue;
          if (correct(space, dic[space.length][k][1])) {
            res += space.length;
            dic[space.length][k][0] = 1;
            break;
          }
        }
      }
    }
  }

  return res;
}
