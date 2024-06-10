const [dx, dy] = [
  [-1, 0, 1, 0],
  [0, 1, 0, -1],
];

function solution(land) {
  let answer = 0;
  const [row, col] = [land.length, land[0].length];
  let num = 1;
  const size = [0];
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (land[i][j]) land[i][j] = -1;
    }
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (land[i][j] !== -1) continue;
      const stack = [[i, j]];
      land[i][j] = num;
      let cnt = 1;
      while (stack.length) {
        const [x, y] = stack.pop();
        for (let d = 0; d < 4; d++) {
          const [nx, ny] = [x + dx[d], y + dy[d]];
          if (nx < 0 || row <= nx || ny < 0 || col <= ny || land[nx][ny] !== -1)
            continue;
          cnt++;
          land[nx][ny] = num;
          stack.push([nx, ny]);
        }
      }
      size.push(cnt);
      num++;
    }
  }

  for (let spot = 0; spot < col; spot++) {
    let total = 0;
    let group = new Set();
    for (let dep = 0; dep < row; dep++) {
      if (land[dep][spot] === 0) continue;
      if (group.has(land[dep][spot])) continue;
      total += size[land[dep][spot]];
      group.add(land[dep][spot]);
    }
    if (answer < total) answer = total;
  }

  return answer;
}
