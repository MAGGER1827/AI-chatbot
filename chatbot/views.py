from django.shortcuts import render
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
import json
import random
from django.http import HttpResponse, JsonResponse

# Load ML assets
try:
    model = load_model(r'E:\Chatbot\chat\files\model_new.h5')
    intents = json.loads(open(r'E:\Chatbot\chat\files\new_intent.json').read())
    words = pickle.load(open(r'E:\Chatbot\chat\files\words.pkl', 'rb'))
    classes = pickle.load(open(r'E:\Chatbot\chat\files\classes.pkl', 'rb'))
except Exception as e:
    raise Exception(f"Failed to load ML assets: {str(e)}")

def index(request):
    return render(request, 'webbot/index.html')

def bot_search(request):
    if request.method == 'GET':
        # Redirect GET to the index page so no old data is shown
        return render(request, 'webbot/index.html')

    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    sentence = request.POST.get('query', '').strip()
    
    if not sentence:
        return render(request, 'webbot/index.html', {
            'error': 'Please enter a valid query'
        })
    
    try:
        response = chatbot_response(sentence)
    except Exception as e:
        response = "I'm experiencing technical difficulties. Please try again later."
    
    return render(request, 'webbot/index.html', {
        'response': response,
        'sentence': sentence
    })

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"found in bag: {w}")
    return np.array(bag)

def predict_class(sentence, model):
    try:
        p = bow(sentence, words)
        res = model.predict(np.array([p]))[0]
        
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": float(r[1])})
            
        return return_list
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return []

def chatbot_response(msg):
    DEFAULT_RESPONSE = "I'm not sure about that question. For further details, please contact the representative."
    MIN_CONFIDENCE = 0.80
    
    if not msg or not msg.strip():
        return DEFAULT_RESPONSE
    
    try:
        ints = predict_class(msg, model)
        
        # If no intent meets the threshold or confidence is too low
        if not ints or ints[0]['probability'] < MIN_CONFIDENCE:
            return DEFAULT_RESPONSE
        
        # If we have a matching intent with sufficient confidence
        tag = ints[0]['intent']
        for i in intents['intents']:
            if i['tag'] == tag:
                return random.choice(i['responses'])
        
        return DEFAULT_RESPONSE
    except Exception as e:
        print(f"Chatbot error: {str(e)}")
        return "I'm having trouble understanding that. Please try again."