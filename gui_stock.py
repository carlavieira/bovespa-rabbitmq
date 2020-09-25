import PySimpleGUI as sg
from stock.emit_stock import EmitStock
from stock.receive_stock import ReceiveStock
import time
import os


sg.theme('Default 1') 

# Layout

layout = [
  [sg.Text('Stock Painel', size=(40, 0), text_color='#8B0000', font=('Helvetica', 12), justification='center')],
  [sg.Text('Servidor'),
   sg.Input('localhost', size=(26,0)),
   sg.Button('Abrir Negociações', size=(21, 0), key='button')],
  [sg.Output(size=(60,20))]
]

#Window
window = sg.Window('Stock Painel', layout, margins=(20, 20))


isUnderNegotiation = False
inNegotiation = False


while True:
  event, values = window.read()
  receive_stock = ReceiveStock(host=values[0])
  if event == 'button' and isUnderNegotiation == False and inNegotiation == False:
    inNegotiation = True
    isUnderNegotiation = True
    window.FindElement('button').Update('Negociações estão abertas')
    print('# Negociacões Abertas #\n')
    receive_stock.start()
  """
  else:
    isUnderNegotiation = False
    window.FindElement('button').Update('Abrir Negociações')
    #receive_stock = ReceiveStock(host=values[0])
    print('\n# Negociacões Fechadas #\n')
    #receive_stock.close()
  """
  if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    break
window.close()




