// 발상
// inorder / postorder를 통해 루트 노드부터 하위 레벨의 노드 값을 차례대로 알아낼 수 있다
// 이진트리이기 때문에 부모 노드로부터 왼쪽, 오른쪽으로 하위 트리가 나뉜다

// 하나의 이진트리가 주어졌을 때,
// postorder의 마지막 값은 루트 노드가 되고
// inorder에서는 그 루트 노드를 기준으로 왼쪽 그룹은 왼쪽 하위 트리, 오른쪽 그룹은 오른쪽 하위 트리 구성 요소이다
// 따라서 루트 노드를 찾고 하위 왼쪽 트리, 하위 오른쪽 트리로 나누어서 다시 각각의 하위 트리의 루트 노드를 찾아간다

// preorder 의 경우,
// 루트 노드를 탐색한 후에 하위 노드의 왼쪽 트리를 먼저 탐색하고
// 왼쪽 트리의 탐색을 완료한 후 오른쪽 트리를 탐색한다
// 따라서 스택 구조를 활용하여 루트 노드를 탐색 후, 스택에 순서대로 오른쪽 트리, 왼쪽 트리를 넣어서 각 트리의 루트 노드를 기록한다
// 이 과정이 완료되면 preorder의 순서를 알 수 있다

// EX)
// 아래와 같은 트리가 있을 때,
////     a
////   b | c
//// d e | f g
// a를 탐색 후, 스택에 순서대로 c와 b를 넣는다
// b를 탐색 후, 스택에 순서대로 e와 d를 넣는다
// 루트 노드의 하위 왼쪽 트리가 모두 탐색되면 하위 오른쪽 트리를 탐색하기 시작한다

function solution(n, in_order, post_order) {
  let res = [];
  // inorder에서 특정 값의 idx를 저장하는 Array
  let in_order_map = [];
  for (let i = 0; i < n; i++) {
    in_order_map[in_order[i]] = i;
  }

  // 스택에는 트리의 정보를 담는다
  // 각 트리의 [preorder 시작 idx, preorder 끝 idx, inorder 시작 idx, inorder 끝 idx]
  let stack = [[0, n - 1, 0, n - 1]];
  while (stack.length !== 0) {
    let [post_first_idx, post_last_idx, in_first_idx, in_last_idx] =
      stack.pop();

    // base case
    if (post_last_idx < post_first_idx) continue;

    // postorder의 마지막 값 = 트리의 루트 노드
    let node_value = post_order[post_last_idx];
    // res에 추가
    res.push(node_value);

    // 다음 2개의 하위 트리 대한 정보
    // 루트 노드의 값이 inorder의 몇번째 idx에 있는지 확인
    let in_idx = in_order_map[node_value];

    // 하위 왼쪽 트리의 크기
    let left_tree_size = in_idx - in_first_idx;
    // 하위 오른쪽 트리의 크기
    let right_tree_size = in_last_idx - in_idx;

    // 하위 왼쪽 트리의 inorder 끝 idx
    let new_left_tree_in_last_idx = in_idx - 1;
    // 하위 오른쪽 트리의 inorder 시작 idx
    let new_right_tree_first_in_idx = in_idx + 1;

    // 하위 왼쪽 트리의 postorder 끝 idx
    let new_left_tree_post_last_idx = post_first_idx + left_tree_size - 1;
    // 하위 오른쪽 트리의 postorder 시작 idx
    let new_right_tree_post_first_idx = post_last_idx - right_tree_size;

    // 순서대로 오른쪽 트리, 왼쪽 트리를 stack에 추가
    stack.push([
      new_right_tree_post_first_idx, // 오른쪽 트리가 없으면 이 값은 post_last_idx
      post_last_idx - 1, // 이 경우 시작 값이 끝 값보다 커짐 => base case
      new_right_tree_first_in_idx,
      in_last_idx,
    ]);
    stack.push([
      post_first_idx,
      new_left_tree_post_last_idx, // 왼쪽 트리가 없으면 시작 값이 끝 값보다 커짐 => base case
      in_first_idx,
      new_left_tree_in_last_idx,
    ]);
  }

  // res 출력
  return res.join(" ");
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
    let n = parseInt(input[0]);
    let in_order = input[1].split(" ").map(Number);
    let post_order = input[2].split(" ").map(Number);
    console.log(solution(n, in_order, post_order));
    process.exit();
  });
