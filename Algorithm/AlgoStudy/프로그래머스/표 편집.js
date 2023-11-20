function solution(n, k, cmd) {
  let link_arr = Array(n);
  for (let i = 0; i < n; i++) {
    link_arr[i] = [i - 1, i + 1];
  }

  let location = k;
  let deleted_stack = [];

  for (let order of cmd) {
    // move
    if (1 < order.length) {
      let dir = order[0];
      let dist = parseInt(order.slice(2));
      // move down
      if (dir === "D") {
        while (0 < dist) {
          if (link_arr[location][1] === n) {
            location = link_arr[location][0];
            break;
          }
          location = link_arr[location][1];
          dist--;
        }
      }

      // move up
      if (dir === "U") {
        while (0 < dist) {
          if (link_arr[location][0] === -1) {
            location = link_arr[location][1];
            break;
          }
          location = link_arr[location][0];
          dist--;
        }
      }
      continue;
    }

    // delete
    if (order === "C") {
      deleted_stack.push(location);
      let [up_idx, down_idx] = link_arr[location];
      if (down_idx !== n) {
        link_arr[down_idx][0] = up_idx;
      }
      if (up_idx !== -1) {
        link_arr[up_idx][1] = down_idx;
      }

      if (down_idx === n) {
        location = up_idx;
      } else {
        location = down_idx;
      }
      continue;
    }

    // reset
    if (order === "Z" && deleted_stack) {
      reset_idx = deleted_stack.pop();
      let [up_idx, down_idx] = link_arr[reset_idx];
      if (down_idx !== n) {
        link_arr[down_idx][0] = reset_idx;
      }
      if (up_idx !== -1) {
        link_arr[up_idx][1] = reset_idx;
      }
    }
  }

  answer = Array(n).fill("O");
  while (0 < deleted_stack.length) {
    answer[deleted_stack.pop()] = "X";
  }
  return answer.join("");
}
