// 이진탐색
// n은 최대 10억
// times Arr의 최대값도 10억

// 가능한 시간 범위 : 0 ~ (10억 * 10억)
// mid값에 해당하는 시간까지 심사관들이 처리할 수 있는 입국자들의 합을 기준으로
// left, right 값을 조정해감

// 단, 모든 입국자를 처리할 수 있는 최소값을 찾아야 하는 조건이 있음
// 따라서 모든 입국자를 처리할 수 있게 되는 가장 작은 값을 찾기 위해
// 처리 가능 입국자가 n보다 작으면 left = mid + 1
// 처리 가능 입국자가 n보다 크거나 같으면 right = mid

// 위 조건에 대한 추가 설명
// 처리 가능 입국자가 n보다 작으면 해당 mid 값은 무조건 불가능한 경우
// 따라서 보다 큰 범위를 찾기 위해 mid보다 큰 mid + 1 을 left로 설정

// 처리 가능 입국자가 n보다 크거나 같으면 해당 mid 값은 답이 될 수도 있는 경우
// 따라서 이를 배제하지 않고 right = mid로 설정

// 이진탐색 응용에 대한 사용 기준
// 1. 원하는 값 중 최소값을 찾아야 할 때
// 최소값을 찾는다는 것은 원하는 값보다 작은 경우를 배제해야 함
// 따라서
// mid값이 원하는 값보다 작은 경우, 이 mid값을 제외하기 위해 left = mid + 1
// mid값이 원하는 값보다 크거나 같은 경우, 이 mid값은 조건에 만족하는 최소값이 될 수도 있는 값이기 때문에
// 이 mid값을 제외하지 않기 위해 right = mid

// 2. 원하는 값 중 최대값을 찾아야 할 때
// 최대값을 찾는다는 것은 원하는 값보다 큰 경우를 배제해야 함
// 따라서
// mid값이 원하는 값보다 작은거나 같은 경우, 이 mid값은 조건에 만족하는 최대값이 될 수도 있는 값이기 때문에
// 이 mid값을 제외하지 않기 위해 left = mid
// mid값이 원하는 값보다 zms 경우, 이 mid값을 제외하기 위해 right = mid - 1

function solution(n, times) {
  let left = 0;
  let right = Math.max(...times) * n;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    let accu = 0;
    for (let time of times) {
      accu += Math.floor(mid / time);
    }

    if (accu < n) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}
