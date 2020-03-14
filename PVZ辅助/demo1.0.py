import win32gui
import win32process
import win32api
# 调用系统内核模块，动态链接库
import ctypes

# 获取窗口句柄
window_handle = win32gui.FindWindow(None,'植物大战僵尸中文版')
# 获取线程与进程ID
process_id = win32process.GetWindowThreadProcessId(window_handle)[1]
print('当前窗口句柄：',end='')
print(window_handle)
print('进程ID：',end='')
print(process_id)
# 获取进程句柄，循环遍历进程列表，0x1F0FFF是所有进程地址常量
process_handle = win32api.OpenProcess(0x1F0FFF,False,process_id)
# 读写内存
kernel32 = ctypes.windll.LoadLibrary(r"C:\Windows\System32\kernel32.dll")
# 缓冲区用来保存数据  4字节  尺寸 返回数据可能不兼容因此使用缓冲区保存
while(1):
    yg1 = ctypes.c_long()
    kernel32.ReadProcessMemory(int(process_handle),0x006A9EC0,ctypes.byref(yg1),4,None)
    yg2 = ctypes.c_long()
    kernel32.ReadProcessMemory(int(process_handle),yg1.value+0x768,ctypes.byref(yg2),4,None)
    yg3 = ctypes.c_long()
    kernel32.ReadProcessMemory(int(process_handle),yg2.value+0x5560,ctypes.byref(yg3),4,None)
    print('当前阳光数量：',end='')
    print(yg3.value)
    sun=input('输入要增加的阳光值：')
    kernel32.WriteProcessMemory(int(process_handle),yg2.value+0x5560,ctypes.byref(ctypes.c_long(int(sun)+int(yg3.value))),4,None)