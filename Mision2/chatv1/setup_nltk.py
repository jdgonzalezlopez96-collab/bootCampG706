import nltk
try:
    nltk.download('punkt')
except Exception as e:
    print("NLTK setuo ",e)