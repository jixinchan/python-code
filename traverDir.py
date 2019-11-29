"""
#对path目录及其子目录下的所有‘某类型(type)’文件进行func操作
"""
def func():
	pass

def getFile(path,type):
	import zipfile
	from pathlib import Path 
	path = Path(path)
	name=path.name
	if path.is_dir():
		for i in path.iterdir():
			# print(i)
			getFile(i)
	elif zipfile.is_zipfile(path):
		pass
	else:
		if name.endswith(type):
			func()
		