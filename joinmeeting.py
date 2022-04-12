from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from time import sleep
from subprocess import Popen

tm_path = r'C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe'

def enter_meeting(mid, pwd, uname):
    Popen(tm_path, shell=True)
    dlg = Desktop(backend="uia").window(title="腾讯会议(LoadingWnd)")
    dlg.wait('visible ready')
    sleep(1)
    # dlg.print_control_identifiers()
    dlg['加入会议'].click_input()
    sleep(1)
    dlg = Desktop(backend="uia").window(title="腾讯会议(JoinWnd)")
    # dlg.print_control_identifiers()
    sleep(1)
    if dlg['入会开启麦克风'].get_toggle_state():
        dlg['入会开启麦克风'].click_input()
    sleep(1)
    if dlg['入会开启摄像头'].get_toggle_state():
        dlg['入会开启摄像头'].click_input()
    sleep(1)
    dlg['您的名称Edit'].click_input()
    sleep(1)
    send_keys("c^a{BACKSPACE}")
    send_keys(uname)
    sleep(1)
    dlg['会议号Edit'].click_input()
    send_keys("c^a{BACKSPACE}")
    sleep(1)
    send_keys(mid.replace('-',''))
    sleep(1)
    # dlg.print_control_identifiers()
    dlg['Join_meeting_Join_meeting'].click_input()
    sleep(1)
    dlg = Desktop(backend="uia").window(title="")
    sleep(1)
    send_keys(pwd+"{ENTER}")
    sleep(1)
    dlg = Desktop(backend="uia").window(title="腾讯会议(InMeetingWnd)")
    # dlg.print_control_identifiers()
    print("[Done] joined meeting {} with name = {} .".format(mid,uname))

