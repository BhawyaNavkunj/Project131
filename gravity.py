import pandas as pd

df = pd.read_csv('final.csv')

print(df.head())

df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df.head())

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

for i in range(0,len(radius)-1):
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30

G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)

df["Gravity"] = gravity

df.to_csv("star_with_gravity.csv")

df.dtypes