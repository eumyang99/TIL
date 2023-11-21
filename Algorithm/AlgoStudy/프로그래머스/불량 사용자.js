// 굉장히 많은 공부가 됐던 문제

// 1. 정규표현식
// 드림코딩의 정규표현식 강의 수강

// 2. array의 복사
// arr.sort()는 원본 arr를 먼저 정렬하고 그 arr를 반환한다
// 따라서 원본 배열을 수정하기 때문에 얕은 복사를 위해서 sorted_arr = arr.slice().sort() 를 사용한다
// ECMA2023에서 이 불편함을 해소하기 위해 toSorted()라는 메소드를 추가한다
// sorted_arr = arr.toSorted()
// 이는 원본 배열을 수정하지 않고 정렬된 배열을 반환한다

// 3. set 사용
// JS set 역시 python의 set처럼 유니크한 값만 저장하기 때문에 중복 처리를 할 수 있다

// 발상
// 백트래킹 DFS 사용
// 하지만 user_id와 banned_id가 굉장히 많을 때, 시간 복잡도가 엄청날 것 같은데 이 풀이가 맞았다
// 조합이나 순열 공식을 사용해서 수학적으로 접근하는 것이 아닐까 했는데...
function similarity_check(banned, user) {
  let pattern = RegExp("^" + banned.replace(/\*/g, ".") + "$");
  return pattern.test(user);
}

function solution(user_id, banned_id) {
  var answer = 0;
  let able_set = new Set();

  let visited = Array(user_id.length).fill(0);
  const DFS = (banned_idx, temp_arr, cnt) => {
    if (cnt === banned_id.length) {
      let sorted_str = temp_arr.slice().sort().join(" ");
      able_set.add(sorted_str);
      return;
    }

    for (let j = 0; j < user_id.length; j++) {
      if (
        visited[j] === 0 &&
        similarity_check(banned_id[banned_idx], user_id[j])
      ) {
        visited[j] = 1;
        temp_arr.push(j);
        DFS(banned_idx + 1, temp_arr, cnt + 1);
        visited[j] = 0;
        temp_arr.pop();
      }
    }
  };

  DFS(0, [], 0);
  answer = able_set.size;

  return answer;
}
