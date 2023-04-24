// retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "Rectangle";

//var toggleMode = function(e)
var toggleMode = (e) => {
    console.log("toggling...");
    if(mode === "Rectangle"){
        mode = "circle";
    } else{
        mode = "Rectangle";
    }

    var buttonToggle = document.getElementById("buttonToggle");
    buttonToggle.innerHTML = mode;
}

//var drawRect = function(e) 
var drawCircle = (e) => {
    var mouseX = e.clientX; 
    var mouseY = e.clientY;
    console.log("mouseclick at ", mouseX, mouseY);

    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 10, 0, 360);
    ctx.fill();
}




c.addEventListener("click", drawCircle);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', toggleMode);


