from flask import Flask, request
from Database.database import Database
from wiki_bot import run as robot
import logging, logging.config 
import json


def configureLogger():
    with open('F:\Python\Proiecte A\Wikipedia Crawler\Config\\apiLoggerConfig.json', 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config=config)

app = Flask(__name__)

@app.route("/top10-tari-arie", methods=["GET"])
def getTop10CountriesByArea():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /top10-tari-arie with url parameters')
    with Database() as connection:
        response = connection.getTopTenBy('Total Area')
        return response

@app.route("/top10-tari-populatie", methods=["GET"])
def getTop10CountriesByPopulation():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /top10-tari-populatie with url parameters')
    with Database() as connection:
        response = connection.getTopTenBy('estimate')
        return response

@app.route("/top10-tari-densitate", methods=["GET"])
def getTop10CountriesByDensity():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /top10-tari-densitate with url parameters')
    with Database() as connection:
        response = connection.getTopTenBy('Density')
        return response

@app.route("/regim-politic", methods=['GET'])
def getCountriesByGovernment():
    government = request.args.get('politicalRegime', default='monarchy', type=str)
    logger=logging.getLogger(__name__)
    logger.info(f'GET Request to /regim-politic with url parameters {government}')
    with Database() as connection:
        response = connection.getCountriesByGovernment(government)
        return response

@app.route("/countries-with-english-language", methods=["GET"])
def getCountriesWhoSpeakEnglish():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /countries-with-english-language with url parameters')
    with Database() as connection:
        return connection.getCountriesByLanguage('English')

@app.route('/countries-with-GMT+2', methods=['GET'])
def getCountriesByTimezone():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /countries-with-UTC+2 with url parameters')
    with Database() as connection:
        return connection.getCountriesByTimezone('UTC+2')

@app.route('/get-capital', methods=['GET'])
def getCapital():
    countries = request.args.get('countries', default=['France'], type=list[str])
    countries = ''.join(countries).split(',')
    logger=logging.getLogger(__name__)
    logger.info(f'GET Request to /get-capital with url parameters {countries}')
    with Database() as connection:
        responseQuery = {}
        for country in countries:
            responseQuery.setdefault(country, connection.getCountryCapital(country))
    return responseQuery

@app.route('/get-language-statistics', methods=['GET'])
def getLanguageStatistics():
    logger=logging.getLogger(__name__)
    logger.info('GET Request to /get-language-statistics with url parameters')
    with Database() as connection:
        return connection.getLanguageStatistics()
    

@app.route('/get-largest-city', methods=['GET'])
def getLargestCity():
    countries = request.args.get('countries', default=['France'], type=list[str])
    countries = ''.join(countries).split(',')
    logger.info(f'GET Request to /get-largest-city with url parameters {countries}')
    with Database() as connection:
        responseQuery = {}
        for country in countries:
            responseQuery.setdefault(country, connection.getCountryLargestCity(country))
    return responseQuery

@app.route('/get-countries-by-language', methods=['GET'])
def getCountriesByLanguage():
    languages = request.args.get('languages', default=['Romanian, English, French'], type=list[str])
    languages = ''.join(languages).split(',')
    logger.info(f'GET Request to /get-largest-city with url parameters {languages}')
    print(languages)
    with Database() as connection:
        responseQuery =[]
        for lang in languages:
            responseQuery.append(connection.getCountriesByLanguage(lang))
    return responseQuery


@app.route('/')
def getMessage():
    return "Hello World"

if __name__ == '__main__':
    # robot()
    configureLogger()
    logger = logging.getLogger(__name__)
    logger.info('Initiating the API...')
    app.run(debug=True)