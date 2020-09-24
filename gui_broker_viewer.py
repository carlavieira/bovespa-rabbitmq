import PySimpleGUI as sg
from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker

sg.theme('Default 1') 

# Layout
layout = [
	[sg.Text('Broker Viewer', size=(40, 0), font=('Helvetica', 12), justification='center')],
	[sg.Text('Servidor'), sg.Input('localhost')],
	[sg.Text('Ativo'), sg.Combo([
	'petr1', 'PETR4', 'petr2',
	'ITUB5', 'BBDC4','BBAS3', 
	'CIEL3', 'PEETR3', 'HYPE3', 
	'VALE3','BBSE3', 'CTIP3', 
	'GGBR4', 'FIBR3', 'RADL3'], key='assets')],
	[sg.Button('Adicionar a Lista', size=(21,0)), sg.Button('Limpar Lista', size=(21,0))],
	[sg.T('Acompanhando:'), sg.T('', size=(40,2), key='tracked_assets')],
	[sg.Button('Acompanhar', size=(42,0))],
	[sg.Output(size=(60,20))]
]

command_history = []
history_offset = 0
#Window

def initialize():
	window = sg.Window('Broker Viewer', layout, margins=(20, 20))

	while True:
		event, values = window.read()
		if event == 'Adicionar a Lista':
			assets = values['assets'].rstrip()
			command_history.append(assets)
			history_offset = len(command_history)-1
			window.FindElement('tracked_assets').Update(command_history)
		elif event == 'Limpar Lista':
			window.FindElement('tracked_assets').Update([])
		elif event == 'Acompanhar':
			arrAssets = []
			for x in command_history:
				assetsNome = '*.'+x
				arrAssets.append(assetsNome)
			receive_brocker = ReceiveBroker(host='localhost', binding_keys=arrAssets)
			receive_brocker.start()
		if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
			break
	window.close()

initialize()


