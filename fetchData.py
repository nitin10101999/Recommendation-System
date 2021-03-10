import os
import re
import pandas as pd

basepath = 'Texts/'
data_dic = {}

def fetch_file_data(filename):
	hotel = filename.split('_')
	hotel = hotel[1]
	#print(hotel)
	for line in open(basepath+filename, 'r'):
		found = ''
		try:
			found = re.search('<(.+?)>',line).group(1)
		except:
			found = '1'
		if found == 'Author':
			author = line[len(found)+2:len(line)-1]
			data_dic.setdefault('authors', []).append(author)
			data_dic.setdefault('hotels', []).append(hotel)
		elif found == 'Rating':
			ratings = line[len(found)+2:len(line)]
			ratings = ratings.split('\t')
			for i in range(len(ratings)-1):
				rating = int(ratings[i])
				data_dic.setdefault('cr'+ str(i+1), []).append(rating)
	#print(data_dic)

# List all files in a directory using os.listdir
for entry in os.listdir(basepath):
	if os.path.isfile(os.path.join(basepath, entry)):
		fetch_file_data(entry)
columns = []
for key in data_dic:
	columns.append(key)
df = pd.DataFrame(data_dic, columns= columns)
df.to_csv (r'data.csv', index = False, header=True)
print(df)
