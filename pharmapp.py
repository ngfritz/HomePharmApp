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
    drug_name = [flask.request.args.get("drug_name")] 
    effect_type = [flask.request.args.get("effect_type")]
    exp_date = [flask.request.args.get("exp_date")]
    active_ingredient = [flask.request.args.get("active_ingredient")]
    storage_location = [flask.request.args.get("storage_location")]
    stock = [flask.request.args.get("stock")]
    other = [flask.request.args.get("other")]
    print(drug_name)
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
    #drug = search_in_drugs_DF(search_name)
    drug_name = ''.join(drug['Name'])
    effect_type = ''.join(drug['Field of effect'])
    exp_date = ''.join(drug['Expiry date'])
    active_ingredient = ''.join(drug['Active ingredient'])
    storage_location = ''.join(drug['Location'])
    stock = ''.join(drug['Stock available'])
    other = ''.join(drug['Other comments'])
    drug_hit = Drug(drug_name, effect_type, exp_date, active_ingredient, storage_location, stock, other)
    return drug_hit

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
    drug_data = make_an_object(drug) #create an object from the hit
    if len(drug_data.drug_name) == 0: # if the object is empty (there was no hit, return message)
        table = "<p id='dont_have'>You don't have such a drug in your inventory.</p> "
    else: # othervise check with the method if it's still usable
        usable = drug_data.is_usable(drug_data.exp_date)
        if usable == True: #if usable show message accordingly paragaph id determines color coding (green)
            table = "<p id='usable'>You can use this " + drug_data.drug_name + ".</p>"
        else: #if not usable show message accordingly paragaph id determines color coding (red)
            table = "<p id='non_usable'>This " + drug_data.drug_name + " has expired. You shouldn't take it.</p>"
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