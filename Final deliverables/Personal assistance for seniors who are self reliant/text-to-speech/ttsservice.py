from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('7NcRcpMT221nhk1kB5DTsWpKGQgjKFaWKa7Ao1BU7zQ')
text_to_speech = TextToSpeechV1(
authenticator=authenticator
)
text_to_speech.set_service_url('https://api.eu-gb.text-tospeech.watson.cloud.ibm.com/instances/e7133289-0146-4193-a7d5-
b354d6831556')
with open('para.wav', 'wb') as audio_file:
audio_file.write(
text_to_speech.synthesize(
'its the time to take paracetomal',
voice='en-US_AllisonV3Voice',
accept='audio/wav'
).get_result().content)
