#coding:utf-8
'''
import wx  
app = wx.PySimpleApp()  
frame = wx.Frame(None,100,'Title',wx.Point(100,50),wx.Size(100,100))
#上面这一句相当于下面的全部 父类，标识符，title,位置，大小
#其中的还可以写 size=wx.Size(100,100)
frame = wx.Frame( None, -1, '' ) #初始化
frame.SetToolTip( wx.ToolTip( 'This is a frame' ) )  
frame.SetCursor( wx.StockCursor( wx.CURSOR_PENCIL ) )  
frame.SetPosition( wx.Point( 0, 0 ) ) #位置
frame.SetSize( wx.Size( 300, 250 ) )  #大小
frame.SetTitle( 'simple2.py' )  #title
frame.Show()  
app.MainLoop()
'''

#こんなに厚顔無恥なひと見たことない
'''
import wx  
def main():  
    app=wx.PySimpleApp()  
    frame=wx.Frame(None,-1,'I am the title',wx.DefaultPosition,wx.Size(350,300))  
    #Icon构造器
    frame.SetIcon(wx.Icon('D:\My Documents\python\App.ico',wx.BITMAP_TYPE_ICO))  
    #这个icon放在title旁边 就像打开notepad++ 窗口左上方有个写字的小图标一样
    frame.Center()  
    frame.Show()  
    app.MainLoop()  
if __name__ == '__main__':  
    main()  
'''
#下面是菜单的例子
'''
import wx  
class MyMenu( wx.Frame ):  
    def __init__(self,parent,ID,title):  
        wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200, 150)) 
        self.SetIcon(wx.Icon('D:\My Documents\python\App.ico',wx.BITMAP_TYPE_ICO))  #用self
        menubar=wx.MenuBar()  
        file=wx.Menu()  
        edit=wx.Menu()  
        help=wx.Menu()  
        
        file.Append(101,'&Open','Open a new document')  
        file.Append(102,'&Save','Save the document')  
        file.AppendSeparator() 
        #一个名字叫quit的菜单 代码是105 quit菜单的图标是app.ico
        quit=wx.MenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application')  
        quit.SetBitmap(wx.Image('D:\My Documents\python\App.ico', wx.BITMAP_TYPE_ICO).ConvertToBitmap())  
        file.AppendItem(quit)  #最后把这个叫做quit的菜单加到file菜单项里 
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
        edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  #两个复选
        submenu = wx.Menu()
        submenu.Append( 301, 'radio item1', kind= wx.ITEM_RADIO )#三个单选（三选一）
        submenu.Append( 302, 'radio item2', kind=wx.ITEM_RADIO )
        submenu.Append( 303, 'radio item3', kind=wx.ITEM_RADIO )
        submenu.Append( 303, 'radio item3', kind=wx.ITEM_RADIO )
        edit.AppendMenu( 203, 'submenu', submenu )#把submenu加到edit里 submenu号码是203 
        menubar.Append(file,'&File')  
        menubar.Append(edit,'&Edit')  
        menubar.Append(help,'&Help')          
        self.SetMenuBar( menubar )  
        self.Centre()  
        wx.EVT_MENU(self, 105, self.OnQuit) #给105号加了一个事件??????为什么不是OnQuit()
        
    def OnQuit(self,event):  
        self.Close() 
class MyApp(wx.App):  
        def OnInit(self):  
            frame=MyMenu(None,-1,'wxpythontest.py')  
            frame.Show(True)  
            return True  
  
app=MyApp(0)  
app.MainLoop()  
'''

