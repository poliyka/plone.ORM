# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

from plone.ORM.browser.engine import Engine
from plone.ORM.models.user import User
from sqlalchemy.orm import aliased

class Test(BrowserView):
    
    def get_db_and_session(self):
        engine = Engine()
        return engine.db_session()
    
    def insert_data(self, session):
        ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
        session.add(ed_user)
        session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')]
        )
        session.commit()
    
    def base_use(self, db):
        with db.connect() as conn:
            sqlString = "select name from users"
            result = conn.execute(sqlString)
            for row in result:
                print("name:", row['name'])
    
    def session_search(self, session):
        for instance in session.query(User).order_by(User.id):
            print(instance.name, instance.fullname)
        
        for row in session.query(User, User.name).all():
            print(row.User, row.name)

        for row in session.query(User.name.label('name_label')).all():
            print(row.name_label)
    
    def aliased_search(self, session):
        user_alias = aliased(User, name='user_alias')
        for row in session.query(user_alias, user_alias.name).all():
            print(row.user_alias)
    
    def query_filter(self, session):
        for name, in session.query(User.name).\
                    filter(User.fullname=='Ed Jones'):
            print(name)
        
        # *Reference https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping
        
        # ColumnOperators.__eq__():
        session.query.filter(User.name == 'ed')
        # ColumnOperators.__ne__():
        session.query.filter(User.name != 'ed')
        # ColumnOperators.like():
        session.query.filter(User.name.like('%ed%'))
        # ColumnOperators.ilike() (case-insensitive LIKE):
        session.query.filter(User.name.ilike('%ed%'))
        # ColumnOperators.in_():
        session.query.filter(User.name.in_(['ed', 'wendy', 'jack']))
        # ColumnOperators.notin_():
        session.query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
        
        # ColumnOperators.is_():
        session.query.filter(User.name == None)
        #! alternatively, if pep8/linters are a concern
        session.query.filter(User.name.is_(None))
        
        # ColumnOperators.isnot():
        session.query.filter(User.name != None)
        #! alternatively, if pep8/linters are a concern
        session.query.filter(User.name.isnot(None))
        
        # AND:
        # use and_()
        from sqlalchemy import and_
        session.query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
        #! or send multiple expressions to .filter()
        session.query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
        #! or chain multiple filter()/filter_by() calls
        session.query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
        
        #OR:
        from sqlalchemy import or_
        session.query.filter(or_(User.name == 'ed', User.name == 'wendy'))
        
        #ColumnOperators.match():
        session.query.filter(User.name.match('wendy'))
        # Query.all() returns a list:
        session.query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
        session.query.all()
        # Query.first() applies a limit of one and returns the first result as a scalar:
        session.query.first()
        # Query.one_or_none()
        session.query.one_or_none()
        # Using Textual SQL
        from sqlalchemy import text
        for user in session.query(User).\
                    filter(text("id<224")).\
                    order_by(text("id")).all():
            print(user.name)
        
        # Bind parameters can be specified with string-based SQL, using a colon. To specify the values, use the Query.params() method:
        session.query(User).filter(text("id<:value and name=:name")).\
                params(value=224, name='fred').order_by(User.id).one()
        
            
    def __call__(self):
        request = self.request
        portal = api.portal.get()
        db, session = self.get_db_and_session()
        
        # *Demo function
        # self.insert_data(session)
        self.base_use(db)
        # self.session_search(session)
        # self.aliased_search(session)
        # self.query_filter(session)
        
        return "Testing done"
