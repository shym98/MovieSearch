from subprocess import Popen, PIPE, STDOUT
import os
from movieAggregator import *
from rottenTitles import *

def parse_titles(request_id, title, genre, start_year, end_year):

    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\title" + str(request_id) + ".json")
    except:
        print('No such file1')
    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\titles" + str(request_id) + ".txt")
    except:
        print('No such file2')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Title\\title" + str(request_id) + ".json")
    except:
        print('No such file3')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\titles" + str(request_id) + ".txt")
    except:
        print('No such file4')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\titlesAwards" + str(request_id) + ".json")
    except:
        print('No such file5')
    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\titlesAwards" + str(request_id) + ".json")
    except:
        print('No such file6')

    command = "scrapy crawl title -o title" + str(request_id) + ".json -a request_id=" + str(request_id) + " -a title=" + str(title) + " -a genre=" + str(genre) + " -a sYear=" + str(start_year) + " -a eYear=" + str(end_year)
    currentPath = 'C:\\Users\\shym9\\Desktop\\tutorial'
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
    output, errors = p.communicate()
    os.rename(currentPath + "\\title" + str(request_id) + ".json", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Title\\title" + str(request_id) + ".json")
    os.rename(currentPath + "\\titles" + str(request_id) + ".txt", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\titles" + str(request_id) + ".txt")

    try:
        scap(request_id)
        os.rename("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\r" + str(request_id) + ".json",
                "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\rotten\\Title\\" + 'r' + str(request_id) + '.json')
    except:
        print('Error')

    movie_agragation(request_id)

    command = "scrapy crawl tAwards -o titlesAwards" + str(request_id) + ".json -a request_id=" + str(request_id)
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
    output, errors = p.communicate()
    os.rename(currentPath + "\\titlesAwards" + str(request_id) + ".json", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\titlesAwards" + str(request_id) + ".json")

    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\titles" + str(request_id) + ".txt")
    except:
        print('No such file')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\rotten\\Title\\r" + str(request_id) + ".json")
    except:
        print('No such file')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Title\\title" + str(request_id) + ".json")
    except:
        print('No such file')
    try:
        os.remove(currentPath + "\\titles_links" + str(request_id) + ".txt")
    except:
        print('No such file')
