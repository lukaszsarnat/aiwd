import pandas as pd
import scipy.stats as st
import matplotlib as plt

dane=pd.read_csv("c:/2015.csv")

dane=dane.sort_values(by="Happiness Score", ascending=False)

kraj=dane["Country"]
region=dane["Region"]
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]
rodzina=dane["Family"]
zdrowie=dane["Health (Life Expectancy)"]
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]
zyczliwosc=dane["Generosity"]

# 1. Jaki kraj w każdym regionie ma najwyższy wskaźnik szczęścia?
'''
Dla najwyższego:
    Potrzebne sortowanie malejące według szczęścia.
    Pętla przechodzi przez każdy wiersz, sprawdza czy region przypisany wierszowi był sprawdzany, (i znajduje się w zmiennej najwyzszyWskaznikRegion) jeśli nie, to dodaje ten wskaźnik. Wiadomo że dodana wartość wskaźnika jest najwyższa dla danego regionu dzięki wstępnym sortownaniu.
Dla najniższego:
    Potrzebne sortowanie rosnące.
    Pętla przebiega tak samo jak przy najwyższych wskaźnikach, ale dodając najniższe.
'''
dane=dane.sort_values(by="Happiness Score", ascending=False)
region=dane["Region"]
kraj=dane["Country"]
wskaznikSzczescia=dane["Happiness Score"]

najwyzszyWskaznikRegion=[]
najwyzszyWskaznikKraj=[]
najwyzszyWskaznikWskaznik=[]
najnizszyWskaznikRegion=[]
najnizszyWskaznikKraj=[]
najnizszyWskaznikWskaznik=[]

for i in range(len(region)):
    if not region[i] in najwyzszyWskaznikRegion:
        najwyzszyWskaznikRegion.append(region[i])
        najwyzszyWskaznikKraj.append(kraj[i])
        zaokraglonyWskaznik=round(wskaznikSzczescia[i],2)
        najwyzszyWskaznikWskaznik.append(zaokraglonyWskaznik)
dane=dane.sort_values(by="Happiness Score", ascending=True)
dane=dane.reset_index(drop=True)
region=dane["Region"]
kraj=dane["Country"]
wskaznikSzczescia=dane["Happiness Score"]
for i in range(len(region)):
    if not region[i] in najnizszyWskaznikRegion:
        najnizszyWskaznikRegion.append(region[i])
        najnizszyWskaznikKraj.append(kraj[i])
        zaokraglonyWskaznik=round(wskaznikSzczescia[i],2)
        najnizszyWskaznikWskaznik.append(zaokraglonyWskaznik)
print(najwyzszyWskaznikKraj)
print(najwyzszyWskaznikRegion)
print(najwyzszyWskaznikWskaznik)
print('*' * 100)
print(najnizszyWskaznikKraj)
print(najnizszyWskaznikRegion)
print(najnizszyWskaznikWskaznik)

# 2. Jaka jest korelacja ekonomii i szczęścia? [Wykres]
'''
Użycie r Pearsona do obliczenia korelacji.
'''
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]

print(st.pearsonr(wskaznikSzczescia,ekonomia))

#Wykres #1
f = plt.figure(figsize=(8,5))
plot1=f.add_subplot(1,1,1)
plot1.plot(wskaznikSzczescia,label="Wskaźnik szczęścia")
plot2=f.add_subplot(1,1,1)
plot2.plot(ekonomia,label="Wpływ PKB")
f.legend()
plot1.set_xlim(0,158)
plot2.set_xlim(0,158)
plot1.set_xlabel("Indeks kraju")
plot2.set_ylabel("Wysokość wskaźnika/wpływu na wskaźnik")

# 3. Który wskaźnik ma najwięcej korelacji ze szczęściem? [Wykres]
'''
Użycie r Pearsona do obliczenia korelacji.
'''
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]
rodzina=dane["Family"]
zdrowie=dane["Health (Life Expectancy)"]
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]
szczodrosc=dane["Generosity"]

korelacjaEkonomia=st.pearsonr(wskaznikSzczescia,ekonomia)[0]
korelacjaRodzina=st.pearsonr(wskaznikSzczescia,rodzina)[0]
korelacjaZdrowie=st.pearsonr(wskaznikSzczescia,zdrowie)[0]
korelacjaWolnosc=st.pearsonr(wskaznikSzczescia,wolnosc)[0]
korelacjaZaufanie=st.pearsonr(wskaznikSzczescia,zaufanie)[0]
korelacjaSzczodrosc=st.pearsonr(wskaznikSzczescia,szczodrosc)[0]
korelacjeWskaznikow=[korelacjaEkonomia,korelacjaRodzina,korelacjaZdrowie,korelacjaWolnosc,korelacjaZaufanie,korelacjaSzczodrosc]
print(korelacjeWskaznikow)

