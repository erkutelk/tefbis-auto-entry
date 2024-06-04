import os
def ExcelDosyalarınıOku(deger):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'excel_file', deger)
    return file_path

HataverenlerExcel=ExcelDosyalarınıOku('HataVerenler.xlsx')
kullanicilar=ExcelDosyalarınıOku('kullanicilar.xlsx')
