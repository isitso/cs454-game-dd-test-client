from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRenderCharacter(ServerResponse):
    def execute(self, data):
        try:
            username = data.getString()
            carType = data.getInt32()
            carPaint = data.getInt32()
            carTires = data.getInt32()

            self.main.emit('ResponseRenderCharacter', {'username': username,
                                                       'carType': carType,
                                                       'carPaint': carPaint,
                                                       'carTires': carTires})

            self.log('Received [' + str(Constants.SMSG_RENDER_CHARACTER) + '] ResponseRenderCharacter')
        except:
            self.log('Bad [' + str(Constants.SMSG_RENDER_CHARACTER) + '] ResponseRenderCharacter')
            print_exc()
