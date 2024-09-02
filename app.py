from flask import Flask, render_template
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
import base64


app = Flask(__name__)


def get_db_connection():
    
    # Cria a conexão com o db sensor_data
    conn = psycopg2.connect("dbname='irrig_sys' user='jorge' password='123456' host='localhost'")
    
    # Abri um cursor para performar consultas no db
    cur = conn.cursor()
    
    # Executar uma consulta
    cur.execute("SELECT * FROM sensor_data")
    
    # Recuperar os dados da consulta
    records = cur.fetchall()
    
    # Fechar o cursor
    cur.close()
    
    # Fechar a conexão
    conn.close()
    
    # Enviar os dados
    return records

@app.route("/", methods=['GET'])
def hello():
    
    sensor_data = get_db_connection()
    
    # Conversão dos dados para Dataframe
    df = pd.DataFrame(sensor_data, columns=['id', 'timestamp', 'soil_moisture', 'temperature', 'rain_sensor'])
    
    # Criação dos gráficos
    plt.figure(figsize=(10,5))
    plt.plot(df['timestamp'], df['soil_moisture'], label='Umidade do Solo')
    plt.plot(df['timestamp'], df['temperature'], label='Temperatura')
    # Criando os eixos
    plt.xlabel('Data')
    plt.ylabel('Valores')
    # Criando o título do gráfico
    plt.title('Temperatura e Umidade do Solo')
    # Posicionamento da legenda do gráfico
    plt.legend(loc='lower left', bbox_to_anchor=(1,1))
    # Formatar as datas para o formato dia/mês/ano
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    # Exibir apenas as datas com dados
    plt.xticks(df['timestamp'])
    # Rotacionar as datas
    plt.xticks(rotation=45)
    
    # Converter o gráfico em imagem para base64
    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    
    return render_template('index.html', plot_url=plot_url)


if __name__ == '__main__':
    app.run(debug=True)

