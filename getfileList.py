"""# getfileList

あるフォルダ以下にあるファイル一覧を表示

名前、拡張子、フォルダの位置で指定可能

名前、拡張子には正規表現を使うことができる

```python
from getfileList import getFileList

filelist = getFileList(fileName="filename",fileExtension="txt",start=".",exclude="exclude",showFile=False)

```
## 引数

### 文字列

* fileName 検索したいファイル名に含まれる文字列　正規表現使用可能
* fileExtension 検索したいファイルの拡張子　正規表現使用可能
* start このディレクトリ以下の階層を検索する　デフォルトではルートディレクトリ（~）
* exclude この文字列を含むパスを除外する

### 真偽値

* showFile ファイルのリストを一覧で表示する・しない

"""


import os
import re

def getfileList(fileName,fileExtension,start = os.path.expanduser("~"),exclude:str = "まあこんな文字列を含むファイル名やパスがあるはずなかろう",showFile = True):
    pthList = []
    #n = 0
    for curDir, dirs,files in os.walk(start):
        for f in files:
            if  re.search(fileName,f) and re.search("\."+fileExtension+"$",f):
                pth = os.path.join(curDir,f)
                pthL = pth.split(".")
                xtn = pthL[len(pthL)-1]
                #print(str(n),":",pth)
                if not re.search(exclude,pth):
                    pthList.append(pth)
                #n+=1
    pthList.sort()
    if showFile:
        for i in range(0,len(pthList)):
            print(str(i).rjust(3,'-'),":"+pthList[i])
    return pthList
