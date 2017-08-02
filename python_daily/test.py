import easygui as g  
import sys  
while 1:  
    g.msgbox("这个是MissZhou的第一个界面游戏，还不知道好用不好用")  
    msg="你学什么呢？"  
    title="小游戏互动"  
    choices=["c++","c","c#"]  
    choice=g.choicebox(msg,title,choices)  
    g.msgbox("you choose:"+str(choice),"结果")  
    msg="restart？"  
    title="choose?"  
    if g.ccbox(msg,title):  
        pass  
    else:  
        sys.exit(0)  