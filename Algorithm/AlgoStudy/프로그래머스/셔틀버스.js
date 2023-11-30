function solution(n, t, m, timetable) {
  for (let i = 0; i < timetable.length; i++) {
    let time = parseInt(timetable[i].slice(0, 2));
    let minute = parseInt(timetable[i].slice(3));
    timetable[i] = time * 60 + minute;
  }
  timetable.sort((a, b) => a - b);

  let bus_time = 540 - t;
  let crew_idx = 0;
  let last_crew = [];
  for (let i = 1; i <= n; i++) {
    bus_time += t;
    let limit_idx = crew_idx + m;
    for (let c_idx = crew_idx; c_idx < limit_idx; c_idx++) {
      if (timetable[c_idx] <= bus_time) {
        if (i === n) {
          last_crew.push(timetable[c_idx]);
        } else {
          crew_idx++;
        }
      } else {
        break;
      }
    }
  }

  let optimized_min;
  if (last_crew.length < m) {
    optimized_min = bus_time;
  } else {
    optimized_min = last_crew[m - 1] - 1;
  }

  let time = String(Math.floor(optimized_min / 60)).padStart(2, "0");
  let minute = String(optimized_min % 60).padStart(2, "0");
  let answer = time + ":" + minute;
  return answer;
}
