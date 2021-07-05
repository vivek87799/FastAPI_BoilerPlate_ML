from mongoengine import connect


class ConnectionToDatabase:
    
    @staticmethod
    def get_conneciton():
        print("<===Connection established===>")
        return connect(db="boilerplate_db", host="mongo_host", port=27017, username="admin", password="admin", authentication_source="admin")