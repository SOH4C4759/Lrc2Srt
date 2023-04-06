from swapsub_ import swapsub
import os
path = os.getcwd()
files = os.listdir(path)
lrc_file = ''
for f in files:
    if os.path.splitext(f)[1] == '.lrc':
        lrc_file = path.replace('\\','/')+'/'+f
        data = swapsub.load(lrc_file)
        export_path = lrc_file.replace('lrc','.srt')
        swapsub.convert(data,export_path)

