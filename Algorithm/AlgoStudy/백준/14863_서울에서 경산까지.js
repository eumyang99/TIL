// 발상 : 배낭문제
// minutes Array = 소요시간 : idx / 총 모금액 : value
// 길이는 K+1, 값은 0으로 초기화

// 이전 지역까지 도착할 수 있는 모든 경우의 수의 소요시간(idx)에 가장 큰 모금액을 저장
// 다음 지역까지 도착할 수 있는 경우의 수는 minutes를 거꾸로 전체 순회하며 값이 있는 경우(해당 소요시간에 이전 지역까지 도착 가능)
// (이전 소요시간 + 걷는 시간)이 K분 보다 작다면 해당 idx에 모금액 누적을 저장
// (이전 소요시간 + 자전거 시간)이 K분 보다 작다면 해당 idx에 모금액 누적을 저장
// 같은 소요시간이 되는 경우 모금액 누적이 큰 값을 저장

// 모든 지역을 탐색 후 minutes의 최대값을 출력

function solution(input) {
  let [N, K] = input[0];
  let edges = input.slice(1);
  // 첫 지역에 해당하는 소요 시간에 모금액 초기화
  let minutes = Array(K + 1).fill(0);
  minutes[edges[0][0]] = Math.max(minutes[edges[0][0]], edges[0][1]);
  minutes[edges[0][2]] = Math.max(minutes[edges[0][2]], edges[0][3]);

  // 두번째 지역부터 마지막 지역까지 순회
  for (let edge = 1; edge < N; edge++) {
    let [walk_time, walk_money, bike_time, bike_money] = edges[edge];
    // minutes를 거꾸로 순회(앞에서부터 순회하면 데이터 오염됨)
    for (let time = K; 0 <= time; time--) {
      // 이전 지역까지 time 소요 시간으로 도착할 수 있는 경우
      if (minutes[time]) {
        // 다음 지역까지 걷는 시간을 더했을 때 K분 보다 작거나 같다면
        if (time + walk_time <= K) {
          // 누적값 중 큰 값을 저장
          minutes[time + walk_time] = Math.max(
            minutes[time + walk_time],
            minutes[time] + walk_money
          );
        }
        // 자전거 경우도 걷기와 같음
        if (time + bike_time <= K) {
          minutes[time + bike_time] = Math.max(
            minutes[time + bike_time],
            minutes[time] + bike_money
          );
        }
        // 이전 도착 시간은 사용했으므로 0으로 초기화
        // 다시 다음 지역을 탐색할 때 현재 지역까지 도착한 소요시간만 사용해야 하기 때문
        minutes[time] = 0;
      }
    }
  }

  // 최대값 출력
  return Math.max(...minutes);
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
    console.log(solution(input));
    process.exit();
  });
