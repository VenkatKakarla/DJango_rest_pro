# n=int(input('enter:'))
# s=int(n/2)+1
# l=[]
# for i in range(2,n+2):
#     if i%2==0:
#         l.append(' * '*(i))
#     else:
#         l.append(' * '*(i-1))
# a = int(len(l) / 2)
# for j in range(1,len(l)+1):
#     if j%2==0:
#         print((' '*(a-j))+l[j-1])
#     else:
#         print((' '*(a-j))+l[j-1])

n=int(input('enter:'))
k=n+3
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print()