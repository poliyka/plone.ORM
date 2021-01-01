from sqlalchemy import create_engine
from plone.ORM.browser.siteSetting import ISiteSetting
from plone import api
from sqlalchemy.orm import sessionmaker

class Engine:
    def __init__(self):
        self.dbString = api.portal.get_registry_record('dbString', interface=ISiteSetting)
        
    def connect_db(self):
        return create_engine(self.dbString, echo=True)
    
    def db_session(self):
        db = self.connect_db()
        Session = sessionmaker(bind=db)
        return db, Session()