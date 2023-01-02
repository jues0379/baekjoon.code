abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']
S = input("")
cnt = 0

for i in abc:
    cnt = 0
    for j in S:
        if i == j:
            print(S.index(j), end=" ")
            cnt += 1
            break
    if cnt == 0:
        print("-1", end=" ")
