
# Importing Libraries
import streamlit as st
import pandas as pd
import pickle as pl
import numpy as np


# Deserializing objects 
with open('ecoders.pkl','rb') as encoderFile:
    labelEncoders = pl.load(encoderFile)

with open('finalModel.pkl','rb') as modelFile:
    model = pl.load(modelFile)


# Building the selection boxes and putting headers
st.header('Mushroom Classification Project')

bruise = st.selectbox('Bruises',['True','False'],placeholder='Choose type of bruise',index=None)
odor = st.selectbox('Odor ',['almond', 'anise', 'creoscote', 'fishy', 'foul', 'musty', 'pungent', 'spicy', 'none'],placeholder='Choose the odor',index=None)
gillSize = st.selectbox('Gill Size',['Broad','Narrow'],placeholder='Choose the size',index=None)
gillColor = st.selectbox('Gill Color',['Black','Brown','Buff','Chocolate','Gray','Green','Orange','Pink','Purple','Red','White','Yellow'],placeholder='Choose the color',index=None)
stalkShape = st.selectbox('Stalk Shape',['Enlarging','Tapering'],placeholder='Choose the shape',index=None)
sporeColor = st.selectbox('Spore Print Color',['Black','Brown','Buff','Chocolate','Green','Orange','Purple','White','Yellow'],placeholder='Choose the spore color',index=None)
population = st.selectbox('Population', ['abundant','clustered','numerous','scattered','several','solitary'],placeholder='Choose the population distribution',index=None)



bruiseDic = {'True': 't','False': 'f'}
odorDic = {'almond': 'a', 'anise': 'l', 'creoscote': 'c' , 'fishy': 'y', 'foul': 'f', 'musty': 'm', 'none': 'n', 'pungent': 'p', 'spicy': 's'}
gillSizeDic = {'Broad': 'b','Narrow': 'n'}
gillColorDic = { 'Black':'k', 'Brown':'n' , 'Buff':'b' , 'Chocolate':'h' , 'Gray':'g' , 'Green':'r' , 'Orange':'o', 'Pink':'p', 'Purple' : 'u', 'Red':'e', 'White':'w', 'Yellow' : 'y' }
stalkShapeDic = {'Enlarging': 'e','Tapering': 't'}
sporeColorDic = { 'Black' : 'k' , 'Brown' : 'n' , 'Buff' : 'b', 'Chocolate' : 'h' , 'Green' : 'r' , 'Orange' : 'o' , 'Purple' : 'u' , 'White' : 'w' , 'Yellow' : 'y'}
populationDic = {'abundant':'a', 'clustered':'c', 'numerous':'n', 'scattered':'s', 'several':'v', 'solitary':'y'}
replaceDic = [bruiseDic,odorDic,gillSizeDic,gillColorDic,stalkShapeDic,sporeColorDic,populationDic]


# The real LOGIC

allValuesOrNot = (bruise==None) or (odor==None) or (gillColor==None) or (gillSize==None) or (stalkShape==None) or (sporeColor==None) or (population==None)
clicked = st.button("Done! ",type='primary')

if ((clicked)):

    if (allValuesOrNot==True):
        st.text("Please give values for all parameters! ")
        
    else:
        encodedDf = {}
        st.write("All parameters given! ")
        labelledDf1 = pd.DataFrame(data = {'bruises': bruise, 'odor': odor,'gill-size': gillSize,'gill-color': gillColor,'stalk-shape': stalkShape,'spore-print-color': sporeColor,'population': population},index = [0])  # columns name is as given cause labelencoding is a dic and it stores the original column names
        st.text("Raw Labeleed Data")
        st.write(labelledDf1)
        
        # This works as well
        #labelledDf1.replace(to_replace={'bruises': ['True','False'],'gill-size': ['Broad','Narrow']},value={'bruises': ['t','f'],'gill-size': ['b','n']},inplace=True)
        
        j=0
        for i in labelledDf1.columns:
          labelledDf1[i].replace(to_replace=replaceDic[j].keys(),value=replaceDic[j].values(),inplace=True)
          j+=1
        
        # st.text("Appropriate labelled data (before one label encoding)")
        # st.write(labelledDf1)
        
        encodedDf = pd.DataFrame({})
        for i in labelledDf1.columns:
            encodedDf[i] = labelEncoders[i].transform(labelledDf1[i])
            
        # st.text("Label Encoded ")
        # st.write(encodedDf)
        
        featureArr = encodedDf.to_numpy()
        # print(featureArr)
        
        prediction = model.predict(featureArr)
        # print(prediction)
        
        if(prediction[0]==0):
            st.write("This mushroom is edible")
        else:
            st.write("This mushroom is poisonous")
            




# Notes
# placeholder will be visisbible if idnex is none, when none is vosible intiially 
# .rename is for renmaing rwos and columns 
# .repalce is for repalcing the valeus in the columns


# DOubt 

# How does it update the apramters (whats the frequency)
## Streamlit reruns the entire script every time a user interaction occurs

# didnt gert he idnex paramter in pd.dataframe 