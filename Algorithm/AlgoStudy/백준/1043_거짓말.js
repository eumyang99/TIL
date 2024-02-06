function solution(n, m, judge, party) {
  let res = m;
  // 진실을 아는 판단자 set
  let judgeSet = new Set(judge);
  // 진실 파티
  let truthParty = Array(m).fill(false);

  // 각 반복 마다 전체 파티를 순회
  while (true) {
    // stop = while문 flag
    let stop = true;

    // 전체 파티 순회
    for (let i = 0; i < m; i++) {
      // 이미 진실 파티라면 continue
      if (truthParty[i]) continue;

      // 미확정 파티 일 때, 해당 파티의 모든 사람을 확인
      for (let person of party[i]) {
        // 판단자가 파티에 있으면
        if (judgeSet.has(person)) {
          // 해당 파티의 모든 사람들을 판단자 set에 추가
          judgeSet = new Set([...judgeSet, ...party[i]]);
          // 해당 파티는 진실 파티로 기록
          truthParty[i] = true;
          // res 감소
          res--;
          // while문을 한번 더 돌게 함
          stop = false;
          break;
        }
      }
    }

    // 모든 파티를 순회했는데 flag가 true면 while 중지
    if (stop) break;
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
    const [n, m] = input[0];
    const judge = input[1].slice(1);
    const party = input.slice(2).map((el) => el.slice(1));

    console.log(solution(n, m, judge, party));
    process.exit();
  });
