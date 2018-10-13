from subprocess import Popen, PIPE, STDOUT
import os
from humanAggregator import *
from rottenHuman import *

def parse_human(request_id, name):

    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\name" + str(request_id) + ".json")
    except:
        print('No such file1')
    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\names" + str(request_id) + ".txt")
    except:
        print('No such file2')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Human\\name" + str(request_id) + ".json")
    except:
        print('No such file3')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\names" + str(request_id) + ".txt")
    except:
        print('No such file4')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\humanAwards" + str(request_id) + ".json")
    except:
        print('No such file5')
    try:
        os.remove("C:\\Users\\shym9\\Desktop\\tutorial\\humanAwards" + str(request_id) + ".json")
    except:
        print('No such file6')

    command = "scrapy crawl human -o name" + str(request_id) + ".json -a request_id=" + str(request_id) + " -a name=" + str(name)
    currentPath = 'C:\\Users\\shym9\\Desktop\\tutorial'
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
    output, errors = p.communicate()
    os.rename(currentPath + "\\name" + str(request_id) + ".json", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Human\\name" + str(request_id) + ".json")
    os.rename(currentPath + "\\names" + str(request_id) + ".txt", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\names" + str(request_id) + ".txt")

    try:
        scrapH(request_id)
        os.rename("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\h" + str(request_id) + ".json",
                "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\rotten\\Human\\" + 'h' + str(request_id) + '.json')
    except:
        print('Error')

    human_agregation(request_id)

    command = "scrapy crawl hAwards -o humanAwards" + str(request_id) + ".json -a request_id=" + str(request_id)
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
    output, errors = p.communicate()
    os.rename(currentPath + "\\humanAwards" + str(request_id) + ".json", "C:\\Users\\shym9\\PycharmProjects\\MovieProj\\humanAwards" + str(request_id) + ".json")

    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\names" + str(request_id) + ".txt")
    except:
        print('No such file')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\rotten\\Human\\h" + str(request_id) + ".json")
    except:
        print('No such file')
    try:
        os.remove("C:\\Users\\shym9\\PycharmProjects\\MovieProj\\other\\Human\\name" + str(request_id) + ".json")
    except:
        print('No such file')
    try:
        os.remove(currentPath + "\\names_links" + str(request_id) + ".txt")
    except:
        print('No such file')
