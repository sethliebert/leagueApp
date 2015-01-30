import champion
import user

def main():

	user.userName = "TrulyInspired"
	user.championPlayed = "Ziggs"
	user.rolePlayed = "Mage"
	user.lanePlayed = "Mid"
	user.kills = 1
	user.deaths = 1
	user.assists = 1

	#print user.userName
	#print user.championPlayed
	#print user.rolePlayed
	#print user.lanePlayed
	#print user.kills
	#print user.deaths
	#print user.assists

	file = open("championList.txt",'r')
	row = file.readlines()

	for char in row:
		print char
	#s = row.split()


	#for line in row:
		

	#file = open('newfile.txt','w')
	#file.close


main()