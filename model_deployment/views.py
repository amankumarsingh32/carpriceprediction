from django.shortcuts import render
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from datetime import datetime
model = pickle.load(open("D:/Artificial Intelligence/Machine Learning End to End Deployment/car price prediction/random_forest_regressor_model.pkl",'rb'))

# def index(request):
#     return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        presentPrice = float(request.POST.get('presentPrice'))
        kms = int(request.POST.get('kms'))
        fuelType = request.POST.get('fuelType')
        sellerType = request.POST.get('sellerType')
        transmissionType = request.POST.get('transmissionType')
        owner = int(request.POST.get('owner'))

        current_year = datetime.now().year
        no_of_year = current_year - year

        if fuelType == 'petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif fuelType == 'diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        if sellerType == 'individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        if transmissionType == 'manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        prediction = model.predict([[presentPrice, kms, owner, no_of_year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(prediction[0],2)

        if output < 0:
            text = {"value": "Sorry you cannot sell this Car!"}
            return render(request, 'predict.html', context=text)
        else:
            text = {"value": "You can sell this Car at {} Lakhs".format(output)}
            return render(request, 'predict.html', context=text)

    return render(request, 'predict.html')

