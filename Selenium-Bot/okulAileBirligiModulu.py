import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from seleniumProjesi import project
from htmlTag import kullanicilar,HataverenlerExcel
import excelTablo
listeApp=[]
def okulAileBirliğiModülü():
    isim1=project()
    WebDriverWait(isim1.driver,10)
    isim1.siteGiris("https://tefbis.meb.gov.tr/giris.aspx")
    isim1.veriler()
    isim1.buttonClick('[name="ctl00$ContentPlaceHolder1$btn_login"]')
    isim1.buttonClick('.rtsLink')
    isim1.siteGiris("https://tefbis.meb.gov.tr/resmi/gelir_n.aspx?SYID=104")
    time.sleep(3)
    veriler=excelTablo.ExcelDegerleri()
    for a in veriler:
        try:
            isim1.buttonClick('#RadOdeyenTip_Input')
            isim1.buttonClick('.rcbItem:nth-child(14)')
            isim1.buttonClick('.btn_ekle')
            
            isim1.InputText(str(a['TC']),"#RadNumericTextBox1",True)
            time.sleep(2)

            isim1.buttonClick('[name="Button1"]')

            isim1.buttonClick('[name="Button1"]')
            isim1.buttonClick('#Table1 > tbody > tr > td:nth-child(3) > a')

            isim1.InputText(str(a['EVRAK NO']),'[name="Txtevrakno"]',False)
            isim1.buttonClick('#GridGelirDetay_ctl00_ctl02_ctl00_InitInsertButton')
            WebDriverWait(isim1.driver,10)
            isim1.buttonClick('.rcbInput radPreventDecorate')
            isim1.buttonClick('.rcbItem:nth-child(5)')
            isim1.InputText(str(a['TUTAR']),'#GridGelirDetay_ctl00_ctl02_ctl02_BIRIM_FIYATTxt',False)
            isim1.buttonClick("[name='GridGelirDetay$ctl00$ctl02$ctl02$btn_ekle']")
            WebDriverWait(isim1.driver,10)
            time.sleep(5)
            isim1.buttonClick("[name='btnKaydet']")
            WebDriverWait(isim1.driver,10)
            isim1.imzalayanKisiSecimi(str(a['IMZALAYAN']))
            isim1.siteGiris("https://tefbis.meb.gov.tr/resmi/gelir_n.aspx?SYID=104")
            
        except:
            isim1.HataVerenlerFonksiyon(a)

    degersss = pd.DataFrame(listeApp)
    output_path = HataverenlerExcel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    degersss.to_excel(output_path, index=False)
    isim1.driver.quit()

