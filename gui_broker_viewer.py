import PySimpleGUI as sg
from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker

from assets.assets_list import AssetsList

sg.theme('Default 1') 

# Layout
layout = [
	[sg.Text('Broker Viewer', size=(40, 0), font=('Helvetica', 12), justification='center')],
	[sg.Text('Servidor'), sg.Input('localhost')],
	[sg.Text('Ativo'), sg.Combo(AssetsList.get_assetslist(), key='assets')],
	[sg.Button('Adicionar a Lista', size=(21,0)), sg.Button('Limpar Lista', size=(21,0))],
	[sg.T('Acompanhando:'), sg.T('', size=(40,2), key='tracked_assets')],
	[sg.Button('Acompanhar', size=(42,0))],
	[sg.Output(size=(60,20))]
]

command_history = []
history_offset = 0
#Window


window = sg.Window('Broker Viewer', layout, margins=(20, 20))
receive_brocker = ReceiveBroker(host='localhost', binding_keys=['*.petr3', '*.itub4'])
receive_brocker.start()

while True:
	event, values = window.read()
	if event == 'Adicionar a Lista':
		assets = values['assets'].rstrip()
		command_history.append(assets)
		history_offset = len(command_history)-1
		window.FindElement('tracked_assets').Update(command_history)
	elif event == 'Limpar Lista':
		window.FindElement('tracked_assets').Update([])
		command_history.clear()
	elif event == 'Acompanhar':
		arrAssets = []
		for x in command_history:
			assetsNome = '*.'+x.lower()
			arrAssets.append(assetsNome)
		print('----')
		#receive_brocker = ReceiveBroker(host='localhost', binding_keys=arrAssets)
		#receive_brocker.start()
	if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
		break
window.close()


