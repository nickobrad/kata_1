# Display the count on a UI
# Display a table with all the data (pagination)

import json
from flask import render_template, url_for, request
from app import app
import os
from flask_paginate import Pagination, get_page_parameter

@app.route('/')
def home():

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    rawdata_url = os.path.join(SITE_ROOT, 'static', 'MOCK_DATA.json')
    rawdata = open(rawdata_url, encoding = "cp437")
    formatdata = json.load(rawdata)

    male = []
    female = []

    for data in formatdata:
        if data['gender'] == "Male":
            male.append(data)
        elif data['gender'] == "Female":
            female.append(data)

    number_male = len(male)
    print(number_male)
    number_female = len(female)
    print(number_female)

    page = request.args.get(get_page_parameter(), type = int, default = 1)
    pagination = Pagination(page = page, total = len(formatdata))
   
    return render_template('index.html', male_no = number_male, female_no = number_female, formatdata = formatdata, pagination = pagination)

