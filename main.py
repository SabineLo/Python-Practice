from bs4 import BeautifulSoup

#allows me to open a file and read the content of that specific file
with open('practice.html', 'r') as html_file:
    content = html_file.read()
    #this prints out the practice.html file
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    #makes it look nicer
    #print(soup.prettify())
    #find only one specifc instance and find_all all of the instances
   
    courses_cards = soup.find_all('div', class_='card')
    #print(courses_html_tags)
    #for course in courses_html_tags:
     #   print(course.text)
    for course in courses_cards:
       course_name = course.h5.text
       course_price = course.a.text.split()[-1]
       print(f'{course_name} costs {course_price}')
       
