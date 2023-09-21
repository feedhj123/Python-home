# 1 ,2 , 3, 4 , 5
count = 0
for i in range(1,101):
    if i % 7 == 0:
        print(i, end='\t')
        count += 1 
        if count % 5 == 0:
            print()
print()
print(count)
