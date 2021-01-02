import sqlalchemy as sa
from plone.ORM.models import Base


class Store(Base):
    __tablename__ = 'stores'
    
    id = sa.Column(sa.Integer, primary_key=True)
    store_id = sa.Column(sa.Integer, unique=True)
    store_name = sa.Column(sa.String)
    store_area = sa.Column(sa.String)
    create_time = sa.Column("Testing create time", sa.DateTime, server_default=sa.text('NOW()'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL"))
    
    def __repr__(self):
        return f"<Store(name='{self.store_name}')>"
