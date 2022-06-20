import streamlit as st
import ibmwatson as ibm
import os
import shutil
from instaloader import Post
import instaloader

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions, EmotionOptions, KeywordsOptions, EntitiesOptions

authenticator = IAMAuthenticator('{api}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

st.header("S.W.A.G Tone Analyser")

radioChoice = st.radio('Analyse Text from', ['Text', 'URL'])
if radioChoice == 'Text':
    data = st.text_area('Analyse Your Text')

    if st.button('Analyse'):
        emotionsList, max_emotion, emo_dict = ibm.getEmotions(data)
        st.success('Your text is analysed!')
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        for i in emotionsList:
            col1.write(i[0])
            col2.write(i[1])
        print(emotionsList)

        keywords, sentiments, score = ibm.getKeywords(data)
        for i in keywords:
            col3.write(i)
        for j in sentiments:    
            col4.write(j)
        col5.write('Sentiment Score')
        col5.write(score)

        if score < -0.7:
            if max_emotion == 'joy' or emo_dict['joy'] > '0.55':
                col6.write('Not HATEFUL')    
            elif max_emotion == 'anger' and emo_dict['fear'] > '0.05' and emo_dict['disgust'] > '0.05':
                col6.write('HATEFUL & Inflammatory')
            elif max_emotion == 'sadness' and emo_dict['anger'] > '0.1':
                col6.write('HATEFUL')
            elif max_emotion == 'disgust':
                if emo_dict['disgust'] > '0.2' and emo_dict['anger'] > '0.05':
                    col6.write('HATEFUL')
                elif emo_dict['anger'] > '0.1':
                    col6.write('HATEFUL')  
        elif emo_dict['disgust'] > '0.17' and emo_dict['anger'] > '0.05':
            col6.write('HATEFUL')
        elif max_emotion == 'sadness' and emo_dict['anger'] > '0.1':
                col6.write('HATEFUL')    


