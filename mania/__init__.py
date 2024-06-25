from flask import Flask, render_template
from flask import request
from mania.adapters.datareader.csvdatareader import CSVReader
from pathlib import Path

def create_app():
    app = Flask(__name__)
    
    data_path = Path("mania") / "adapters" / "data" / "maniadata.csv"
    
    file = CSVReader(data_path)
    question_answer = file.read_file()
    
    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    @app.route('/question', methods=['GET'])
    def question():
        number = request.args.get('number')
        return render_template('question.html', 
                               question=question_answer[int(number)-1][0].question, 
                               number=number,
                               A1=(question_answer[int(number)-1][1].a1)[0], 
                               A2=(question_answer[int(number)-1][1].a2)[0], 
                               A3=(question_answer[int(number)-1][1].a3)[0], 
                               A4=(question_answer[int(number)-1][1].a4)[0], 
                               A5=(question_answer[int(number)-1][1].a5)[0], 
                               A6=(question_answer[int(number)-1][1].a6)[0], 
                               A7=(question_answer[int(number)-1][1].a7)[0], 
                               A8=(question_answer[int(number)-1][1].a8)[0], 
                               A1P=(question_answer[int(number)-1][1].a1)[1], 
                               A2P=(question_answer[int(number)-1][1].a2)[1],
                               A3P=(question_answer[int(number)-1][1].a3)[1], 
                               A4P=(question_answer[int(number)-1][1].a4)[1], 
                               A5P=(question_answer[int(number)-1][1].a5)[1], 
                               A6P=(question_answer[int(number)-1][1].a6)[1], 
                               A7P=(question_answer[int(number)-1][1].a7)[1], 
                               A8P=(question_answer[int(number)-1][1].a8)[1])
    
    return app
# cd Documents/Personal/Projects

# virtualenv venv
# source venv/bin/activate
# pip install <packages>