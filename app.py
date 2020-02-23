import eel
from search import search
import asyncio
import json
import datetime

# Inits
INDEX_FILE = 'index.csv'
last_search_query = ''
response = []
response_time = .0

# Web files location
eel.init('web')


def search_pls(input):
    global response
    global last_search_query
    global response_time

    a = datetime.datetime.now()
    response = search(INDEX_FILE, input)
    b = datetime.datetime.now()
    last_search_query = input
    c = b - a
    response_time = c.microseconds
    print('Search took %s microseconds' % response_time)


# EEL Functions
@eel.expose
def getWordsFromFile(n, file):
    fi = open('web/docs/' + file, "r")
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