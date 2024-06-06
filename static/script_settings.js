const navUsername = document.getElementById("navUsername");
const changeUsernameButton = document.getElementById("changeUsernameButton");
const user = localStorage.getItem("username");
const deleteButton = document.getElementById("deleteAll")

// function to change username
function changeUsername(){
    localStorage.removeItem("username");
    localStorage.setItem("username",enterUsername.value);
}

// function for the Delete alert
function alert(){
    confirm("Please confirm that you want to delete records!\nThis transaction is not reversible.");
}

// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
}


// change username
changeUsernameButton.addEventListener("click",changeUsername);

// delete records alert
deleteButton.addEventListener("click",alert);