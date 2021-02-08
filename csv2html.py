import pandas as pd


df = pd.read_csv('papers.csv', delimiter=';', header=0, engine='python', keep_default_na=False)
df.sort_values(by=['Year'])
years = df['Year'].unique()
header = df.columns

html = ""
for year in years:
    publications = df.loc[df['Year'] == year]
    html += "<p style='font-size:26px;text-align:center'><strong>{}</strong></p><ul>".format(year)

    yearstr = ""
    for index, row in publications.iterrows():
        yearstr += "<li style='margin-bottom: 10px'><b>{}</b>|".format(row['Name'])
        yearstr += "<a href='{}' target='_blank' rel='noopener'> <img src='/wp-content/uploads/sites/53/2019/09/link_icon.png' width='14' height='14'> </a>".format(row['Link'])
        yearstr += "<span style='font-size: 10pt'><br><em>{} | {} | {}</em></span><br></li>".format(row['Authors'], row['Where'], year)

    html += "{}</ul>".format(yearstr)

with open("htmlcode.txt", 'w') as f:
    f.write(html)