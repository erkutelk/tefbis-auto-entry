import pandas as pd
import logging
from htmlTag import kullanicilar
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExcelTabloCLASS:
    def __init__(self, dosya):
        self.dosya = dosya
        self.dataFrame = pd.read_excel(dosya)  
        self.isim = self.dataFrame.iloc[0]
        logging.info('Excel dosyası okuma işlemi tamamlandı...')

    def deger(self, *degerler):
        results = []
        satirSayisi = len(self.dataFrame)
        for index in range(satirSayisi):
            # Her satır için bir sözlük oluştur
            row_data = {}
            for deg in degerler:
                # Her sütun adı için sözlük anahtarını ve o satırdaki değerini kaydet
                row_data[deg] = self.dataFrame[deg].iloc[index]
            results.append(row_data)
        return results
    
    def sifreKullanici(self):
        try:
            KullanıcıKod = self.isim['KULLANICI KOD']
            sifre = self.isim['SIFRE']
            return round(KullanıcıKod), sifre
        except:
            print('Hata Meydana geldi:')
        


ExcelTablosuNesnesi = ExcelTabloCLASS(kullanicilar)
ExcelDegerleri=ExcelTablosuNesnesi.deger('TC', 'EVRAK NO', 'IMZALAYAN', 'TUTAR')
# for a in ExcelTablosuNesnesi.deger('TC', 'IMZALAYAN'):
#     try:
#         print(f"TC:\t {a['TC']} \t  IMZALAYAN: \t {a['IMZALAYAN']}")
#     except:
#         print('Excell Tablosunu okurken hata meydana geldi...')

# Kullanıcı kodu ve şifreyi alıyoruz
kullanicikodu, sifre = ExcelTablosuNesnesi.sifreKullanici()
