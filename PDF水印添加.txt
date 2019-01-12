# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:29:47 2018

@author: Administrator
"""
import PyPDF2
import os
import wx
import webbrowser

app=wx.App()    #初始化
win=wx.Frame(None,title='pdf文件自动添加水印软件V1.0',size=(420,350))
bkg = wx.Panel(win)
hbox = wx.BoxSizer()
filename = wx.TextCtrl(bkg,value='运输职院水印软件V1.0')
contents = wx.TextCtrl(bkg,style= wx.TE_MULTILINE)
os.chdir(r'C:\Users\Administrator\Desktop\学院工作11.1\软件著作权\pdf\cqgypdf')
def load(event): 
    #打开pdf文件
    cqgy_file = open('jxjb.pdf','rb') 
    #读取打开的PDF文件
    pdf_reader = PyPDF2.PdfFileReader(cqgy_file)
    #打开水印pdf文件
    water = PyPDF2.PdfFileReader(open('water.pdf','rb'))
    #创建新的pdf，并写入
    pdfwriter = PyPDF2.PdfFileWriter()
    #pdfwriter.addPage(cqgy_file_firstpage)
    #遍历pdf每一页
    #将每一页的pdf与水印合并
    for num in range(pdf_reader.numPages):
        pagerag = pdf_reader.getPage(num)
        pagerag.mergePage(water.getPage(0))
        pdfwriter.addPage(pagerag)
        
    newfile = open('addwater.pdf','wb')
    pdfwriter.write(newfile)
    cqgy_file.close()
    newfile.close()
    contents.Clear()
    contents.AppendText('\n\n\n\n\n                 恭喜！水印添加成功')
loadButton = wx.Button(bkg, label='开始添加水印')
loadButton.Bind(wx.EVT_BUTTON,load)     #开始按键事件设置


def save(event):
    for filenames in os.walk('.'):
        filelist = []
        filelist.append(filenames)
        b = '已经添加水印' #+ str(filelist) + '\n'
    webbrowser.open('addwater'+'.pdf')
    contents.Clear()
    contents.AppendText(b)

saveButton = wx.Button(bkg, label='查看')
saveButton.Bind(wx.EVT_BUTTON,save)     #查看按键事件设置

hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
bkg.SetSizer(vbox)
win.Show()
app.MainLoop()


