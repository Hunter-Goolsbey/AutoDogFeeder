import machine
import network
import urequests
from utime import sleep
from machine import Pin, PWM

sleep(8)
def getFeedTime():
    #sleep(0.3)
    c = 1
    # led_output_sequence(1)

    try:
        #sleep(0.1)
        response = urequests.get(url=[API URL])
        # led_output_sequence(2)

        q = response.json()[-1]

        present = q['title']

        return present

    except Exception as e:
        print("get feed time [error]: " + str(e))
        c += 1
        getFeedTime()


USERNAME = [Username]
TOKEN = [Token]
GRAPH_ID = [GraphID]
led = machine.Pin("LED", machine.Pin.OUT)

toNum = [To Number]
fromNum = [Account Number]

has_been_fed = False


def led_output_sequence(number):
    for i in range(0,number):
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)
    sleep(0.25)


def networkConnect():
    try:
        sleep(0.5)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect([WIFI Name], [WIFI Password])
        sleep(2.8)
        ##print(wlan.isconnected())

        if wlan.isconnected() == False:
            networkConnect()
        else:
            return wlan.isconnected()
    except Exception as e:
        print("Network [Error]: " + str(e))
        ##print(e)
        networkConnect()
        
def getDate():
    #sleep(0.3)
    c = 1
    # led_output_sequence(1)

    try:
        sleep(0.1)
        response = urequests.get(url="http://worldtimeapi.org/api/timezone/America/Vancouver")
        # led_output_sequence(2)

        l = response.json()
        present = l["datetime"].split("-")
        dateR = present[-2].split("T")
        present.append(dateR[0])

        #print(present)
        return present

    except Exception as e:
        c += 1
        print("get current date [Error]: " + str(e))
        
        ##print("Get-Date-Error: "+ str(e))
        getDate()


def rotationStation():
    ##print("Spinning")
    
    poisition = {1: 1500,
                 2: 600}
    
    servo = PWM(Pin(0))
    servo.freq(50)
    
    servo.duty_u16(poisition[1])
    sleep(1)
    
    servo.duty_u16(poisition[2])
    sleep(2)
    
    servo.duty_u16(0)
    sleep(2)
    
    return True


def setPixel(now):
    pixel_data = {
            "date": str(now),
            "quantity": str(1)
        }
    
    d = 1
    
    led_output_sequence(3)
    
    token = TOKEN
    headers = {}
    headers['X-USER-TOKEN'] = token
    pixela_endpoint = "https://pixe.la/v1/users"
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    
    try:
        sleep(0.3)
        response = urequests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
        sleep(0.3)
        answer = str(response.json())
        #sleep()

        if answer != "{'isSuccess': False, 'isRejected': True, 'message': 'Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter. If you are interested in being a Pixela supporter, please see: https://github.com/a-know/Pixela/wiki/How-to-support-Pixela-by-Patreon-%EF%BC%8F-Use-Limited-Features'}":
            ##print(answer)
            pass
            # response.close()
        else:
            setPixel(now)
    
    except Exception as e:
#                d += 1
#                 if d > 1:
#                     print("Retrying Process...")
#                     update_feedCount(has_been_fed)
#                     d = 1
#                 else:
        ##print("Pixel-set-error: "+ str(e))
        print("Set Pixel [Error]: " + str(e))
        setPixel(now)
        
    
def send_TwilioSMS():
    url = "https://api.twilio.com/2010-04-01/Accounts/[apiKey]/Messages.json"

    payload = 'Body=The%20dog%20has%20been%20fed%20today!&To=%2B' + str(toNum) + '&From=%2B'+ str(fromNum)
    headers = {
        'Authorization': 'Basic [Auth Key],
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # response = requests.request("POST", url, headers=headers, data=payload)

    response = urequests.post(url, headers=headers, data=payload)

def feederSystem():
    #sleep(5)
    try:
        networkConnect()
        led_output_sequence(3)
        feed_time = getFeedTime()

        while True:
            present = getDate()
            ##print('GetDate: Passed')
            now = str(present[0]) + str(present[1]) + str(present[4])
            
            now_h = getDate()[2][3:8]
            ##print('DateFormatted: Passed')
            ##print('feed time is: ' + str(feed_time))
            while int(now_h.replace(":", "")) != int(feed_time.replace(":", "")):
                led.on()
                sleep(60)
                ##print('in loop')
                ##print(now_h+str(' from the main loop'))
                now_h = getDate()[2][3:8]
                feed_time = getFeedTime()
                ##print(feed_time)
                
                
            
            setPixel(now)
            ##print("Sent to Pixela")
            send_TwilioSMS()
            ##print('SMS Sent')
            sleep(60)
            #led_output_sequence(4)
            led.on()
    except Exception as e:
        ##print(e)
        print("Feeder system [Error]: "+ str(e))
        feederSystem()
        
try:
    feederSystem()
except Exception as e:
    print("Top level [Error]" + str(e))
    feederSystem()


