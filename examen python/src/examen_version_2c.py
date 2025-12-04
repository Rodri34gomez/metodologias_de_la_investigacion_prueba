# problema rescate 
f = [0, 1]
n = int(input("give your numbers: "))
 
for _ in range(n-2):
    f.append(f[-1] + f[-2])

for num in f[:n]:
    print(num)