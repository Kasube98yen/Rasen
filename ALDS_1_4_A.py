def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    c = 0

    for k in T:
        if k in S:
            c += 1
    print(c)

if __name__ == "__main__":
    main()
    