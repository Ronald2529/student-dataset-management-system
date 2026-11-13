import numpy as np

students = np.array([
    [1001, 21, 85, 78, 90, 88],
    [1002, 22, 75, 82, 80, 85],
    [1003, 20, 90, 88, 92, 95],
    [1004, 21, 65, 70, 75, 72],
    [1005, 23, 88, 85, 80, 90],
    [1006, 20, 78, 75, 82, 80],
    [1007, 22, 92, 90, 88, 94],
    [1008, 21, 70, 68, 75, 78],
    [1009, 19, 82, 85, 80, 87],
    [1010, 22, 95, 92, 90, 96],
    [1011, 21, 80, 78, 85, 82],
    [1012, 20, 72, 75, 70, 78],
    [1013, 23, 88, 90, 85, 92],
    [1014, 22, 68, 72, 75, 70],
    [1015, 19, 91, 89, 94, 93],
    [1016, 21, 76, 80, 78, 85],
    [1017, 20, 84, 82, 88, 86],
    [1018, 23, 93, 95, 90, 98],
    [1019, 22, 74, 70, 78, 76],
    [1020, 21, 86, 88, 84, 90]
])

print("Student Dataset:")
print(students)

print("\nDataset Properties")

print(students.shape)
print(students.ndim)
print(students.size)
print(students.dtype)



#Compare Python Lists vs NumPy Arrays.

marks_list=[20,30,40,50,60]

result=[]

for mark in marks_list :
    result.append(mark + 10 )

print(result)

marks_array=np.array([20,30,40,50,60])

result= marks_array + 10

print("NumPy Array :", result)



#Convert the dataset into a 3D array representing two classrooms.

classroom = students.reshape(2,10,6)

print("Classroom Dataset:")
print(classroom)

print("Shape:", classroom.shape)
print("Dimentions:", classroom.ndim)
print("Size:", classroom.size)