#工具栏
'''
import wx 
class MyToolBar( wx.Frame ):  #继承wx.Frame类的自定义类 MyToolBar
    def __init__( self, parent, ID, title ):  
        wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )  
    
        #vbox = wx.BoxSizer( wx.HORIZONTAL ) #用的是类继承
        vbox = wx.BoxSizer( wx.VERTICAL )
        #toolbar = wx.ToolBar( self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER )  #ToolBar类的初始化 __init__
        toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL | wx.NO_BORDER )  #ToolBar类的初始化 __init__
        #上面两行可以改变toolbar是横着的还是竖着的 
        #下面定义toolbar的按钮
        toolbar.AddSimpleTool( 1, wx.Image( 'D:\My Documents\python\\1.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'New', '' )  
        toolbar.AddSimpleTool( 2, wx.Image( 'D:\My Documents\python\\2.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Open', '' )  
        toolbar.AddSimpleTool( 3, wx.Image( 'D:\My Documents\python\\3.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Save', '' )  
        toolbar.AddSeparator()  
        toolbar.AddSimpleTool( 4, wx.Image( 'D:\My Documents\python\\4.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Exit', '' )  
        
        toolbar.Realize() 
        vbox.Add( toolbar, 0, border=5 )  
        self.SetSizer( vbox )  
        self.statusbar = self.CreateStatusBar()  
        self.Centre()  
        
        #toolbar按钮对应的动作
        wx.EVT_TOOL( self, 1, self.OnNew )  
        wx.EVT_TOOL( self, 2, self.OnOpen )  
        wx.EVT_TOOL( self, 3, self.OnSave )  
        wx.EVT_TOOL( self, 4, self.OnExit )  
        
        #对动作的定义
    def OnNew( self, event ):  
        self.statusbar.SetStatusText( 'New Command' )  
  
    def OnOpen( self, event ):  
        self.statusbar.SetStatusText( 'Open Command' )  
  
    def OnSave( self, event ):  
        self.statusbar.SetStatusText( 'Save Command' )  
  
    def OnExit( self, event ):  
        self.Close()  


class MyApp( wx.App ):  #继承wx.App类的自定义类 MyApp自定义的类还有更多的需求 属性 方法 
    def OnInit( self ):  
        frame = MyToolBar( None, -1, ' wxPythontest.py' )  #__init__的参数用来初始化
        frame.Show( True )  
        return True  
        
app = MyApp( 0 )  
app.MainLoop() #mainloop()就是一直不停地循环，之后的程序只有在关掉弹出窗口之后才运行。

'''
#创建按钮极其格局 
'''
import wx  
class MyFrame(wx.Frame):  
    def __init__(self,parent,ID,title):  
        wx.Frame.__init__(self,parent,ID,title,wx.DefaultPosition,wx.Size(290,250))  #老样子
        panel=wx.Panel(self,-1)  #创建一个panel
        #不会改变的按钮 button 直接加在panel
        
        #wx.Button(panel,-1,'Button1',(0,0))  #panel上加button
        #wx.Button(panel,-1,'Button2',(90,0))  
        #wx.Button(panel,-1,'Button3',(180,0))  
        
        
        #会改变的按钮 button在box上 box在panel上 中间多了一个box
        box=wx.BoxSizer(wx.VERTICAL) 
        #Add(wx.Window window,integer proportion=0,integer flag=0,integer border=0)flag 和border的可选值很多 
        box.Add( wx.Button( panel, -1, 'Button1' ), 0, wx.LEFT, 9 )  #注意0,1,2的不同表现
        box.Add( wx.Button( panel, -1, 'Button2' ), 1, wx.EXPAND)  
        box.Add( wx.Button( panel, -1, 'Button3' ), 2, wx.ALIGN_CENTER)  
  
        panel.SetSizer(box)  
        self.Centre()  
  
class MyApp(wx.App):  
    def OnInit(self):  
        frame=MyFrame(None,-1,'wxPythontest.py')  
        frame.Show(True)  
        frame.Centre()  
        return True
app = MyApp(0)  
app.MainLoop()  


'''

