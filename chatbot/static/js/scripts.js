
async function translateText() {
    var data = document.getElementById("data").value
    const res = await fetch("http://127.0.0.1:5000/translate", {
        method: "POST",
        body: JSON.stringify({
            q: data,
            source: splitted[0],
            //kieli johon käännetään on käyttäjän valitsema ja se on talletettu state muuttujaan
            target: splitted[1],

        }),
        headers: { "Content-Type": "application/json" }
    });
    var translated = await res.json()
    document.getElementById("data").value = " "
    document.getElementById("data").value = translated.translatedText

}

$(function () {
    $("#train").submit(function (event) {
        // Stop form from submitting normally
        event.preventDefault();
        var trainForm = $(this);
        // Send the data using post
        var posting = $.post(trainForm.attr('action'), trainForm.serialize());
        // if success:
        posting.done(function (data) {
        });
        // if failure:
        posting.fail(function (data) {
            // 4xx or 5xx response, alert user about failure
        });
    });
});

function showTranslateOpt(cb) {
    if (cb) {
        document.getElementById("translateBtn").hidden = false
        document.getElementById("languages").hidden = false
    }
    if (cb.checked == false) {
        document.getElementById("translateBtn").hidden = true
        document.getElementById("languages").hidden = true
    }

}
var splitted=[]
//select elementissä valittu teksti
function getLanguages(lang) {
    var langPairs=lang.options[lang.selectedIndex].text
    splitted=langPairs.split('-')
    console.log(splitted)

}