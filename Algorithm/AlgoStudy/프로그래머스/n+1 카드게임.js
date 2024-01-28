// 발상
// 각 라운드에서 손에 있는 카드와 짝이 맞는 카드가 있으면 무조건 구매
// 라운드를 넘길 때 짝이 맞는 카드가 손에 없으면
// 지나쳤던 라운드들에서 짝이 맞는 카드 조합을 구매(필요할 때 나중에 구매함)
// 이를 위해 손 밖에 있는 카드들의 짝도 카운팅해 나감

function solution(coin, cards) {
  let answer = 1;
  const n = cards.length;

  let inHandSet = new Set(); // 짝을 기다리는 손 안의 카드
  let notInHandSet = new Set(); // 짝을 기다리는 손 밖의 카드
  let inHandChance = 0; // 손 안의 짝이 맞는 카드 조합 수
  let notInHandChance = 0; // 손 밖의 짝이 맞는 카드 조합 수

  // 처음 n / 3개 카드를 inHandSet에 담으면서 inHandChance 카운팅
  for (let i = 0; i < n / 3; i++) {
    // 손에 들어온 카드 num
    // 그 카드의 짝 카드 counterNum
    let [num, counterNum] = [cards[i], n + 1 - cards[i]];
    // 만약 손에 counterNum이 있으면 짝이 맞으니
    if (inHandSet.has(counterNum)) {
      // 손 안에서 counterNum을 제거하고
      inHandSet.delete(counterNum);
      // inHandChance 증가
      inHandChance++;

      // 손 안에 counterNum이 없으면
    } else {
      // inHandSet에 추가
      inHandSet.add(num);
    }
  }

  // inHandSet과 notInHandSet으로 분배하는 함수
  const distributeNum = (num) => {
    const counterNum = n + 1 - num;
    // inHandSet에 counterNum이 있으면 무조건 구매
    if (0 < coin && inHandSet.has(counterNum)) {
      inHandSet.delete(counterNum);
      inHandChance++;
      // 코인 1개 사용
      coin--;
      return;
    }

    // notInHandSet에 counterNum이 있으면
    if (notInHandSet.has(counterNum)) {
      notInHandSet.delete(counterNum);
      // notInHandChance 증가
      notInHandChance++;
      return;
    }

    // 위 경우 둘 다 아니면 notInHandSet에 추가
    notInHandSet.add(num);
  };

  let startIdx = n / 3;
  // 모든 라운드를 순회
  while (startIdx <= n - 2) {
    let [num1, num2] = [cards[startIdx], cards[startIdx + 1]];
    distributeNum(num1);
    distributeNum(num2);

    // inHandChance가 있으면
    if (0 < inHandChance) {
      // inHandChance 소비하고
      inHandChance--;
      // answer 증가
      answer++;
      // startIdx 조정
      startIdx += 2;
      continue;
    }

    // notInHandChance가 있으면서 coin이 2개 이상일 때
    if (2 <= coin && 0 < notInHandChance) {
      // notInHandChance 소비하고
      notInHandChance--;
      // 코인 2개 사용
      coin -= 2;
      // answer 증가
      answer++;
      // startIdx 조정
      startIdx += 2;
      continue;
    }

    // 위 두 경우에서 continue 되지 않았다면 라운드 종료
    break;
  }

  return answer;
}
