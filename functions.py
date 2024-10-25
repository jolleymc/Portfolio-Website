'''Michael Jolley - '''

import random
import matplotlib.pyplot as plt
import numpy as np
import statistics

class Student:
    def __init__(self):
        self.classAndGrade = {
            'Math': random.randint(0, 100),
            'Physics': random.randint(0, 100),
            'Recreation': random.randint(0, 100),
            'History': random.randint(0, 100),
            'English': random.randint(0, 100),
            'Chemistry': random.randint(0, 100)
        }

numStudents = random.randint(15, 25)

# version 1 of generate_grades - generates random grades for a random number of students
'''
def generate_grades(numStudents):
    students = [Student() for _ in range(numStudents)]
    return students
'''

# version 2 of generate_grades - generates grades from a file
def generate_grades(filename):
    students = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            grades = list(map(int, line.split(',')))
            student = Student()
            student.classAndGrade = {
                'Math': grades[0],
                'Physics': grades[1],
                'Recreation': grades[2],
                'History': grades[3],
                'English': grades[4],
                'Chemistry': grades[5]
            }
            students.append(student)
    return students

def plotGrades(grades):
    # Get the list of subjects
    subjects = list(grades[0].classAndGrade.keys())
    # Initialize a dictionary to store the total grades for each subject
    averages = {subject: 0 for subject in subjects}
    # For each student, add their grade for each subject to the total
    for student in grades:
        for subject in subjects:
            averages[subject] += student.classAndGrade[subject]
    # Calculate the average grade for each subject
    for subject in subjects:
        averages[subject] /= numStudents
    # Create a bar plot of the average grades for each subject
    fig, ax = plt.subplots()
    ax.bar(subjects, [averages[subject] for subject in subjects])
    ax.set_ylabel('Average Grade')
    ax.set_title('Average Grade by Subject')
    plt.show()

def calculateStatistics(grades):
    # Get the list of subjects
    subjects = list(grades[0].classAndGrade.keys())
    # Initialize a dictionary to store the statistics for each subject
    stats = {subject: [] for subject in subjects}
    # For each subject, calculate the statistics
    for subject in subjects:
        subject_grades = [student.classAndGrade[subject] for student in grades]
        stats[subject].append(max(subject_grades))  # Maximum
        stats[subject].append(min(subject_grades))  # Minimum
        stats[subject].append(sum(subject_grades) / len(grades))  # Average
        stats[subject].append(statistics.median(subject_grades))  # Median
        stats[subject].append(statistics.stdev(subject_grades))  # Standard deviation
    return stats

def plotStatistics(grades):
    # Calculate the statistics
    stats = calculateStatistics(grades)

    # Get the list of subjects
    subjects = list(stats.keys())

    # Create a bar plot for each statistic
    for subject in subjects:
        fig, ax = plt.subplots()
        ax.bar(['Max', 'Min', 'Avg', 'Median', 'StdDev'], stats[subject])
        ax.set_ylabel('Value')
        ax.set_title(f'Statistics for {subject}')
        plt.show()

def plotMathHistogram():
    # Generate grades for a random number of students
    grades = generate_grades(numStudents)

    # Get the Math grades for all students
    math_grades = [student.classAndGrade['Math'] for student in grades]

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(math_grades, bins=10)
    ax.set_xlabel('Math Grade')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Math Grades')
    plt.show()
