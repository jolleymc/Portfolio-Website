'''Michael Jolley and Cole Walther - PA 4 - 3/26/2024'''

from functions import generate_grades, plotGrades, calculateStatistics, plotStatistics, plotMathHistogram, numStudents

# Generate grades
grades = generate_grades(numStudents)

# Plot grades
plotGrades(grades)

# Calculate statistics
calculateStatistics(grades)

# Plot statistics
plotStatistics(grades)

# Plot math histogram
plotMathHistogram()
