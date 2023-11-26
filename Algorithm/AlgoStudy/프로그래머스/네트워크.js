function solution(n, computers) {
  let visited = Array(n).fill(0);
  let answer = 0;
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      let que = [i];
      visited[i] = 1;
      while (0 < que.length) {
        let cpu = que.shift();
        for (let next_cpu = 0; next_cpu < n; next_cpu++) {
          if (computers[cpu][next_cpu] && !visited[next_cpu]) {
            visited[next_cpu] = 1;
            que.push(next_cpu);
          }
        }
      }
      answer++;
    }
  }

  return answer;
}
