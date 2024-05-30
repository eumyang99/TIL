function solution(n) {
  const memo = Array(n + 1).fill(Infinity);
  memo[1] = 0;
  const visited = Array(n + 1).fill(false);
  // cnt, now_len, clip_len
  const que = [[2, 2, 1]];
  while (que.length) {
    const [cnt, now, clip] = que.shift();
    if (now === n) return cnt;
    memo[now] = cnt;

    if (cnt + 1 < memo[now - 1]) {
      que.push([cnt + 1, now - 1, clip]);
    }
    if (cnt + 1 < memo[now + clip]) {
      que.push([cnt + 1, now + clip, clip]);
    }
    if (!visited[now]) {
      que.push([cnt + 1, now, now]);
      visited[now] = true;
    }
  }
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
    console.log(solution(parseInt(input[0])));
    process.exit();
  });
