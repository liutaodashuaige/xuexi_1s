n=int(input('输入程序数量：'))
MAX=[[] for i in range(3)]
Allocation=[[] for i in range(3)]
Need=[[] for i in range(3)]
for i in range(n):
    for j in range(3):
        print('输入第%d项资源最大值，已分配值'%(j+1))
        MAX[i].append(int(input()))
        Allocation[i].append(int(input()))
        Need[i][j]=MAX[i][j]-Allocation[i][j]

print(Need)