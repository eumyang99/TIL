// 발상
// 맨 마지막 줄을 제외한 모든 숫자에 대해
// 자기 바로 밑의 두 숫자 중 큰 숫자를 자신에게 더한다
// 이 과정을 triangle[-2]부터 triangle[0]까지 진행한다
// 그리고 triangle[0][0]을 리턴한다

function solution(triangle) {
  for (let i = triangle.length - 2; 0 <= i; i--) {
    for (let j = 0; j < triangle[i].length; j++) {
      triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
    }
  }
  return triangle[0][0];
}
