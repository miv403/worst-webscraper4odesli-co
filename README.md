---
author: miv403
date: 2023-08-12
---
# odesli.co için web scraper

> odesli.co sitesini kullanarak spotify bağlantılarını yutub bağlantılarına dönüştüren piton sikripti.

## kullanımı:

1. spotify masaüstü programını açıktan sonra herhangi bir oynatma listesini açın.

2. tüm parçaları seçmek için `CTRL + A` kısayolunu kullanın.

3. tüm parçaları seçtikten sonra `CTRL + C` kısayolu ile parçaları kopyalayın.

4. `playlist.txt` adlı bir dosya oluşturup içine listeyi yapıştırın. `main.py` ile aynı dizine taşıyın.

5. `main.py` dosyasının olduğu dizinde bir uçbirim açın ve `python python.py` komutunu yürütün.

6. işlem bittikten sonra yutub eşleşmesi olan tüm parçaları `output.txt` adlı dosyanın içinde bulabilirsiniz.

7. bu listeyi doğrudan [jdownloader](https://www.jdownloader.org/) içerisine yapıştırarak parçaları kolayca indirebilirsiniz ya da bağlantıları başka bir amaç için kullanabilirsiniz orası size kalmış  `¯\_(ツ)_/¯`

### not-0:

yaptığınız her işlemden sonra `output.txt` dosyasının içini silip kaydetmeyi ya da silmeyi unutmayın!

eğer dosyayı silmez ya da içini temizlemezseniz eski bağlantılardan itibaren yeni bağlantılar eklenmeye başlayacaktır. bu kafa karışıklığına ya da kullanımınızın aksamasına neden olabilir.

### not-1:

bazı bağlantılar yutub eşleşmesi olmadığı için oluşturulamayabilir. olmayanları elemek için ilgili işlem numarası ile `playlist.txt` içerisindeki satırı eşleştirmeniz yeterli.

### not-2:

>[!IMPORTANT]
> bu program bütünüyle eğlence amaçlı hazırlanmıştır.
