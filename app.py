from flask import Flask, render_template

from utils import load_family

import datetime


app = Flask(__name__, static_folder="public")

@app.route("/")
def main():
    family_data = sorted(load_family(), key=lambda x: datetime.datetime.strptime(x['dob'], '%d/%m/%Y'))
    return render_template(
        "index.html",
        family=family_data
    )
    
@app.route('/<path:text>')
def person(text):
    family_data = load_family()
    person_data = [member for member in family_data if f"/{text}" == member["siteref"]][0]
    return render_template(
        "person.html",
        person=person_data
    )

if __name__ == "__main__":  
    app.run(debug=True)
