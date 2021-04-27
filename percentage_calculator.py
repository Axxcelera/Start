print('\t \t ------Percentage Caculator--------')
eng = float(input("Enter marks obtained in English : "))
hin = float(input("Enter marks obtained in Hindi : "))
mat = float(input("Enter marks obtained in Maths : "))
sci = float(input("Enter marks obtained in Science : "))
sst = float(input("Enter marks obtained in S.st : "))
Total_marks = 500
obtained_marks = eng + hin + mat + sci + sst
percentage = (obtained_marks/Total_marks) * 100
print(f" Total Percentage obtained by the student is {percentage}")
