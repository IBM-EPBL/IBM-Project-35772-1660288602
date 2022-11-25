from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('63s6J5crAYXonyQBql09wrk3J-kkSONLepEibsit4UKW')
                                                     
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/6e24c0dd-412e-45de-9165-d02d2963be23')

with open('Medicine.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Its time for your medicine',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)

