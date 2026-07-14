import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TSA11.20260713220302.csv')

df_clean = df[
    (df['Statistic Label'] == 'Value of Exports') &
    (df['Year'] == 2017) &
    (~df['Sector of Activity'].str.contains('All Sectors', case = False))
]

sector_totals = df_clean.groupby('Sector of Activity')['VALUE'].sum()
print(sector_totals)

top_sector = sector_totals.idxmax()
top_value = sector_totals.max()
print (top_sector,'-',top_value)

df_all_years = df[
    (df['Statistic Label']== 'Value of Exports') &
    (~df['Sector of Activity'].str.contains('All Sectors',case=False))
]

yearly_totals = df_all_years.groupby(['Year','Sector of Activity'])['VALUE'].sum()
print(yearly_totals)

chart_data = yearly_totals.unstack()
print(chart_data)

plt.figure(figsize=(12,6))
chart_data.plot(kind='line',marker = 'o')
plt.title("Ireland Export by Sector (2017 -2022)")
plt.xlabel('Year')
plt.ylabel('Value (€ Millions)')
plt.legend(title = 'Sector',bbox_to_anchor =(0,1),loc = 'upper left',fontsize = 9, title_fontsize=10)
plt.tight_layout()
plt.savefig('exports_by_sector.png', dpi = 150, bbox_inches = 'tight')
plt.show()