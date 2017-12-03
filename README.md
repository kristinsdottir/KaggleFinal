## Setup Instructions
Run ```pip install requirements.txt```
Please download and unzip the kaggle data into the /data directory

Run ```./keef data``` to generate tokens.csv - though it takes forever.
Instead, ask James for tokens.csv, which is a token vector per image
```
KaggleFinal/
    data/* (the data we download from our kaggle competition)
    pipeline/
    |   data/
    |    ├──tokens.csv
    |    └──tokens.json
    ├── sentence_to_tokens.py
    ├── tasks.py (tasks to tokenize words and convert to vector)
    └── tokens_to_vec.py
    keef (command line utility)
    cleaners/
    ├── sentence_cleaner.py
    └── test_sentence_cleaner.py
```
 
