N=int(input(""))

in_contar=0
out_contar=0
for _ in range(N):
    X = int(input())
    if 10 <= X <= 20:
        in_contar +=1
    else:
        out_contar +=1
print(f"{in_contar} in")
print(f"{out_contar} out")