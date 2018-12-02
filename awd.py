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

# 3. Który wskaźnik ma najwięcej korelacji ze szczęściem? [Wykres]
wskaznikSzczescia=dane["Happiness Score"]
ekonomia=dane["Economy (GDP per Capita)"]
rodzina=dane["Family"]
zdrowie=dane["Health (Life Expectancy)"]
wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]
zyczliwosc=dane["Generosity"]

print(st.pearsonr(wskaznikSzczescia,ekonomia))
print(st.pearsonr(wskaznikSzczescia,rodzina))
print(st.pearsonr(wskaznikSzczescia,zdrowie))
print(st.pearsonr(wskaznikSzczescia,wolnosc))
print(st.pearsonr(wskaznikSzczescia,zaufanie))
print(st.pearsonr(wskaznikSzczescia,zyczliwosc))

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
    else:
        sredniWskaznikRegion.append(region[i])
        sredniWskaznikWskaznik.append(sum(listaWskaznikow)/len(listaWskaznikow))
        del listaWskaznikow
        listaWskaznikow=[]

print(sredniWskaznikRegion)
print(sredniWskaznikWskaznik)

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



# 6. Jaka jest korelacja między wolnością a zaufaniem do rządu?

wolnosc=dane["Freedom"]
zaufanie=dane["Trust (Government Corruption)"]

print(st.pearsonr(wolnosc,zaufanie))

# 7. Jaka jest korelacja między ekonomią a zdrowiem?

ekonomia=dane["Economy (GDP per Capita)"]
zdrowie=dane["Health (Life Expectancy)"]

print(st.pearsonr(ekonomia,zdrowie))
