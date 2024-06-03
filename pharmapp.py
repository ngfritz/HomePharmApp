# load flask and define app
import flask
app = flask.Flask ("webnote")

# DateTime module to compare current date with expiry date
from datetime import date


# function to get html codes
def get_html (page_name):
    html_file = open("templates/" + page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

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
    
    # method valid or not, if the expiry date is before the current date it shouldnt be used.
    def is_usable (self, exp_date):
        today = date.today()
        valid_until = exp_date.replace("-",",")
        if valid_until <= today:
            usable = True
            return usable
        else:
            usable = False
            return usable


         




# routes
    
@app.route("/")
def home():
    return get_html("index")