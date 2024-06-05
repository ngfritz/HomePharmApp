# load flask and define app
import flask
app = flask.Flask ("webnote")

# DateTime module to compare current date with expiry date
from datetime import date

# Pandas module to deal with the objects: transform them to dataframes, save as csv, etc
import pandas as pd


# function to get html codes
def get_html (page_name):
    html_file = open("templates/" + page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# fubnction to add a new drug
def add_new_drug ():
    # get the entered values
    dn = flask.request.args.get("drug_name")
    et = flask.request.args.get("effect_type")
    ed = flask.request.args.get("exp_date")
    if dn == "" or et == "" or ed == "":
        html_page = get_html("index")
        message = "<h3 id='mandatory_field'>* Enter vaslue(s) to the mandatory fields!</h3>"
        return html_page.replace("<h3>* mandatory fields</h3>", message)
    else:
        drug_name = [flask.request.args.get("drug_name")] 
        effect_type = [flask.request.args.get("effect_type")]
        exp_date = [flask.request.args.get("exp_date")]
        active_ingredient = [flask.request.args.get("active_ingredient")]
        storage_location = [flask.request.args.get("storage_location")]
        stock = [flask.request.args.get("stock")]
        other = [flask.request.args.get("other")]
        # combine the new values to one 
        drug_data = {'Name': drug_name, 'Field of effect': effect_type, 'Expiry date': exp_date, 'Active ingredient': active_ingredient,'Location': storage_location,'Stock available':stock,'Other comments':other}
        new_data_frame = pd.DataFrame(drug_data) # set the new entry as DF
        all_drugs_DF = pd.read_csv("database/drugs.csv", index_col=[0]) #open the exisitng dataset from the csv
        all_drugs_DF = all_drugs_DF._append(new_data_frame, ignore_index = True) # append the new data to the end
        all_drugs_DF.to_csv("database/drugs.csv") # save the updated dataset to the csv 
        return get_html("add") # go back to the clean form

# function to get all drugs in a html table from csv storage
def get_all_drugs_in_html():
    all_drugs_DF = pd.read_csv("database/drugs.csv", index_col=[0])
    all_drugs_html_table = all_drugs_DF.to_html()
    return all_drugs_html_table

# function to get all drugs as DF from csv storage
def get_all_drugs_in_DF():
    all_drugs_DF = pd.read_csv("/database/drugs.csv", index_col=[0])
    return all_drugs_DF

# funtion to search in the drug DataFrame and return a rows that contains the search term as a list
def search_in_drugs_DF(search_name):
    all_drugs = pd.read_csv("database/drugs.csv", index_col=[0])
    result = (all_drugs.loc[all_drugs['Name'].isin([search_name])])
    drug = result.to_dict('list')
    return drug

# each drug in the inventory is one object defined by the drug class. it has some parameters
class Drug:
    def __init__(self, drug_name, effect_type, exp_date, active_ingredient, storage_location, stock, other):
        self.drug_name = drug_name
        self.effect_type = effect_type
        self.exp_date = exp_date
        self.active_ingredient = active_ingredient
        self.storage_location = storage_location
        self.stock = stock
        self.other = other
    
    # method to check usability, if the expiry date is before the current date it shouldn't be used.
    def is_usable (self, exp_date):
        today = date.today()
        valid_until = exp_date.replace("-0","-")
        to_numbers = valid_until.split("-")
        dates = date(int(to_numbers[0]), int(to_numbers[1]), int(to_numbers[2]))
        if dates > today:
            usable = True
            return usable
        else:
            usable = False
            return usable

# function to create an object from the list that was returned from the search
def make_an_object(drug):
    #drug = search_in_drugs_DF(search_name) # I rather run this separately, got too complicated
    drug_name = ','.join(drug['Name']) # get all the coulumns that is in the hit list to a dictionary
    drug_names = drug_name.split(",") # transform the dictionary values to a list
    effect_type = ','.join(drug['Field of effect'])
    effect_types = effect_type.split(",")
    exp_date = ','.join(drug['Expiry date'])
    exp_dates = exp_date.split(",")
    active_ingredient = ','.join(drug['Active ingredient'])
    active_ingredients = active_ingredient.split(",")
    storage_location = ','.join(drug['Location'])
    storage_locations = storage_location.split(",")
    stock = ','.join(drug['Stock available'])
    stocks = stock.split(",")
    other = ','.join(drug['Other comments'])
    others = other.split(",")
    # for each hit (hit = one row in the DataFrame create an object up to the number of hits)
    table = "" # variable to store the results
    if drug_names == ['']: # if the object is empty (there was no hit, return message)
        table = "<p class='table' id='dont_have'>You don't have such a drug in your inventory.</p> "
        return table
    else: #if there's hit create on object for all of them
        for i in range(len(drug_names)):
            # define a variable that has all the parameters for the Drug class as a list
            param = [drug_names[i], effect_types[i], exp_dates[i], active_ingredients[i], storage_locations[i], stocks[i], others[i]]
            drug_data = Drug(*param) # then create the object
            usable = drug_data.is_usable(drug_data.exp_date) #check usability (before or after exp. date)
            if usable == True: #if usable show message accordingly paragaph id determines color coding (green)
                table += "<p id='usable'>You can use this <b>" + drug_data.drug_name + "</b> until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
            else:
                table += "<p id='non_usable'>This <b>" + drug_data.drug_name + "</b> has expired on <b>"  + drug_data.exp_date + "</b>. You shouldn't take it.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
        return table
    

# routes
    
@app.route("/")
def home():
    return get_html("index")

@app.route("/add")
def add():
    addnew_page = add_new_drug () # run the add_new_drug function: save the entered data and reload the page
    return addnew_page

@app.route("/check")
def check_start():
    html_page = get_html("check")
    table = "<h2>Search or list all.</h2>"
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/check_list")
def check_list():
    html_page = get_html("check")
    table = ""
    search_name = flask.request.args.get("search_name") #get the search term
    drug = search_in_drugs_DF(search_name) # search in the loaded DF, return the row that matches
    #drug_data = make_an_object(drug) #create an object from the hit
    # if len(drug_data.drug_name) == 0: # if the object is empty (there was no hit, return message)
    #     table = "<p class='table' id='dont_have'>You don't have such a drug in your inventory.</p> "
    # else: # othervise check with the method if it's still usable
    #     usable = drug_data.is_usable(drug_data.exp_date)
    #     if usable == True: #if usable show message accordingly paragaph id determines color coding (green)
    #         table = "<p id='usable'>You can use this <b>" + drug_data.drug_name + "</b> until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
    #     else: #if not usable show message accordingly paragaph id determines color coding (red)
    #         table = "<p id='non_usable'>This <b>" + drug_data.drug_name + "</b> has expired on <b>"  + drug_data.exp_date + "</b>. You shouldn't take it.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
    table = make_an_object(drug)
    print("table in route: " + str(table))
    return html_page.replace("$$DRUGS_TABLE$$", table)


@app.route("/check_all")
def check_all():
    html_page = get_html("check")
    table = ""
    table = get_all_drugs_in_html()
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/settings")
def settings():
    return get_html("settings")

# python -m flask --app pharmapp.py run