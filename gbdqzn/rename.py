import os,re
path = './pdf/'
fileList = os.listdir(path)
n = 0
with open('./ids.txt','r',encoding='utf-8') as f:
  s = f.read()
  result = re.split(',',s)
  group_result = [result[i:i+3] for i in range(0, len(result), 3)]
  print(group_result)
for i in group_result:
  oldname = path + i[1] + '.pdf'
  newname = path + i[0] + '.pdf'
  os.rename(oldname,newname)
  print(oldname,'====>',newname)
  n+=1