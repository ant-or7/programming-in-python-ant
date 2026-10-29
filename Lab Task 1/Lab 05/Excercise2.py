students = [
[201, "Amina", [78, 85, 90]],
[202, "Rahim", [65, 70, 68]],
[203, "Nadia", [92, 88, 95]],
[204, "Hasan", [55, 60, 65]],
[205, "Tania", [80, 80, 80]]
]
def calculateAverage(students,id): 
    for x in students:
        if x[0]==id:
            marks=x[2]
            return sum(marks)/len(x[2])
    return None    

print(calculateAverage(students,201))

def classifyPerformence(average):
    if average is None:
        print('Student not found')

    elif average>=80:
        print('Excellent')

    elif average>=70:
       print('Good')

    elif average>=60:
        print('Satisfactory')

    else:
        print('Needs Improvement')

    print('-----------------------')

classifyPerformence(calculateAverage(students,201))

def displayReports(students):
    for x in students:
        id=x[0]
        print(x)
        classifyPerformence(calculateAverage(students,id))
        

displayReports(students)