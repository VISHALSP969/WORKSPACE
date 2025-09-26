text="Programming is fun"

vowels="aeiouAEIOU"

for i in vowels:
    text=text.replace(i,"*")

print("After replacing vowels :",text)