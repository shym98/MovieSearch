import json

class Human:

    def __init__(self):
        self.data = {}

    def addRotten(self, rottenData, find):
        self.data['rottenLink'] = rottenData['rottenLink']
        self.data['highestRating'] = rottenData['highestRating']
        self.data['lowestRating'] = rottenData['lowestRating']
        self.data['bio'] = rottenData['bio']
        if not find:
            self.data['birthday'] = rottenData['birthday']
            self.data['photo'] = rottenData['photo']
            self.data['name'] = rottenData['name']

    def addImdb(self, imdbData):
        self.data['name'] = imdbData['name']
        self.data['born'] = imdbData['born']
        self.data['died'] = imdbData['died']
        self.data['imdbLink'] = imdbData['imdbLink']
        self.data['proffesions'] = imdbData['proffesions']
        self.data['filmography'] = imdbData['filmography']
        self.data['photoLink'] = imdbData['photoLink']

    def print(self):
        print(json.dumps(self.data, indent=4))

def human_agregation(request_id):

    with open("other/Human/name" + str(request_id) + ".json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    people = []
    result = []

    for p in data:
        people.append(p)

    with open("rotten/Human/h" + str(request_id) + ".json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    for p in data:
        name = p['name']
        date = p['birthday']
        find = False
        for i in range(0, len(people)):
            imdbName = people[i]['name']
            imdbYear = people[i]['born']
            if imdbYear != None:
                year,month,day = imdbYear.split('-')
                if len(month) < 2: month = '0' + month
                imdbYear = year + '-' + month
                if name.lower() == imdbName.lower() and date.startswith(imdbYear):
                    newHuman = Human()
                    newHuman.addImdb(people[i])
                    newHuman.addRotten(p, True)
                    result.append(newHuman)
                    people.pop(i)
                    find = True
                    break

    for i in range(0, len(people)):
        newHuman = Human()
        newHuman.addImdb(people[i])
        result.append(newHuman)

    all = []

    for i in range(0, len(result)):
        all.append(result[i].data)

    with open("resultHuman" + str(request_id) + ".json", "w") as outfile:
         json.dump(all, outfile, indent=4)