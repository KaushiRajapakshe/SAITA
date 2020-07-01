f = open("D:\\testShellScript.ps1", "w+")
c = "\nSet-PSDebug -Trace 1 \nSFC /scannow"
x = "AnyDesk"

a = "Clear-Content d:\ExecutionStatus.txt"
b = "\nSet-PSDebug -Trace 1"

e = "\nRestart-Service -ServiceName variableA"
e = e.replace("variableA", x)
stat = "\nWrite-output" + " $? >> d:\ExecutionStatus.txt"

commands = [a, b, e]

for line in commands:
    f.write(line)
    f.write(stat)
