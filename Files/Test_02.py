import collections
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Ongoing\Melani\CSV\Southwales_2020.csv')

grouped_data = df.groupby('Month')
counts = collections.Counter(grouped_data.groups)
for value, count in counts.items():
    print(f"{value}: {count}")

print(grouped_data.groups)
value_counts = df['Crime type'].value_counts()
#print(value_counts)
#print(value_counts.keys())
print(value_counts.values)

plt.bar(value_counts.keys(), value_counts.values, color='g', width=0.72, label=value_counts.keys())
plt.xlabel('Names')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()

plt.pie(value_counts.values,labels = value_counts.keys(),autopct = '%.2f%%')
plt.title( 'Crime Percentages', loc = 'left', color='blue', fontweight='bold', fontsize = 15)
plt.show()
