alert("Welcome to NRIIT Learning Management System")
let heading = document.getElementById("welcome");
heading.innerHTML = "Welcome Future Software Engineers"
console.log("Heading element: ", heading)
let msg = document.getElementById("message")
msg.innerHTML = "Javascript is fun"
console.log("Message element:", msg)
function showmessage() {
    alert("Welcome to NRIIT Learning Management System")
}
function changeHeadings() {
    document.getElementById("welcome").
        innerHTML = "Welcome Python Fullstack Developers"
}
let heading1 = document.querySelector("#welcome");
console.log("heading element:", heading1)
let button = document.getElementById("btnGreeting");
button.addEventListener("click", function () {
    alert("welcome to javascript event handling");
});
let registerForm = document.getElementById("registerForm");
registerForm.addEventListener("sumbit", function (event) {
    event.preventDefault();
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    if(!name || !email || !password) {
        alert("please fill in all fields.");
        return;
    }
    alert("registration Successful");
    console.log("Name:", name);
    console.log("email:", email);
    console.log("password:", password);
});
