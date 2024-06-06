PharmApp

This webApp helps users to track their drug inventory at home to avoid redundant purchasing and wasting.

The application can store some basic information about the drugs in a searchable format.

The user is able to quickly loog up a drug before purchasing it in the pharmacy. If current stock allows, it is not necessary to purchase again.


Pages:
1. Register a drug
To register a drug some information shall be entered:
- drug name: like Aspirin 500, or Panadol extra
- type: like painkiller, antibiotics
- expiry date: yyyy-mm-dd 
- active ingredient: like paracetamol
- storage location
- stock
- other
Name, type and expiry dates are mandatory!

2. Search for a drug:
With any field it's possible to search, the app lists all the relavant hits

3. Edit stock/location/other (subject to my capabilities and time)


Thecnical parameters:
Backend: Python(3)
Frontend: JavaScript
Style: CSS
Webserver: Flask

additional modules that has to be installed:
Flask: pip instal flask #webserver
Pandas pip instal Pandas #database mngmnt


Checklist:
## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: pandas
- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that  `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: pharmapp.py
  - Line number(s) for the class definition: 76
  - Name of two properties: drug_name, effect_type
  - Name of two methods: is_usable, available
  - File name and line numbers where the methods are used: pharmapp.py 132, 133
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to the same file feature.
- []x It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: pharmapp.py
  - Line number(s): 29
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: pharmapp.py
  - Line number(s): 128
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] It is styled using your own CSS.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.