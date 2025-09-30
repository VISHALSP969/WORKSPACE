# uppercase and filter short names
names=["anna","bob","christina","ed"]

upper_long=list(map(str.upper,filter(lambda s:len(s)>3,names)))
print(upper_long)