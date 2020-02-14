from tkinter import *

def interface():
	global board

	if type(board) == Canvas:
		board.destroy()
	board = Canvas(window,width=610,height=610,bg="white",bd=5, relief = "solid")
	board.pack()
	board.create_line(207.5,0,207.5,620,fill="black",width=5)
	board.create_line(412.5,0,412.5,620,fill="black",width=5)
	board.create_line(0,207.5,620,207.5,fill="black",width=5)
	board.create_line(0,412.5,620,412.5,fill="black",width=5)
	
	for i in range(3):
		for j in range(3):
			board.create_line(i*205+6,j*205+72.6,i*205+206,j*205+72.6,fill="black",width=1)
			board.create_line(i*205+6,j*205+139.3,i*205+206,j*205+139.3,fill="black",width=1)

			board.create_line(j*205+72.6,i*205+6,j*205+72.6,i*205+206,fill="black",width=1)
			board.create_line(j*205+139.3,i*205+6,j*205+139.3,i*205+206,fill="black",width=1)


def end_game(winner):
	global board
	global end

	if winner == '1':
		board.create_line(20,20,600,600,fill="red",width=20,cap="round")
		board.create_line(20,600,600,20,fill="red",width=20,cap="round")
	if winner == '2':
		board.create_oval(20,20,600,600,outline="blue",width=20)
	if winner == '0':
		board.create_line(20,310,600,310,fill="grey",width=20,cap="round")
	end = True


def test_end_game(c):
	global list_morpion
	global end

	winner = '0'
	for i in range(9):
		if type(list_morpion[i]) != str:
			winner = ''

	if list_morpion[c] == '1' or list_morpion[c] == '2':
		if list_morpion[3*(c//3)] == list_morpion[3*(c//3)+1] == list_morpion[3*(c//3)+2] or list_morpion[c] == list_morpion[(c+3)%9] == list_morpion[(c+6)%9]:
			winner = list_morpion[c]

	if list_morpion[4] == '1' or list_morpion[4] == '2':
		if list_morpion[0] == list_morpion[4] == list_morpion[8] or list_morpion[2] == list_morpion[4] == list_morpion[6]:
			winner = list_morpion[c]

	if winner != '':
		end_game(winner)
		


def test_end_morpion(c):
	global list_morpion
	global board

	coormorpionX = (c[0]%3)*205+6
	coormorpionY = (c[0]//3)*205+6
	end_morpion = None

	if place_available(c[0]) == []:
		end_morpion = '0'
	if list_morpion[c[0]][3*(c[1]//3)] == list_morpion[c[0]][3*(c[1]//3)+1] == list_morpion[c[0]][3*(c[1]//3)+2] or list_morpion[c[0]][c[1]] == list_morpion[c[0]][(c[1]+3)%9] == list_morpion[c[0]][(c[1]+6)%9]:
		end_morpion = '1' if player else '2'
	if list_morpion[c[0]][4] != None and (list_morpion[c[0]][0] == list_morpion[c[0]][4] == list_morpion[c[0]][8] or list_morpion[c[0]][2] == list_morpion[c[0]][4] == list_morpion[c[0]][6]) :
		end_morpion = '1' if player else '2'

	if end_morpion != None:
		list_morpion[c[0]] = end_morpion
		if end_morpion == '1':
			board.create_line(coormorpionX+5,coormorpionY+5,coormorpionX+190,coormorpionY+190,fill="red",width=10,cap="round")
			board.create_line(coormorpionX+5,coormorpionY+190,coormorpionX+190,coormorpionY+5,fill="red",width=10,cap="round")
		if end_morpion == '2':
			board.create_oval(coormorpionX+5,coormorpionY+5,coormorpionX+190,coormorpionY+190,outline="blue",width=10)
		if end_morpion == '0':
			board.create_line(coormorpionX+10,coormorpionY+95,coormorpionX+180,coormorpionY+95,fill="grey",width=15,cap="round")
		test_end_game(c[0])


def clicButton(c):
	global player
	global morpion
	global list_buttons

	coormorpionX = ((c[0]%3)*205+6) + ((c[1]%3)*66.6)
	coormorpionY = ((c[0]//3)*205+6) + ((c[1]//3)*66.6)
	list_morpion[c[0]][c[1]] = player
	if player :
		board.create_line(coormorpionX+3,coormorpionY+3,coormorpionX+62,coormorpionY+62,fill="red",width=2,cap="round")
		board.create_line(coormorpionX+3,coormorpionY+62,coormorpionX+62,coormorpionY+3,fill="red",width=2,cap="round")
	else :
		board.create_oval(coormorpionX+3,coormorpionY+3,coormorpionX+62,coormorpionY+62,outline="blue",width=2)

	for button in list_buttons:
		button.destroy()
	list_buttons.clear()

	test_end_morpion(c)

	player = not player
	morpion = 9 if type(list_morpion[c[1]]) == str else c[1]
	prepare_turn()


def createButton(c):
	global board

	b = Button (board, activebackground = "gray",bd=2 ,bg = "white", relief="raised", command=lambda :clicButton(c))
	return b
	

def place_available (morpion):
	global list_morpion

	available = []
	for i in range(9):
		if list_morpion[morpion][i] == None:
			available.append((morpion,i))
	return available


def prepare_turn():
	global list_buttons
	global morpion
	global end

	if not end:
		if morpion == 9:
			available = []
			for i in range(9):
				if type(list_morpion[i]) == list:
					available+=place_available(i)
		else:
			available = place_available(morpion)

		for c in available:
			list_buttons.append(createButton(c))
			list_buttons[-1].place(x=((c[0]%3)*205+8) + ((c[1]%3)*66.6),y=((c[0]//3)*205+8) + ((c[1]//3)*66.6), height = 62, width = 62)
	else:
		retry = Button(window, activebackground = "gray", bd=5, bg = "white", relief="raised", command=lambda: play(), text="RETRY", anchor=CENTER)
		retry.place(relx=0.5, rely=0.5, anchor=CENTER)


def play():
	global list_morpion
	global player
	global morpion
	global end
	global list_buttons

	list_morpion = []
	for i in range(9):
		list_morpion.append([None]*9)
	player = True
	morpion = 9
	end = False
	list_buttons = []
	interface()
	prepare_turn()


list_morpion = None
player = None
morpion = None
end = None
list_buttons = None
window = Tk()
window.title("Meta Morpion V1")
board = None
play()

window.mainloop()