const navUsername = document.getElementById("navUsername");
const user = localStorage.getItem("username");

// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
}