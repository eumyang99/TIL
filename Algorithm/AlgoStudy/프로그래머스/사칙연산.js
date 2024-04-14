// top-down DP 사용

function solution(arr) {
  const opts = [];
  let init = 0;
  let first_m = arr.length;

  // 처음 "-"가 등장하기 전까지 나오는 숫자들을 더해서 저장
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "+") continue;
    if (arr[i] === "-") {
      first_m = i;
      break;
    }
    init += parseInt(arr[i]);
  }

  // "-"와 "-" 사이의 숫자들 처리
  // 앞의 "-"를 바로 뒤의 숫자에만 적용하고 다음 "-" 전까지의 숫자를 모두 더한 상황
  // ex) -3 + 5 + 2
  // 앞의 "-"를 다음 "-" 전까지의 모든 숫자들에 괄호를 적용한 상황
  // ex -(3 + 5 + 2)
  // 두 상황을 opts에 저장
  let temp = [0, 0];
  for (let i = first_m + 1; i < arr.length; i += 2) {
    if (arr[i - 1] === "+") {
      temp[0] += parseInt(arr[i]);
      temp[1] -= parseInt(arr[i]);
      continue;
    }
    if (arr[i - 1] === "-") {
      opts.push(temp);
      temp = [-parseInt(arr[i]), -parseInt(arr[i])];
      continue;
    }
  }
  opts.push(temp);
  if (opts.length === 1) return init;

  // 만약 opts = [[3, -5], [-2, -8] ...] 일 때,
  // [3, -5]에서 3을 선택했다면 [-2, -8]은 전체 합에서 "-"값을 가짐
  // [3, -5]에서 -5를 선택했다면 [-2, -8]은 앞의 "-"에 포함될 수도, 포함되지 않을 수도 있기 때문에
  // [-2, -8]이거나 [2, 8]의 값을 가질 수 있음
  const memo = Array.from({ length: opts.length }, (el) => Array(2).fill(0));
  function recur(start, is_neg) {
    // memo[현재단계][is_neg] 값이 있으면 해당 값 리턴
    if (memo[start][is_neg]) return memo[start][is_neg];

    // 마지막 단계일 때, 재귀로 연결하지 않고 is_neg에 따라 현재 단계의 최대값을 반환
    if (opts.length - 1 === start) {
      memo[start][is_neg] = is_neg
        ? Math.max(...opts[start])
        : Math.max(...opts[start], -opts[start][0], -opts[start][1]);
      return memo[start][is_neg];
    }
    // 현재 "-"가 담고 있는 값 = temp
    // = ["-"를 바로 뒷 숫자에만 적용한 값, "-"를 다음 "-" 이전까지의 모든 숫자에 적용한 값]
    const temp = [0, 0];
    // 이전 단계의 괄호에 포함되는 지, 몇 번째로 포함되는지에 따라 현재 값에 "-"를 붙여야 될 수도 있음
    // "-"를 붙여야 되는 상황은 is_neg로 판단

    // is_neg가 true이면 temp[0]에 opts[현재단계][0]을,
    // is_neg가 false이면 temp[0]에 (opts[현재단계][0], -opts[현재단계][0]) 중 큰 값을 더함
    // temp[1]의 경우도 마찬가지
    temp[0] += is_neg
      ? opts[start][0]
      : Math.max(opts[start][0], -opts[start][0]);
    temp[1] += is_neg
      ? opts[start][1]
      : Math.max(opts[start][1], -opts[start][1]);

    // temp[0]에 다음 단계의 값을 추가로 더함, 단 is_neg는 현재의 is_neg를 그대로 전달
    // temp[1]에 다음 단계의 값들 중 큰 값을 더함, temp[1]은 다음 단계에 is_neg를 전달할 수도, !is_neg를 전달할 수도 있음
    temp[0] += recur(start + 1, is_neg);
    temp[1] += Math.max(recur(start + 1, 0), recur(start + 1, 1));

    // memo[현재 단계][is_neg]에 temp 중 큰 값을 저장하고 리턴
    memo[start][is_neg] = Math.max(...temp);
    return memo[start][is_neg];
  }

  // 초기 "-"가 등장하기 전까지 더한 값과 이후 더해질 수 있는 최대값을 더한 뒤 리턴
  return init + recur(1, 1);
}
