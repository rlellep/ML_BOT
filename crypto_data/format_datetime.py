import os
from datetime import datetime

old_folder = 'data'
new_folder = 'data_timeformat'

data_files = os.listdir(old_folder)

for data_file in data_files:
	with open(os.path.join(old_folder, data_file), 'r') as f:
		lines = f.readlines()
	new_lines = [lines[0]]
	for line in lines[1:]:
		features = line.split(', ')
		features[0] = str(datetime.fromtimestamp(int(features[0])/1000))
		new_lines.append(','.join(features))
	with open(os.path.join(new_folder, data_file), 'w') as f:
		f.writelines(new_lines)