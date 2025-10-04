import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 20, "Delhi"],
    ["Bob", 22, "Mumbai"],
    ["Charlie", 21, "Bangalore"]
]

with open("people.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(data)