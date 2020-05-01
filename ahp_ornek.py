# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:25:08 2020

@author: Taha
"""
import numpy as np
import pandas as pd

def satir_ortalamalari(kriter_matrisi): 
    for i in kriter_matrisi: #fonksiyona yolladığımız matrisin içinde dolaş.
        kriter_matrisi[i]=kriter_matrisi[i]/kriter_matrisi[i].sum() #kriter_matrisi'nin her elemanını ilgili sütun toplamına böl
    satir_ortalamasi=kriter_matrisi.mean(axis=1) #kriter_matrisi'nin satırlarının ortalamasını al (axis=1: satır bazında işlem yap)
    return satir_ortalamasi #satır ortalamasını döndür.

#Kriterler
emlak_fiyati = pd.DataFrame([[1,3,1],
                             [0.333,1,0.2],
                             [1,5,1]])
tedarikci_yakinligi = pd.DataFrame([[1,6,0.333],
                                    [0.166,1,0.111],
                                    [3,9,1]])
isgucu_rezervi = pd.DataFrame([[1,0.333,1],
                               [3,1,5],
                               [1,0.2,1]])
isgucu_maliyeti = pd.DataFrame([[1,0.333,0.5],
                                [3,1,3],
                                [2,0.333,1]])

#Kriterlerin kendi aralarındaki önem sırası
onem_matrisi=pd.DataFrame([[1,0.2,3,4],[5,1,9,7],[0.333,0.111,1,1],[0.25,0.142,1,1]])

#Kriterlerin satır ortalamaları matrisi
EF_SO = satir_ortalamalari(emlak_fiyati) #emlak_fiyati satır ortalamaları
TY_SO = satir_ortalamalari(tedarikci_yakinligi) #tedarikci_yakinligi satır ortalamaları
IR_SO = satir_ortalamalari(isgucu_rezervi )#isgucu_rezervi satır ortalamaları
IM_SO = satir_ortalamalari(isgucu_maliyeti) #isgucu_maliyeti satır ortalamaları
satir_ortalamalari_matrisi = pd.concat([EF_SO,TY_SO,IR_SO,IM_SO],axis=1) #satır ortalamalarını matris olarak birleştir.

OM_SO = satir_ortalamalari(onem_matrisi) #onem_matrisi Satır ortalamaları

#satir_ortalamalari_matrisi ile OM_SO matrisini çarpabilmek için ikisini de Numpy array'ine çevirdik.
satir_ortalamalari_matrisi = np.array(satir_ortalamalari_matrisi)
OM_SO = np.array(OM_SO)
son_satir_toplam=np.dot(satir_ortalamalari_matrisi,OM_SO[:,None])
#
#indexlere isim verebilmek için tekrar Pandas DataFrame'ine çevirdik.
son_satir_toplam=pd.DataFrame(son_satir_toplam,index=["A","B","C"]) 
print(son_satir_toplam)