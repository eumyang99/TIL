// 1. 제거 가능 횟수(remain)가 남아있을 때
// 1-1. 스택 top보다 작은 숫자가 들어오면 remain 차감 후 continue
// 1-2. 스택 top보다 큰 숫자가 들어왔는데 stack이 꽉 찼을 때
//      스택 top이 더 커질 때까지 && remain이 남아있을 때까지
//      stack pop 후 새로운 숫자를 스택에 추가
//      (앞 숫자는 뒷 숫자보다 크거나 같도록 remain이 허용하는 한 유지됨)

// 2. remain을 다 사용했을 때
// 2-1. 스택에 있는 숫자 + 아직 탐색하지 않은 숫자를 합쳐서 return

// 3. 연달아 같은 숫자가 들어오면 stack에 fullSize보다 많이 쌓이게 됨
// 3-1. 전체 숫자를 탐색한 후 stack의 앞부분 fullSize 만큼 잘라서 return

function solution(n, k, line) {
  // 반환할 숫자의 최대 길이
  const fullSize = n - k;
  // 차감 횟수
  let remain = k;

  const stack = [line[0]];
  for (let i = 1; i < n; i++) {
    // remain이 0이면 스택 + 남은 숫자를 반환
    if (remain === 0) return stack.map(String).join("") + line.slice(i);

    // 스택 top보다 작은 숫자가 들어왔을 때 스택이 꽉 차있다면
    if (line[i] < stack.at(-1) && fullSize <= stack.length) {
      // 해당 숫자를 제거했다는 의미로 remain 차감
      remain--;
      continue;
    }

    // 들어온 숫자가 stack top보다 크고 remain이 남아있을 때까지
    while (stack.at(-1) < line[i] && remain) {
      // stack pop
      stack.pop();
      // remain 차감
      remain--;
    }

    // 현재 숫자 push
    stack.push(line[i]);
  }

  // 같은 숫자들이 stack에 있어서 stack 길이가 fullSize보다 클 수 있으니
  // 잘라서 return
  return stack.map(String).join("").slice(0, fullSize);
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
    const [n, k] = input[0].split(" ").map(Number);
    const line = input[1];
    console.log(solution(n, k, line));
    process.exit();
  });
