grade=input("Enter grade: ").strip().upper()

if grade[0]=="A":
  final_grade=4
elif grade[0]=="B":
  final_grade=3
elif grade[0]=="C":
  final_grade=2
elif grade[0]=="D":
  final_grade=1
elif grade[0]=="F":
  final_grade=0
else:
  print("Invalid input")

if grade[1]=="+":
  final_grade=final_grade+0.3
elif grade[1]=='-':
  final_grade=final_grade-0.3

print(final_grade)
