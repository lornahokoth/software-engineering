alert("I am an alert");
console.log("I am a log statement!!");

window.onload = () => { // onload makes sure the content is loaded on page first
    document.getElementById('myCoolButt').addEventListener('click', () => {
        // Anything you want to do when this button is clicked should be added below
        console.log('Button was clicked!'); // console.log is like printing in JS!
        document.getElementById("flashes").style.color = "green";
    });
};
function validateForm() {
    let val = document.forms[0].elements[0].value;
    if (val === "lokoth1") {
        return true;
    }
    alert("Wrong campus ID");
    return false;
}