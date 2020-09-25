import PySimpleGUI as sg

from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker
from assets_list import AssetsList

sg.theme('Default 1') 

# Get assets from assets_list
assets = AssetsList.get_assetslist()

# Layout
layout = [
  [sg.Text('Broker Panel', size=(40, 0), font=('Helvetica', 12), justification='center')],
  [sg.Text('Servidor'), sg.Input('localhost', size=(0,2))],
  [sg.Text('Informações da oferta:', size=(30,2))],
  [sg.Text('Broker'), sg.Combo(assets)],
  [sg.Text('Ativo'), sg.Combo(assets)],
  [sg.Text('Quantidade'), sg.Input('')],
  [sg.Text('Preço'), sg.Input('')],
  [sg.Button('Compra', size=(20, 0)), sg.Button('Venda', size=(20, 0))],
  [sg.Button('Abrir Visualizador', size=(42,0))]
]

#Window
window = sg.Window('Broker Panel', layout, margins=(20, 20))

while True:
  event, values = window.read()
  if event.lower() == 'compra' or event.lower() == 'venda':
    routing_key = event.lower() + '.' + values[2].lower()
    message = values[3] + '; ' + values[4] + '; ' + values[1].lower()
    print(message)
    emit_broker = EmitBroker(host=values[0], routing_key=routing_key, message=message)
    emit_broker.start() 
  if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    break
