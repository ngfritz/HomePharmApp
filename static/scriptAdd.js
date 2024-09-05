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
const saveNewDrugButton = document.getElementById("saveNewDrugButton");
const addNewButton = document.getElementById("addNewButton");
const editNewButton = document.getElementById("editNewButton");


// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
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


// function to update entered values
function updateDrug(){
    const dn = localStorage.setItem("Drug Name");
    const et = localStorage.setItem("Field of Effect");
    const ed = localStorage.setItem("Expiry Date");
    const ai = localStorage.setItem("Active Ingredient");
    const sl = localStorage.setItem("Storage Location");
    const stk = localStorage.setItem("Stock available");
    const oth = localStorage.setItem("Other Comment");
    const table = "<p>Drug Name: <b>" + dn + "</b></p><p>Fiels of Effect: <b>" + et + "</b></p><p>Expiry Date: <b>" + ed + "</b></p><p>Active Ingredient: <b>" + ai + "</b></p><p>Storage Location: <b>" + sl + "</b></p><p>Stock available: <b>" + stk + "</b></p><p>Other comments: <b>" + oth + "</b></p>"; 
    addedDrug.innerHTML = table;
}

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
saveNewDrugButton.addEventListener("click",saveDrug);
editNewButton.addEventListener("click",updateDrug);
addNewButton.addEventListener("click",clean);
