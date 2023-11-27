function solution(n, works) {
  var answer = 0;
  let works_sum = works.reduce((a, b) => a + b);
  if (works_sum <= n) {
    return answer;
  }
  works.sort((a, b) => b - a);
  works.push(0);
  let flag = false;
  let max_cnt = [works[0], 1];
  for (let i = 1; i < works.length; i++) {
    if (!flag) {
      let gap = (max_cnt[0] - works[i]) * max_cnt[1];
      n -= gap;
      if (0 < n) {
        max_cnt[0] = works[i];
        max_cnt[1]++;
      } else {
        n *= -1;
        let q = Math.floor(n / max_cnt[1]);
        let r = n % max_cnt[1];
        answer += (works[i] + q) ** 2 * (max_cnt[1] - r);
        answer += (works[i] + q + 1) ** 2 * r;
        answer += works[i] ** 2;
        flag = true;
      }
    } else {
      answer += works[i] ** 2;
    }
  }
  return answer;
}
