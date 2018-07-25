__author__ = 'MSteger'

import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime())
    title = Column(String(250))
    company = Column(String(250))
    location = Column(String(250))
    link = Column(String(1000))
    interesting = Column(Boolean)

def connect_and_create(host='localhost', port=3306, user='jobCrawler', pw='test', db='jobCrawler', **engine_kwargs):
    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(user, pw, host, port, db),**engine_kwargs)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(bind=engine)
    return engine, session

def record_exists(session, table, filter_logic):
    return session.query(table).filter_by(**filter_logic).scalar() is not None

def commit(session, entry):
    session.add(entry)
    session.commit()
    return

def select_desc(session, table, limit = 500, to_dict = False):
    query = session.query(table).order_by(jobs.date.desc()).limit(limit)
    if to_dict:
        query = [item.__dict__ for item in query]
        for q in query: del q['_sa_instance_state']
    return query

def select_interested_desc(session, table, to_dict = False):
    query = session.query(table).filter(table.interesting == True).order_by(jobs.date.desc())
    if to_dict:
        query = [item.__dict__ for item in query]
        for q in query: del q['_sa_instance_state']
    return query

def select_last24h(session, table, to_dict = False):
    threshold = datetime.datetime.now() - datetime.timedelta(hours=24)
    query = session.query(table).filter(table.date >= threshold).order_by(jobs.date.desc())
    if to_dict:
        query = [item.__dict__ for item in query]
        for q in query: del q['_sa_instance_state']
    return query

if __name__== '__main__':
    engine, session = connect_and_create()
    query = select_last24h(session = session, table = jobs, to_dict=True)
    if not record_exists(session = session, table = jobs, filter_logic={'title': 'test'}):
        entry = jobs(date='2018-07-15 12:30:30', title='test', company='test GmbH', location='Munich', link='http://test.github.com', interesting = True)
        commit(session = session, entry = entry)
        print 'INSERT: {}'.format(entry)
    print 'done'