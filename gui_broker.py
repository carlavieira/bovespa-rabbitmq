import PySimpleGUI as sg

from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker
from assets.assets_list import AssetsList

sg.theme('Default 1') 

# Layout

layout = [
  [sg.Text('Broker Panel', size=(40, 0), font=('Helvetica', 12), justification='center')],
  [sg.Text('Servidor'), sg.Input('localhost')],
  [sg.Text('Broker'), sg.Input('BKR1')],
  [sg.Text('Ativo'), sg.Combo(AssetsList.get_assetslist())],
  [sg.Text('Quantidade'), sg.Input('', key='quantity')],
  [sg.Text('Preço'), sg.Input('', key='price')],
  [sg.Button('Compra', size=(20, 0)), sg.Button('Venda', size=(20, 0))],
  [sg.Button('Abrir Visualizador', size=(42,0))]
]

#Window
window = sg.Window('Broker Panel', layout, margins=(20, 20))

while True:
  event, values = window.read()
  """
  submitValues = {
    "ip": values[0],
    "broker": values[1],
    "active": values[2] ,
    "quantity": values[3],
    "price": values[4],
    "event": event.lower()
  }
  print(routing_key, message)

  print(submitValues)
  """
  # if values[3] != 0 and values[4] != 0:
  window.FindElement('price').Update('') 
  window.FindElement('quantity').Update('')
  if event.lower() == 'compra' or event.lower() == 'venda':
    routing_key = event.lower() + '.' + values[2].lower()
    message = values[3] + '; ' + values[4] + '; ' + values[1]
    
    emit_broker = EmitBroker(host=values[0], routing_key=routing_key,      message=message)
    emit_broker.start()
    window.FindElement('price').Update('') 
    window.FindElement('quantity').Update('')
  if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    break
window.close()