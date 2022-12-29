import win32api

availableDrive=win32api.GetLogicalDriveStrings()
print(availableDrive)

drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr]

#drives=drives.split('\000')[:-1]

print(drives)