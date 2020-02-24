import eel
from analyser import checkAutoAnalyse
from search import search
import asyncio
import json
import datetime

# Inits
WEB_FOLDER = '../web'
INDEX_FILE = '../data/index.csv'
DOCS_FOLDER = '../web/docs'
CACHE_DIMENSION = 20     # 0 means no cache
last_search_query = ''
response_time = .0
cache = []
response = []
last_search_query = ''

# Auto-analyse if needed
checkAutoAnalyse(DOCS_FOLDER, INDEX_FILE)

# Web files location
eel.init(WEB_FOLDER)

def search_pls(input):
    global response
    global last_search_query
    global response_time

    a = datetime.datetime.now()
    checkAutoAnalyse(DOCS_FOLDER, INDEX_FILE)
    last_search_query = input
    result = None
    for res in cache:
        if input in res:
            result = res[input]

    if result == None:
        response = search(INDEX_FILE, input)
        # Check if cache has reached its limit
        cache.append({input : response})
        if len(cache) > CACHE_DIMENSION:
            cache.pop(0)
    else:
        response = result
    

    b = datetime.datetime.now()
    c = b - a
    response_time = c.microseconds
    print('Search took %s microseconds' % response_time)

# EEL Functions
@eel.expose
def getWordsFromFile(n, file):
    fi = open(DOCS_FOLDER + '/' + file, "r")
    res = ' '.join(fi.read().split()[:n]) + ' ...'
    return res


@eel.expose
def search_pressed(input):
    # We process the search input and generate the response as soon as the
    # search button was pressed, even if the response web page is not loaded yet
    search_pls(input)

@eel.expose
def get_response(input):
    if last_search_query != input:
        search_pls(input)
    res = {'results' : response, 'response_time': response_time}
    return json.dumps(res)


# Crash fix
def on_close(page, sockets):
    return

# Start
eel.start('index.html', size=(1280, 720), app_mode=False, host='127.0.0.1', close_callback=on_close, all_interfaces=True, js_result_timeout=100000)