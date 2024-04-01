// 벨만포드 공부해야 함

function solution(info, edges) {
  const [n, m, w] = info;
  const oppositeDir = [];
  for (let i = 0; i < m + w; i++) {
    if (i < m) {
      const [s, e, w] = edges[i];
      oppositeDir.push([e, s, w]);
    } else {
      edges[i][2] *= -1;
    }
  }
  const edgesArr = oppositeDir.concat(edges);
  const visited = Array(n + 1).fill(false);

  function bellmanFord(start, dist) {
    dist[start] = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < edgesArr.length; j++) {
        const [s, e, w] = edgesArr[j];
        if (dist[s] !== Infinity && dist[s] + w < dist[e]) {
          dist[e] = dist[s] + w;
          if (!visited[e]) visited[e] = true;
          if (i === n - 1) return true;
        }
      }
    }
    return false;
  }

  for (let i = 1; i < n + 1; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    const dist = Array(n + 1).fill(Infinity);
    if (bellmanFord(i, dist)) return "YES";
  }
  return "NO";
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
    const TC = parseInt(input[0]);
    const arr = input.slice(1).map((el) => el.split(" ").map(Number));
    let startLine = 0;
    for (let i = 0; i < TC; i++) {
      const endLine = startLine + arr[startLine][1] + arr[startLine][2] + 1;
      console.log(solution(arr[startLine], arr.slice(startLine + 1, endLine)));
      startLine = endLine;
    }

    process.exit();
  });

// // function solution(info, edges) {
// //   const [n, m, w] = info;
// //   const edgesArr = Array.from({ length: n + 1 }, () =>
// //     Array(n + 1).fill(-10001)
// //   );
// //   edges.forEach(([s, e, w], idx) => {
// //     if (idx < m) {
// //       edgesArr[s][e] = w;
// //       edgesArr[e][s] = w;
// //     } else {
// //       edgesArr[s][e] = -w;
// //     }
// //   });

// //   function backTracking(s, cost) {
// //     for (let e = 1; e < n + 1; e++) {
// //       if (flag) return;
// //       const edgeCost = edgesArr[s][e];
// //       if (edgeCost === -10001) continue;
// //       if (cost[e] === -Infinity) {
// //         cost[e] = cost[s] + edgeCost;
// //         backTracking(e, cost.slice());
// //         cost[e] = -Infinity;
// //         continue;
// //       }
// //       if (cost[s] + edgeCost < cost[e]) {
// //         flag = true;
// //       }
// //     }
// //   }

// //   let flag = false;
// //   for (let s = 0; s < n + 1; s++) {
// //     const cost = Array(n + 1).fill(-Infinity);
// //     cost[s] = 0;
// //     backTracking(s, cost);
// //     if (flag) return "YES";
// //   }
// //   return "NO";
// // }

// // let input = [];
// // const readline = require("readline").createInterface({
// //   input: process.stdin,
// //   output: process.stdout,
// // });
// // readline
// //   .on("line", (line) => {
// //     input.push(line);
// //   })
// //   .on("close", () => {
// //     const TC = parseInt(input[0]);
// //     const arr = input.slice(1).map((el) => el.split(" ").map(Number));
// //     let startLine = 0;
// //     for (let i = 0; i < TC; i++) {
// //       const endLine = startLine + arr[startLine][1] + arr[startLine][2] + 1;
// //       console.log(solution(arr[startLine], arr.slice(startLine + 1, endLine)));
// //       startLine = endLine;
// //     }

// //     process.exit();
// //   });
