# load flask and define app
import flask
app = flask.Flask ("homepharmapp")

# DateTime module to compare current date with expiry date
from datetime import date

# Pandas module to deal with the objects: transform them to dataframes, save as csv, etc
import pandas as pd

# function to get all drugs as DF from csv storage
def get_all_drugs_in_DF():
    all_drugs_DF = pd.read_csv("database/drugs.csv", index_col=[0])
    return all_drugs_DF

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
    if dn == "" or et == "" or ed == "": # makes the name, field of effect and exp date fields mandatory
        html_page = get_html("index")
        message = "<h3 id='mandatory_field'>* Enter vaslue(s) to the mandatory fields!</h3>"
        return html_page.replace("<h3>* mandatory fields</h3>", message)
    else: # get all input values from the frontend
        drug_name = [flask.request.args.get("drug_name")] 
        effect_type = [flask.request.args.get("effect_type")]
        exp_date = [flask.request.args.get("exp_date")]
        ai = [flask.request.args.get("active_ingredient")] # if no entry add default value to non-mandatory fields
        if ai == ['']:
            active_ingredient = "not defined"
        else:
            active_ingredient = ai
        sl = [flask.request.args.get("storage_location")]
        if sl == ['']:
            storage_location = "not defined"
        else:
            storage_location = sl
        stk = [flask.request.args.get("stock")]
        if stk == ['']:
            stock = "not defined"
        else:
            stock = stk
        oth = [flask.request.args.get("other")]
        if oth == ['']:
            other = "-"
        else:
            other = oth
        # combine the new values to one 
        drug_data = {'Name': drug_name, 'Field of effect': effect_type, 'Expiry date': exp_date, 'Active ingredient': active_ingredient,'Location': storage_location,'Stock available':stock,'Other comments':other}
        new_data_frame = pd.DataFrame(drug_data, dtype="string") # set the new entry as DF
        all_drugs_DF = pd.read_csv("database/drugs.csv", index_col=[0]) #open the exisitng dataset from the csv
        all_drugs_DF = all_drugs_DF._append(new_data_frame, ignore_index = True) # append the new data to the end
        all_drugs_DF.to_csv("database/drugs.csv") # save the updated dataset to the csv 
        return get_html("add") # go back to the clean form

# function to get all drugs in a html table from csv storage
def get_all_drugs_in_html():
    all_drugs_DF = get_all_drugs_in_DF()
    if len(all_drugs_DF) == 0: # check if the database has any values, if not return message
        all_drugs_html_table = "<p id='dont_have'>Your database is empty!</p>"
        return all_drugs_html_table
    else:   # else return the database in html table
        all_drugs_html_table = all_drugs_DF.to_html() # transforms to html table, taken as template
        return all_drugs_html_table

# funtion to search in the drug DataFrame and return all rows that contains the search term "Name" as a list
def search_name_in_drugs_DF(search_name):
    all_drugs_DF = get_all_drugs_in_DF()
    # result = (all_drugs_DF.loc[all_drugs_DF['Name'].isin([search_name])]) # exact match case sensitive
    result = all_drugs_DF.loc[all_drugs_DF['Name'].str.lower().isin([search_name.lower()])] # case insensitive search
    # for partial match the 'isin' should be changed to 'contains'. But that would return a boolean, that is not compatible wiht the rest of the worflow.
    drug = result.to_dict('list')
    return drug

# function to search in the drug DataFrame and return all rows that contains the search term "Field of Effect" as a list
def search_effect_in_drugs_DF(search_effect):
    all_drugs_DF = get_all_drugs_in_DF()
    result = all_drugs_DF.loc[all_drugs_DF['Field of effect'].isin([search_effect])] # as the values are predefined at input and at search exact match is enough
    drug = result.to_dict('list')
    return drug

# each drug in the inventory shall be transformed to an object defined by the Drug class. it has some parameters
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
        valid_until = exp_date.replace("-0","-") # transform the strings to date
        to_numbers = valid_until.split("-")
        dates = date(int(to_numbers[0]), int(to_numbers[1]), int(to_numbers[2]))
        if dates > today:
            usable = True
            return usable
        else:
            usable = False
            return usable
    
    # methode to check availability (stock > 0)
    def available (self, stock):
        if str(stock) == "0" :
            availability = False
            return availability
        

# function to create an object from the list that was returned from the search by name
def make_an_object_by_name(drug):
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
    else: #if there's hit create one object for all of them
        for i in range(len(drug_names)):
            # define a variable that has all the parameters for the Drug class as a list
            param = [drug_names[i], effect_types[i], exp_dates[i], active_ingredients[i], storage_locations[i], stocks[i], others[i]]
            drug_data = Drug(*param) # then create the object
            usable = drug_data.is_usable(drug_data.exp_date) #check usability (before or after exp. date)
            available = drug_data.available(drug_data.stock) # check availability 
            if usable == True: #if usable, show message accordingly paragaph id determines color coding (green), append all
                if available == False:
                    table += "<p id='usable'><b>"+ drug_data.drug_name +":</b> You can use this drug until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It was stored in: <b>" + drug_data.storage_location + "</b> but you dont have anything left. You also registered the following comment: " + drug_data.other + ".</p>"
                else:
                    table += "<p id='usable'><b>"+ drug_data.drug_name +":</b> You can use this drug until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
            else: #if NOT usable, show message accordingly paragaph id determines color coding (red), append all
                table += "<p id='non_usable'><b>" + drug_data.drug_name + "</b>: This drug has expired on <b>"  + drug_data.exp_date + "</b>. You shouldn't take it.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
        return table
    
