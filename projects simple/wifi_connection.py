from subprocess import check_output

scanoutput = check_output(["iwlist", "wlan0", "scan"])
ssid=[]
for line in scanoutput.split():
  if line.startswith("ESSID"):
    ssid = line.split('"')[1]
    
print(ssid[1])