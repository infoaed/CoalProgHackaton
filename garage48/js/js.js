var results = $("#results");
function search() {
    startSpinner();
    results.empty();
    var mandatory = $("#mandatory").val().replace(/ /g, '');
    var optional = $("#optional").val().replace(/ /g, '');
    $.getJSON("http://193.40.11.124/test/index.py?mandatory=" + mandatory + "&optional=" + optional, function (data) {
        var items = [];
        $.each( data, function( key, val ) {
            var str = "<li id='" + key + "'><b>" + val.title + "</b></li>";
            items.push(str);
            var events = val.events;
            $.each( events, function (key, val) {
                var text = "<p>Event id: " + key + "</p><p class='inner-text'>" + val.text + "</p>"
                items.push(text);
                var words = "<ul>"
                $.each(val.words, function (key, val) {
                    words += "<li>" + key
                        + "<p>total: " + val.totalcount + "</p>"
                        + "<p>event: " + val.eventcount + "</p>"
                    + "</li>";
                });
                words += "</ul>";
                items.push(words);
            })
        });

        $( "<ul/>", {
            html: items.join( "" )
        }).appendTo("#results");

        if (strNotEmpty(optional)) {
            highlightWords(mandatory + "," + optional);
        } else {
            highlightWords(mandatory);
            console.log("HELLO")
        }
        stopSpinner();
    })

}

function highlightWords(words) {
    var wordArray = words.split(",");
    // results.mark(wordArray);
    $(".inner-text").mark(wordArray);
}

var spinner = null;
function startSpinner() {
    if (spinner == null) {
        spinner = new spin("SpinnerDiv", getSpinnerOpts());
    }
    $.blockUI({
        css: { backgroundColor: '#f00', color: 'red', border: 'none' },
        message: "<div id='SpinnerDiv'></div>"
    });
    spinner.start();
}
function stopSpinner(){
    spinner.stop();
    $.unblockUI();
}

function SortByEvent(a, b){
    var aName = a.name.toLowerCase();
    var bName = b.name.toLowerCase();
    return ((aName < bName) ? -1 : ((aName > bName) ? 1 : 0));
}

function calculateOccurences(word) {

}