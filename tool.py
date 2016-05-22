#encoding=utf-8
#by 不灭的小灯灯
#date 2016/5/22
#site www.winterfeel.com
import os
import sys
from PIL import Image

iosSizes = ['27@1x','27@2x','27@3x','40@1x','40@2x','40@3x','60@1x','60@2x','60@3x','76@1x','76@2x','167@1x']
androidSizes = [36,48,72,96,144,192]
androidNames = ['ldpi','mdpi','hdpi','xhdpi','xxhdpi','xxxhdpi']

sizes = [(640,960),(640, 1136),(750, 1334),(1242, 2208),(1536, 2048),(2048, 2732)]
folders = ['iPhone4s','iPhone5','iPhone6','iPhone6plus','iPad','iPadLarge']

def processIcon(filename,platform):
	icon = Image.open(filename).convert("RGBA")
	if icon.size[0] != icon.size[1]:
		print 'Icon file must be a rectangle!'
		return
	if platform == 'android':
		#安卓圆角
		mask = Image.open('mask.png')
		r,g,b,a = mask.split()
		icon.putalpha(a)
		if not os.path.isdir('androidIcon'):
			os.mkdir('androidIcon')
		index = 0
		for size in androidSizes:
			im = icon.resize((size,size),Image.BILINEAR)
			im.save('androidIcon/icon-'+ androidNames[index]+'.png')
			index = index + 1
	else:
		if not os.path.isdir('iosIcon'):
			os.mkdir('iosIcon')
		for size in iosSizes:
			originalSize = int(size.split('@')[0])#原始尺寸
			multiply = int(size.split('@')[1][0:1])#倍数
			im = icon.resize((originalSize*multiply,originalSize*multiply),Image.BILINEAR)
			im.save('iosIcon/icon'+size+'.png')
	print 'Congratulations!It\'s all done!'

def walk_dir(dir):
	files = os.listdir(dir)
	for name in files:
		if name.split('.')[-1] == 'jpg' or name.split('.')[-1] == 'png':#处理jpg和png
			produceImage(name)
	print 'Congratulations!It\'s all done!'

def produceImage(filename):
	print 'Processing:' + filename
	img = Image.open(filename)
	index = 0
	for size in sizes:
		if not os.path.isdir(folders[index]):
			os.mkdir(folders[index])
		if img.size[0] > img.size[1]:#如果是横屏，交换坐标
			im = img.resize((size[1],size[0]),Image.BILINEAR)
			im.save(folders[index]+'/'+filename)
		else:
			im = img.resize(size,Image.BILINEAR)
			im.save(folders[index]+'/'+filename)
		index = index + 1

action = sys.argv[1]#action:icon or screenshot
if action == 'screenshot':	
	walk_dir('./')
elif action == 'icon':
	filename = sys.argv[2]#image filename
	platform = sys.argv[3]#platform
	if not os.path.exists(filename):
		print 'Hey,File Not Found!'
	else:
		if platform == 'ios':
			processIcon(filename,'ios')
		elif platform == 'android':
			processIcon(filename,'android')
		else:
			print 'Hey,Platform can only be "ios" or "android" !'
else:
	print 'Hey,action can only be "icon" or "screenshot" !'
