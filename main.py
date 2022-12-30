import machine
import network
import urequests
from utime import sleep
from machine import Pin, PWM

#sleep(5)

USERNAME = ##[Enter Username]
TOKEN = ##[Enter Token]
GRAPH_ID = ##[Enter Graph ID]
led = machine.Pin("LED", machine.Pin.OUT)


#def rotationStation(boolean):
#     if boolean:
         #sleep(10)
#         print("Spinning")
#         servo = PWM(Pin(0))
#         servo.freq(50)
#         #while True:
#         servo.duty_u16(1500)
#         sleep(1)
#         servo.duty_u16(600)
#         sleep(2)
#         servo.duty_u16(0)
#         sleep(2)
#         ##return Rotating(True)

def led_output_sequence(number):
    for i in range(0,number):
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)
    sleep(0.25)
    
def networkConnect():
        sleep(1)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(##[Enter WIFI Name], ##[Enter Password])
        sleep(0.8)
        print(wlan.isconnected())
        return wlan.isconnected()


def update_feedCount():
    data = []
    sleep(2)
    with open('mem.csv','r') as file:
        for line in file:
            data.append(line.rstrip('\n').rstrip('\r').split(','))
    #file.close()
    
    memory_count = int(data[-1][0])
    
    print(memory_count)
    
    
    
    
    
    def getDate(connection, sleepyTime):
        sleep(sleepyTime)
        if connection:
            c = 1
            led_output_sequence(1)
            try:
                sleep(sleepyTime)
                response = urequests.get(url="http://worldtimeapi.org/api/timezone/America/Vancouver")
                led_output_sequence(2)
                l = response.json()
                return l
                
            except OSError as e:
                c += 1
                if c>1:
                    update_feedCount()
                    c=1
                else:
                    print("Get-Date-Error: "+ str(e))
                    getDate(connection, sleepyTime+0.25)
        
        
            
        
    
    unformattedDate = getDate(networkConnect(),0.7)
    #led_output_sequence(5)
    print("passed date get")
    present = unformattedDate["datetime"].split("-")
    
    dateR = present[-2].split("T")
    
    present.append(dateR[0])
    
    now = str(present[0])+str(present[1])+str(present[4])

    
    
    
    token = ##[Enter token]
    headers = {}
    headers['X-USER-TOKEN'] = token
    pixela_endpoint = "https://pixe.la/v1/users"
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    
    print(str(now))
    
    currDate = str(data[-1][-1]).replace(" ", "")
    
    print(currDate)
    
    newCount = 1
    
    if currDate == str(now):
        newCount = memory_count + 1
        
    pixel_data = {
        "date": str(now),
        "quantity": str(newCount)
    }
    
        
    def setPixel(sleepy):
        d = 1
        led_output_sequence(3)
        try:
            sleep(sleepy)
            response = urequests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
            sleep(sleepy)
            answer = str(response.json())
            sleep(sleepy)
            if answer != "{'isSuccess': False, 'isRejected': True, 'message': 'Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter. If you are interested in being a Pixela supporter, please see: https://github.com/a-know/Pixela/wiki/How-to-support-Pixela-by-Patreon-%EF%BC%8F-Use-Limited-Features'}":
                print(answer)
                #response.close()
            else:
                setPixel(sleepy)
            
        
        except OSError as e:
            d +=1
            if d>1:
                print("Retrying Process...")
                update_feedCount()
                d = 1
            else:
                print("Pixel-set-error: "+ str(e))
                setPixel(sleepy+0.25)
    
    setPixel(0)
    led_output_sequence(4)
    
    logf = open("mem.csv","at")
    
    try:
        logf.write(pixel_data["quantity"]+ ", " +pixel_data["date"] + "\r\n")
        
    except OSError:
        print("Disk full?")
        
    logf.close()
    
    
    #while True:
    led.on()

#while True:
    
try:
    update_feedCount()
except Exception as e:
    import machine
    import network
    import urequests
    from utime import sleep
    from machine import Pin, PWM
    #sleep(5)

    USERNAME = ##[Username]
    TOKEN = ##[Token]
    GRAPH_ID = ##[Graph ID]
    led = machine.Pin("LED", machine.Pin.OUT)
    print("Restarting Process Due To: " + str(e))
    update_feedCount()
    
    
    #machine.reset()
