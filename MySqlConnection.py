import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="celil123",
    database="restorantyonetimi"
)

class RestorantYonetimi():
    def __init__(self, table_name) -> None:
        self.mydb = db
        self.table_name = table_name
        # Database sütün sayılarını yakalıyorum
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COUNT(*) FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}'")
        self.result = self.mycursor.fetchone()

    def GetAll(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(F"SELECT * FROM {self.table_name}")
        values = self.mycursor.fetchall()
        for i in range(0, self.result[0]):
            for x in values:
                print(x[i])

    def GetById(self, id):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}' AND ORDINAL_POSITION = 1")
        result = self.mycursor.fetchone()
        for column_name in result:
            self.mycursor.execute(
                f"SELECT * FROM {self.table_name} WHERE {column_name} = {id}")
            values = self.mycursor.fetchone()
            for i in values:
                print(i)

    def Delete (self, id):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}' AND ORDINAL_POSITION = 1")
        result = self.mycursor.fetchone()
        for column_name in result:
            self.mycursor.execute(
                f"DELETE FROM {self.table_name} WHERE {column_name} = {id}")
            self.mydb.commit()
            print("DELETED BAŞARILI")