#创建表格
'''
import wx  
class MyFrame( wx.Frame ):  
    def __init__( self, parent, id, title ):  
        wx.Frame.__init__( self, parent, id, title )  
  
        vbox = wx.BoxSizer( wx.VERTICAL )  
        hbox1 = wx.BoxSizer( wx.HORIZONTAL )  #第一行的box
        hbox2 = wx.BoxSizer( wx.HORIZONTAL )  #第二行
        #每个panel的不同样式 就是最后一个参数 border参数 边框有细微的差别
        pnl1 = wx.Panel( self, -1, style=wx.SIMPLE_BORDER )  
        pnl2 = wx.Panel( self, -1, style=wx.RAISED_BORDER )  
        pnl3 = wx.Panel( self, -1, style=wx.SUNKEN_BORDER )  
        pnl4 = wx.Panel( self, -1, style=wx.DOUBLE_BORDER )  
        pnl5 = wx.Panel( self, -1, style=wx.STATIC_BORDER )  
        pnl6 = wx.Panel( self, -1, style=wx.NO_BORDER )  
        #第一行box有三个panel 其中样式（wx.EXPAND和上一个例子一样）
        hbox1.Add( pnl1, 1, wx.EXPAND | wx.ALL, 9 )  
        hbox1.Add( pnl2, 1, wx.EXPAND | wx.ALL, 3 )  
        hbox1.Add( pnl3, 1, wx.EXPAND | wx.ALL, 3 )  
        #第二行也有三个
        hbox2.Add( pnl4, 1, wx.EXPAND | wx.ALL, 3 )  
        hbox2.Add( pnl5, 1, wx.EXPAND | wx.ALL, 3 )  
        hbox2.Add( pnl6, 1, wx.EXPAND | wx.ALL, 3 )  
  
        vbox.Add( hbox1, 1, wx.EXPAND )  
        vbox.Add( hbox2, 1, wx.EXPAND )  
  
        self.SetSizer( vbox )  
        self.Centre()  
  
class MyApp( wx.App ):  
    def OnInit( self ):  
        frame = MyFrame( None, -1, 'aaaaaaaaaa.py' )  #XXXXX.py 只是窗口显示的字 叫什么都行 不用和这个文件名一样
        frame.Show( True )  
        return True  
  
app = MyApp( 0 )  
app.MainLoop()  
'''
#一个计算器--------------------------------------------------------------------------
#!/usr/bin/env python  
# FileName: calculator.py  
import wx  
class MyFrame( wx.Frame ):  
    def __init__( self, parent, id, title ):  
        wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(300, 250))  
  
        self.results = False #结果值   
        self.formula = False #屏幕值   
        self.sign = False #(+ - * /) 运算符 False 可使用 True 不可使用  
        self.dot = False #点运算符 False 可使用 True 不可使用  
  
        menubar = wx.MenuBar()   
        file = wx.Menu()  
        file.Append( 22, '&Close', 'Exit Calculator' )  #给file添加一个叫做close的菜单
        menubar.Append( file, '&File' )  
        self.SetMenuBar( menubar )  
        wx.EVT_MENU( self, 22, self.OnClose )  #菜单关闭按钮  点击22号菜单就会执行close类/函数？
  
        sizer = wx.BoxSizer( wx.VERTICAL )  
        self.display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT) #创建文本控件  
        sizer.Add(self.display, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 4)   #展示文本控件     
  
  
  
        gs = wx.GridSizer(5, 4, 3, 3) #创建5行4列间隔3的布局 行列数不对会报错  
        gs.AddMany([(wx.Button(self, 20, 'Close'), 0, wx.EXPAND),  
        (wx.Button(self, 21, 'Bck'), 0, wx.EXPAND),  
        (wx.StaticText(self, -1, ''), 0, wx.EXPAND),  
        (wx.Button(self, 22, 'Cls'), 0, wx.EXPAND),  
        (wx.Button(self, 1, '7'), 0, wx.EXPAND),  
        (wx.Button(self, 2, '8'), 0, wx.EXPAND),  
        (wx.Button(self, 3, '9'), 0, wx.EXPAND),  
        (wx.Button(self, 4, '/'), 0, wx.EXPAND),  
        (wx.Button(self, 5, '4'), 0, wx.EXPAND),  
        (wx.Button(self, 6, '5'), 0, wx.EXPAND),  
        (wx.Button(self, 7, '6'), 0, wx.EXPAND),  
        (wx.Button(self, 8, '*'), 0, wx.EXPAND),  
        (wx.Button(self, 9, '1'), 0, wx.EXPAND),  
        (wx.Button(self, 10, '2'), 0, wx.EXPAND),  
        (wx.Button(self, 11, '3'), 0, wx.EXPAND),  
        (wx.Button(self, 12, '-'), 0, wx.EXPAND),  
        (wx.Button(self, 13, '0'), 0, wx.EXPAND),  
        (wx.Button(self, 14, '.'), 0, wx.EXPAND),  
        (wx.Button(self, 15, '='), 0, wx.EXPAND),  
        (wx.Button(self, 16, '+'), 0, wx.EXPAND)])  
           
        sizer.Add(gs, 1, wx.EXPAND)  
        self.SetSizer(sizer)  
        self.Centre()  
  
        wx.EVT_BUTTON(self, 20, self.OnClose)  
        wx.EVT_BUTTON(self, 21, self.OnBackspace)  
        wx.EVT_BUTTON(self, 22, self.OnClear)  
        wx.EVT_BUTTON(self, 1, self.OnSeven)  
        wx.EVT_BUTTON(self, 2, self.OnEight)  
        wx.EVT_BUTTON(self, 3, self.OnNine)  
        wx.EVT_BUTTON(self, 4, self.OnDivide)  
        wx.EVT_BUTTON(self, 5, self.OnFour)  
        wx.EVT_BUTTON(self, 6, self.OnFive)  
        wx.EVT_BUTTON(self, 7, self.OnSix)  
        wx.EVT_BUTTON(self, 8, self.OnMultiply)  
        wx.EVT_BUTTON(self, 9, self.OnOne)  
        wx.EVT_BUTTON(self, 10, self.OnTwo)  
        wx.EVT_BUTTON(self, 11, self.OnThree)  
        wx.EVT_BUTTON(self, 12, self.OnMinus)  
        wx.EVT_BUTTON(self, 13, self.OnZero)  
        wx.EVT_BUTTON(self, 14, self.OnDot)  
        wx.EVT_BUTTON(self, 15, self.OnEqual)  
        wx.EVT_BUTTON(self, 16, self.OnPlus)  
  
    def OnClear(self, event):  
        self.display.Clear()  
          
    def OnBackspace(self, event):  
        formula = self.display.GetValue()  
        self.display.Clear()  
        self.display.SetValue(formula[:-1])  
          
    def OnClose(self, event):  
        self.Close()  
          
    def OnDivide(self, event):  
        if self.sign  :  
            return  
        self.display.AppendText('/')  
        self.results = False  
        self.sign = True  
        self.dot = False          
          
    def OnMultiply(self, event):  
        if self.sign  :  
            return  
        self.display.AppendText('*')  
        self.results = False  
        self.sign = True  
        self.dot = False          
          
    def OnMinus(self, event):  
        if self.sign  :  
            return  
        self.display.AppendText('-')  
        self.results = False  
        self.sign = True  
        self.dot = False          
          
    def OnPlus(self, event):  
        if self.sign  :  
            return  
        self.display.AppendText('+')  
        self.results = False  
        self.sign = True  
        self.dot = False  
          
    def OnDot(self, event):  
        if self.dot:  
            return   
        self.display.AppendText('.')  
        self.dot = True  
          
    def OnEqual(self, event):  
        if self.formula:  
            return    
        formula = self.display.GetValue()  
        self.formula = True;  
          
          
        try:  
            self.display.Clear()  
  
            output = eval(formula)  
            self.display.AppendText(str(output))  
            self.results = True;  
            self.sign = False  
            self.dot = True  
  
        except :  
            self.display.AppendText("Error")  
              
    def OnZero(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('0')  
              
              
    def OnOne(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('1')  
              
    def OnTwo(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('2')  
              
    def OnThree(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('3')  
          
    def OnFour(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('4')  
              
    def OnFive(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('5')  
              
    def OnSix(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('6')  
              
    def OnSeven(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('7')  
              
    def OnEight(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('8')  
              
    def OnNine(self, event):  
        if  self.results == False:  
             self.formula = False  
             self.sign = False  
             self.display.AppendText('9')  
  
class MyApp(wx.App):  
    def OnInit(self):  
        frame = MyFrame(None, -1, "calculator")  
        frame.Show(True)  
        self.SetTopWindow(frame)  
        return True  
      
app = MyApp(0)  
app.MainLoop()  