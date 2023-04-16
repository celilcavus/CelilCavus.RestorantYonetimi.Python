import MySqlConnection as base


class MenuController(base.RestorantYonetimi):
    def __init__(self, table_name) -> None:
        self.table_name = table_name
        super().__init__(self.table_name)

    def InsertMenu(self, *args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            F"INSERT INTO {self.table_name} (YemekAdi,YemekFiyat,YemekTarif,YemekKategori) values (%s,%s,%s,%s)", (args))
        self.mydb.commit()
        print("işlem başarili")

    def UpdateMenu(self, *args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}' AND ORDINAL_POSITION = 1")
        result = self.mycursor.fetchone()
        for column_name in result:
            self.mycursor.execute(
                F"UPDATE {self.table_name} SET YemekAdi = %s ,YemekFiyat = %s,YemekTarif= %s,YemekKategori= %s WHERE {column_name} = %s ", (args))
            self.mydb.commit()
            print("Update Başarili")







# r1 = MenuController("menu")
# r1.InsertMenu("tarhana",30,"yok","çorba")
# r1.GetAll()
# r1.UpdateMenu("tarhana",30,"Tarhana çorbası domates","çorba",2)
# r1.DeleteMenu(2)
# r1.UpdateMenu(tarhana = "adas")

# list = {
#     "tarhana",
#     30,
#     "domates",
#     "corba"
# }