# function to create an object from the list that was returned from the search by effect (same logic as with Name search)
def make_an_object_by_effect(drug):
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
    if effect_types == ['']: # if the object is empty (there was no hit, return message)
        table = "<p class='table' id='dont_have'>You don't have such a drug in your inventory.</p> "
        return table
    else: #if there's hit create one object for all of them
        for i in range(len(effect_types)):
            # define a variable that has all the parameters for the Drug class as a list
            param = [drug_names[i], effect_types[i], exp_dates[i], active_ingredients[i], storage_locations[i], stocks[i], others[i]]
            drug_data = Drug(*param) # then create the object
            usable = drug_data.is_usable(drug_data.exp_date) #check usability (before or after exp. date)
            available = drug_data.available(drug_data.stock) # check availability 
            if usable == True: #if usable, show message accordingly paragaph id determines color coding (green)
                if available == False:
                    table += "<p id='usable'><b>"+ drug_data.drug_name +":</b> You can use this drug until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It was stored in: <b>" + drug_data.storage_location + "</b> but you dont have anything left. You also registered the following comment: " + drug_data.other + ".</p>"
                else:
                    table += "<p id='usable'><b>"+ drug_data.drug_name +":</b> You can use this drug until <b>" + drug_data.exp_date + "</b>.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
            else: #if NOT usable, show message accordingly paragaph id determines color coding (red)
                table += "<p id='non_usable'><b>" + drug_data.drug_name + "</b>: This drug has expired on <b>"  + drug_data.exp_date + "</b>. You shouldn't take it.</p><p class='table'>It is a/an <b>" + drug_data.effect_type + "</b>. It is stored in: <b>" + drug_data.storage_location + "</b> and you have still <b>" + drug_data.stock + "</b> from it. You also registered the following comment: " + drug_data.other + ".</p>"
        return table

# function to delete all data from the csv
def delete_all_data():
    all_drugs_DF = get_all_drugs_in_DF() # load csv to a DF
    all_drugs_DF = all_drugs_DF[:0] # keep all raws after roe[0]-1 => delete all
    all_drugs_DF.to_csv("database/drugs.csv") # save the empty DF to csv
    return get_html("settings")

# function to delete expired drugs from the csv   
def delete_expired():
    today = date.today() # define today's date
    all_drugs_DF = get_all_drugs_in_DF() # load csv to a DF 
    all_drugs_DF['Expiry date'] = pd.to_datetime(all_drugs_DF['Expiry date'], format='%Y-%m-%d') # transform Expiry date str values to date
    result = all_drugs_DF.loc[(all_drugs_DF['Expiry date'] >= str(today))] # filter for those that are not yet expired and save in another DF
    result.to_csv("database/drugs.csv") #save the not expitred to the database csv

    

# routes
    
@app.route("/")
def home():
    return get_html("index")

@app.route("/add", methods=('GET','POST'))
def add():
    # addnew_page = add_new_drug () # run the add_new_drug function: save the entered data and reload the page
    # return addnew_page
    return get_html("add")

@app.route("/check")
def check_start():
    html_page = get_html("check")
    table = "<h2>Search or list all.</h2>"
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/check_list")
def check_list():
    html_page = get_html("check")
    search_effect = "" #set the variables
    search_name = ""
    table = ""
    search_name = flask.request.args.get("search_name") # get the searched name 
    search_effect = flask.request.args.get("search_effect") # get the searched effect
    if str(search_effect) != "None": # if serarch_effect was used, run the relevant functions
        drug_effect = search_effect_in_drugs_DF(search_effect) # search in the loaded DF, return the row that matches by Field of Effect
        table = make_an_object_by_effect(drug_effect)
        return html_page.replace("$$DRUGS_TABLE$$", table)
    elif str(search_name) != "None": # if serarch_name was used, run the relevant functions
        drug_name = search_name_in_drugs_DF(search_name) # search in the loaded DF, return the row that matches by Drug name
        table = make_an_object_by_name(drug_name) # add the hit(s) to a variable
        return html_page.replace("$$DRUGS_TABLE$$", table)
    else: # if the user managed to launch a search without any search term
        table = "Set at least one search term!" 
        return html_page.replace("$$DRUGS_TABLE$$", table)


@app.route("/check_all")
def check_all():
    html_page = get_html("check")
    table = ""
    table = get_all_drugs_in_html() # serch for all data without any filter
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/settings")
def settings():
    return get_html("settings")

@app.route("/settings_del")
def delete_all():
    delete_term = ""
    delete_term = flask.request.args.get("deleteSelect") # get the value from the dropdown
    if str(delete_term) == "selected": # check the value is still the default one
        html_page = get_html("settings")
        table = '<h1 class="mandatory_field" id="mandatoryField">Please select what data you want to delete!</h1>'
        return html_page.replace("<h1>Do you want to delete some of your data?</h1>", table)
    elif str(delete_term) == "delete_all": # check the value, if delete all:
        delete_all_data() # delete all data
        html_page = get_html("check") # then load the search all page (Checl_all)
        table = ""
        table = get_all_drugs_in_html() 
        return html_page.replace("$$DRUGS_TABLE$$", table)
    elif str(delete_term) == "delete_expired": # check the value, if delete only expired:
        delete_expired()  # delete all expired
        html_page = get_html("check") # then load the search all page (Checl_all)
        table = ""
        table = get_all_drugs_in_html() 
        return html_page.replace("$$DRUGS_TABLE$$", table)
    else:
        pass

# python -m flask --app pharmapp.py run