k = input().split()
m,n = k[0], k[1]
m = int(m)
n = int(n)
matrix = []
for row in range(m):
    tmp = input().split()
    rows = []
    for t in tmp:
        rows.append(int(t))
    matrix.append(rows)

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            if matrix[i][j] == 1:
                print(2)
                exit(0)
print(4)
