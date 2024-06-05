const navUsername = document.getElementById("navUsername");
const user = localStorage.getItem("username");

// user name dependent welcome message

if ( user != null){
    navUsername.innerHTML = "Username: " + user;
}

// const drug_name = document.getElementById ("drug_name");
// const effect_type = document.getElementById ("effect_type");
// const exp_date = document.getElementById ("exp_date"); 
// const active_ingredient = document.getElementById ("active_ingredient");
// const storage_location = document.getElementById ("storage_location");
// const stock = document.getElementById ("stock");
// const other = document.getElementById ("other");
// const added_drug = document.getElementById ("added_drug");
// const addNewDrugButton = document.getElementById("addNewDrugButton");
// const backToAddButton = document.getElementById("backToAddButton");


// function saveDrug(){
//     localStorage.setItem("Drug Name", drug_name.value);
//     localStorage.setItem("Field of Effect", effect_type.value);
//     localStorage.setItem("Expiry Date", exp_date.value);
//     localStorage.setItem("Active Ingredient", active_ingredient.value);
//     localStorage.setItem("Storage Location", storage_location.value);
//     localStorage.setItem("Stock available", stock.value);
//     localStorage.setItem("Other Comment", other.value);
//     dn = localStorage.getItem("Drug Name");
//     et = localStorage.getItem("Field of Effect");
//     ed = localStorage.getItem("Expiry Date");
//     ai = localStorage.getItem("Active Ingredient");
//     sl = localStorage.getItem("Storage Location");
//     stk = localStorage.getItem("Stock available");
//     oth = localStorage.getItem("Other Comment");
//     table = "<p>Drug Name: " + dn + "</p><p>Fiels of Effect: " + et + "</p><p>Expiry Date: " + ed + "</p><p>Active Ingredient: " + ai + "</p><p>Storage Location: " + sl + "</p><p>Stock available: " + stk + "</p><p>Other comments: " + oth + "</p>"; 
//     added_drug.innerHTML = table;
// };

// function clean(){
//     localStorage.clear();
// };


// addNewDrugButton.addEventListener("click",saveDrug);
// backToAddButton.addEventListener("click",clean);