function solution(sticker) {
  if (sticker.length < 3) return Math.max(...sticker);

  const dp_1 = [0, sticker[0], 0];
  const dp_2 = [0, 0, sticker[1]];

  for (let i = 2; i < sticker.length; i++) {
    dp_1.push(sticker[i] + Math.max(dp_1[i - 2], dp_1[i - 1]));
    dp_2.push(sticker[i] + Math.max(dp_2[i - 2], dp_2[i - 1]));
  }

  const max_dp_1 = Math.max(dp_1.at(-2), dp_1.at(-3));
  const max_dp_2 = Math.max(dp_2.at(-1), dp_2.at(-2));
  return Math.max(max_dp_1, max_dp_2);
}
