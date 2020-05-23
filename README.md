# Peake-Harvest
Repo for Peake Harvest Project


## Getting started
This repo uses python 3.6+, so make sure that version of Python is downloaded

* Clone the repo to a local folder
* Create a virtual environment
```bash
python3 -m venv MY_NEW_VIRTUAL_ENV
```
```bash
source MY_NEW_VIRTUAL_ENV/bin/activate
```

* Install the dependencies
```bash
pip install -r requirements.txt
```

* Connect to Google sheets API
    - Visit this [link](https://developers.google.com/sheets/api/quickstart/python) and click on `Enable the Google Sheets API`\
    - Save the `credentials.json` file



* Copy the `.example.env` file into a new file called `.env`
```bash
cp .example.env .env
```