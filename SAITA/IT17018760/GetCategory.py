
start=["start","Start","STARTED","Begin","begin"]
stop=["stop","Stop","STOPPED","End","terminate"]
registry=["edit registry","Edit Registry","registry","Registry"]




issueType=input("What do you want to do with SAITA (Start Service/Stop Service/Edit Registry) :")


if any(word in issueType for word in start):
    exec(open("Powershell/StartService.py").read())
elif any(word in issueType for word in stop):
    exec(open("Powershell/StopService.py").read())
elif any(word in issueType for word in registry):
    print("Still Build in process")
else:
    print("Enter the Correct Category")
    exec(open("GetCategory.py").read())
