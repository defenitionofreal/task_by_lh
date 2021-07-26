import requests
url = 'http://127.0.0.1:5000/get_form'



# check first form template
payload = {'callback_comment': 'hello', 'callback_date': '20.04.1993', 'callback_phone': '+7 777 777 77 77'}

#check second form template with one extra value
payload = {'login_email': 'hello@mail.com', 'login_password': 'asdd', 'test': 'asdd',}

# check input data with only one option from form template
payload = {'new_field': 'asdd', 'some': 'bobo', 'login_password': 'asdld',}

# check input data without options from form templates
payload = {'new_field': 'asdd', 'some': 'bobo',}



res = requests.post(url, data=payload)
print(res.text)