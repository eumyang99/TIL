function solution(dice) {
  const n = dice.length;

  // 각 주사위 마다 나타나는 숫자의 개수를 카운팅
  // dice_map의 idx = 주사위 번호
  // dice_map[idx] = {주사위 숫자 : 등장 빈도 수}
  let dice_map = Array.from({ length: n + 1 }, (_, idx) => {
    if (idx === 0) return null;
    let dice_info = new Object();
    for (let i = 0; i < 6; i++) {
      let num = dice[idx - 1][i];
      if (dice_info[num]) dice_info[num]++;
      else dice_info[num] = 1;
    }
    return dice_info;
  });

  // dice_map에서 만들어 놓은 정보 활용
  // ex) [1,2,3] 주사위 조합
  // 1번 주사위 = [2,2,2,3,3,4] = {2:3, 3:2, 4:1}
  // 2번 주사위 = [1,2,3,3,5,6] = {1:1, 2:1, 3:2, 5:1, 6:1}
  // 3번 주사위 = [4,4,4,4,4,4] = {4:6}
  // case [2 + 1 + 4] => 3 * 1 * 6 개의 경우의 수
  // case [3 + 3 + 4] => 3 * 2 * 6 개의 경우의 수
  // 주사위 숫자들의 합과 그 경우의 수를 game_set에 Object 형식으로 저장
  const res_sum = (nth, arr, sum, cnt) => {
    if (nth === arr.length) {
      // game_set의 마지막 요소에 저장
      if (game_set.at(-1)[1][sum]) game_set.at(-1)[1][sum] += cnt;
      else game_set.at(-1)[1][sum] = cnt;
      return;
    }

    for (let [key, value] of Object.entries(dice_map[arr[nth]])) {
      res_sum(nth + 1, arr, sum + parseInt(key), cnt * value);
    }
  };

  // 주사위 번호 조합
  const combi = (n, arr, start) => {
    // 조합이 완성되면 res_sum 함수를 사용하여 해당 조합으로 만들 수 있는 숫자들과 그 빈도수를 카운팅
    if (arr.length === n / 2) {
      // game_set에 [주사위 번호 조합]과 {주사위 숫자 합계 : 빈도수}를 담을 Object push
      game_set.push([arr.slice(), {}]);
      // res_sum으로 해당 조합의 정보 저장
      res_sum(0, arr, 0, 1);
      return;
    }

    for (let i = start; i <= n; i++) {
      if (arr.includes(i)) continue;
      arr.push(i);
      combi(n, arr, i + 1);
      arr.pop();
    }
  };

  // game_set 구성
  let game_set = [];
  combi(n, [], 1);
  let game_set_len = game_set.length;

  // res = [최대 승리 횟수, 그 주사위 번호 조합]
  let res = [0, null];

  // game_set에 저장되는 주사위 조합은 오름차순으로 정렬되어 있음
  // 따라서 Array의 양쪽 끝부터 차례대로 좁혀가며 두 주사위 조합을 비교
  for (let left_idx = 0; left_idx < game_set_len / 2; left_idx++) {
    let right_idx = game_set_len - left_idx - 1;
    let [left_win_cnt, right_win_cnt] = [0, 0];

    // 두 주사위 조합에 해당하는 숫자 총합의 대소를 비교하면서
    // 이긴 쪽 조합에 승리 회수를 누적 카운팅
    for (let [left_sum, left_cnt] of Object.entries(game_set[left_idx][1])) {
      for (let [right_sum, right_cnt] of Object.entries(
        game_set[right_idx][1]
      )) {
        // A조합의 숫자 총합 중에 10이 5번 등장하고
        // B조합의 숫자 총합 중에 15이 4번 등장한다면
        // 이 숫자 비교에서 B는 5 * 4회 승리 경우를 가져감
        if (parseInt(left_sum) > parseInt(right_sum))
          left_win_cnt += left_cnt * right_cnt;
        else if (parseInt(left_sum) < parseInt(right_sum))
          right_win_cnt += left_cnt * right_cnt;
      }
    }

    // 승리 회수가 같은 경우는 의미 없음
    if (left_win_cnt === right_win_cnt) continue;

    // res에 저장된 최대 승리 회수와 비교하면서 주사위 번호 조합을 갱신
    if (left_win_cnt < right_win_cnt) {
      if (res[0] < right_win_cnt) res = [right_win_cnt, game_set[right_idx][0]];
    } else {
      if (res[0] < left_win_cnt) res = [left_win_cnt, game_set[left_idx][0]];
    }
  }

  // res에 저장된 주사위 번호 조합 return
  return res[1];
}
