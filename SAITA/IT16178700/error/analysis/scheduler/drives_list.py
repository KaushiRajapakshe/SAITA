import win32api


# GET Windows Drive list for prevention error scanner
def get_os_drives_list():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives
