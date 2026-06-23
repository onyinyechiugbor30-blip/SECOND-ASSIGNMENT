'''QUESTION 3 — Student Performance Ranking System
Topics: Functions · Lists · Nested Loops · If statements

Create these functions:
calculate_average(scores_list)` — returns average of a list of scores.
get_grade(average)` — returns letter grade + remark using if-elif.
rank_students(student_data)` — where `student_data` is a list of tuples `(name, [score1, score2, score3, score4])`.

The ranking function should:
Calculate average and grade for each student.
Sort students by average (descending) using nested loops (no built-in sort).
Print a ranked table with position, name, average, and grade.'''
# Function to calculate the average score of a student
def calculate_average(scores_list):
    # Variable to store the total of all scores
    total = 0
    # Go through each score in the list
    for score in scores_list:
        # Add the current score to the total
        total += score
    # Divide the total score by the number of scores
    average = total / len(scores_list)
    # Send the average back to wherever the function was called
    return average
# Function to determine a student's grade and remark
def get_grade(average):
    # Check if the average is 70 or above
    if average >= 70:
        return "A - Excellent"
    # Check if the average is between 60 and 69
    elif average >= 60:
        return "B - Very Good"
    # Check if the average is between 50 and 59
    elif average >= 50:
        return "C - Good"
    # Check if the average is between 40 and 49
    elif average >= 40:
        return "D - Fair"
    # Any score below 40 gets an F
    else:
        return "F - Fail"

# Function to calculate averages, assign grades,rank students, and display the final table
def rank_students(student_data):
    # create Empty list to store each student's result
    results = []
    # Go through every student in the student_data list
    for student in student_data:
        # Get the student's name
        name = student[0]
        # Get the student's list of scores
        scores = student[1]
        # Calculate the student's average score
        average = calculate_average(scores)
        # Determine the student's grade and remark
        grade = get_grade(average)
        # Store the student's details in a new list
        # Format: [name, average, grade] append is used to add items to list
        results.append([name, average, grade])

    # Sort students from highest average to lowest average using nested loops 
    # Outer loop selects one student at a time
    for i in range(len(results)):
        # Inner loop compares the selected student with all students after it
        for j in range(i + 1, len(results)):
          # Compare their averages
            if results[j][1] > results[i][1]:
                # If student j has a higher average,swap their positions
                temp = results[i]
                results[i] = results[j]
                results[j] = temp
    
    # DISPLAY RESULT SECTION
    # Print table heading
    print("STUDENT PERFORMANCE RANKING")
    print("-" * 60)
    # Print column titles
    print("Pos\tName\t\tAverage\t\tGrade")
    print("-" * 60)
    # Position starts from 1
    position = 1
    # Go through the sorted results list
    for student in results:
        # Display position, name, average and grade
        print(
            position,
            "\t",
            student[0],
            "\t",
            round(student[1], 2),
            "\t\t",
            student[2])
      # Increase position for the next student
        position += 1
# STUDENT DATA
# Each student is stored as:
# (Name, [Score1, Score2, Score3, Score4])
students = [
    ("Ebere", [80, 75, 90, 85]),
    ("Austin", [65, 70, 60, 68]),
    ("Chisom", [95, 92, 90, 94]),
    ("Wisdom", [50, 55, 60, 58]),
    ("Sarah", [72, 74, 70, 76])
]
# Run the ranking system
rank_students(students)