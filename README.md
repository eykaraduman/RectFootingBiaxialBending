## RectFootingBiaxialBending
Eğik eğilme etkisi altındaki dikdörtgen tekil temellerde basınç bölgeleri A, B, C, D ve E olmak üzere 5 farklı bölgeye ayrılabilir.
- C tam başınç bölgesi
- A üçgen basınç bölgesi
- D x yönünde trapez basınç bölgesi
- E y yönünde trapez basınç bölgesi
- B beşgen basınç bölgesi

Bu uygulama verili temel boyutları ve kesit tesirleri için köşe noktalardaki zemin gerilmelerini hesaplamak için geliştirilmiştir. Pozitif momentler şekildeki gibidir.

<img src="https://eykaraduman.github.io/assets/images/biaxialbend.png" width="500" />

- RectFootingBiaxialBending ile dikdörtgen temelin herhangi bir noktasında zemin gerilme hesaplanabilir.
- Çeşitli yükleme halleri istenilen kesit yerleri için topluca zemin gerilmeleri bulunabilir.

```ini
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

<img src="https://eykaraduman.github.io/assets/images/RectFootApp.png" width="500" />

#### Kaynaklar
- [Özmen, G. (2011). “Determination of base stresses in rectangular footings under biaxial bending.” Teknik Dergi, 22, 5659-5674.](http://www.imo.org.tr/resimler/ekutuphane/pdf/16498_15_12.pdf) 
- Trupia, A., Saygun, A. Betonarme Yüzeysel Temeller, Nobel Yayın Dağıtım, Ankara, 2009. 
- [Bellos, John & Bakas, Nikolaos. (2017). Complete Analytical Solution for Linear Soil Pressure Distribution under Rigid Rectangular Spread Footings. International Journal of Geomechanics.](https://www.researchgate.net/publication/312362987_Complete_Analytical_Solution_for_Linear_Soil_Pressure_Distribution_under_Rigid_Rectangular_Spread_Footings)
