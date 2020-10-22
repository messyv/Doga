#429
def disp_data():
    for items in datas:
        print(items,end=" ")
    print()

num_1 = float(input("Szám:"))
num_2 = float(input("Szám:"))
num_3 = float(input("Szám:"))
num_4 = float(input("Szám:"))

datas = [num_1, num_2, num_3, num_4]
print('before',end =" ")
disp_data()
n = len(datas)-1

for i in range(0,n):
    for j in range(0,n-i):
        if (datas[j]>datas[j+1]) :
            datas[j],datas[j+1]=datas[j+1],datas[j]

print("after",end=" ")
disp_data()
