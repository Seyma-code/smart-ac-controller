\# Akıllı Klima Kontrol Sistemi



> Bulanık Mantık (Fuzzy Logic) kullanılarak geliştirilen akıllı klima kontrol sistemi.



\## Proje Hakkında



Bu proje, \*\*Bulanık Mantık (Fuzzy Logic)\*\* yaklaşımı kullanılarak sıcaklık, nem ve oda boyutu bilgilerine göre klima fan hızını otomatik olarak belirleyen bir kontrol sistemini gerçekleştirmektedir.



Geleneksel kontrol sistemleri genellikle sabit eşik değerlerine dayanır. Örneğin sıcaklık belirli bir değerin üzerine çıktığında fan hızı artırılır. Ancak gerçek hayatta kullanıcı konforu yalnızca sıcaklığa değil, aynı zamanda nem oranına ve odanın büyüklüğüne de bağlıdır.



Bu projede geliştirilen sistem, insan benzeri karar verme mantığını taklit ederek aşağıdaki gibi sözel kuralları kullanır:



\* Eğer sıcaklık yüksek, nem yüksek ve oda büyük ise fan hızı hızlı olmalıdır.

\* Eğer sıcaklık düşük, nem düşük ve oda küçük ise fan hızı yavaş olmalıdır.

\* Eğer değerler orta seviyede ise fan hızı orta düzeyde olmalıdır.



Sistem, bulanıklaştırma, kural değerlendirme, çıkarım ve durulaştırma adımlarını kullanarak en uygun fan hızını hesaplamaktadır.



\---



\# Proje Amacı



Bu projenin temel amacı:



\* Bulanık mantık teorisini gerçek bir probleme uygulamak,

\* Mamdani çıkarım sistemini kullanmak,

\* Centroid durulaştırma yöntemi ile sayısal sonuç üretmek,

\* Python tabanlı etkileşimli bir kullanıcı arayüzü geliştirmek,

\* Farklı senaryolar altında sistemi test etmek ve değerlendirmektir.



\---



\# Problem Tanımı



Bir odanın ideal şekilde soğutulabilmesi yalnızca sıcaklığa bağlı değildir.



Aynı sıcaklık değerinde:



\* Nem oranı arttığında ortam daha bunaltıcı hissedilir.

\* Oda büyüklüğü arttığında daha fazla hava sirkülasyonu gerekir.



Bu nedenle fan hızının belirlenmesinde birden fazla faktörün birlikte değerlendirilmesi gerekir.



Bulanık mantık, bu belirsizlikleri ve ara durumları modellemek için oldukça uygun bir yöntemdir.



\---



# Kullanılan Teknolojiler

- Python 3.x
- NumPy
- SciPy
- NetworkX
- Matplotlib
- scikit-fuzzy
- Streamlit



\---



\# Giriş ve Çıkış Değişkenleri



\## Giriş Değişkenleri



| Değişken   |      Aralık | Açıklama         |

| ---------- | ----------: | ---------------- |

| Sıcaklık   |   0 – 40 °C | Oda sıcaklığı    |

| Nem        |   0 – 100 % | Bağıl nem oranı  |

| Oda Boyutu | 10 – 100 m² | Odanın büyüklüğü |



\## Çıkış Değişkeni



| Değişken |    Aralık | Açıklama                   |

| -------- | --------: | -------------------------- |

| Fan Hızı | 0 – 100 % | Klima fanının çalışma hızı |



\---



\# Üyelik Fonksiyonları



Her değişken için üç dilsel tanımlama kullanılmıştır.



\## Sıcaklık



\* Düşük

\* Orta

\* Yüksek



\## Nem



\* Düşük

\* Orta

\* Yüksek



\## Oda Boyutu



\* Küçük

\* Orta

\* Büyük



\## Fan Hızı



\* Yavaş

\* Orta

\* Hızlı



\---



\# Kural Tabanı



Sistem toplam \*\*27 adet bulanık kural\*\* içermektedir.



Örnek kurallar:



1\. IF Sıcaklık Düşük AND Nem Düşük AND Oda Boyutu Küçük THEN Fan Hızı Yavaş

2\. IF Sıcaklık Orta AND Nem Orta AND Oda Boyutu Orta THEN Fan Hızı Orta

3\. IF Sıcaklık Yüksek AND Nem Yüksek AND Oda Boyutu Büyük THEN Fan Hızı Hızlı



\---



\# Kullanılan Yöntemler



\## Çıkarım Sistemi



\* Mamdani Fuzzy Inference System



\## AND Operatörü



\* Minimum (min)



\## Birleştirme



\* Maksimum (max)



\## Durulaştırma



\* Centroid (Ağırlık Merkezi) Yöntemi



\---



\# Proje Dosya Yapısı



