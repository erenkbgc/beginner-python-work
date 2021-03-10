mt1=float(input("enter your mt1 grade:"))
mt2=float(input("enter your mt2 grade:"))
final=float(input("enter your final grade:"))
lecture_grade=(mt1*30/100+mt2*30/100+final*40/100)

if lecture_grade>30 and lecture_grade<50:
    print("Your grade is DD")
elif lecture_grade>50 and lecture_grade<65:
    print("Your grade is CC")
elif lecture_grade>65 and lecture_grade<85:
    print("Your grade is BB")
elif lecture_grade >= 85:
    print("Your grade is AA.Well done")
else:
    print("You have failed.Take this course again")