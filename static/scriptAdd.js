// things for the username
const navUsername = document.getElementById("navUsername");
const user = localStorage.getItem("username");
// things for the added drug display
const drugName = document.getElementById ("drug_name");
const effectType = document.getElementById ("effect_type");
const expDate = document.getElementById ("exp_date"); 
const activeIngredient = document.getElementById ("active_ingredient");
const storageLocation = document.getElementById ("storage_location");
const stock = document.getElementById ("stock");
const other = document.getElementById ("other");
const addedDrug = document.getElementById ("added_drug");
const addNewDrugButton = document.getElementById("addNewDrugButton");
const backToAddButton = document.getElementById("backToAddButton");


// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
}

// function to display the entered values
function savedDrug(){
    const dn = localStorage.getItem("Drug Name");
    const et = localStorage.getItem("Field of Effect");
    const ed = localStorage.getItem("Expiry Date");
    const ai = localStorage.getItem("Active Ingredient");
    const sl = localStorage.getItem("Storage Location");
    const stk = localStorage.getItem("Stock available");
    const oth = localStorage.getItem("Other Comment");
    const table = "<p>Drug Name: <b>" + dn + "</b></p><p>Fiels of Effect: <b>" + et + "</b></p><p>Expiry Date: <b>" + ed + "</b></p><p>Active Ingredient: <b>" + ai + "</b></p><p>Storage Location: <b>" + sl + "</b></p><p>Stock available: <b>" + stk + "</b></p><p>Other comments: <b>" + oth + "</b></p>"; 
    addedDrug.innerHTML = table;
};

// function that deletes entered values from local storage
function clean(){
    localStorage.removeItem("Drug Name");
    localStorage.removeItem("Field of Effect");
    localStorage.removeItem("Expiry Date");
    localStorage.removeItem("Active Ingredient");
    localStorage.removeItem("Storage Location");
    localStorage.removeItem("Stock available");
    localStorage.removeItem("Other Comment");

};


savedDrug();// it is run every time when page is loaded
backToAddButton.addEventListener("click",clean);