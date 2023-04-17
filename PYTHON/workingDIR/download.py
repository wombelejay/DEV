#!/usr/bin/env python3

"""
-------Microsoft Cumputer 1/04/2023---------------- 

-------script python creé by SORE SOUMAILA---------

if you want to improve this script you are welcome
"""

"""--------------Differents libraries for python to call function-------------------"""
import urllib.request
import shutil,os


#--------------Download function to download your pdf -----------------------------#
def download(fil_name,fil_name_1,dest):
    for i in range(len(fil_name)):
        for j in range(len(fil_name_1)):
             if(i==j):
                 urllib.request.urlretrieve(fil_name[i],fil_name_1[i])
    for k in range(len(fil_name_1)):
        shutil.move(fil_name_1[k],dest)

URL = []
for url in range(1,9):
    pdf = 'cours{}_2021_slides.pdf'.format(url)
    #print(pdf)
    URL = 'https://irma.math.unistra.fr/~franck/cours/Pythonl2/{}'.format(pdf)
    print(URL)




URL1='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours1_2021_slides.pdf'
URL2='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours2_2021_slides.pdf'
URL3='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours3_2021_slides.pdf'
URL4='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours4_2021_slides.pdf'
URL5='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours5_2021_slides.pdf'
URL6='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours6_2021_slides.pdf'
URL7='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf'
URL8='https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours8_2021_slides.pdf'

pdf1='cours1_2021_slides.pdf'
pdf2='cours2_2021_slides.pdf'
pdf3='cours3_2021_slides.pdf'
pdf4='cours4_2021_slides.pdf'
pdf5='cours5_2021_slides.pdf'
pdf6='cours6_2021_slides.pdf'
pdf7='cours7_2021_slides.pdf'
pdf8='cours8_2021_slides.pdf'


#----------------Differents list  to download files nothing you can't do -----------------#
tab1=[URL1,URL2,URL3,URL4,URL5,URL6,URL7,URL8]
tab2=[pdf1,pdf2,pdf3,pdf4,pdf5,pdf6,pdf7,pdf8]


#---------------Download and put differents files to your choice directory-----------------#

#---------------Choose your directory and put them -----------------------------------------#

dest='/mnt/c/Users/Ricardo Kouakou/OneDrive/Documents/TRAINING/PYTHON/workingDIR/COURS'

#-------------Call function to download and put them in your directory-----------------------#
#download(tab1,tab2,dest)
            

# -------------------Good bye -----------------------------------#

