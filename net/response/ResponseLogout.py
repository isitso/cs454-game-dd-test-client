from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogout(ServerResponse):
    def execute(self, data):
        try:
            self.main.emit('ResponseLogout', {})

            self.log('Received [' + str(Constants.SMSG_DISCONNECT) + '] ResponseLogout')
        except:
            self.log('Bad [' + str(Constants.SMSG_DISCONNECT) + '] ResponseLogout')
            print_exc()
