from collections import deque

def main():
    sche = input()
    V = deque()
    idx = deque()
    count_well = 0
    start_flag = -1

    for i, terrain in enumerate(sche)
        if terrain == "\\":
            idx.append(i)
        elif terrain == "/" and idx: # 対応する "\" がある場合
            j = idx.pop()
            v = j - i # 小面積
            V.append((j,v)) # こっからわからん



        

