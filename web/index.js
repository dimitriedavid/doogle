function searchPressed() {

    document.getElementById("forMod").innerHTML = '<div class="lds-dual-ring"></div>'

    // Compute response
    let search_inp = document.getElementById("search-inp").value;
    if(search_inp != '') {
        eel.search_pressed(search_inp);

        // Go to response page
        document.location.href = "responses.html?q=" + encodeURIComponent(search_inp)
    }
}

var input = document.getElementById("search-inp");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      document.getElementById("myButton").click();
    }
  });