text=input("Enter a sentence : ")

# clean and split the sentence into words
words=text.strip().split()

# count total words
print("Total words :",len(words))

# count the frequency of each word
print("\nWord frequencies :")
for word in set(words):
    print(word,":",words.count(word))