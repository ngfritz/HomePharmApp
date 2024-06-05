// things for the uername feature
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


// things for the added drug display

const drug_name = document.getElementById ("drug_name");
const effect_type = document.getElementById ("effect_type");
const exp_date = document.getElementById ("exp_date"); 
const active_ingredient = document.getElementById ("active_ingredient");
const storage_location = document.getElementById ("storage_location");
const stock = document.getElementById ("stock");
const other = document.getElementById ("other");
const added_drug = document.getElementById ("added_drug");
const addNewDrugButton = document.getElementById("addNewDrugButton");



function saveDrug(){
    localStorage.setItem("Drug Name", drug_name.value);
    localStorage.setItem("Field of Effect", effect_type.value);
    localStorage.setItem("Expiry Date", exp_date.value);
    localStorage.setItem("Active Ingredient", active_ingredient.value);
    localStorage.setItem("Storage Location", storage_location.value);
    localStorage.setItem("Stock available", stock.value);
    localStorage.setItem("Other Comment", other.value);
}

addNewDrugButton.addEventListener("click",saveDrug);

