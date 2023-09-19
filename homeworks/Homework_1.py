"""

1) 5 tane geçerli, 5 tane geçersiz tanimlanmiş değişken oluşturun neden geçerli olup olmadiklarini açiklayin. 

Gecerli degiskenler:

1) ana_para                                   ** Degisken isimlendirme kurallarina uygundur.
2) basit_faiz                                 ** Degisken isimlendirme kurallarina uygundur.
3) isim                                       ** Degisken isimlendirme kurallarina uygundur.
4) soy_isim                                   ** Degisken isimlendirme kurallarina uygundur.
5) yas                                        ** Degisken isimlendirme kurallarina uygundur.

Gecersiz degiskenler:

1) 12alper                                    ** Degisken isimleri rakamla baslayamaz.     
2) kullanici adi                              ** Degisken isimlerinde bosluk olamaz.
3) +alper                                     ** Degisken isimleri islem belirten karakterlerle baslayamaz.
4) while                                      ** Degisken isimleri pythonda anlam ifade eden kelimeler olamaz. 
5) if                                         ** Degisken isimleri pythonda anlam ifade eden kelimeler olamaz.


"""



"""


2) Escape karakterinin amacina örneklendirme yapin.


----------------------------------------------------------------------------------------------------


1) \ karakteri normalde izin verilmeyen durumlarda tirnak isareti kullanmamizi sağlar.

Input:

print("Öğretmen \"Odevlerini en gec cumaya kadar yapin \" dedi. ")


Output: 

Öğretmen "Odevlerini en gec cumaya kadar yapin " dedi.


----------------------------------------------------------------------------------------------------


2) \n 'Newline' anlamina gelir yeni satira geçmeyi sağlar. 

Input:

print("Birinci satir\nIkinci satir\nUçüncü satir")


Output:

Birinci satir
Ikinci satir
Uçüncü satir


----------------------------------------------------------------------------------------------------


3) \t Bir Tab (varsayilan olarak 4 boşluk) boşluk birakmaya yarar.

Input:

print("Merhaba\tDünya!")


Output:

Merhaba    Dünya!


"""



"""


3) Tür dönüşümlerine birkaç örnek verin.


----------------------------------------------------------------------------------------------------


Input:

x = 2.564
y = 5
z = 17


x = int(x)
y = float(y)
z = complex(z)


print(x)
print(y)
print(z)


print("\n---------------------------------------------------\n")


print(type(x))
print(type(y))
print(type(z))


Output:

2
5.0
(17+0j)

---------------------------------------------------

<class 'int'>
<class 'float'>
<class 'complex'>


"""



"""


4) String fonksiyonlarindan en az üçüne örnek verin ve çiktiyi açiklayin.


----------------------------------------------------------------------------------------------------


Input:

metin = "Merhaba ben Alper 18 yasindayim."

print(metin.lower())
print(metin.upper())
print(metin.title())
print(metin.capitalize())


Output:

merhaba ben alper 18 yasindayim.
MERHABA BEN ALPER 18 YASINDAYIM.
Merhaba Ben Alper 18 Yasindayim.
Merhaba ben alper 18 yasindayim.

"""



