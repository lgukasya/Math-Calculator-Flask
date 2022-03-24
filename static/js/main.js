// Main.js

var body = document.getElementById('body');
var img_container = document.getElementById('img-container');
var submit = document.getElementById('submit');
var close = document.getElementById('close');
var spinner = document.getElementById('spinner');
var picturec = document.getElementById('picture-cont');
var a = document.getElementById('a');
var b = document.getElementById('b');
var c = document.getElementById('c');

async function petition(data) { 
    const url = 'http://localhost:5000/parabola';

    picturec.style.display = 'none';
    spinner.style.display = 'block';


    body.style.display = 'none';
    img_container.style.display = 'block';

    const response = await fetch(url, {
        method: 'post',
        cache: 'no-cache',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
    document.getElementById('result').src = `data:image/jpeg;base64,${await response.text()}`;

    picturec.style.display = 'block';
    spinner.style.display = 'none';
}

close.onclick = e => {
    body.style.display = 'block';
    img_container.style.display = 'none';
}

submit.onclick = e => {
    var data = {
        "variables": {
            "a": a.value,
            "b": b.value,
            "c": c.value,
        }
    }

    petition(data);
}