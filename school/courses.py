def view_courses(courses_data: list):
    """
    Displays a list of available courses with details such as course name, duration, 
    and instructor.

    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', and 'duration'.
    """

    print("\nAvailable Courses:")
    for kurs in range(len(courses_data)):
        print(f"{kurs + 1}. {courses_data[kurs]['course_name']} (Duration: {courses_data[kurs]["duration"]}, Instructor: {courses_data[kurs]["instructor"]})")