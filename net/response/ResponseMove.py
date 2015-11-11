from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):
    def execute(self, data):
        try:
            username = data.getString()
            x = data.getFloat64()
            y = data.getFloat64()
            z = data.getFloat64()
            h = data.getFloat64()

            self.main.emit('ResponseMove', {'username': username, 'x': x, 'y': y, 'z': z, 'h': h})

            self.log('Received [' + str(Constants.SMSG_MOVE) + '] ResponseMove')
        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] ResponseMove')
            print_exc()
