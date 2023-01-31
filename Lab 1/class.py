class Course:
    def __init__(self, department, number, name, credits, days, start, end, average):
        self.department = department 
        self.number = number
        self.name = name
        self.credits = credits
        self.days = days
        self.start = start
        self.end = end 
        self.average = average 
 
def parse_classes(file_name):
    courses = [] # list of courses
    with open(file_name, 'r') as f: 
        num_courses = int(f.readline().strip()) # read number of courses
        for i in range(num_courses): # for each course add all the information to the list
            department = f.readline().strip()
            number = f.readline().strip() 
            name = f.readline().strip() 
            credits = int(f.readline().strip()) 
            days = f.readline().strip()
            start = f.readline().strip() 
            end = f.readline().strip()
            average = int(f.readline().strip())
            courses.append(Course(department, number, name, credits, days, start, end, average))
    return courses # return list of courses

def format_classes(courses): # this is to format the courses in a nice way
    formatted = [] 
    for i, course in enumerate(courses):
        formatted.append("COURSE {}: {}{}: {}\nNumber of Credits: {}\nDays of Lectures: {}\nLecture Time: {} - {}\nStat: on average, students get {}% in this course\n".format(
            i+1, course.department, course.number, course.name, course.credits, course.days, course.start, course.end, course.average
        )) 
    return formatted 


input_file = "classesInput.txt" # input file name
output_file = "classesOutput.txt" # output file name
courses = parse_classes(input_file) # parse classes
formatted_classes = format_classes(courses) # format classes
with open(output_file, 'w') as f: # write to output file
    for course in formatted_classes:
        f.write(course)

