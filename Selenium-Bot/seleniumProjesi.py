import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import excelTablo
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

class project():
    hataVerenlerlist=[]
    def __init__(self) -> None:
        self.sifre = excelTablo.kullanicikodu
        self.mail = excelTablo.sifre
        self.driver = webdriver.Chrome(options=self.create_chrome_options())
        self.driver.maximize_window()
        print('Giriş Tamamlandı')
    
    def create_chrome_options(self):
        options = Options()
        options.headless = False
        return options

    def siteGiris(self, siteURL):
        self.driver.get(siteURL)
        WebDriverWait(self.driver, 10)

    def veriler(self, girisBtn):
        try:
            kullanici_adi_element = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_txtAd')
            kullanici_adi_element.send_keys(self.sifre)

            sifre_element = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_txt_sifre')
            sifre_element.send_keys(self.mail)
            time.sleep(8)
            self.buttonClick(girisBtn)
        except Exception as e:
            print(f'Bir hata meydana geldi...{e}')

    def buttonClick(self, deger):
        try:
            self.driver.find_element(By.CSS_SELECTOR, deger).click()
            WebDriverWait(self.driver, 10)
            time.sleep(1)
        except Exception as e:
            print(f'Bir hata meydana geldi{e}')

    def InputText(self, ExcelDegerler, textClass, deger):
        try:
            if deger:
                iframe = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
                )
                self.driver.switch_to.frame(iframe)
            else:
                self.driver.switch_to.default_content()

            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, textClass))
            )
            element.send_keys(ExcelDegerler)
        except:
            logging.error('Hata Meydana Geldi')

    def imzalayanKisiSecimi(self, imzaAtan):
        try:
            iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            self.driver.switch_to.frame(iframe)
            time.sleep(2)

            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#RCBImza_Input')))
            dropdown.click()

            isimler = self.driver.find_elements(By.CSS_SELECTOR, '#RCBImza_DropDown > div > ul > li')
            imzaAtanlar = [isim.text for isim in isimler]
            
            for degerler in imzaAtanlar:
                try:
                    if degerler == imzaAtan:
                        imazaAtanKisi = imzaAtanlar.index(imzaAtan)
                        self.driver.find_element(By.CSS_SELECTOR, f'#RCBImza_DropDown li:nth-child({imazaAtanKisi+1})').click()
                        self.driver.find_element(By.NAME, 'bntKaydet').click()
                        print('BÜTÜN Fonksiyonlar tamam')
                except:
                    print('Hata meydana geldi...')
        except Exception as e:
            print(f'Bir hata meydana geldi...{e}')

    def HataVerenlerFonksiyon(self,ErrorUser):
            self.driver.refresh()
            print('Program hata verdi lütfen yeniden deneyiniz...')
            project.hataVerenlerlist.append(ErrorUser)