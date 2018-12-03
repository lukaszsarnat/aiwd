import pandas as pd
import scipy.stats as st

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
dane=dane.sort_values(by="Happiness Score", ascending=False)
region=dane["Region"]
kraj=dane["Country"]
wskaznikSzczescia=dane["Happiness Score"]

najwyzszyWskaznikRegion=[]
najwyzszyWskaznikKraj=[]
najwyzszyWskaznikWskaznik=[]

for i in range(len(region)):
    if not region[i] in najwyzszyWskaznikRegion:
        najwyzszyWskaznikRegion.append(region[i])
        najwyzszyWskaznikKraj.append(kraj[i])
        zaokraglonyWskaznik=round(wskaznikSzczescia[i],2)
        najwyzszyWskaznikWskaznik.append(zaokraglonyWskaznik)
print(najwyzszyWskaznikKraj)
print(najwyzszyWskaznikRegion)
print(najwyzszyWskaznikWskaznik)

# 2. Jaka jest korelacja ekonomii i szczęścia? [Wykres]
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]

print(st.pearsonr(wskaznikSzczescia,ekonomia))

#Wykres #1
plt.plot(wskaznikSzczescia,label="Wskaźnik szczęścia")
plt.plot(ekonomia,label="Zadowolenie z sytuacji ekonomicznej")
plt.legend()
plt.xlabel("Indeks kraju")
plt.ylabel("Wysokość wskaźnika/ wpływu na wskaźnik")
plt.show()

# 3. Który wskaźnik ma najwięcej korelacji ze szczęściem? [Wykres]
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]
rodzina=dane["Family"]
zdrowie=dane["Health (Life Expectancy)"]
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]
zyczliwosc=dane["Generosity"]

korelacjaEkonomia=st.pearsonr(wskaznikSzczescia,ekonomia)[0]
korelacjaRodzina=st.pearsonr(wskaznikSzczescia,rodzina)[0]
korelacjaZdrowie=st.pearsonr(wskaznikSzczescia,zdrowie)[0]
korelacjaWolnosc=st.pearsonr(wskaznikSzczescia,wolnosc)[0]
korelacjaZaufanie=st.pearsonr(wskaznikSzczescia,zaufanie)[0]
korelacjaZyczliwosc=st.pearsonr(wskaznikSzczescia,zyczliwosc)[0]
korelacjeWskaznikow=[korelacjaEkonomia,korelacjaRodzina,korelacjaZdrowie,korelacjaWolnosc,korelacjaZaufanie,korelacjaZyczliwosc]
print(korelacjeWskaznikow)

#Wykres #2
podpisy=["Ekonomia","Rodzina","Zdrowie","Wolność","Zaufanie","Życzliwość"]
plt.bar(podpisy,korelacjeWskaznikow)
plt.xlabel("Wskaźnik")
plt.ylabel("Wartość korelacji")
plt.show()

# 4. Jakie jest średnie szczęście w każdym regionie? [Wykres]
dane=dane.sort_values(by="Region")
dane=dane.reset_index(drop=True)
region=dane["Region"]
wskaznikSzczescia=dane["Happiness Score"]

sredniWskaznikRegion=[]
sredniWskaznikWskaznik=[]
listaWskaznikow=[]

for i in range(len(region)):
    if i!=157 and region[i+1]==region[i]:
        listaWskaznikow.append(wskaznikSzczescia[i])
    elif i==157:
        listaWskaznikow.append(wskaznikSzczescia[i])
        sredniWskaznikRegion.append(region[i])
        sredniWskaznikWskaznik.append(sum(listaWskaznikow)/len(listaWskaznikow))
        del listaWskaznikow
        listaWskaznikow=[]
    else:
        listaWskaznikow.append(wskaznikSzczescia[i])
        sredniWskaznikRegion.append(region[i])
        sredniWskaznikWskaznik.append(sum(listaWskaznikow)/len(listaWskaznikow))
        del listaWskaznikow
        listaWskaznikow=[]
print(sredniWskaznikRegion)
print(sredniWskaznikWskaznik)

#Wykres #3
podpisyRegion=["AANZ","CAEE","EA","LAAC","MEANA","NA","SEA","SA","SSA","WE"]
plt.bar(podpisyRegion,sredniWskaznikWskaznik)
plt.xlabel("Region")
plt.ylabel("Średnia wartość oceny szczęścia")
plt.show()

# 5. Który region ma najwięcej krajów ze wskaźnikiem szczęścia powyżej mediany? [Wykres]
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
podpisyRegion=["AANZ","CAEE","EA","LAAC","MEANA","NA","SEA","SA","SSA"]
iloscPowyzejMediany=[listaRegionow["Australia and New Zealand"],listaRegionow["Central and Eastern Europe"],listaRegionow["Eastern Asia"],listaRegionow["Latin America and Caribbean"],listaRegionow["Middle East and Northern Africa"],listaRegionow["North America"],listaRegionow["Southeastern Asia"],listaRegionow["Southern Asia"],listaRegionow["Sub-Saharan Africa"],listaRegionow["Western Europe"]]
plt.bar(podpisyRegion,iloscPowyzejMediany)
plt.xlabel("Region")
plt.ylabel("Kraje o wartości ocenionego szczęścia powyżej mediany")
plt.show()
# 6. Jaka jest korelacja między wolnością a zaufaniem do rządu?
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]

print(st.pearsonr(wolnosc,zaufanie))

# 7. Jaka jest korelacja między ekonomią a zdrowiem?
ekonomia=dane["Economy (GDP per Capita)"]
zdrowie=dane["Health (Life Expectancy)"]

print(st.pearsonr(ekonomia,zdrowie))
