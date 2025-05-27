
async function translateText() {
    var data = document.getElementById("data").value
    const res = await fetch("http://127.0.0.1:5000/translate", {
        method: "POST",
        body: JSON.stringify({
            q: data,
            source: langPairs[0],
            //kieli johon käännetään on käyttäjän valitsema ja se on talletettu state muuttujaan
            target: langPairs[1],

        }),
        headers: { "Content-Type": "application/json" }
    });
    var translated = await res.json()
    document.getElementById("data").value = " "
    document.getElementById("data").value = translated.translatedText

}
var filetext = ""
function openTextFile() {
    fetch('/static/js/lttext.txt')
        .then(response => response.text())
        .then(text => {
            filetext = text
            translateFileContent(filetext)
            
        })
        
}
async function translateFileContent(filetext) {
    const res = await fetch("http://127.0.0.1:5000/translate", {
        method: "POST",
        body: JSON.stringify({
            q: filetext,
            source: langPairs[0],
            target: langPairs[1],

        }),
        headers: { "Content-Type": "application/json" }

    });
     var translated = await res.json()
  
       var blob = new Blob([translated.translatedText], {
            type: "text/plain;charset=utf-8",
         });
         saveAs(blob, "lttext.txt");

}



async function availableLangs() {
    const res = await fetch("http://127.0.0.1:5000/languages")
        .then(res => {
            return res.json()
        })
        .then(data => {
            console.log(data)
            //[0].targets on json-vastauksen property, josta saadaan kielet, joita api tukee
            data[0].targets.forEach(d => {
                //luodaan <option> ja <br> tagit
                const opt = document.createElement("option")
                const linebreak = document.createElement("br")
                //option tagin teksti d on silmukkamuuttuja
                opt.innerText = "en-" + d
                //lisätään languages id:llä nimettyyn options valikkoon
                document.getElementById("languages").appendChild(opt)
                document.getElementById("languages").appendChild(linebreak)

            });

        })



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
var langPairs = []
//select elementissä valittu teksti
function getLanguages(lang) {
    var pairs = lang.options[lang.selectedIndex].text
    langPairs = pairs.split('-')
    console.log(langPairs)

}


