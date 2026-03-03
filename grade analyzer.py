def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages


def classify_grades(averages):
    classified = {}
    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    return classified


def generate_report(classified):
    print("Student Report")
    for name, (avg, grade) in classified.items():
        print(name, avg, grade)


students = {
    "Alice": [85, 90, 84],
    "Bob": [60, 65, 62]
}

averages = process_scores(students)
classified = classify_grades(averages)
generate_report(classified)