import PySimpleGUI as sg
sg.theme('Default 1') 

class Screen:
  def __init__(self):
    # Layout

    layout = [
      [sg.Text('Broker Panel')],
      [sg.Text('Servidor'), sg.Input('localhost')],
      [sg.Text('Broker'), sg.Input('BKR1')],
      [sg.Text('Ativo'), sg.Combo(['ABEV3', 'PETR4', 'VALE5', 'ITUB5', 'BBDC4','BBAS3', 'CIEL3', 'PEETR3', 'HYPE3', 'VALE3',
      'BBSE3', 'CTIP3', 'GGBR4', 'FIBR3', 'RADL3'])],
      [sg.Text('Quantidade'), sg.Input()],
      [sg.Text('Preço'), sg.Input('')],
      [sg.Button('Comprar', size=(20, 0)), sg.Button('Vender', size=(20, 0))],
      [sg.Button('Abrir Visualizador', size=(42,0))]
    ]

    #Window
    janela = sg.Window('Broker Panel', element_justification='c').layout(layout)

    # Data
    self.button, self.values = janela.Read()

  def initialize(self):
    print(self.values)

tela = Screen()
tela.initialize()