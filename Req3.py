import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('Req2.csv')
pos = 0
maxval = [[],[],[],[]]
minval = [[],[],[],[]]
openval = [[],[],[],[]]
closeval = [[],[],[],[]]
for i in range(3080):
    if (i > 0) and (df["Дата"][i] != df["Дата"][i-1]):
        pos+=1
    maxval[pos].append(df["Макс"][i])
    minval[pos].append(df["Мин"][i])
    openval[pos].append(df["Открытие"][i])
    closeval[pos].append(df["Закрытие"][i])
columns = []
for i in range(4):
    columns.append(openval[i])
    columns.append(maxval[i])
    columns.append(minval[i])
    columns.append(closeval[i])
plt.boxplot(columns)
plt.xticks([i for i in range(1, 17)], ["13/09/18 - Открытие", "13/09/18 - Макс", "13/09/18 - Мин", "13/09/18 - Закрытие", "15/10/18 - Открытие", "15/10/18 - Макс", "15/10/18 - Мин", "15/10/18 - Закрытие", "13/11/18 - Открытие", "13/11/18 - Макс", "13/11/18 - Мин", "13/11/18 - Закрытие", "13/12/18 - Открытие", "13/12/18 - Макс", "13/12/18 - Мин", "13/12/18 - Закрытие"]) 
plt.show()
