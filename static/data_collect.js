
// make frame 1 visible
showFrame1();

function showFrame2(){
	document.getElementById("frame-1").style.display = "none";
	document.getElementById("frame-2").style.display = "block";
	document.getElementById("step-number").innerHTML = "2";
}

function showFrame1(){
	document.getElementById("frame-1").style.display = "block";
	document.getElementById("frame-2").style.display = "none";
	document.getElementById("step-number").innerHTML = "1";
}
