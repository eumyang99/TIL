// 발상
// 처음에 접근하기가 어려웠다
// 문제에 수학적인 제한이 있다는 것은 느껴졌는데 명확하게 구체화하지 못해서 모든 경우를 찾아보려 했었다
// 찾아낸 방법은 주어신 배열을 오름차순으로 정렬했을 때, 맨 마지막 숫자 3개만 target이 될 수 있다는 것이다
// 문제의 좋은 배열에서 다른 모든 원소의 합과 같은 원소는 해당 배열에서 가장 큰 숫자여야 한다
// 따라서 자기 자신보다 크거나 같은 숫자가 남아 있다면 불가능하다
// 마지막에서 4번째 원소는 자기 자신보다 크거나 같은 숫자가 3개이기 때문에 이 중 2개를 없애도 여전히 배열에서 가장 큰 숫자가 될 수 없다

// 초기 처리
// 동일한 가장 큰 숫자가 4개 이상인 경우 불가능하기 때문에 0을 출력

// 1) 타겟이 마지막 원소인 경우 (가장 복잡한 경우)
// 자기 자신보다 왼쪽에 있는 모든 숫자들 중 2개를 뽑아서 제거하는 경우를 찾아야 한다
// 해시맵을 사용하여 등장하는 숫자의 빈도를 저장한다
// 등장하는 숫자를 중복없이 배열에 저장한다
// 조건에 맞는 두 숫자의 빈도수를 서로 곱해서 res에 추가
// 두 숫자가 같은 숫자라면 nC2를 사용해서 res에 추가
// 투포인터를 사용해서 등장하는 숫자 배열을 탐색하고 해당 값으로 해시맵에서 값을 꺼내서 사용함

// 2) 타겟이 (마지막 - 1)원소인 경우
// 맨 마지막 원소를 무조건 제거하고 남는 값을 해시맵에서 찾아서 res에 추가

// 3) 타겟이 (마지막 - 2)원소인 경우
// 마지막 원소 + (마지막 - 1) 원소를 더했을 때 조건에 맞으면 res에 1 추가

function solution(n, arr) {
  let res = 0;
  let set = new Set(arr.slice(n - 4));
  if (set.size === 1) {
    return res;
  }

  let dic = {};
  let nums = [];
  for (let num of arr) {
    if (dic[num]) {
      dic[num]++;
      continue;
    }
    dic[num] = 1;
    nums.push(num);
  }

  const total = arr.reduce((accu, cur) => {
    return (accu += cur);
  }, 0);

  for (let i = 1; i < 4; i++) {
    let target_num = arr[n - i];
    dic[target_num]--;
    let searched_num = total - target_num * 2;
    if (i === 1) {
      let [left_idx, right_idx] = [0, nums.length - 1];
      while (left_idx <= right_idx) {
        let [left_num, right_num] = [nums[left_idx], nums[right_idx]];
        let both_sum = left_num + right_num;
        if (both_sum === searched_num) {
          if (left_idx !== right_idx) {
            res += dic[left_num] * dic[right_num];
          } else {
            res += (dic[left_num] * (dic[right_num] - 1)) / 2;
          }
          left_idx++;
          right_idx--;
          continue;
        }
        if (both_sum < searched_num) {
          left_idx++;
          continue;
        }
        if (both_sum > searched_num) {
          right_idx--;
          continue;
        }
      }
    }
    if (i === 2) {
      searched_num -= arr[n - 1];
      dic[arr[n - 1]]--;
      if (dic[searched_num]) {
        res += dic[searched_num];
      }
      dic[arr[n - 1]]++;
    }
    if (i === 3) {
      if (searched_num === arr[n - 1] + arr[n - 2]) {
        res += 1;
      }
    }
    dic[target_num]++;
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
    input.push(line);
  })
  .on("close", () => {
    const n = parseInt(input[0]);
    const arr = input[1]
      .split(" ")
      .map(Number)
      .sort((a, b) => a - b);
    console.log(solution(n, arr));
    process.exit();
  });
