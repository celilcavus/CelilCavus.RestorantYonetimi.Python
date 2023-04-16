import MySqlConnection as my


class PersonelController(my.RestorantYonetimi):
    def __init__(self, table_name) -> None:
        super().__init__(table_name)

    def InsertPersonel(self, *args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            F"INSERT INTO {self.table_name}(persAdi,persSoyadi,PersPozisyon,PersMaas) values ( %s, %s, %s, %s)", (args))
        self.mydb.commit()

    def UpdatePersonel(self, *args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}' AND ORDINAL_POSITION = 1")
        result = self.mycursor.fetchone()
        for column_name in result:
            self.mycursor.execute(
                F"UPDATE SET {self.table_name} (persAdi = %s, persSoyadi = %s PersPozisyon = %s ,PersMaas = %s WHERE {column_name} = {id}")
        self.mydb.commit()
