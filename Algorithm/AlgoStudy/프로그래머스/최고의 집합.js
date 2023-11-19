function solution(n, s) {
  if (s < n) {
    return [-1];
  }

  let q = Math.floor(s / n);
  let r = s % n;

  answer = Array(n).fill(q);
  for (let i = n - 1; 0 < r; i--) {
    answer[i] += 1;
    r--;
  }

  return answer;
}
