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


# define a DataFrame, that is the "database" for this app




# function to save a drug
def add_note(text):
    new_drug = open ("database/drugs.txt", "a")
    new_drug.write ("\n" + text) #each note starts in a new line
    new_drug.close

# function to get the drugs in a DataFrame from csv storage
def get_all_drugs_in_DF():
    all_drugs_DF = pd.read_csv("database/drugs.csv")
    all_drugs_html_table = all_drugs_DF.to_html()
    return all_drugs_html_table



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
        if valid_until > today:
            usable = True
            return usable
        else:
            usable = False
            return usable


         




# routes
    
@app.route("/")
def home():
    return get_html("index")

@app.route("/add")
def add():
    return get_html("add")

@app.route("/check")
def check_start():
    html_page = get_html("check")
    table = ""
    table = "Search or list all."
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/check_all")
def check_all():
    html_page = get_html("check")
    table = ""
    table = get_all_drugs_in_DF()
    return html_page.replace("$$DRUGS_TABLE$$", table)

@app.route("/settings")
def settings():
    return get_html("settings")

# python -m flask --app pharmapp.py run