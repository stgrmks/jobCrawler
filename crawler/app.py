# coding: utf-8
__author__ = 'MSteger'

from crawler.db.db import jobs, connect_and_create, select_desc, select_interested_desc, select_last24h
from crawler.db.settings import MySQL_config
from flask import Flask, render_template, request
from crawler.helpers import timeDiffDays

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    engine, session = connect_and_create(**MySQL_config)
    job_query = select_desc(session = session, table = jobs, to_dict=True, limit = 10000)
    for job in job_query: job['date'] = timeDiffDays(job['date'])
    return render_template('index.html', job_query = job_query)

@app.route('/interested')
def interested():
    engine, session = connect_and_create(**MySQL_config)
    job_query = select_interested_desc(session=session, table=jobs, to_dict=True)
    for job in job_query: job['date'] = timeDiffDays(job['date'])
    return render_template('index.html', job_query = job_query)

@app.route('/last24h')
def last24h():
    engine, session = connect_and_create(**MySQL_config)
    job_query = select_last24h(session=session, table=jobs, to_dict=True)
    for job in job_query: job['date'] = timeDiffDays(job['date'])
    return render_template('index.html', job_query = job_query)

@app.route('/update', methods = ['POST'])
def update(): #TODO
    if request.method == 'POST': return render_template('index.html')

if __name__== '__main__':
    app.run()