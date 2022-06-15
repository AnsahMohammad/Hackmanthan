import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions, EmotionOptions, KeywordsOptions


# Adding the API Key
authenticator = IAMAuthenticator('{api key}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
                                          version='2022-04-07',
                                          authenticator=authenticator
                                          )


# Adding the url
natural_language_understanding.set_service_url('{url}')


# Fetching the analysed response from the NLU Tool for "Categories"
response1 = natural_language_understanding.analyze(
                                          url = 'https://www.linkedin.com/posts/garvit-shah-1287001b8_internship-design-team-activity-6891667234469539840-i0s7?utm_source=linkedin_share&utm_medium=member_desktop_web',
                                          features = Features( categories=CategoriesOptions(limit=3))
                                          ).get_result()  
print(response1['categories'])


# Fetching the analysed response from the NLU Tool for "Emotions"
response2 = natural_language_understanding.analyze(
                                          url = 'https://www.linkedin.com/posts/garvit-shah-1287001b8_internship-design-team-activity-6891667234469539840-i0s7?utm_source=linkedin_share&utm_medium=member_desktop_web',
                                          features = Features( emotion=EmotionOptions())
                                          ).get_result()  

for i in list(response2['emotion']['document']['emotion'].keys()):                
     print(i + ' - ', response2['emotion']['document']['emotion'][i])             


# Fetching the analysed response from the NLU Tool for "Keywords" combined with emotions and sentiments
response3 = natural_language_understanding.analyze(
                                          url = 'https://www.linkedin.com/posts/garvit-shah-1287001b8_internship-design-team-activity-6891667234469539840-i0s7?utm_source=linkedin_share&utm_medium=member_desktop_web',
                                          features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True))
                                          ).get_result()     

print(json.dumps(response3, indent=4))
