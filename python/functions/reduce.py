from functools import reduce
import operator

nums=[1,2,3,4]

# sum using reduce
sum_result=reduce(lambda a,b:a+b,nums)
print(sum_result)

# product using reduce and operator.mul
prod=reduce(operator.mul,nums,1)
print(prod)

# find max
maxium=reduce(lambda a,b:a if a>b else b,nums)
print(maxium)

# build a concatenated string
words=["hello","world"]
concat=reduce(lambda a,b:a+" "+b,words)
print(concat)