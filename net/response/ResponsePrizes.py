from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePrizes(ServerResponse):
    def execute(self, data):
        try:
            itemId = data.getInt32()

            self.main.emit('ResponsePrizes', {'itemId': itemId})

            self.log('Received [' + str(Constants.SMSG_PRIZES) + '] ResponsePrizes')
        except:
            self.log('Bad [' + str(Constants.SMSG_PRIZES) + '] ResponsePrizes')
            print_exc()
