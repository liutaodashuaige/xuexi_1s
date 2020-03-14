import win32gui
import win32process
import win32api

# 获取窗口句柄
window_name = input('输入窗口名称：')
window_handle = win32gui.FindWindow(None,window_name)
# 获取线程与进程ID
process_id = win32process.GetWindowThreadProcessId(window_handle)[1]
print('当前窗口句柄：',end='')
print(window_handle)
print('进程ID：',end='')
print(process_id)
# 获取进程句柄，循环遍历进程列表，0x1F0FFF是所有进程地址常量
process_handle = win32api.OpenProcess(0x1F0FFF,False,process_id)
print('当前进程句柄：',end='')
print(process_handle,end='')