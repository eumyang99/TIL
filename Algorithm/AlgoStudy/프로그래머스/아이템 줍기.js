// 1*1 정사각형으로 모든 타일을 채움
// 정사각형의 좌표는 min(x), min(y)

// 모든 정사각형을 순회하면서
// 네 방향을 탐색하며 정사각형이 아닌 경우
// 해당 방향에 따라 두 꼭지점의 양방향 edge 정보를 border 배열에 저장

// characterX, characterY 를 시작점으로
// border에 저장된 egde 정보를 활용해 BFS로 최단거리를 구함

// 우, 하, 좌, 상
const [dx, dy] = [
  [0, 1, 0, -1],
  [1, 0, -1, 0],
];
// 사각형에서 빈 공간을 접하는 방향에 따라 선분의 두 꼭지점의 좌표를 조정하는 상수
const [adx, ady, bdx, bdy] = [
  [0, 1, 0, 0],
  [1, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 0, 1],
];

// x, y 좌표의 사각형, i 방향 선분을 잇는 두 꼭지점의 edge 정보를 저장
function slide(x, y, i, border) {
  const [ax, ay, bx, by] = [x + adx[i], y + ady[i], x + bdx[i], y + bdy[i]];
  // 양방향으로 할당
  border[ax][ay]
    ? border[ax][ay].push([bx, by])
    : (border[ax][ay] = [[bx, by]]);
  border[bx][by]
    ? border[bx][by].push([ax, ay])
    : (border[bx][by] = [[ax, ay]]);
}

function solution(rectangle, characterX, characterY, itemX, itemY) {
  // 사각형 정보 정렬
  rectangle = rectangle.sort((a, b) => a[0] - b[0]);
  // 1*1 정사각형 표시
  const board = Array.from({ length: 51 }, () => Array(51).fill(0));
  for (let [x1, y1, x2, y2] of rectangle) {
    for (let x = x1; x < x2; x++) {
      for (let y = y1; y < y2; y++) {
        if (!board[x][y]) board[x][y] = 1;
      }
    }
  }

  // edge 정보를 담을 border 배열
  // border[꼭지점x][꼭지점y] = [[한쪽 꼭지점x, 한쪽 꼭지점y], [다른쪽 꼭지점x, 다른쪽 꼭지점y]]
  const border = Array.from({ length: 51 }, () => Array(51).fill(null));
  const stack = [[rectangle[0][0], rectangle[0][1]]];
  // 사각형 방문처리는 2로 표시
  board[rectangle[0][0]][rectangle[0][1]] = 2;
  while (stack.length) {
    const [x, y] = stack.pop();
    // 네 방향의 사각형을 탐색
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      // 방문하지 않은 사각형이라면 stack에 추가 후 방문처리
      if (board[nx][ny] === 1) {
        stack.push([nx, ny]);
        board[nx][ny] = 2;
        // 빈공간이라면 외접하는 선분의 두 꼭지점 edge 기록
      } else if (board[nx][ny] === 0) {
        slide(x, y, i, border);
      }
    }
  }

  // characterX, characterY를 시작점으로 BFS 탐색
  // 양방향으로 동시에 출발하여 먼저 도착하는 쪽의 거리를 반환
  const que = [[characterX, characterY, 0]];
  const visited = Array.from({ length: 51 }, () => Array(51).fill(0));
  visited[characterX][characterY] = 1;
  while (que.length) {
    const [x, y, dist] = que.shift();
    // 도착했다면 dist 반환
    if (x === itemX && y === itemY) return dist;
    // 현재 꼭지점에서 갈 수 있는 두 꼭지점을 거리를 증가시키며 que에 추가
    for (let [nx, ny] of border[x][y]) {
      if (visited[nx][ny]) continue;
      que.push([nx, ny, dist + 1]);
      visited[nx][ny] = 1;
    }
  }
}
