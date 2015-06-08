#coding=utf-8
import SocketServer
import win32pdh,time
import win32api, win32pdhutil, win32con
import string
 
def netstat() :
        object = "Network Interface"
        items, instances = win32pdh.EnumObjectItems( None, None, object, win32pdh.PERF_DETAIL_WIZARD )
        ifs = {}#字典
        for interface in instances:
                hq = win32pdh.OpenQuery()
                hcs = [ ]
                item = "Bytes Total/sec"
                path = win32pdh.MakeCounterPath( ( None, object, interface, None, 0, item ) )
                hcs.append( win32pdh.AddCounter( hq, path ) )
                win32pdh.CollectQueryData( hq )
                time.sleep( 0.01 )
                win32pdh.CollectQueryData( hq )
                for hc in hcs:
                        type, val = win32pdh.GetFormattedCounterValue( hc, win32pdh.PDH_FMT_LONG )
                        win32pdh.RemoveCounter( hc )
                win32pdh.CloseQuery( hq )
                ifs[interface] = val
        return ifs
 
while 1:
        interfaces = netstat()#方法返回值 ifs 
        for interface in interfaces:#每一项 
                print '-----------------'
                print interface
                print '!!!!!!!!!!!!!!!!!'
                print ' Current netload: ' + str(interfaces[interface]) + 'B/s'#返回值 
        time.sleep(1)#每秒刷新 