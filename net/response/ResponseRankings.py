from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRankings(ServerResponse):
    def execute(self, data):
        try:
            type = data.getInt16()
            numberOfPlayers = data.getInt32()
            players = []
            for i in range(numberOfPlayers):
                username = data.getString()
                score = data.getInt32()
                players.append({'username': username, 'score': score})

            self.main.emit('ResponseRankings', {'type': type, 'players': players})

            self.log('Received [' + str(Constants.SMSG_RANKINGS) + '] ResponseRankings')
        except:
            self.log('Bad [' + str(Constants.SMSG_RANKINGS) + '] ResponseRankings')
            print_exc()
