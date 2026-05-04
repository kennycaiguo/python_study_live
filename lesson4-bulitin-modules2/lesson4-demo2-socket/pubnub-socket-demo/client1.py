# pip3 install 'pubnub>=7.1.0' to install pubnub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os

pnconf = PNConfiguration()
userId = os.path.basename(__file__)
pnconf.publish_key = 'demo'
pnconf.subscribe_key = 'demo'
pnconf.user_id = userId
pnconf.ssl = True

pubnub = PubNub(pnconf)

def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    pass

class MySubscribCallBack(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass 
    def message(self, pubnub, message):
       if message.publisher == userId: return
       print("from device " + message.publisher + ": " + message.message)

pubnub.add_listener(MySubscribCallBack())
pubnub.subscribe().channels('chan-1').execute()


while True:
   msg = input(">>>")
   if msg == 'exit': os.exit(1)
   pubnub.publish().channel('chan-1').message(str(msg)).pn_async(my_publish_callback)