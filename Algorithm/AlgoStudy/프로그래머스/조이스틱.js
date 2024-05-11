// 각 문자를 바꿀 때의 최소 비용들을 모두 누적 = 상하 움직임
// 조작할 문자의 위치 이동 계산 = 좌우 움직임

// 상하 움직임 계산
// 모든 문자에 대해
// 위로 조작하는 것과 아래로 조작하는 것 중 빠른 방향 선택 후 이동 횟수 누적
const A_num = "A".charCodeAt();
function upDownCnt(name) {
  let accu = 0;
  for (let char of name) {
    const char_num = char.charCodeAt();
    accu += Math.min(char_num - A_num, A_num + 26 - char_num);
  }
  return accu;
}

// 좌우 움직임 계산 -> "A"를 최대한 거치지 않는 방법
// 문자열을 2개 연결함
// 좌우 파트의 기준 문자 -> 두번째 문자열의 첫 문자 -> ABCDE"A"BCDE
// 시작 문자는 두번째 문자열의 첫 문자 -> ABCDE"A"BCDE
// 해당 문자부터 첫번째 문자열의 둘째 문자까지 순회 -> A"B"CDEABCDE
// abcde "ABCDE"
// abcd "EABCD" e
// abc "DEABC" de
// ab "CDEAB" cde
// a "BCDEA" bcde
// 탐색할 대문자에서 기준 문자 "A"의 오른쪽 끝부터 기준 문자 전까지 "A"가 등장하기 전까지의 문자 개수 카운팅
// 반대로 기준 문자 "A"의 왼쪽 끝부터 기준 문자 전까지 "A"가 등장하기 전까지의 문자 개수 카운팅
// 이후 왼쪽과 오른쪽 중 (적은 문자 개수 * 2 + 많은 문자 개수)를 계산
// 왕복해야 하는 구간이 있을 수 있기 때문에 보다 적은 문자를 가진 쪽을 왕복해서 움직임을 줄임
function leftRightCnt(name) {
  const doubleName = name + name;
  const nameLength = name.length;
  let minMove = nameLength - 1;

  for (let i = nameLength; 0 < i; i--) {
    let [l_part, r_part] = [nameLength - i, i - 1];
    for (let l = i; l < nameLength; l++) {
      if (doubleName[l] !== "A") break;
      l_part--;
    }
    for (let r = i + nameLength - 1; nameLength < r; r--) {
      if (doubleName[r] !== "A") break;
      r_part--;
    }
    const minTemp = Math.min(l_part, r_part) * 2 + Math.max(l_part, r_part);
    if (minTemp < minMove) minMove = minTemp;
  }
  return minMove;
}

function solution(name) {
  let answer = 0;
  // 상하 움직임 추가
  answer += upDownCnt(name);
  // 좌우 움직임 추가
  answer += leftRightCnt(name);
  return answer;
}
