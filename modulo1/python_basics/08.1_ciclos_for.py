ventas = [120,80,200,50,300]
print("Ventas Diarias")

total = 0
for n in ventas:
    if(n > 100):
        total = total + n
        print(n)
        if (n > 250):
            total = total + 30
        else:
            total = total + 10

print(total)