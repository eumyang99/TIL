function makeSec(time) {
  const [h, m, s] = time.split(":").map(Number);
  return h * 60 * 60 + m * 60 + s;
}

function makeTime(seconds) {
  const form = (t) => t.toString().padStart(2, "0");
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  return `${form(h)}:${form(m)}:${form(s)}`;
}

function solution(play_time, adv_time, logs) {
  const [entireSec, advLength] = [makeSec(play_time), makeSec(adv_time)];
  logs = logs.map((t) => t.split("-").map(makeSec));

  const timeLine = Array(entireSec + 1).fill(0);
  for (let [s, e] of logs) {
    timeLine[s]++;
    timeLine[e]--;
  }
  for (let t = 1; t < entireSec; t++) {
    timeLine[t] += timeLine[t - 1];
  }

  let [start, lastStart] = [0, entireSec - advLength];
  let totalSum = timeLine
    .slice(start, advLength)
    .reduce((accu, el) => accu + el);
  let maxSum = totalSum;
  for (let t = 1; t <= lastStart; t++) {
    const nextTotalSum =
      totalSum - timeLine[t - 1] + timeLine[t + advLength - 1];
    totalSum = nextTotalSum;
    if (nextTotalSum <= maxSum) continue;
    start = t;
    maxSum = nextTotalSum;
  }

  return makeTime(start);
}
