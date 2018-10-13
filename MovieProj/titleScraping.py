from scraper import *
import sys

request_id = sys.argv[1]
title = sys.argv[2]
genre = sys.argv[3]
start_year = sys.argv[4]
end_year = sys.argv[5]

parse_titles(request_id, title, genre, start_year, end_year)