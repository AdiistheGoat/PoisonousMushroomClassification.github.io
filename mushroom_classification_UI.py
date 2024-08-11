from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle as pl

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load the model and encoders
with open('finalModel.pkl', 'rb') as model_file:
    model = pl.load(model_file)

with open('ecoders.pkl', 'rb') as encoder_file:
    labelEncoders = pl.load(encoder_file)

# Mapping dictionaries for encoding inputs
bruiseDic = {'True': 't', 'False': 'f'}
odorDic = {'almond': 'a', 'anise': 'l', 'creosote': 'c', 'fishy': 'y', 'foul': 'f', 'musty': 'm', 'none': 'n', 'pungent': 'p', 'spicy': 's'}
gillSizeDic = {'Broad': 'b', 'Narrow': 'n'}
gillColorDic = {'Black': 'k', 'Brown': 'n', 'Buff': 'b', 'Chocolate': 'h', 'Gray': 'g', 'Green': 'r', 'Orange': 'o', 'Pink': 'p', 'Purple': 'u', 'Red': 'e', 'White': 'w', 'Yellow': 'y'}
stalkShapeDic = {'Enlarging': 'e', 'Tapering': 't'}
sporeColorDic = {'Black': 'k', 'Brown': 'n', 'Buff': 'b', 'Chocolate': 'h', 'Green': 'r', 'Orange': 'o', 'Purple': 'u', 'White': 'w', 'Yellow': 'y'}
populationDic = {'abundant': 'a', 'clustered': 'c', 'numerous': 'n', 'scattered': 's', 'several': 'v', 'solitary': 'y'}

replaceDic = [bruiseDic, odorDic, gillSizeDic, gillColorDic, stalkShapeDic, sporeColorDic, populationDic]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bruise = request.form['bruise']
        odor = request.form['odor']
        gillSize = request.form['gillSize']
        gillColor = request.form['gillColor']
        stalkShape = request.form['stalkShape']
        sporeColor = request.form['sporeColor']
        population = request.form['population']

        # Check if all values are provided
        if None in [bruise, odor, gillSize, gillColor, stalkShape, sporeColor, population]:
            return render_template('index.html', error="Please provide values for all parameters.")

        # Create the DataFrame
        labelledDf1 = pd.DataFrame(data={
            'bruises': bruise,
            'odor': odor,
            'gill-size': gillSize,
            'gill-color': gillColor,
            'stalk-shape': stalkShape,
            'spore-print-color': sporeColor,
            'population': population
        }, index=[0])

        # Replace with encoded values
        j = 0
        for i in labelledDf1.columns:
            labelledDf1[i].replace(to_replace=replaceDic[j].keys(), value=replaceDic[j].values(), inplace=True)
            j += 1

        # Encode the DataFrame
        encodedDf = pd.DataFrame({})
        for i in labelledDf1.columns:
            encodedDf[i] = labelEncoders[i].transform(labelledDf1[i])

        # Predict using the model
        featureArr = encodedDf.to_numpy()
        prediction = model.predict(featureArr)

        result = "This mushroom is edible" if prediction[0] == 0 else "This mushroom is poisonous"
        return render_template('result.html', prediction=result, data=request.form)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
