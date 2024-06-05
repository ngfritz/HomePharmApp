const welcome = document.getElementById ("welcome");
const enterUsername = document.getElementById("enterUsername");
const navUsername = document.getElementById("navUsername");
const changeUsernameButton = document.getElementById("changeUsernameButton");
const user = localStorage.getItem("username");


function saveUser(){
    localStorage.setItem("username", addUsername.value);
    welcome.innerHTML = "Welcome <em>" + user + "</em>!";
}



// user name dependent welcome message

if ( user === null){
    welcome.innerHTML = '<h1 id="welcome">Welcome! How can I call you?</h1><input type="text" placeholder="Your Name" id="addUsername"><br><br><a href="/"><input type="submit" value="Save" id="saveUsernameButton"></a>';
    const addUsername = document.getElementById ("addUsername");
    const saveUsernameButton = document.getElementById ("saveUsernameButton");
    saveUsernameButton.addEventListener("click",saveUser);
}
else {
    navUsername.innerHTML = "Username: " + user;
    welcome.innerHTML = "Welcome <em>" + user + "</em>!";
    
}




