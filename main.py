import champion
import user
import Tkinter 
from Tkinter import Tk, Canvas, Frame, Button
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT

def lanePlayed():
	print "lanePlayed"
	user.lanePlayed = lanePlayed

def championPlayed():
	print "championPlayed"



def main():
	"""
	user.userName = "TrulyInspired"
	user.championPlayed = "Ziggs"
	user.rolePlayed = "Mage"
	user.lanePlayed = "Mid"
	user.kills = 1
	user.deaths = 1
	user.assists = 1
	print user.userName
	print user.championPlayed
	print user.rolePlayed
	print user.lanePlayed
	print user.kills
	print user.deaths
	print user.assists
	"""
	
	file = open("championList.txt",'r')
	contents = file.readlines()

	aList = []

	for i in contents:
		aList.append(i.strip())




	#file = open('newfile.txt','w')
	#file.close
	
	root = Tkinter.Tk()

	# create and pack containers
	top = Tkinter.Frame(root, background="purple")
	bottom = Tkinter.Frame(root, background="blue")
	top.pack(fill="x")
	bottom.pack(expand="yes", fill="both")

	# just use pack on buttons on top
	b1 = Tkinter.Button(top, text="Top Lane", command = lanePlayed)
	b2 = Tkinter.Button(top, text="Mid Lane", command = lanePlayed)
	b3 = Tkinter.Button(top, text="Jungle", command = lanePlayed)
	b4 = Tkinter.Button(top, text="Bottom Lane", command = lanePlayed)
	b1.pack(side="left", expand="yes", fill="x", padx=5, pady=5)
	b2.pack(side="left", expand="yes", fill="x", padx=5, pady=5)
	b3.pack(side="left", expand="yes", fill="x", padx=5, pady=5)
	b4.pack(side="left", expand="yes", fill="x", padx=5, pady=5)

	# use grid on the bottom
	for x in range(1):
	    for y in range(4):
	        b = Tkinter.Button(bottom, text= aList[y], command = championPlayed)
	        b.grid(row=x, column=y, sticky="news", padx=5, pady=5)

	for i in range(4):
	    bottom.columnconfigure(i, weight=1)
	    bottom.rowconfigure(i, weight=1)
	    
	root.mainloop()




main()