var results = $("#results");
var count = 0;
function search() {
    startSpinner();
    count=0;
    results.empty();
    var mandatory = $("#mandatory").val().replace(/ /g, '');
    var optional = $("#optional").val().replace(/ /g, '');
    $.getJSON("http://193.40.11.124/test/index.py?mandatory=" + mandatory + "&optional=" + optional, function (data) {
        var items = [];
        $.each( data, function( key, val ) {
            items.push("<div class='divide64'></div>");
            items.push("<div class='group draft'>");
            // var str = "<li id='" + key + "'><b>" + val.title + "</b></li>";
            items.push("<div class='element event-title'><b>" + key + val.title + "</b></div>");
            items.push("<div class='divide8'></div>")
            var events = val.events;

            $.each( events, function (key, val) {
                count += 1;
                var text = "<div class='element event-id'>Sündmuse id: " + key + "</div><div class='element event-content inner-text'>" + val.text + "</div>"
                items.push(text);
                // var words = "<ul>"
                $.each(val.words, function (key, val) {
                    //     words += "<li>" + key
                    //         + "<p>total: " + val.totalcount + "</p>"
                    //         + "<p>event: " + val.eventcount + "</p>"
                    //     + "</li>";
                });
                // words += "</ul>";
                // items.push(words);
                items.push("<div class='divide16'></div><div class='border'></div>")
            })
            items.push("</div>")
        });
        $("#count").text(count);
        $( "<div/>", {
            html: items.join( "" )
        }).appendTo("#results");

        if (strNotEmpty(optional)) {
            highlightWords(mandatory + "," + optional);
        } else {
            highlightWords(mandatory);
        }
        $(".draft-count").show();
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