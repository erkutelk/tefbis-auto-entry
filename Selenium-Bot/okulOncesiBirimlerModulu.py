import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumProjesi import project
import excelTablo
import pandas as pd
from htmlTag import kullanicilar,HataverenlerExcel

def okulOncesiBirimler():
    isim1 = project()
    WebDriverWait(isim1.driver, 10)
    isim1.siteGiris("https://tefbis.meb.gov.tr/giris.aspx")
    isim1.veriler('[name="ctl00$ContentPlaceHolder1$btn_login"]')
    WebDriverWait(isim1.driver, 10)

    isim1.siteGiris("https://tefbis.meb.gov.tr/resmi/gelir_n.aspx?SYID=122")
    
    veriler=excelTablo.ExcelDegerleri()
    listeApp=[]
    for a in veriler:
        try:
            isim1.buttonClick('#RadOdeyenTip_Input')
            isim1.buttonClick('.rcbItem:nth-child(2)')
            isim1.buttonClick('.btn_ekle')
            isim1.InputText(str(round(a['TC'])), "#RadNumericTextBox1", True)
            sleep(1)

            isim1.buttonClick('[name="Button1"]')
            isim1.buttonClick('[name="Button1"]')
            isim1.buttonClick('#Table1 > tbody > tr > td:nth-child(3) > a')
            isim1.InputText(str(round(a['EVRAK NO'])), '[name="Txtevrakno"]', False)
            sleep(1)
            isim1.buttonClick('#GridGelirDetay_ctl00_ctl02_ctl00_InitInsertButton')

            WebDriverWait(isim1.driver, 10)
            isim1.InputText(str(round(a['TUTAR'])), '#GridGelirDetay_ctl00_ctl02_ctl02_BIRIM_FIYATTxt', False)
            sleep(1)

            isim1.buttonClick("[name='GridGelirDetay$ctl00$ctl02$ctl02$btn_ekle']")
            WebDriverWait(isim1.driver, 10)
            isim1.buttonClick("[name='btnKaydet']")
            WebDriverWait(isim1.driver, 10)
            isim1.imzalayanKisiSecimi(str(a['IMZALAYAN']))
            isim1.siteGiris("https://tefbis.meb.gov.tr/resmi/gelir_n.aspx?SYID=122")
            
            sleep(3)
           
        except:
            isim1.HataVerenlerFonksiyon(a)

        

    degersss = pd.DataFrame(project.hataVerenlerlist)
    output_path = HataverenlerExcel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    degersss.to_excel(output_path, index=False)
    isim1.driver.quit()

