import json
import re


class Movie:

    def __init__(self):
        self.data = {}

    def addRotten(self, rottenData, find):
        self.data['rottenLink'] = rottenData['link']
        self.data['rottenRating'] = rottenData['rating']
        if not find:
            self.data['title'] = rottenData['name']
            self.data['year'] = rottenData['year']

    def addImdb(self, imdbData):
        self.data['title'] = imdbData['title']
        self.data['year'] = imdbData['year']
        self.data['length'] = imdbData['length']
        self.data['imdbRating'] = imdbData['rating']
        self.data['poster_link'] = imdbData['poster_link']
        self.data['description'] = imdbData['description']
        self.data['ageRating'] = imdbData['ageRating']
        self.data['genres'] = imdbData['genres']
        self.data['trailer_link'] = imdbData['trailer']
        self.data['budget'] = imdbData['budget']
        self.data['gross'] = imdbData['gross']
        self.data['company'] = imdbData['company']
        self.data['crew'] = imdbData['crew']
        self.data['directors'] = imdbData['directors']
        self.data['writers'] = imdbData['writers']
        self.data['imdbLink'] = imdbData['imdbLink']
        self.data['metacriticLink'] = imdbData['metacriticLink']
        self.data['metacriticRating'] = imdbData['metacriticRating']

    def print(self):
        print(json.dumps(self.data, indent=4))

# Levenshtein distance
def levenshtein(s, t):
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]

def movie_agragation(request_id):
    with open("other/Title/title" + str(request_id) + ".json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    titles = []
    result = []

    for p in data:
        titles.append(p)

    with open("rotten/Title/r" + str(request_id) + ".json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    for p in data:
        titleName = p['name']
        year = p['year'].replace(' ', '')
        year = re.sub('[^0-9]', '', year)
        find = False
        for i in range(0, len(titles)):
            imdbName = titles[i]['title']
            imdbYear = re.sub('[^0-9]', '', str(titles[i]['year']).replace(' ', ''))
            if (levenshtein(titleName.lower(), imdbName.lower()) < 5 or titleName.lower().find(imdbName.lower())!=-1 or imdbName.lower().find(titleName.lower())!=-1) and \
                    (imdbYear.find(year) != -1 or year.find(imdbYear) != -1):
                newMovie = Movie()
                newMovie.addImdb(titles[i])
                newMovie.addRotten(p, True)
                result.append(newMovie)
                titles.pop(i)
                find = True
                break
        # if not find:
        #     newMovie = Movie()
        #     newMovie.addRotten(p, False)
        #     result.append(newMovie)

    for i in range(0, len(titles)):
        newMovie = Movie()
        newMovie.addImdb(titles[i])
        result.append(newMovie)

    all = []

    for i in range(0, len(result)):
        all.append(result[i].data)

    with open("result" + str(request_id) + ".json", "w") as outfile:
         json.dump(all, outfile, indent=4)