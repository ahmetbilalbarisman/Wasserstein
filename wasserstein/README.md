3 adet script 1 adet wasserstein_rapor ve sunum mevcut

Sunum wasserstein ve jennsen-Shannon karşılaştırılmasını içeriyor.
Rapor wasserstein ve data drif konularını içeriyor.


1-Testwasserstein ve Testwasserstein2

Çalışma süreci:  iki veri setini karşışatırır ve seçilen stattest ve istenilen ayarları uyguladıktan sonra html rapor dosyası üretir. 
    -Referans ve güncel data rastgele oluşturulmuştur(Testwasserstein)
    -Referans ve güncel veri aynı veriyi içerir. (Testwasserstein2)
    -Evidently kütüphanesi kullanılarak oluşturulmuştur. referans 1 ve 2
    -Çeşitli kişiselleştirmeler yapılabilir.
        -Stat test türü seçilebilir(wasserstein ve jennsen shannon)  referans3
        -Data drift thresholdları ayarlanabilir. referans3
        -Rapor şeması değiştirilebilir. referans 4

2-comparision_test
    -Veriler rastgele oluşturulmuştur.
    -Scipy kütüphanesi kullanıalrak iki metric histogram grafiği ile karşılaştırılması yapılmıştır.
    -Sunumda kullanılan görseller buradan elde edilmiştir.

Notlar: 
1- Ilk ikisi güncel env ile çalışır durumda ancak 3.sü için farklı bir env gerekiyor.



Referans:
1- Data drift report >> https://docs.evidentlyai.com/presets/data-drift

2- Wasserstein Algortihm >> https://docs.evidentlyai.com/reference/api-reference/evidently.calculations/evidently.calculations.stattests#module-evidently.calculations.stattests.wasserstein_distance_norm

3- Kişiselleştirme >> https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests

4- Raporun şemasının kişiselleştirilmesi >> https://docs.evidentlyai.com/user-guide/customization/options-for-color-schema