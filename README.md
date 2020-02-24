# Doogle

Doogle is an open-source search engine designed to be very fast and efficient. It handles big queries and files easily. Written in Python, it also incorporates a GUI and many other fetaures.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All the prerequisites will be installed automatically. Doogle was designed to run on Ubuntu 18.04, along with Google Chrome.

### Installing

First of all, clone the Github repository and navigate to the respective folder.

To install Doogle just run the following command:
```
chmod +x ./src/install.sh; ./install.sh
```
After installing, there are some variables you can configure, stored in `src/config.py`

* `DOCS_FOLDER` - specifies the folder where the documents will be stored -> it is best to be left **default** (`web/docs`), so that there are no problems with the web server.

* `INDEX_FILE` - specifies the file where the index values will be stored

* `CACHE_DIMENSION` - specifies the search cache length (number of searches to be remembered)

* `HOST` - web server host

* `PORT` - web server port

### Loading documents

All the documents that you want to use in this search engine will be stored in `web/docs`.

You don't have to do any more steps, because Doogle auto-analyses the files on any change.

### Running

You can very easily run Doogle with:
```
python3 ./src/app.py
```
#### Stopping
Remember that Doogle also has a web server integrated and for stopping it, you need to close the Python process with `Ctrl+C` 

## Usage

To use Doogle just run `python3 ./src/app.py` and Doogle will open in a new Google Chrome tab.

The search queries are extended in a way that you can specify if you want to exclude some words from your search.
Here are some examples:

* `Python && !(Java)`  -> It searches for documents with the word `python` in them excluding documents with the word `java`.

* `Programming || engineering`  -> It searches for documents with the word `programming` or `engineering` in them.

***To be remembered:*** Doogle is **NOT** case-sensitive! 

## How does it work

Doogle uses an `inverted index` structure for storing the words in the documents. When it starts and also before every search, it check if there is analysis of documents needed. Doogle is very efficient and was created with performance in mind. 

To solve the search queries, Doogle uses boolean logic on arrays that hold the apparition of a word in the documents list. (`True` - the word is in that document, `False` - the word is not in that document).

Using Eel, Doogle now has an intuitive GUI. Eel allows JavaScript functions to be called from Python and vice versa. You can also pass data between the Python process and JavaScript, also by using these `exposed functions`.


## Features

Doogle is not just a simple common search engine. It comes with a lot of features for making everyones life easier.

### GUI

Doogle uses an Electron-like offline HTML/JS GUI that runs as a web server.

It works best with Google Chrome as it is native supported, but you can also use Doogle from any other browser. You just need to enter this URL: `http://{HOST}:{PORT}/index.html`

Also, did you know that Doogle can be accesed by other people in your network? Well yes, since it is a web server.

### Auto-analysis of documents with SHA 1 Hashing

Doogle checks at every search request if the documents to search changed, and if it detects any change it re-analyses all the files again. We chose SHA 1 because it is the fastest Hashing algorithm and we do not care about security.

### Search-cache

Doogle rememberes last `CACHE_DIMENSION` searches and deliveres them very fast, without searching again. Try it yourself: search the same thing twice and compare the search time.

### Parallel search

Doogle uses Python multiprocessing for parallel search. Even if it is a little bit slower with small search queries, the performance improvement is definetely visible in larger search queries or bigger index files.

### Extended search query interpretation

We extended the search query format so that searching multiple words with no logic in between them also has an asnwer. Check this example:
* `hi my name is Dimi`  -->  `hi && my && name && is && Dimi`

### Extras:
#### Index file
We made it very easy for anyone to use our analysing algorithm. We save the index file as a csv, so that anyone can understand it.
#### Very efficient document analysis
Also, the analysis algorithm is very efficient, being capable of analysing documents at about 40MB/s on a medium spec computer.
#### Easy accessible Python API
We created Doogle with extendability and integrability in mind. You can very easy use our Python functions as described here:

**analyser.py**
* `checkAutoAnalyse(folder, index_output)` -> Call this function whenever you want to check if the documents changed, to auto re-analyse them. `folder` is the folder that contains the documents and `index_output` is the file that will hold the index.
* `analyseDocuments(folder, index_output)` -> Call this function to manually analyse documents in a folder. Parameters are the same as above.

**search.py**
* `search(index_file, search_string)` -> Call this function to search `search_string` in `index_file` and get a boolean array as return value that specifies the files that match the search_string.

## Built With

* [Eel/Python](https://github.com/samuelhwilliams/Eel) - The web framework used

