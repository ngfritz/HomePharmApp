const navUsername = document.getElementById("navUsername");
const changeUsernameButton = document.getElementById("changeUsernameButton");
const user = localStorage.getItem("username");



function changeUsername(){
    localStorage.removeItem("username");
    localStorage.setItem("username",enterUsername.value);
}

// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
}

// change username
changeUsernameButton.addEventListener("click",changeUsername);