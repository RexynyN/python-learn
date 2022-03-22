import requests as r 
import datetime as dt
from PIL import Image
from IPython.display import display
from urllib.parse import quote
import csv

 
def get_datasets (y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label':labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return[{
            'label': labels[0],
            'data':y
        }] 

def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'

    return {
        'title': title,
        'display': display
    }

def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y,labels)
    options = set_title(title)

    chart = {
        'type':kind,
        'data': {
            'labels':x,
            'datasets':datasets,
        },
        'options':options
    }
    return chart

def get_api_chart(chart):
    url = 'https://quickchart.io/chart'
    resp = r.get(f'{url}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

def get_api_qrcode(link):
    text = quote(link) # parsing do link para URL
    url = 'http://quickchart.io/qr'
    resp = r.get(f'{url}?text={text}')
    return resp.content

url = "https://api.covid19api.com/dayone/country/brazil"
resp = r.get(url)
print(resp.status_code)

raw_data = resp.json()
# print(raw_data)

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
# print(final_data)

final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

# Formatando a Data
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

with open('projeto-covid.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], "%Y-%m-%d")

y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime("%d/%m/%Y"))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')

url = 'https://quickchart.io/chart'
link = f'{url}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')
