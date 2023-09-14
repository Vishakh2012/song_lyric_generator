from flask import render_template, redirect, url_for, request
from app import app
import numpy as np
import tensorflow as tf
import pickle


#Tokenizer = tf.keras.preprocessing.text.Tokenizer
model_from_json = tf.keras.models.model_from_json 
lyrics = ""

with open("app/model/tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)
    
# load json and create model
json_file = open('app/model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("app/model/model.h5")
print("Loaded model from disk")



@app.route("/")
def project():
    return render_template("project.html")

@app.route("/about")
def project():
    return render_template("about.html")

def predict_lyrics(seed :str):
    
    num_words = 300 
    print("started")
    print([seed])

    try:
        for _ in range(num_words):
            seed = seed.strip().lower()
            tok_sen = tokenizer.texts_to_sequences([seed])[0]
            pad_sequence = tf.keras.preprocessing.sequence.pad_sequences

            pad_tok_sen = pad_sequence([tok_sen], maxlen= 1986 , padding="pre", truncating="pre")
            
            next_word_index = np.argmax(model.predict(pad_tok_sen), axis= -1 )
            next_word = ""
            for word,index in tokenizer.word_index.items():
                if index == next_word_index:
                    next_word = word
                    break   
                   
                
            seed += " " + next_word
        words = seed.split()
        for i in range(0, len(words), 4):
            line = ' '.join(words[i:i+4])
            print(line + "\n")

    except:
        print("some error with code")
    
    return seed
    
    

@app.route("/submit" , methods = ["POST", "GET"])
def predict():
    if request.method == "POST":
        seed_text = str(request.form["lyrics"])
    lyrics = predict_lyrics(seed_text)
    
    
    return render_template("project.html", lyrics = lyrics)
