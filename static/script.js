// things for the uername feature
const welcome = document.getElementById ("welcome");
const enterUsername = document.getElementById("enterUsername");
const navUsername = document.getElementById("navUsername");
const changeUsernameButton = document.getElementById("changeUsernameButton");
const user = localStorage.getItem("username");
// things for the added drug display
const drugName = document.getElementById ("drug_name");
const effectType = document.getElementById ("effect_type");
const expDate = document.getElementById ("exp_date"); 
const activeIngredient = document.getElementById ("active_ingredient");
const storageLocation = document.getElementById ("storage_location");
const stock = document.getElementById ("stock");
const other = document.getElementById ("other");
const added_drug = document.getElementById ("added_drug");
const addNewDrugButton = document.getElementById("addNewDrugButton");



// save username function
function saveUser(){
    localStorage.setItem("username", addUsername.value);
    welcome.innerHTML = "Welcome <em>" + user + "</em>!";
}

// store entered value in local strorage when adding new drug
function saveDrug(){
    localStorage.setItem("Drug Name", drugName.value);
    localStorage.setItem("Field of Effect", effectType.value);
    localStorage.setItem("Expiry Date", expDate.value);
    localStorage.setItem("Active Ingredient", activeIngredient.value);
    localStorage.setItem("Storage Location", storageLocation.value);
    localStorage.setItem("Stock available", stock.value);
    localStorage.setItem("Other Comment", other.value);
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

// event listener for saveDrug function
addNewDrugButton.addEventListener("click",saveDrug);

