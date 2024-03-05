from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

def translate(text, dest_lang) -> str:
    """
    Translates text to the specified destination language using Google Translate API.
    """
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest=dest_lang)
    return translated_text.text

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        text_input = request.form.get("text_input")
        dest_lang = request.form.get("dest_lang")
        lang_dict = {"Hindi": "hi", "Malayalam": "ml", "Kannada": "kn", "Tamil": "ta"}
        selected_lang = lang_dict.get(dest_lang, "en")
        translated_text = translate(text_input, selected_lang)
        return render_template("index.html", translated_text=translated_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
