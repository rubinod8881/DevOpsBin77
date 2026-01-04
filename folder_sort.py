import os, shutil, time
downloads="C:/Users/VINOD/Downloads"
for file in os.listdir(downloads):
    path=os.path.join(downloads,file)
	if os.path.isfile(path):
	    ex=file.split('.')[-1]
		folder=os.path.join(downloads,ext)
		os.makedirs(folder,exist_ok=true)
		shutil.move(path,folder)