#Wykres #2
podpisy=["Ekonomia","Rodzina","Zdrowie","Wolność","Zaufanie","Szczodrość"]
f = plt.figure(figsize=(8,5))
bar = f.add_subplot(1,1,1)
bar.bar(podpisy,korelacjeWskaznikow)
bar.set_xlim(-1,6)
bar.set_xlabel("Czynnik wpływu")
bar.set_ylabel("Wartość korelacji")

# 4. Jakie jest średnie szczęście w każdym regionie? [Wykres]
'''
Potrzebne sortowanie według regionów.
Pętla przechodzi przez każdy wiersz i dodaje wartości takiego samego regionu do listy, i jeśli następna komórka nie jest dla takiego samego regionu, liczy średnią w liście i zapisuje do zmiennej, po czym przechodzi do następnego regionu.
'''
dane=dane.sort_values(by="Region")
dane=dane.reset_index(drop=True)
region=dane["Region"]
wskaznikSzczescia=dane["Happiness Score"]

sredniWskaznikRegion=[]
sredniWskaznikWskaznik=[]
listaWskaznikow=[]

for i in range(len(region)):
    if i!=157 and region[i+1]==region[i]:
        listaWskaznikow.append(round(wskaznikSzczescia[i],2))
    elif i==157:
        '''
        Liczy ostatni wiersz
        '''
        listaWskaznikow.append(round(wskaznikSzczescia[i],2))
        sredniWskaznikRegion.append(region[i])
        sredniWskaznikWskaznik.append(sum(listaWskaznikow)/len(listaWskaznikow))
        del listaWskaznikow
        listaWskaznikow=[]
    else:
        listaWskaznikow.append(round(wskaznikSzczescia[i],2))
        sredniWskaznikRegion.append(region[i])
        sredniWskaznikWskaznik.append(sum(listaWskaznikow)/len(listaWskaznikow))
        del listaWskaznikow
        listaWskaznikow=[]
print(sredniWskaznikRegion)
print(sredniWskaznikWskaznik)

#Wykres #3
podpisyRegion=["AANZ","CAEE","EA","LAAC","MEANA","NA","SEA","SA","SSA","WE"]
f = plt.figure(figsize=(8,5))
bar = f.add_subplot(1,1,1)
bar.bar(podpisyRegion,sredniWskaznikWskaznik)
bar.set_xlim(-1,10)
bar.set_xlabel("Region")
bar.set_ylabel("Średnia wartość wskaźnika szczęścia")

# 5. Który region ma najwięcej krajów ze wskaźnikiem szczęścia powyżej mediany? [Wykres]
'''
Potrzebne sortowanie malejące według szczęścia.
Pętla przechodzi przez wiersz, jeśli wartość wskaźnika szczęścia jest w nim większa od mediany, pozycja tego samego regionu co w wierszu zostaje zwiększona o 1.
'''
kraj=dane["Country"]
region=dane["Region"]
wskaznikSzczescia=dane["Happiness Score"]
mediana=wskaznikSzczescia.median()

listaRegionow={"Australia and New Zealand":0,"Central and Eastern Europe":0,"Eastern Asia":0,"Latin America and Caribbean":0,"Middle East and Northern Africa":0,"North America":0,"Southeastern Asia":0,"Southern Asia":0,"Sub-Saharan Africa":0,"Western Europe":0}

for i in range(len(region)):
    if wskaznikSzczescia[i]>mediana:
        for p in listaRegionow:
            if region[i]==p:
                listaRegionow[p]+=1

print(listaRegionow)

#Wykres #4
podpisyRegion=["AANZ","CAEE","EA","LAAC","MEANA","NA","SEA","SA","SSA","WE"]
iloscPowyzejMediany=[listaRegionow["Australia and New Zealand"],listaRegionow["Central and Eastern Europe"],listaRegionow["Eastern Asia"],listaRegionow["Latin America and Caribbean"],listaRegionow["Middle East and Northern Africa"],listaRegionow["North America"],listaRegionow["Southeastern Asia"],listaRegionow["Southern Asia"],listaRegionow["Sub-Saharan Africa"],listaRegionow["Western Europe"]]
f = plt.figure(figsize=(8,5))
bar = f.add_subplot(1,1,1)
plt.bar(podpisyRegion,iloscPowyzejMediany)
bar.set_xlim(-1,10)
bar.set_xlabel("Region")
bar.set_ylabel("Ilość krajów o wartości wskaźnika powyżej mediany")

# 6. Jaka jest korelacja między wolnością a zaufaniem do rządu?
'''
Użycie r Pearsona do obliczenia korelacji.
'''
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]

print(st.pearsonr(wolnosc,zaufanie))

# 7. Jaka jest korelacja między ekonomią a zdrowiem?
'''
Użycie r Pearsona do obliczenia korelacji.
'''
ekonomia=dane["Economy (GDP per Capita)"]
zdrowie=dane["Health (Life Expectancy)"]

print(st.pearsonr(ekonomia,zdrowie))
