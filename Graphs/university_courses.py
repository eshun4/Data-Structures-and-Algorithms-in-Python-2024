# Define the graph using dictionary representation
university_courses = {
    'Math': set(['Physics', 'Computer Science']),
    'Physics': set(['Math', 'Chemistry']),
    'Chemistry': set(['Physics']),
    'Computer Science': set(['Math']),
}

def DFS(courses, start_course, passed_courses):
    """
    Function implementing the DFS algorithm to traverse the graph.
    """
    if start_course in passed_courses: # Check if the course was taken earlier
        return

    passed_courses.add(start_course) # Add the course to the set of passed courses
    print(start_course, end=' --> ')

    # TODO: Code the recursive call inside the DFS function
    for neibouring_course in courses[start_course]:
        if neibouring_course not in passed_courses:
            DFS(courses, neibouring_course, passed_courses)

passed_courses = set()
# Call the DFS function, start the traversal with 'Math'
DFS(university_courses, 'Math', passed_courses) 