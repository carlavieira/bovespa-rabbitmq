import PySimpleGUI as sg
from stock.emit_stock import EmitStock
from stock.receive_stock import ReceiveStock
import time


sg.theme('Default 1') 

# Layout

layout = [
  [sg.Text('Stock Painel', size=(40, 0), font=('Helvetica', 12), justification='center')],
  [sg.Text('Servidor'), sg.Input('localhost')],
  [sg.Output(size=(60,20))]
]

#Window
window = sg.Window('Stock Painel', layout, margins=(20, 20))

receive_stock = ReceiveStock(host='localhost')
receive_stock.start()


while True:
  event, values = window.read()
  #print(event)
  #print(values)
  if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    break
window.close()




