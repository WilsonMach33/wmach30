console.log("hello");

function addP(){
    const newP = document.createElement("p");
    const list = document.getElementById("thelist");

    newP.innerHTML = "hi new text";
    list.appendChild(newP);
}

function addRed(){
    const list = document.getElementById("thelist");
    list.setAttribute("font-color","red");
}

var buttonP = document.getElementById("b");
buttonP.addEventListener('click', addP);