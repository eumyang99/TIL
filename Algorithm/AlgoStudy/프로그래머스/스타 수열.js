// 특정 숫자를 무조건 포함시켜 다른 수와 짝지었을 때, 가장 많은 짝을 지을 수 있는 횟수를 찾는 문제
// 단, 수열의 위치를 바꿀 수 없기 때문에 주어진 순서를 유지한 상태에서 짝지어야 함

// 풀이
// 각 숫자의 idx를 hashmap에 array로 저장
// 이후 각 array를 순회하면서 만들 수 있는 짝의 개수를 카운팅

// idxArr = [특정 숫자의 idx들]
// idxArr를 순회하면서 특정 숫자를 어떤 수와 짝지었을 때,
// 특정 숫자와 어떤 수의 idx 중 큰 값으로 현재 idxArr 요소를 갱신

// 짝지어진 숫자 중 가장 큰 idx(idxArr에서 이전에 순회한 요소의 갱신된 값)과
// 현재 짝지을 숫자의 idx - 1 값을 비교해서
// 전자가 더 작다면
// cnt++

// 전자와 후자가 같다면 이미 짝지어진 숫자이기 때문에 현재 숫자의 오른쪽 숫자와 짝지어야 함
// 현재 숫자와 오른쪽 숫자를 비교해서 둘이 같다면
// 현재 숫자는 짝지어질 수 없음(왼쪽 오른쪽 모두와 짝이 될 수 없기 때문)

// 현재 숫자와 오른쪽 숫자가 다르면
// cnt++ 이후 현재의 idxArr 값을 오른쪽 숫자의 idx값으로 갱신

function counting(idxArr, limit) {
  let cnt = 0;
  for (let i = 1; i < idxArr.length; i++) {
    if (idxArr[i - 1] < idxArr[i] - 1) {
      cnt++;
      continue;
    }
    if (limit <= idxArr[i] + 1) break;
    if (idxArr[i - 1] === idxArr[i] - 1) {
      if (idxArr[i] + 1 === idxArr[i + 1]) continue;
      cnt++;
      idxArr[i] = idxArr[i] + 1;
    }
  }
  return cnt;
}

function solution(a) {
  let answer = 0;
  const map = new Object();
  for (let i = 0; i < a.length; i++) {
    map[a[i]] ? map[a[i]].push(i) : (map[a[i]] = [-1, i]);
  }
  for (let idxArr of Object.values(map)) {
    answer = Math.max(answer, counting(idxArr, a.length));
  }
  return answer * 2;
}
