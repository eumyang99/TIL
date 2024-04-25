## 코드의 "#" 처리 방법
## 코드 string을 순회하면서 각 코드를 arr에 담는다.
## 코드 순회 중 "#"이 나오면 arr의 마지막 알파벳을 소문자로 바꾼다

## 파이썬은 string 포함을 검사할 때, in 으로 찾는 것이 효율적
## 따라서 음악 재생 시간동안 등장하는 모든 코드를 위와 같이 변형하고
## 검사할 코드 역시 변형 후 포함 여부를 확인한다

def new_code(code):
    arr = []
    for word in code:
        if word == "#":
            arr[-1] = chr(ord(arr[-1]) + 32)
        else:
            arr.append(word)
    return "".join(arr)

def solution(m, musicinfos):
    new_m = new_code(m)
    answer, music_long = '(None)', 0
    for info in musicinfos:
        s, e, t, c = info.split(",")
        new_c = new_code(c)
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        long = 60 * (eh - sh) + (em - sm)
        rep, remain = divmod(long, len(new_c))
        code = new_c * rep + new_c[:remain]
        if new_m not in code: continue
        if long <= music_long: continue
        answer = t
        music_long = long
        
    return answer