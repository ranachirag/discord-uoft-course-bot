import requests
from bs4 import BeautifulSoup

course = str(input())
URLy = "https://fas.calendar.utoronto.ca/course/" + course + "y1"
URLh = "https://fas.calendar.utoronto.ca/course/" + course + "h1"
pagey = requests.get(URLy)
pageh = requests.get(URLh)

soupy = BeautifulSoup(pagey.content, 'html.parser')
souph = BeautifulSoup(pageh.content, 'html.parser')

namey = soupy.find(id='page-title')
nameh = souph.find(id='page-title')
if nameh.text.strip() != "Sorry, this course is not in the current Calendar.":
    print(nameh.text.strip())
    info = souph.find_all("div", class_="field-items")
    labels = souph.find_all("div", class_="field-label")
elif namey.text.strip() != "Sorry, this course is not in the current Calendar.":
    print(namey.text.strip())
    info = soupy.find_all("div", class_="field-items")
    labels = soupy.find_all("div", class_="field-label")
else:
    info = []
    labels = []

text_info = []
text_labels = []
for thing in info:
    text_info.append(thing.text.strip())
for thing in labels:
    text_labels.append(thing.text.strip())

if info != []:
    description = text_info[1]
    exclu_i = 0
    exclu = ""
    prereq_i = text_labels.index("Prerequisite:")
    if "Exclusion:" in text_labels:
        exclu_i = text_labels.index("Exclusion:")
    breadth_i = text_labels.index("Breadth Requirements:")

    prereq = text_labels[prereq_i] + "\n" + text_info[prereq_i+1]
    if exclu_i != 0:
        exclu = text_labels[exclu_i] + "\n" + text_info[exclu_i+1]
    breadth = text_labels[breadth_i] + "\n" + text_info[breadth_i+1]

    print(description)
    print(prereq)
    if exclu_i != 0:
        print(exclu)
    print(breadth)
else:
    print("Course not found")

