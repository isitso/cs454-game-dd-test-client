from common.Constants import Constants

from net.request.RequestLogout import RequestLogout
from net.request.RequestMove import RequestMove
from net.request.RequestPowerUpUse import RequestPowerUpUse
from net.request.RequestPowerUpPickUp import RequestPowerUpPickUp
from net.request.RequestChangeHealth import RequestChangeHealth
from net.request.RequestResults import RequestResults
from net.request.RequestRankings import RequestRankings
from net.request.RequestPrizes import RequestPrizes
from net.request.RequestCollision import RequestCollision
from net.request.RequestDead import RequestDead
from net.request.RequestHeartbeat import RequestHeartbeat

class ServerRequestTable:
    """
    The ServerRequestTable contains a mapping of all requests for use
    with the networking component.
    """
    requestTable = {}

    def __init__(self):
        """Initialize the request table."""
        #self.add(Constants.CMSG_AUTH, 'RequestLogin')
        self.add(Constants.CMSG_DISCONNECT, 'RequestLogout')
        #self.add(Constants.CMSG_REGISTER, 'RequestRegistration')
        #self.add(Constants.CMSG_FORGOT_PASSWORD, 'RequestAccountInformation')
        #self.add(Constants.CMSG_CREATE_CHARACTER, 'RequestCharacterCreation')
        #self.add(Constants.CMSG_CHAT, 'RequestChat')
        self.add(Constants.CMSG_MOVE, 'RequestMove')
        self.add(Constants.CMSG_POWER_UP, 'RequestPowerUpUse')
        self.add(Constants.CMSG_POWER_PICKUP, 'RequestPowerUpPickUp')
        self.add(Constants.CMSG_HEALTH, 'RequestChangeHealth')
        #self.add(Constants.CMSG_ENTER_LOBBY, 'RequestEnterLobby')
        #self.add(Constants.CMSG_ENTER_GAME_LOBBY, 'RequestEnterGameLobby')
        #self.add(Constants.CMSG_ENTER_GAME_NAME, 'RequestEnterGameName')
        #self.add(Constants.CMSG_CREATE_LOBBY, 'RequestCreateLobby')
        #self.add(Constants.CMSG_PRIVATE_CHAT, 'RequestPrivateChat')
        #self.add(Constants.CMSG_INVITE, 'RequestInvite')
        #self.add(Constants.CMSG_CAR_CHOICE, 'RequestCarChoice')
        #self.add(Constants.CMSG_CAR_PAINT, 'RequestCarPaint')
        #self.add(Constants.CMSG_CAR_TIRES, 'RequestCarTires')
        #self.add(Constants.CMSG_GARAGE_PURCHASE, 'RequestGaragePurchase')
        self.add(Constants.CMSG_RESULTS, 'RequestResults')
        self.add(Constants.CMSG_RANKINGS, 'RequestRankings')
        self.add(Constants.CMSG_PRIZES, 'RequestPrizes')
        self.add(Constants.CMSG_COLLISION, 'RequestCollision')
        self.add(Constants.CMSG_DEAD, 'RequestDead')
        #self.add(Constants.CMSG_READY, '')
        self.add(Constants.REQ_HEARTBEAT, 'RequestHeartbeat')

    def add(self, constant, name):
        """Map a numeric request code with the name of an existing request module."""
        if name in globals():
            self.requestTable[constant] = name
        else:
            print 'Add Request Error: No module named ' + str(name)

    def get(self, requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in self.requestTable:
            serverRequest = globals()[self.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest
