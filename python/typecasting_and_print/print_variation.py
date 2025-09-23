print("a","b","c")
print("a","b","c",sep=" - ")    
print("No newline",end="")      # stay on same line
print("next")                   # continues on same line

# Write to a file
# with open("out.txt","w") as f:
#     print("Hello file",file=f)

# Force immediate output (useful in long-running scripts)
print("Progress...",flush=True)