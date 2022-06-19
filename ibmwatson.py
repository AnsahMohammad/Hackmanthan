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

natural_language_understanding.set_service_url('{url')


def getEmotions(data):
    emotions = []
    response_emo = natural_language_understanding.analyze(
    text = data,
    features = Features( emotion=EmotionOptions())
    ).get_result() 


    for i in list(response_emo['emotion']['document']['emotion'].keys()):
        emotions.append([i, str(response_emo['emotion']['document']['emotion'][i])])
    
    return response_emo['emotion']['document']['emotion'], emotions    


