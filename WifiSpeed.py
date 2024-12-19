import speedtest

wifi = speedtest.Speedtest()
download = wifi.download()
upload = wifi.upload()
print("download speed is :",download /1024/1024)
print("upload speed is :",upload)