from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import  get_object_or_404
import requests
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
from matplotlib import style
import pandas as pd
import pickle
from sklearn.externals import joblib
import csv
from django.http import HttpResponse

# Create your views here.
def test(request):
    return render(request, 'mbti_model/index.html')

def result(request):
    if request.method == "GET":
        sepal_length = request.GET.get('sepalLength')
        sepal_width = request.GET.get('sepalWidth')
        petal_length =request.GET.get('petalLength')
        petal_width = request.GET.get('petalWidth')
       
        #csv.DictReader
        

        iris_test = pd.DataFrame({'sepal length (cm)':[sepal_length],
             'sepal width (cm)':[sepal_width],
             'petal length (cm)':[petal_length],
             'petal width (cm)':[petal_width]})

        model = joblib.load('/Users/tlsal/samsungsds-project/shinminyong/conver2mbti/mbti_model/is_model.pkl')

        pred = model.predict(iris_test)[0]

        return render(request, 'mbti_model/result.html', {'pred' : pred})


