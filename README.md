# Simulação da Bolsa de Valores com Rabbit MQ

Escreva um ou dois  parágrafo resumindo o objetivo do seu projeto.

## Alunos integrantes da equipe

* Carla d'Abreu Martins Vieira
* Otávio Vinícius Guimarães Silveira Rocha

## Professor responsável

* Hugo Bastos de Paula

## Instruções de utilização

### RabbitMQ

Para baixar e instalar o RabbitMQ você pode sequir as orientações na [Documentação Oficial do RabbitMQ](https://www.rabbitmq.com/download.html)

Uma opção recomendada é utilizar a imagem docker produzida pela comunidade, rodando o seguinte comando no terminal:

```shell
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

### Python

O sistema foi desenvolvido utilizando a versão 3.6.9 do Python. Para baixar a última versão do Python, você pode acessar [a página oficial do Python](https://www.python.org/downloads/).
Caso tenha interesse, você pode utilizar de um ambiente vitual. Você pode utilizar [Tutorial da Documentação Oficial do Python](https://docs.python.org/3/tutorial/venv.html) para criar um ambiente virtual e ativá-lo.

### Requirements

A dependẽncias básica para o sistema pode ser encontrados no arquivo [requirements.txt](https://github.com/PUC-ES-LDAMD/bovespa-rabbitmq-carlavieira-oGuimaraes/blob/master/requirements.txt) e são eles: 

```txt
pika==1.1.0
PySimpleGUI==4.29.0
```

Para instalar as dependências do projeto, você pode rodar o seguinte comando:
```shell
pip install -r requirements.txt
```
## Interface da Corretora

Para ter acesso a interface da corretora, vocẽ deve, na raiz do projeto, rodar o seguinte comando:

```shell
python gui_broker.py
```
Nessa interface vocẽ pode colocar o servidor o qual quer conectar ao RabbitMQ e as informações da oferta de compra ou venda, sendo elas o nome da corretora que está ofertando, qual dos ativos a disposição vai ser ofertado, a quantidade e o preço, nessa respectiva ordem.
Se for uma oferta de compra, selecionar o botão "Compra", se for de venda, o botão "Venda"
Para poder acompanhar qualquer motimentação (ofertas de compra, ofertas de venda ou transações) sobre um ou mais ativos, você pode apertar o botão "Abrir Visualizador". 
Assim, irá abrir uma nova interface onde você pode colocar o servidor o qual quer conectar ao RabbitMQ, e então selecionar os ativos que quer seguir. Para selecionar um ativo, basta escolhe-lo entre as opções mostradas e clicar no botão "Adicionar a lista". Caso tenha cometido algum erro ou queira mudar as seleções escolhidas, você pode clicar em "Limpar Lista" e recomeçar a sua escolha. Quando você estiver sua lista pronta, clique em "Acompanhar" para receber no painel qualquer motimentação sobre aqueles ativos.

## Interface da Bolsa de Valores

Para ter acesso a interface da bolsa de valores, vocẽ deve, na raiz do projeto, rodar o seguinte comando:

```shell
python gui_stock.py
```
Nela você pode inserir o servidor que gostaria de conectar ao RabbitMQ e então abrir as negociações da bolsa. No visor você irá receber ofertas de compra e venda das corretoras, e a bolsa encaminha essas ofertas para as corretoras que estão acompanhando os respectivos ativos. Quando uma opção de compra for de preço maior ou igual de uma oferta de venda cadastrada no livro de ofertas sobre um mesmo ativo ou uma oferta de venda for de valor menor ou igual a uma de compra cadastrada, é gerado automaticamente uma trnasação entre as corretoras e a mensagem sobre a trnasação é enviada a todas as corretoras que acompanham aquele ativo.