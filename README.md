#Script to generate icons and splash for iOS/Android
##Introduction
Hey guys! It's a python script to generate icons and screenshots for iOS and Android Apps. 

Check this,you will find out what we do.

![demo](https://github.com/winterfeel/IconSplashMaker/blob/master/demo.png "demo")

Now we support iOS 10!

##Environment
Python 2.7

PIL or Pillow

##How to use
in command line or terminal:
>python tool.py [action] [filename] [platform]

* action：icon or screenshot
* filename：your icon filename(screenshot not needed)
* platform：ios or android

Examples:

>To generate iOS icon：python tool.py icon icon.jpg ios

>To generate Android icon：python tool.py icon icon.jpg android

>To generate iOS screenshots：python tool.py screenshot ios

>To generate Android screenshots：python tool.py screenshot android

##Tips
* You need to prepare a 'mask.png' to crop Android icon. It's size must be (512px,512px) and 70px cornerRadius.

	Dont worry,we've already prepare one for you in GitHub.

* When you generate screenshots,the script will scan all JPG/PNG file in current folder,and you don't need to worry about the orientation.

#About
Hello,I'm Arsene,from China.

I'm a individual full stack developer,I love evey kinds of codes,Ahahahahah...

My Blog:[www.winterfeel.com ](http://www.winterfeel.com )
