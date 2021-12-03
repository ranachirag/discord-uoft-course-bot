import requests
import re
from bs4 import BeautifulSoup
from typing import List


def scrape(course: str) -> List[str]:
    out = []
    course = course.lower()
    utsg = re.compile(r'^\w{3}[1-4]\d{2}$')
    utsc = re.compile(r'^\w{3}[A-Da-d]\d{2}$')
    is_utsg = re.match(utsg, course)
    is_utsc = re.match(utsc, course)
    if is_utsg:
        urly = "https://fas.calendar.utoronto.ca/course/" + course + "y1"
        urlh = "https://fas.calendar.utoronto.ca/course/" + course + "h1"
    elif is_utsc:
        urly = "https://utsc.calendar.utoronto.ca/course/" + course + "y3"
        urlh = "https://utsc.calendar.utoronto.ca/course/" + course + "h3"
    else:
        out.append('Not a valid course')
        return out
    pagey = requests.get(urly)
    pageh = requests.get(urlh)

    soupy = BeautifulSoup(pagey.content, 'html.parser')
    souph = BeautifulSoup(pageh.content, 'html.parser')

    namey = soupy.find(class_='page-title')
    nameh = souph.find(class_='page-title')
    namey = namey.text.strip()
    nameh = nameh.text.strip()
    if nameh != "Sorry, this course is not in the current Calendar." and \
            nameh != "Sorry, this course has been retired and is no longer offered.":
        out.append(nameh)
        link = urlh
        info = []
        info.append(souph.find_all("div", class_="field--name-body")[3].text.strip())
        for thing in souph.find_all("div", class_="field--name-field-prerequisite"):
            find = thing.find(class_="field__item")
            find = find.text.strip()
            info.append(find)
        for thing in souph.find_all("div", class_="field--name-field-corequisite"):
            find = thing.find(class_="field__item")
            find = find.text.strip()
            info.append(find)
        for thing in souph.find_all("div", class_="field--name-field-exclusion"):
            find = thing.find(class_="field__item")
            find = find.text.strip()
            info.append(find)
        for thing in souph.find_all("div", class_="field--name-field-breadth-requirements"):
            find = thing.find(class_="field__item")
            find = find.text.strip()
            info.append(find)
        labels = souph.find_all("div", class_="field__label")
    elif namey != "Sorry, this course is not in the current Calendar." and \
            namey != "Sorry, this course has been retired and is no longer offered.":
        out.append(namey)
        link = urly
        info = soupy.find_all("div", class_="field__items")
        labels = soupy.find_all("div", class_="field__label")
    else:
        return []
    text_info = info
    text_labels = []
    for thing in labels:
        text_labels.append(thing.text.strip())
    if info == []:
        return[]

    if "Hours" in text_labels:
        text_labels.remove("Hours")
    description = text_info[0]
    out.append(description)
    if "Prerequisite" in text_labels:
        prereq_i = text_labels.index("Prerequisite")
        prereq = text_labels[prereq_i] + ": \n" + text_info[prereq_i + 1]
        out.append(prereq)
    else:
        out.append(None)
    if "Corequisite" in text_labels:
        coreq_i = text_labels.index("Corequisite")
        coreq = text_labels[coreq_i] + ": \n" + text_info[coreq_i + 1]
        out.append(coreq)
    else:
        out.append(None)

    if "Exclusion" in text_labels:
        exclu_i = text_labels.index("Exclusion")
        exclu = text_labels[exclu_i] + ": \n" + text_info[exclu_i + 1]
        out.append(exclu)
    else:
        out.append(None)

    if "Breadth Requirements" in text_labels:
        breadth_i = text_labels.index("Breadth Requirements")
        breadth = text_labels[breadth_i] + ": \n" + text_info[breadth_i]
        out.append(breadth)
    else:
        out.append(None)
    out.append(link)
    return out
