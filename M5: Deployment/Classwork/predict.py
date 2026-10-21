import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


churn = pipeline.predict_proba([customer])[0, 1]
print(f'Churn probability: {churn:.3f}')

if churn >= 0.5:
    print('The customer is likely to churn, send marketing email')
else:
    print('The customer is not likely to churn, do not send marketing email')