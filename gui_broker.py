import PySimpleGUI as sg

from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker
from assets.assets_list import AssetsList


class gui_broker():
  
  #Set theme layout
  sg.theme('Default 1') 

  # Get assets from assets_list
  assets = AssetsList.get_assetslist()

  # Layout
  layout = [
    [sg.Text('Painel da Corretora', size=(40, 0), text_color='#8B0000', font=('Helvetica', 12), justification='center')],
    [sg.Text('Servidor'), sg.Input('localhost', size=(20,2))],
    [sg.Text('Informações da oferta:',text_color='red', justification='center')],
    [sg.Text('Cod. Corretora'), sg.Combo(assets), sg.Text('Ativo'), sg.Combo(assets)],
    [sg.Text('Quantidade'), sg.Input('', size=(7,0)), sg.Text('Preço'), sg.Input('', size=(7,0))],
    [sg.Button('Compra', size=(20, 0)), sg.Button('Venda', size=(20, 0))],
    #[sg.Button('Abrir Visualizador', size=(42,0))]
  ]

  #Window
  window = sg.Window('Painel da Corretora', layout, margins=(20, 20))

  while True:
    event, values = window.read()
    # Checks if quantity and price is not null
    if values[3] != '' and values[3] != '0' and values[4] != '' and values[4] != '0':

      # Checks if active and broker have been completed
      if values[1] != '' and values[2] != '':

        if event.lower() == 'compra' or event.lower() == 'venda':
          routing_key = event.lower() + '.' + values[2].lower()
          message = values[3] + '; ' + values[4] + '; ' + values[1].lower()

          emit_broker = EmitBroker(host=values[0], routing_key=routing_key, message=message)
          emit_broker.start() 

        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
          break
