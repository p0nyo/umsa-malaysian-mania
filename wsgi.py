from mania import create_app
from mania.adapters.datareader.csvdatareader import CSVReader
from pathlib import Path

app = create_app()

if __name__ == "__main__":
        app.run(debug=True)
        
        
# virtualenv venv
# source venv/bin/activate
# pip3 install 'requirements.txt'