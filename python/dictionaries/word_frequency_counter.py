text=input("Enter a sentence:\n")

words=text.split()
freq={}

for w in words:
    freq[w]=freq.get(w,0)+1

print("\nWord frequencies:")
for word,count in freq.items():
    print(f"{word!r} : {count}")