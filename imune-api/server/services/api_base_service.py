from server.database.database import db


class ApiBaseService:

    def __init__(self):
        self.db = db
