# skip muliples if 3&5 between 1 and 100 
for i in range(1,100):
    if i%3==0 and i%5==0:
        continue
    print(i)