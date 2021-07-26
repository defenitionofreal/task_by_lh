from flask import Flask, request
import re
import collections
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')

def get_date(date):
    if re.match(r'^\d{2}\.\d{2}\.\d{4}$', date) \
            or re.match(r'^\d{4}\-\d{2}\-\d{2}$', date):
        return True
    return False

def get_phone(phone):
    if re.match(r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', phone):
        return True
    return False

def get_email(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return True
    return False

def get_type(value):
    if get_date(value):
        return 'date'
    elif get_phone(value):
        return 'phone'
    elif get_email(value):
        return 'email'
    return 'text'

@app.route('/get_form', methods=['POST'])
def check():
    data = request.form
    forms = db
    data_type_list = []
    form_type_list = []
    number = 0
    # check for the same keys
    for form in forms:
        for key in set(form).intersection(set(data)):
            if key in form:
                data_type_list.append(get_type(data[key]))
                form_type_list = list(form.values())
                # check if all values are in and check there type
                if collections.Counter(data_type_list) == collections.Counter(
                        form_type_list[1::]):
                    return f"Form: {form_type_list[0]}"
    fields = {}
    for k, v in data.items():
        number += 1
        k = 'f_name'
        fields[f'{k}{number}'] = get_type(v)
    return fields


if __name__ == '__main__':
    app.run(host='0.0.0.0')