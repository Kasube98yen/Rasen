from collections import deque

def main():
    
    # input & initialize
    n, q = map(int, input().split())

    total_time = 0

    dname = deque()
    dtime = deque()

    for i in range(n):
        nametmp, timetmp = input().split()
        dname.append(nametmp)
        dtime.append(int(timetmp))
    
    while dname or dtime: # queueになにか入っていればTrue
        name = dname.popleft()
        time = dtime.popleft()
        if time <= q: # q以下だったら除外
            total_time += time
            print(name, total_time)
        else: # q以上だったらtime減らしてFIFOに戻す
            total_time += q
            time -= q
            dname.append(name)
            dtime.append(time)

if __name__ == "__main__":
    main()



