## RectFootingBiaxialBending
Eğik eğilme etkisi altındaki dikdörtgen tekil temellerde basınç bölgeleri A, B, C, D ve E olmak üzere 5 farklı bölgeye ayrılabilir.
- C tam başınç bölgesi
- A üçgen basınç bölgesi
- D x yönünde trapez basınç bölgesi
- E y yönünde trapez basınç bölgesi
- B beşgen basınç bölgesi

Bu uygulama verili temel boyutları ve kesit tesirleri için köşe noktalardaki zemin gerilmelerini hesaplamak için geliştirilmiştir. [^1] [^2] [^3] Pozitif momentler şekildeki gibidir.

<img src="https://eykaraduman.github.io/assets/images/biaxialbend.png" width="500" />

- RectFootingBiaxialBending ile dikdörtgen temelin herhangi bir noktasında zemin gerilmesi tekil olarak hesaplanabilir.
- Ayrıca çeşitli yükleme halleri için istenilen kesit yerlerinde zemin gerilmelerini bulmakta mümkündür. Bunun bir örneği olan `test.ini` dosyasının içeriği aşağıda verilmiştir.

```ini
# (test.ini)
[Boyutlar]
# x yönünde temel genişliği
Lx=7.02
# y yönünde temel genişliği
Ly=6.75

[Yukler]
# No=Hal Ad, N, Mx, My
1=İnşaat Sonu,553.04,-203.67,51.51
2=İnşaat Sonu Depremli,595.75,-729.94,51.51
3=İşletme Hali,476.80,-282.20,11.05
4=İşletme Hali Depremli,521.71,-878.72,8.71
5=Taşkın Hali,420.30,-350.69,-46.60

[Kesitler]
# Kesit No= x koordinat, y koordinat
1=5.52,4.25
2=3.52,4.25
3=2.00,4.25
4=1.00,4.25
```
- RectFootingBiaxialBending, dosyadan hesaplanan gerilmeler ve karakteristik bilgiler için hesap dosya ile aynı adlı bir metin dosyası oluşturur. (Örneğin `test.txt`)
```txt
(test.txt)
----------------------------------------------------------------------------------------------------------------
|Hal Ad                   | Lx (m) | Ly (m) |     N(t)     |    Mx(tm)    |    My(tm)    |    ex    |    ey    |
----------------------------------------------------------------------------------------------------------------
|İnşaat Sonu              |  7.02  |  6.75  |   553.0400   |  -203.6700   |   51.5100    |  0.0931  | -0.3683  |
|İnşaat Sonu Depremli     |  7.02  |  6.75  |   595.7500   |  -729.9400   |   51.5100    |  0.0865  | -1.2252  |
|İşletme Hali             |  7.02  |  6.75  |   476.8000   |  -282.2000   |   11.0500    |  0.0232  | -0.5919  |
|İşletme Hali Depremli    |  7.02  |  6.75  |   521.7100   |  -878.7200   |    8.7100    |  0.0167  | -1.6843  |
|Taşkın Hali              |  7.02  |  6.75  |   420.3000   |  -350.6900   |   -46.6000   | -0.1109  | -0.8344  |
----------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
|Hal Ad                   | Basınç Bölge  |    Xn (m)    |    Yn (m)    |    Xq(m)     |    Yp(m)     |   s1(t/m²)   |   s2(t/m²)   |   s3(t/m²)   |   s4(t/m²)   |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
|İnşaat Sonu              |       C       |    62.04     |    14.51     |    0.0000    |    0.0000    |    8.7797    |    6.9215    |   14.5627    |   16.4209    |
|İnşaat Sonu Depremli     |       D       |    98.46     |     6.68     |    0.0000    |    6.2052    |    0.0000    |    0.0000    |   25.3563    |   27.3029    |
|İşletme Hali             |       C       |    273.94    |     9.92     |    0.0000    |    0.0000    |    4.9678    |    4.5692    |   15.1567    |   15.5553    |
|İşletme Hali Depremli    |       D       |    495.47    |     5.11     |    0.0000    |    5.0357    |    0.0000    |    0.0000    |   29.0960    |   29.5142    |
|Taşkın Hali              |       C       |    68.02     |     8.36     |    0.0000    |    0.0000    |    1.4508    |    3.1319    |   16.2890    |   14.6079    |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kesit-1
------------------------------------------
|Hal Ad                   |Gerilme (t/m²)|
------------------------------------------
|İnşaat Sonu              |    12.13     |
|İnşaat Sonu Depremli     |    15.56     |
|İşletme Hali             |    11.32     |
|İşletme Hali Depremli    |    14.74     |
|Taşkın Hali              |    11.06     |
------------------------------------------

Kesit-2
------------------------------------------
|Hal Ad                   |Gerilme (t/m²)|
------------------------------------------
|İnşaat Sonu              |    12.66     |
|İnşaat Sonu Depremli     |    16.11     |
|İşletme Hali             |    11.43     |
|İşletme Hali Depremli    |    14.86     |
|Taşkın Hali              |    10.58     |
------------------------------------------

Kesit-3
------------------------------------------
|Hal Ad                   |Gerilme (t/m²)|
------------------------------------------
|İnşaat Sonu              |    13.06     |
|İnşaat Sonu Depremli     |    16.53     |
|İşletme Hali             |    11.52     |
|İşletme Hali Depremli    |    14.95     |
|Taşkın Hali              |    10.21     |
------------------------------------------

Kesit-4
------------------------------------------
|Hal Ad                   |Gerilme (t/m²)|
------------------------------------------
|İnşaat Sonu              |    13.33     |
|İnşaat Sonu Depremli     |    16.81     |
|İşletme Hali             |    11.58     |
|İşletme Hali Depremli    |    15.01     |
|Taşkın Hali              |     9.97     |
------------------------------------------
```
- RectFootingBiaxialBending uygulaması Python ile geliştirilmiştir.
<img src="https://eykaraduman.github.io/assets/images/RectFootApp.png" width="500" />

[^1]: [Özmen, G. (2011). “Determination of base stresses in rectangular footings under biaxial bending.” Teknik Dergi, 22, 5659-5674.](http://www.imo.org.tr/resimler/ekutuphane/pdf/16498_15_12.pdf) 

[^2]: Trupia, A., Saygun, A. Betonarme Yüzeysel Temeller, Nobel Yayın Dağıtım, Ankara, 2009. 

[^3]: [Bellos, John & Bakas, Nikolaos. (2017). Complete Analytical Solution for Linear Soil Pressure Distribution under Rigid Rectangular Spread Footings. International Journal of Geomechanics.](https://www.researchgate.net/publication/312362987_Complete_Analytical_Solution_for_Linear_Soil_Pressure_Distribution_under_Rigid_Rectangular_Spread_Footings)
