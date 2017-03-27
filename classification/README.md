# Machine Learning Classification with Python and Scikit-Learn

About the input data: It is common to order the data in chronological order.
Train an test the first 80% of it and validate with the 20% remaining.
Always sanitize text information, with tokenizer(split by ponctuation), stopwords(words with no feeling), stemmer(word root), and length(> 3).

## Requirements
* Python + pip + NumPy + SciPy + Scikit-Learn + Pandas + NLTK

## Installation
Windows 32bits + Python 2.7:
* Download pre-build Windows packages compatible with your python version and architecture from: http://www.lfd.uci.edu/~gohlke/pythonlibs/
* NumPy (pip install numpy-1.11.3+mkl-cp27-cp27m-win32.whl)
* SciPy (pip install scipy-0.19.0-cp27-cp27m-win32.whl)
* Scikit-learn (pip install scikit_learn-0.18.1-cp27-cp27m-win32.whl)
* Pandas (pip install pandas-0.19.2-cp27-cp27m-win32.whl)
* NLTK (pip install nltk-3.2.2-py2.py3-none-any.whl)

Linux:
* pip install numpy
* pip install scipy
* pip install scikit-learn
* pip install pandas
* pip install nltk

Download additional NLTK libraries:
>>> import nltk

NLTK Stopwords Corpus: nltk.download('stopwords')
Portuguese Language Sufix Remover Stemmer: nltk.download('rslp')
Ponctuation Tokenizer: nltk.download('punkt')

## Usage
Two categories classification:

```$python classify_animals.py``` - simple pig or dog classification

```$python classify_accesses.py``` - client chance to buy based on page access

```$python classify_searches.py``` - client chance to buy based on page search

Three categories classification:

```$python classify_client_situations.py``` - client feeling based on page access

```$python classify_client_situations_kfold.py``` - client feeling based on page access, using kfold

Other:

```$python classify_emails.py``` - classifying emails and categorizing it

```$python classify_cleaned_emails.py``` - classifying cleaned emails and categorizing it
