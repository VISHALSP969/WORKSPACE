sub1,sub2,sub3=input("Enter marksof 3 subjects : ").split()
with open("marks.txt","w") as file:
    file.write(str(sub1)+"\n")
    file.write(str(sub2)+"\n")
    file.write(str(sub3)+"\n")

with open("marks.txt","r") as file:
    m1,m2,m3=file.read().split()

avg=(int(m1)+int(m2)+int(m3))/3
print("Average :",avg)
