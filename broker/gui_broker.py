import PySimpleGUI as sg
sg.theme('Default 1') 

# Layout

layout = [
  [sg.Text('Broker Panel', size=(40, 0), font=('Helvetica', 12), justification='center')],
  [sg.Text('Servidor'), sg.Input('localhost')],
  [sg.Text('Broker'), sg.Input('BKR1')],
  [sg.Text('Ativo'), sg.Combo([
    'ABEV3', 'PETR4', 'VALE5',
    'ITUB5', 'BBDC4','BBAS3', 
    'CIEL3', 'PEETR3', 'HYPE3', 
    'VALE3','BBSE3', 'CTIP3', 
    'GGBR4', 'FIBR3', 'RADL3'])],
  [sg.Text('Quantidade'), sg.Input()],
  [sg.Text('Preço'), sg.Input('')],
  [sg.Button('Comprar', size=(20, 0)), sg.Button('Vender', size=(20, 0))],
  [sg.Button('Abrir Visualizador', size=(42,0))]
]

#Window
window = sg.Window('Broker Panel', layout, margins=(20, 20))

while True:
  event, values = window.read()
  submitValues = {
    "ip": values[0],
    "broker": values[1],
    "active": values[2] ,
    "quantity": values[3],
    "price": values[4],
    "event": event.lower()
  }
  print(submitValues)
  if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    break
window.close()