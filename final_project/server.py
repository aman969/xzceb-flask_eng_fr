from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishText=translator.english_to_french(textToTranslate)
    return englishText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchText=translator.french_to_english(textToTranslate)
    return frenchText

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