```text

smart-ac-controller/

│── Bulanik\_Mantik\_Proje\_Raporu.docx

│── fuzzy\_controller.py

│── app.py

│── requirements.txt

│── README.md

```



\---



\# Dosya Açıklamaları



\## fuzzy\_controller.py



Bulanık mantık sisteminin tanımlandığı ana dosyadır.



İçerdiği bileşenler:



\* Giriş ve çıkış değişkenleri

\* Üyelik fonksiyonları

\* 27 kural

\* Mamdani çıkarım sistemi

\* Centroid durulaştırma

\* Fan hızı hesaplama fonksiyonu

\* Aktif kuralları listeleme fonksiyonu



\## app.py



Streamlit tabanlı kullanıcı arayüzüdür.



Özellikleri:



\* Slider ile giriş değerlerini değiştirme

\* Hesapla butonu

\* Sayısal sonuç gösterimi

\* Aktif kuralların listelenmesi

\* Üyelik fonksiyonlarının grafiksel gösterimi



\## requirements.txt



Projede kullanılan Python paketlerinin listesini içerir.



\## README.md



Proje hakkında açıklamalar ve kullanım talimatları.



\## Bulanik\_Mantik\_Proje\_Raporu.docx



Detaylı akademik proje raporu.



\---



\# Kurulum



\## 1. Projeyi İndirin



```bash

git clone https://github.com/kullanici-adi/smart-ac-controller.git

cd smart-ac-controller

```



> Not: Eğer Git kullanmıyorsanız, projeyi ZIP olarak indirip klasöre çıkarabilirsiniz.



\## 2. Gerekli Paketleri Kurun



```bash

pip install -r requirements.txt

```



\---



\# Uygulamanın Çalıştırılması



```bash

streamlit run app.py

```



Komut çalıştırıldıktan sonra uygulama varsayılan web tarayıcısında otomatik olarak açılır.



\---



\# Kullanım Talimatları



1\. Sıcaklık değerini belirleyin.

2\. Nem oranını seçin.

3\. Oda boyutunu girin.

4\. "Hesapla" butonuna tıklayın.

5\. Hesaplanan fan hızını görüntüleyin.

6\. Aktif kuralları inceleyin.

7\. Üyelik fonksiyonlarını grafiksel olarak analiz edin.



\---



\# Arayüz Özellikleri



\* Etkileşimli slider kontrolleri

\* Gerçek zamanlı hesaplama

\* Sayısal sonuç gösterimi

\* Aktif kural listesi

\* Üyelik fonksiyonu grafikleri

\* Kullanıcı dostu tasarım



\---



\# Örnek Test Senaryosu



| Sıcaklık |  Nem | Oda Boyutu | Fan Hızı |

| -------: | ---: | ---------: | -------: |

|    30 °C | 80 % |      75 m² |   88.4 % |



\### Yorum



Yüksek sıcaklık, yüksek nem ve büyük oda nedeniyle sistem yüksek fan hızı üretmektedir.



\---



\# Test ve Değerlendirme



Sistem farklı giriş değerleriyle test edilmiş ve şu sonuçlar gözlemlenmiştir:



\* Giriş değerleri arttıkça fan hızı mantıklı biçimde artmaktadır.

\* Çıkış değerleri ani sıçramalar göstermemektedir.

\* Sistem insan benzeri kararlar üretmektedir.

\* Sonuçlar kararlı ve tutarlıdır.



\---



\# Sistemin Güçlü Yönleri



\* Açıklanabilir ve yorumlanabilir yapı

\* İnsan uzman bilgisine dayalı tasarım

\* Belirsiz durumları başarıyla değerlendirme

\* Kolay genişletilebilir mimari

\* Kullanıcı dostu arayüz



\---



\# Sistemin Sınırlamaları



\* Üyelik fonksiyonları manuel olarak belirlenmiştir.

\* Otomatik öğrenme yeteneği yoktur.

\* Kural sayısı arttıkça karmaşıklık artabilir.



\---



\# Gelecekte Yapılabilecek Geliştirmeler



\* Dış ortam sıcaklığının eklenmesi

\* Hava kalitesi sensörlerinin kullanılması

\* Kullanıcı tercihleriyle kişiselleştirme

\* Yapay sinir ağları ile hibrit sistem tasarımı

\* Mobil uygulama desteği



\---



\# Kaynakça



\* Python Documentation

\* NumPy Documentation

\* Matplotlib Documentation

\* scikit-fuzzy Documentation

\* Streamlit Documentation

\* Timothy J. Ross, Fuzzy Logic with Engineering Applications



\---



\# Geliştirici Bilgileri



\*\*Öğrenci Adı:\*\* Şeyma Elahmed

\*\*Öğrenci Numarası:\*\* 22430070906

\*\*Ders:\*\* Bulanık Mantık

\*\*Teslim Tarihi:\*\* 15.05.2026



\---







Bu proje eğitim amaçlı hazırlanmıştır.



