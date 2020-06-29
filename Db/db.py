from App.app import db
from sqlalchemy.ext.automap import automap_base


class Db:

    # def __init__(self):
    #     self.Db = db
    #     self.Base = automap_base()
    #     self.Base.prepare(db.engine, reflect=True)

    Db = db
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    def get_table(self, table_name):
        """

        :type table_name: String
        """
        table_instance = getattr(self.Base.classes, table_name)
        table = db.session.query(table_instance()).all()
        return table

