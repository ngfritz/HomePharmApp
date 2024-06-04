const drug_name = document.getElementById ("drug_name");
const effect_type = document.getElementById ("effect_type");
const exp_date = document.getElementById ("exp_date"); 
const active_ingredient = document.getElementById ("active_ingredient");
const storage_location = document.getElementById ("storage_location");
const stock = document.getElementById ("stock");
const other = document.getElementById ("other");
const added_drug = document.getElementById ("added_drug")

function saveDrug(){
    localStorage.setItem("Drug Name", drug_name.value);
    localStorage.setItem("Field of Effect", effect_type.value);
    localStorage.setItem("Expiry Date", exp_date.value);
    localStorage.setItem("Active Ingredient", active_ingredient.value);
    localStorage.setItem("Storage Location", storage_location.value);
    localStorage.setItem("Stock available", stock.value);
    localStorage.setItem("Other Comment", other.value);
};
saveDrug()
function getValuesForTable(){

}
    
table =<table class="table">
        <thead>
            <tr>
            <th scope="col">Characteristic</th>
            <th scope="col">Adde value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <th scope="row"></th>
            <td>Drug Name</td>
            <td>localStorage.getItem("Drug Name")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Field of Effect</td>
            <td>localStorage.getItem("Field of Effect")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Expiry Date</td>
            <td>localStorage.getItem("Expiry Date")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Active Ingredient</td>
            <td>localStorage.getItem("Active Ingredient")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Storege Location</td>
            <td>localStorage.getItem("Storege Location")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Stock available</td>
            <td>localStorage.getItem("Stock available")</td>
            </tr>
            <tr>
            <th scope="row"></th>
            <td>Other Comment</td>
            <td>localStorage.getItem("Other Comment")</td>
            </tr>
        </tbody>
        </table>;
        
added_drug.innerHTML = table

backToAddButton.addEventListener("click",saveDrug)