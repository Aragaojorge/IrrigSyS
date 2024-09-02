# Projeto de Monitoramento de Umidade e Temperatura do Solo


## Este projeto tem como objetivo monitorar e visualizar dados de umidade do solo e temperatura coletados em tempo real. A aplicação utiliza Flask como framework web, PostgreSQL como banco de dados, Pandas para manipulação de dados e Matplotlib para geração de gráficos. A interface permite ao usuário selecionar um intervalo de tempo específico para visualizar a evolução das medições.


## Estrutura do Projeto

```
/IRRIGSYS
│
├── /static
│   └── /css
│       └── styles.css     # Arquivo CSS para estilização da página
|── /templates
|    └── index.html        # Template HTML para a interface do usuário
├── app.py                 # Arquivo principal da aplicação Flask
├── config.py              # Configuração dos pinos do Raspberry PI
├── irrigation_control.py  # Lógica da irrigação
├── main.py                # Execução da lógica da irrigação
└── sensors.py             # Leitura dos dados dos sensores e persistências dos dados no bando de dados sensor_Data
```

## Funcionalidades

Monitoramento de Umidade e Temperatura: Coleta e armazena dados em um banco de dados PostgreSQL.

Visualização Gráfica: Gera gráficos de umidade do solo e temperatura ao longo do tempo.

Filtro por Intervalo de Tempo: Permite a seleção de datas específicas para visualização dos dados.


## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado os seguintes componentes:

Python 3.x

PostgreSQL

pip (gerenciador de pacotes do Python)


## Instalação

Clone o repositório para a sua máquina local:

git clone https://github.com/Aragaojorge/IrrigSyS/

cd seu_projeto


## Crie um ambiente virtual:

python -m venv venv

source venv/bin/activate   

# No Windows: venv\Scripts\activate


## Configure o banco de dados PostgreSQL:

Crie um banco de dados chamado irrig_sys.

Ajuste as configurações de conexão no arquivo app.py se necessário.


## Execute a aplicação:


flask run


## Acesse a aplicação via navegador no endereço:

http://127.0.0.1:5000/


## Como Usar

Acesse a Interface Web: Ao iniciar a aplicação, abra o navegador e navegue até http://127.0.0.1:5000/.


## Tecnologias Utilizadas

Flask: Framework web para criar a aplicação.

PostgreSQL: Banco de dados utilizado para armazenar as leituras dos sensores.

Pandas: Biblioteca para manipulação de dados tabulares.

Matplotlib: Biblioteca para geração de gráficos.

HTML/CSS: Usados para criar a interface do usuário.


## Contribuição

Sinta-se à vontade para contribuir com o projeto. Para isso, siga as etapas abaixo:



## Fork o projeto.

Crie uma branch para sua funcionalidade (git checkout -b feature/sua-funcionalidade).

Commit suas alterações (git commit -am 'Add nova funcionalidade').

Push para a branch (git push origin feature/sua-funcionalidade).

Crie um novo Pull Request.


## Licença

Este projeto está licenciado sob a MIT License.


## Agradecimentos
Este projeto foi desenvolvido como parte de um trabalho de extensão da disciplina Tópicos de Big Data em Python do curso Análise e Desenvolvimento de Sistema da faculdade Estácio, focado em monitoramento ambiental utilizando tecnologias Raspberry(Captação de dados de sensores de monitoramento), análises de dados(Pandas), exibição de dados(Matplotlib) web(Flask) e banco de dados(Postgres).

