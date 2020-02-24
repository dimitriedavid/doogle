const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
search_input = urlParams.get('q');

// Call eel function to get parameters
eel.get_response(search_input)(handleResponse)

async function handleResponse(response) {
    let decoded_response = JSON.parse(response);
    if(decoded_response['results'].length == 0) {
        document.getElementById("hereGoesEverything").innerHTML += '<h4>No results found</h4>';
    } else {
        for (const res of decoded_response['results']) {
            words = await eel.getWordsFromFile(30, res)();
            document.getElementById("hereGoesEverything").innerHTML += '<div class="jumbotron"><h4><b>' + res + '</b></h1><p>' + words + '</p><a class="btn btn-primary btn-sm" href="/docs/' + res + '" role="button">Open document</a></div>';
        }
    }
    document.getElementById("hereGoesEverything").innerHTML += '<p>Search took: ' + decoded_response['response_time'] / 1000 + ' milliseconds</p>';
}