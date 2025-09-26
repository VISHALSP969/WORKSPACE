paragraph="""The sun rises in the east. 
The birds are singing. 
the river flows gently."""

# convert to lowercase to avoid case mismatch
words=paragraph.lower().split()

count=words.count("the")

print("The word 'the' appears",count,"times.")