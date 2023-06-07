from uiautomator import Device
def sendMsg():
    device = Device('MQS0219610005725')
    device(text="微信").click()

if __name__ == '__main__':
    sendMsg()