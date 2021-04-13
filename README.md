# Directional Stock Prediction using news and viral tweets

## Install Dependencies

```
pip install pandas transformers sklearn nltk
```

Start the Jupyter notebook server

```
jupyter notebook
```

## Data preprocessing

There are two files for initial mapping of Charts and Stocks datasets

1. `Code/Para_Extracter.py` - Extracting paragraphs from news dataset
2. `Code/ParaPrice_Mapper.py` - Map stock price chart with extracted paragraphs

Run these two files in order to create the mapped dataset, which will be used in all further notebooks

## Twitter Data Extraction

There are three notebooks:

1. `Code/Twitter Stock volume extraction.ipynb` - Extract recent tweets for a particular stock symbol.
2. `Code/Twitter Breakout.ipynb` - Detecting breakout hours from extracted tweets
3. `Code/Web Content Extraction.ipynb` - Extract news URL contents scraped from tweets

## Model Training

1. `Code/Stock_Models.ipynb` - Contains code for training the following algorithms: XGBoost, Decision tree, SVC, Naive Bayes, Random forest, Logistic regression
2. `Code/gpt2classifier_recent_news.ipynb` - GPT-2 classifier

## Model Evaluation

1. `Code/Model earnings.ipynb` - Logic for evaluating ROIs for any given prediction output
