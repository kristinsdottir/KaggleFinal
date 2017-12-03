## Setup Instructions
Run ```pip install requirements.txt```
Please download and unzip the kaggle data into the /data directory

Run ```python pipeline.py``` to generate tokens.csv - though it takes forever.
Instead, ask James for tokens.csv, which is a token vector per image
```
KaggleFinal/
    data/* (the data we download from our kaggle competition)
    pipeline/
    |   data/
    |    ├──tokens.csv
    |    └──tokens.json
    ├── sentence_to_tokens.py
    └── tokens_to_vec.py
    pipeline.py (runs scripts to tokenize words and convert to vector)
    cleaners/
    ├── sentence_cleaner.py
    └── test_sentence_cleaner.py
    Collaborative Filtering.ipynb
```
 
