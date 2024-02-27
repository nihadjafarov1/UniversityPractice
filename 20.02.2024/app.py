# diametr =  int(input("Enter diametr of round\n"))
# height = int(input("Enter height of door\n"))
# width = int(input("Enter width of door\n"))

# if(diametr <= min(height, width)):
#     print("Round can pass")
# else:
#     print("Round can not pass")

# numbers = []
# user_input = ''

# while True:
#     user_input = input("Eded daxil edin: ")

#     if(user_input) != 'q':
#         numbers.append(int(user_input))
#     else: 
#         break
# geometricMean = sum(numbers)/len(numbers)
# print(geometricMean)

students = []
points = []

while True:
    user_student_input = input("Enter student's name: ")

    if(user_student_input) == 'q':
        break
    else: 
        user_point_input = input("Eded daxil edin: ")
        students.append(user_student_input)
        points.append(int(user_point_input))
average = sum(points)/len(points)
print(average)

count = int(0)
for point in points:
    if point >= average:
        print(students[count])
    count += 1