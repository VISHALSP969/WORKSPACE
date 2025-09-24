# Finding total and average of 3 marks entered
subject1,subject2,subject3=map(int,input("Enter marks of 3 subjects :").split())
total=subject1+subject2+subject3
print("Total marks =",total)
print("Average =",total/3)