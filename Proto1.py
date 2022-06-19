import streamlit as st
import ibmwatson as ibm

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions, EmotionOptions, KeywordsOptions, EntitiesOptions

authenticator = IAMAuthenticator('Uj0kpwPhaj99JT04MYpaAtOuOlLc4YoOMMNRu3hMS1Sc')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

st.header("S.W.A.G Tone Analyser")

k = st.radio('Analyse Text from', ['Text', 'URL'])
if k == 'Text':
    data = st.text_input('Analyse Your Text')

    if st.button('Analyse'):
        emotionsJson, emotionsList = ibm.getEmotions(data)
        st.success('Your text is analysed!')
    # st.json(emotionsJson)
    # st.balloons()
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        for i in emotionsList:
            col1.write(i[0])
            col2.write(i[1])
        print(emotionsList)