"""


5) String formatlama operatörlerinden her birine ikişer örnek oluşturun.


----------------------------------------------------------------------------------------------------


Input:

kullanici_adi = "Alper"

print(f"Merhaba {kullanici_adi} hoşgeldin!")


Output:

Merhaba Alper hoşgeldin!


----------------------------------------------------------------------------------------------------


Input:

birinci_sayi = 5
ikinci_sayi = 17
toplam = birinci_sayi + ikinci_sayi

print(f"{birinci_sayi} ile {ikinci_sayi} \'nin toplami {toplam} yapar.")


Output:

5 ile 17 'nin toplami 22 yapar.


----------------------------------------------------------------------------------------------------


Input:

lipsum_metin = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nEtiam maximus ut ipsum eget tincidunt. Nulla facilisi. Pellentesque \nhabitant morbi tristique."


print('''Lorem Ipsum, kisaca Lipsum, masaüstü yayincilik ve basin yayin sektöründe \nkullanilan taklit yazi bloğu olarak tanimlanir.
Ornek Metin: {lipsum}'''.format(lipsum = lipsum_metin))


Output:

Lorem Ipsum, kisaca Lipsum, masaüstü yayincilik ve basin yayin sektöründe 
kullanilan taklit yazi bloğu olarak tanimlanir.
Ornek Metin: Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Etiam maximus ut ipsum eget tincidunt. Nulla facilisi. Pellentesque 
habitant morbi tristique.


----------------------------------------------------------------------------------------------------


Input:

boeing_wikipedia = '''Boeing 787, \n7 Temmuz 2007'de tanitimi gerçekleştirilen Boeing \nfirmasinin 14 yil aradan sonra üretime geçtiği yeni model yolcu uçaği.
Boeing 787 Dreamliner'in en önemli özelliği şimdiye kadar yapilmiş yolcu uçaklarinin en \nverimlisi olmasi; kendi sinifindaki diğer uçaklardan %20 daha az 
yakit tükettiği iddia ediliyor. Yolcu kapasitesi 290-330 kişi arasindan modeline göre \ndeğişmekte. Toplam 4 gövde modeli ile satişa sunulacak. Modeline 
göre menzili 2500 ile 8500 deniz mili arasinda değişebilecek. Tam yüklü ağirliği 165 \nile 245 ton arasi olan uçak 2011 yilinda servise girmiştir.'''

print('''Boeing 787 uçaği hakkinda wikipediada yer alan açiklama şu şekilde: {boeing}'''.format(boeing = boeing_wikipedia)))


Output:

Boeing 787 uçaği hakkinda wikipediada yer alan açiklama şu şekilde: Boeing 787, 
7 Temmuz 2007'de tanitimi gerçekleştirilen Boeing 
firmasinin 14 yil aradan sonra üretime geçtiği yeni model yolcu uçaği.
Boeing 787 Dreamliner'in en önemli özelliği şimdiye kadar yapilmiş yolcu uçaklarinin en 
verimlisi olmasi; kendi sinifindaki diğer uçaklardan %20 daha az 
yakit tükettiği iddia ediliyor. Yolcu kapasitesi 290-330 kişi arasindan modeline göre 
değişmekte. Toplam 4 gövde modeli ile satişa sunulacak. Modeline 
göre menzili 2500 ile 8500 deniz mili arasinda değişebilecek. Tam yüklü ağirliği 165 
ile 245 ton arasi olan uçak 2011 yilinda servise girmiştir.


----------------------------------------------------------------------------------------------------


Input:

print("π sayisi %.2f\'e tekabül etmektedir." % (3.14159) )


Output:

π sayisi 3.14'e tekabül etmektedir.


----------------------------------------------------------------------------------------------------


Input:

merkur_tanim = "Güneş Sistemi'ndeki en küçük ve Güneş'e en yakin gezegen. Yaklaşik 88 \nDünya gününe eşit yörünge süresi ile yörüngesinde Güneş Sistemi'ndeki diğer tüm \ngezegenlerden daha hizli devinir. Kendi ekseni çevresindeki dönüşünü yaklaşik \n59 günde tamamlar. Bilinen hiç doğal uydusu yoktur. Adini tanrilarin habercisi \nRoma tanrisi Merkür'den alir."

print("Merkür: %s" % (merkur_tanim))


Output:

Merkür: Güneş Sistemi'ndeki en küçük ve Güneş'e en yakin gezegen. Yaklaşik 88 
Dünya gününe eşit yörünge süresi ile yörüngesinde Güneş Sistemi'ndeki diğer tüm 
gezegenlerden daha hizli devinir. Kendi ekseni çevresindeki dönüşünü yaklaşik 
59 günde tamamlar. Bilinen hiç doğal uydusu yoktur. Adini tanrilarin habercisi 
Roma tanrisi Merkür'den alir.

"""



"""


6) İçiçe stringlerde tanimlama kurallarini yazin.

**Iç içe string tanimlarken string olduğunu belirtmek için kullandigimiz işaret 
eğer "(çift tirnak) ise stringin içinde tanimlayacağimiz stringin '(tek tirnak) 
ile ifade etmeliyiz. Bu durumun tam terside geçerlidir.

Ornek:

metin = 'Kitaplari tek tek raflara yerleştirirken: " En çok Tolstoy okumayi seviyorum." dedi.'

"""



"""


7) İkinci derste işlenen konulardan seçtiğiniz iki tanesini açiklamaya çalişin. (Doğru olmasi önemsiz, sadece deneyin.)


split, bir string fonksiyonudur ve amaci belirlediğmiz bir karakterin bulunduğu yerlerden bölerek böldüğü elemanlari bir listede toplar.


endswith, bu da bir string fonksiyonudur eğer string bizim endswith fonksiyonuna girdiğimiz değer ile bitiyorsa 'True' döndürür girdiğimiz 
değer ile uyuşmuyorsa 'False' döndürür.



"""

