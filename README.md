# Machine Learning Sandbox with Python and Scikit-Learn

## Requirements
* Python + pip + NumPy + SciPy + Scikit-Learn + Pandas

## Installation
Windows 32bits + Python 2.7:
* Download pre-build Windows packages compatible with your python version and architecture from: http://www.lfd.uci.edu/~gohlke/pythonlibs/
* NumPy (pip install numpy-1.11.3+mkl-cp27-cp27m-win32.whl)
* SciPy (pip install scipy-0.19.0-cp27-cp27m-win32.whl)
* Scikit-learn (pip install scikit_learn-0.18.1-cp27-cp27m-win32.whl)
* Pandas (pip install pandas-0.19.2-cp27-cp27m-win32.whl)

Linux:
* pip install numpy
* pip install scipy
* pip install scikit-learn
* pip install pandas


## Usage
Two categories classification:

```$python classify_animals.py``` - simple pig or dog classification

```$python classify_accesses.py``` - client chance to buy based on page access

```$python classify_searches.py``` - client chance to buy based on page search

Three categories classification:

```$python classify_client_situations.py``` - client feeling based on page access

```$python classify_client_situations_kfold.py``` - client feeling based on page access, using kfold
