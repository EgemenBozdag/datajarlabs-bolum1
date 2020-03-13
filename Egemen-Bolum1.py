#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[1]:


3+5


# In[2]:


"Selam"


# In[3]:


print("Toplama işleminin sonucu :",  3+5)


# In[4]:


print("Bootcamp'e hoş geldiniz!")


# In[5]:


3+5
"Bootcamp'e hoş geldiniz!"


# In[6]:


print("Toplama işleminin sonucu :",  3+5)
print("Bootcamp'e hoş geldiniz!")


# In[7]:


print ("Bugün hava" , 15 , "derece")


# In[8]:


print('Tek tırnak')
print("Çift tırnak")
print("""Üç çift tırnak""")


# In[9]:


print ("Türkiye'nin üç tarafı denizlerle çevrilidir.")


# In[10]:


print ("Bugün hava" , 15 , "derece")
print ("Bugün hava" , 15 , "derece", sep="+")


# In[11]:


print ("Bugün hava" , 15 , "derece")
print ("Bugün hava" , 15 , "derece", sep="&")


# In[12]:


print ("Bugün hava" , 15 , "derece")
print ("Bugün hava" , 15 , "derece", sep="  ")


# In[13]:


print("Meyve")
print("Sebze")


# In[14]:


print("Meyve", end=" ")
print("Sebze", end=" ")


# In[15]:


pi = 3.14
r = 4
print('Dairenin çevresi :', 2 * pi * r, 'cm')


# In[16]:


soyisim = "Yılmaz"

print ("Merhaba, benim adım" , isim , soyisim)


# In[18]:


isim = "Egemen"
soyisim = "Bozdag"

print ("Merhaba, benim adım" , isim , soyisim)


# In[19]:


Ocak = Mart = Mayıs = Temmuz = Ağustos = Ekim = Aralık = 31
Nisan = Haziran = Eylül = Kasım = 30
Şubat = 28
print (Ocak, Şubat, Mart, Nisan, Mayıs, Haziran, Temmuz, Ağustos, Eylül, Ekim, Kasım, Aralık)


# In[22]:


Sinav_Notu = '42'
print ("Sinav_Notu değişkeninin tipi   : ", type(Sinav_Notu))
print ("Sinav_Notu değişkeninin değeri : ", Sinav_Notu)


# In[21]:


Sinav_Notu = "Kırkiki"
print ("Sinav_Notu değişkeninin tipi   : ", type(Sinav_Notu))
print ("Sinav_Notu değişkeninin değeri : ", Sinav_Notu)


# In[23]:


Sinav_Basarisi = False
print ("Sinav_Basarisi değişkeninin tipi   : ", type(Sinav_Basarisi))
print ("Sinav_Basarisi değişkeninin değeri : ", Sinav_Basarisi)


# In[24]:


# Toplama
toplam = 15 + 22  
print("15 ve 22 sayılarının toplamı : ", toplam)

# Çıkarma
fark = 22 - 15
print("22 ve 15 sayılarının farkı   : ", fark)


# In[25]:


# Çarpma
carpim = 15 * 22  
print("15 ve 22 sayılarının çarpımı : ", carpim)

# Kuvvetini alma
kare = 9 ** 2  
print("9'un karesi : ", kare)
kuvvet = 4 ** 3  
print("4 üzeri 3   : ", kuvvet)


# In[26]:


bolum = 130/2  
print("130'un 11'e bölümü (Tek / ile)  :", bolum)
ciftli_bolum = 130//2  
print("130'un 11'e bölümü (Çift // ile):", ciftli_bolum)

# Mod alma
kalan = 25%7
print("25'in 7'ye bölümünden kalan     :", kalan)


# In[28]:


x=5
print ('x değeri       : ', x)
x +=2
print ("x'in 2 fazlası : ", x, "\n")

y = 10
print ('y değeri       : ', y)
y -=2
print ("y'nin 2 eksiği : ", y, "\n")

z = 6
print ('z değeri       : ', z)
z *=2
print ("z'nin 2 katı   : ", z, "\n")


# In[29]:


meyve = 'Portakal'
sebze = "Domates"
print(meyve, " ve " , sebze)


# In[30]:


print('Kelime                 : ' , meyve)
print('İlk harf               : ' , meyve[0])
print('İkinci harf            : ' , meyve[1])
print("3 ila 5'inci harfler   : " , meyve[2:5])
print("3'üncü harften sonrası : " , meyve[2:])


# In[33]:


print(meyve , 'kelimesinin uzunluğu :' , len(meyve))


# In[34]:


print("+ işareti ile :", meyve + sebze)
print("* işareti ile :", 2 * meyve)


# In[35]:


miktar = 15
metin = 'Aldığımız toplam {} miktarı {} kilogramdır.'
print(metin.format(meyve, miktar))


# In[36]:


pi = 22/7
print(pi)
print("Pi sayısı ({:.2f}) dairenin çevresinin çapına oranıdır.".format(pi) )


# In[37]:


print ("{1} {3} {0} {2}".format("veri bilimcisi",6,"olacağız","ayda"))


# In[38]:


output = 'Benim hayatım %s %s %d' % ("merhaba", "dünya", 35)  
print (output)

output2 = 'Benim hayatım %s %s %.2f' % ("merhaba", "dünya", 35)  
print (output2)


# In[39]:


ad = input('Adınız : ')
yas = input('Yaşınız: ') 
print ("Adınız {} ve {} yaşındasınız.".format(ad,yas))


# In[40]:


Ad = 'Ahmet'
Soyad = "Yılmaz"
Yas = strength = 4
Meslek= None
print (Meslek)


# In[41]:


a = 42
b = "10"
c = "1.5"
d = "Elma"

print(a-int(b))
print(a-float(c))
print(d+str(a))


# In[56]:


faiz=12
anapara=1000
bitcoin= anapara*(1+faiz/100)**7-anapara
print (bitcoin)


# In[60]:


metin="Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama %{} kazançla, bir hafta sonunda {:.2f} dolar kazandırdık"
print (metin.format(anapara,faiz,bitcoin))


# In[ ]:




