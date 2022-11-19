import time
import sys
import ibmiotf
import ibmiotf.device
import random
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Provide your IBM Watson Device Credentials
organization = "7l1il5" # repalce it with organization ID
deviceType = "Iotsensor" #replace it with device type
deviceId = "12345" #repalce with device id
authMethod = "token"
authToken = "Anandh@1973"#repalce with token
authenticator = IAMAuthenticator('9aUkwzosUqF1y0gJfUA0Vq50z0dLa70tE1Ujbecq0p_L')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/53de65a2-1737-4f34-9a7b-15ca2e0819bc')



def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)        
        if cmd.data['n']!='undefined':
               print(cmd.data['n'])
               x="its time to take "+ cmd.data['n']
               with open('hello_world.wav', 'wb') as audio_file:
                    audio_file.write(text_to_speech.synthesize(x,voice='en-US_AllisonV3Voice',accept='audio/wav').get_result().content)
        else:
           print("LIGHT OFF")
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
      
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
