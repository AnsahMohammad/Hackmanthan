# Hackmanthan
# Tone Analyser - Using IBM Watson Natural Language Understanding API

The ibmwatson.py is custom made module with is imported in the Proto1 to use the following functions - 
 - Fetching the emotion:score pairs 
   • getEmotions(data): data is the text input given by the user. It returns 3 things - List containing the emotion:score pairs, Emotion with maximum emotion score, dictionary form of emotion:score pairs.
      
 - Fecting keywords that are analysed for the sentiments
   • getKeywords(data): data is the text input given by the user. It also returns 3 things - list containing the keywords, their sentiments and their sentiment-scores.
