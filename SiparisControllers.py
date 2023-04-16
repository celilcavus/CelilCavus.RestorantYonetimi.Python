import MySqlConnection as base

class SiparisControllers(base.RestorantYonetimi):
    def __init__(self, table_name) -> None:
        super().__init__(table_name)
    
    def InsertSiparis(self,*args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(F"INSERT INTO {self.table_name} (SiparisMusteriAdi,SiparisToplamUcret) values (%s,%s)",(args))
        self.mydb.commit()
        print("Sipariş Ekleme işlemi başarılı")

    def UpdateSiparis(self, *args):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = 'restorantyonetimi' AND table_name = '{self.table_name}' AND ORDINAL_POSITION = 1")
        result = self.mycursor.fetchone()
        for column_name in result:
            self.mycursor.execute(
                F"UPDATE {self.table_name} SET SiparisMusteriAdi = %s,SiparisToplamUcret = %s WHERE {column_name} = %s ", (args))
            self.mydb.commit()
            print("Update Başarili")

   
        






s1   = SiparisControllers("siparis")
# s1.InsertSiparis("Siparisdeneme",300)
# s1.GetAll()
# s1.Delete(1)
# s1.UpdateSiparis("Siparisdeneme1",300,2)