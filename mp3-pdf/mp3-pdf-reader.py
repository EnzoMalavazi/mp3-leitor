import pyttsx3
from pypdf import PdfReader
from flask import Flask, request, render_template
import os


#insert name of your pdf 
def pdf_reader(path: str):

    pdf_reader = PdfReader(path)
    speaker = pyttsx3.init()
    print('olá')

    for page_num in range(len(pdf_reader.pages)):

        text = pdf_reader.pages[page_num].extract_text()

        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    #name mp3 file whatever you would like
    speaker.save_to_file(clean_text, 'story.mp3')
    speaker.runAndWait()

    speaker.stop()


app = Flask(__name__)

@app.route('/')

def index():
    return render_template('front-html.html')

@app.route('/upload', methods=['POST'])
def upload():
    print("oi")
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo enviado'

    arquivo = request.files['arquivo']
    
    arquivo.save(os.path.join('uploads', arquivo.filename))
    
    return " tudo ok "


app.run(debug=True)


