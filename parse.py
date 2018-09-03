def gamesSuffix(g):
	if g == "Victor":
		return "Victor"


	if int(g) == 11 or int(g) == 12 or int(g) == 13:
		h = str(g) + 'th'
	elif int(g)%10 == 1:
		h = str(g) + 'st'
	elif int(g)%10 == 2:
		h = str(g) + 'nd'
	elif int(g)%10 ==3:
		h = str(g) + 'rd'
	else:
		h = str(g) + 'th'
	return h

if __name__ == "__main__":
	fopen = open('zscore.csv','r')
	wopen = open('js/controllers/fullScoreController.js','w')
	
	wopen.write("app.controller('fullScoreController',\n\t['$scope', function($scope){\n")
	wopen.write('\t$scope.list = [\n')

	start = True
	for i in fopen:
		i = i.strip().split(',')
		wopen.write('\t\t{\n')

		rank = i[0]
		percentile = i[1]
		name = i[2]
		gameNum = i[3]
		gameDays = i[4]
		district = i[5]
		member = i[6]
		deathDay = i[7]
		placement = i[8]
		tScore = i[9]
		kills = i[10]
		zscore = i[11]

		wopen.write('\t\t\trank: ' + rank + ',\n')
		wopen.write('\t\t\tpercentile: ' + percentile + ',\n') 
		wopen.write('\t\t\tname: "' + name + '",\n') 
		wopen.write('\t\t\tgameNum: ' + gameNum + ',\n') 
		wopen.write('\t\t\tgameDays: "' + gameDays + '",\n')
		wopen.write('\t\t\tdistrict: "' + district + '",\n')
		wopen.write('\t\t\tmember: "' +  member + '",\n') 
		wopen.write('\t\t\tdeathDay: "' + deathDay + '",\n')
		wopen.write('\t\t\tplacement: "' + placement + '",\n')
		wopen.write('\t\t\ttScore: ' + tScore + ',\n') 
		wopen.write('\t\t\tkills: ' + kills + ',\n') 
		wopen.write('\t\t\tzscore: ' + zscore + '\n')

		if rank == str(628):
			wopen.write('\t\t}\n')
		else:
			wopen.write('\t\t},\n')

	wopen.write('\t\t];')
	wopen.write('}]);')





