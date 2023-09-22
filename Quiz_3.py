student_credit = [90, 45, 64, 9 ,17, 29]
results=[]
for a in student_credit :
    if a >= 71 :
        print("A")
        results.append("A")
    elif a >= 41 :
        print("B")
        results.append("B")
    elif a >= 11 :
        print("C")
        results.append("C")
    else :
        print("D")
        results.append("D")

print(results)
