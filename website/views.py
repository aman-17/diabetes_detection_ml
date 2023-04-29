from os import abort
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask.globals import session
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")

views = Blueprint('views',__name__,template_folder="templates/",static_folder="../static/")

df = pd.read_csv('./diabetes_012_health_indicators_BRFSS2015.csv')
df.isnull().sum()
df.dropna(inplace = True)
duplicate = df[df.duplicated()]
df['Diabetes_012'] = df['Diabetes_012'].astype('int')
df['HighBP'] = df['HighBP'].astype('int')
df['HighChol'] = df['HighChol'].astype('int')
df['CholCheck'] = df['CholCheck'].astype('int')
df['BMI'] = df['BMI'].astype('int')
df['Smoker'] = df['Smoker'].astype('int')
df['Stroke'] = df['Stroke'].astype('int')
df['HeartDiseaseorAttack'] = df['HeartDiseaseorAttack'].astype('int')
df['PhysActivity'] = df['PhysActivity'].astype('int')
df['Fruits'] = df['Fruits'].astype('int')
df['Veggies'] = df['Veggies'].astype('int')
df['HvyAlcoholConsump'] = df['HvyAlcoholConsump'].astype('int')
df['AnyHealthcare'] = df['AnyHealthcare'].astype('int')
df['NoDocbcCost'] = df['NoDocbcCost'].astype('int')
df['GenHlth'] = df['GenHlth'].astype('int')
df['MentHlth'] = df['MentHlth'].astype('int')
df['PhysHlth'] = df['PhysHlth'].astype('int')
df['DiffWalk'] = df['DiffWalk'].astype('int')
df['Sex'] = df['Sex'].astype('int')
df['Age'] = df['Age'].astype('int')
df['Education'] = df['Education'].astype('int')
df['Income'] = df['Income'].astype('int')
X = df.drop('Diabetes_012', axis=1)
y = df['Diabetes_012']

def labels(new_data):
    loaded_model = pickle.load(open('./logistic_regression_model.sav', 'rb'))
    predictions = loaded_model.predict(new_data)
    probabilities = loaded_model.predict_proba(new_data)
    print('Probabilities:', probabilities[0])
    if predictions == 0:
        labels = 'Non-Diabetic'
    elif predictions == 1:
        labels = 'Pre-Diabetic'
    elif predictions == 2:
        labels = 'Diabetic'
    return labels, probabilities[0]

@views.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        ab = request.form.get('1')
        ab1 = request.form.get('2')
        ab2 = request.form.get('3')
        ab3 = request.form.get('4')
        ab4 = request.form.get('5')
        ab5 = request.form.get('6')
        ab6 = request.form.get('7')
        ab7 = request.form.get('8')
        ab8 = request.form.get('9')
        ab9 = request.form.get('10')
        ab10 = request.form.get('11')
        ab11 = request.form.get('12')
        ab12 = request.form.get('13')
        ab13 = request.form.get('14')
        ab14 = request.form.get('15')
        ab15 = request.form.get('16')
        ab16 = request.form.get('17')
        ab17 = request.form.get('18')
        ab18 = request.form.get('19')
        ab19 = request.form.get('20')
        ab20 = request.form.get('21')

        new_data = np.array([[int(ab),int(ab1),int(ab2),int(ab3),int(ab4),int(ab5),int(ab6),int(ab7),int(ab8),int(ab9),int(ab10),int(ab11),int(ab12),int(ab13),int(ab14),int(ab15),int(ab16),int(ab17),int(ab18),int(ab19),int(ab20)]])
        result=labels(new_data)
        return render_template("report.html",pred=result[0], prob = result[1])
    return render_template("enterdetails.html")