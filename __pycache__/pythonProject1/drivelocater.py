import win32api
availableDrives = win32api.GetLogicalDriveStrings()
print(availableDrives)

drives=[drivestr for drivestr in availableDrives.split('\000') if drivestr]

#drives = drives.split('\000')[:-1]
print(drives)