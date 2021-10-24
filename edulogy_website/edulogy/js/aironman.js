const url = "http://localhost:8000";

function askToExperAI(document="Michael Jordan was one of the best basketball players of all time."){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        value: document
    }));

    xhr.onreadystatechange = function () {
        if (this.readyState != 4) return;

        if (this.status == 200) {
            var data = JSON.parse(this.responseText);
            console.log("response data", data)

            let temp = "";
            temp += "<p>Numero dei paragrafi: "+data.paragraphs+"</p>";
            temp += "<p>Numero dei tokens: "+data.tokens+"</p>";
            temp += "<p>Numero di mainSentences: "+data.mainSentences+"</p>";
            temp += "<p>Numero di mainPhrases: "+data.mainPhrases+"</p>";
            temp += "<p>Numero di topics: "+data.topics+"</p>";
            temp += "<p>Numero di entities: "+data.entities+"</p>";
            // document.getElementById("metadata").innerHTML = "";
            // document.getElementById("metadata").innerHTML += data.paragraphs
            setText1(temp)
        }
    };
}