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

natural_language_understanding.set_service_url('{url}')


def getEmotions(data):
    emotions = []
    emotions_dict = {}
    emotions_scores = []
    response_emo = natural_language_understanding.analyze(
                    text = data,
                    features = Features( emotion=EmotionOptions())
                    ).get_result() 

    for i in list(response_emo['emotion']['document']['emotion'].keys()):
        emotions.append([i, str(response_emo['emotion']['document']['emotion'][i])])
        emotions_scores.append(str(response_emo['emotion']['document']['emotion'][i]))

    for i in list(response_emo['emotion']['document']['emotion'].keys()):
        emotions_dict[i] = str(response_emo['emotion']['document']['emotion'][i])   

    emotions_scores.sort()

    for e in emotions:
        print(e)
        if emotions_scores[-1] == e[1]:
            print('Check')
            max_emo = e[0]    

    return emotions, max_emo, emotions_dict    

def getKeywords(data):
    Keywords = []
    Sentiments = []
    score = 0
    response_keyw = natural_language_understanding.analyze(
                    text = data,
                    features=Features(keywords=KeywordsOptions(sentiment=True, limit=10))).get_result()

    i = 0
    print('\n')
    while i < len(response_keyw['keywords']):
        Keywords.append(response_keyw['keywords'][i]['text'])
        Sentiments.append(response_keyw['keywords'][i]['sentiment']['label'])
        score += response_keyw['keywords'][i]['sentiment']['score']
        i+=1
        
    return Keywords, Sentiments, score/(len(Keywords))
    # return response_keyw['keywords']


