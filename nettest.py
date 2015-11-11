import math, sys

""" Panda3D imports """
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData

""" Custom imports"""
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager



class Tester(object):
    def __init__(self, main):
        self.main = main

        self.phase = 0
        self.t = 0

        self.characters = []

        emitter = main.emitter
        emitter.on('connection', self.onConnection)
        emitter.on('ResponseRenderCharacter', self.onRenderCharacter)
        emitter.on('ResponseRemoveUser', self.onRemoveUser)
        # phase 1
        emitter.on('ResponseMove', self.onMove)
        # phase 2
        emitter.on('ResponsePowerUpPickUp', self.onPowerUpPickUp)
        emitter.on('ResponsePowerUpUse', self.onPowerUpUse)
        # phase 3
        emitter.on('ResponseChangeHealth', self.onChangeHealth)
        emitter.on('ResponseCollision', self.onCollision)
        # phase 4
        emitter.on('ResponseDead', self.onDead)
        emitter.on('ResponseResults', self.onResults)
        emitter.on('ResponsePrizes', self.onPrizes)
        emitter.on('ResponseLogout', self.onLogout)

        print '----------------------------------------------------------------------'
        print '----------------------------------------------------------------------'
        print '--              _____ _____ _____ _____ _____    _____              --'
        print '--             |  _  |  |  |  _  |   __|   __|  |  _  |             --'
        print '--             |   __|     |     |__   |   __|  | |_| |             --'
        print '--             |__|  |__|__|__|__|_____|_____|  |_____|             --'
        print '--                                                                  --'
        print '--           Goals: * Initiate a connection to the server           --'
        print '--                  * Retrieve list of connected players            --'
        print '--                                                                  --'
        print '----------------------------------------------------------------------'
        print '----------------------------------------------------------------------'

    def onConnection(self, data):
        self.phase = 1
        taskMgr.doMethodLater(0.1, self.tick, 'Tester.tick')

        print '----------------------------------------------------------------------'
        print '----------------------------------------------------------------------'
        print '--              _____ _____ _____ _____ _____    ___                --'
        print '--             |  _  |  |  |  _  |   __|   __|  |_  |               --'
        print '--             |   __|     |     |__   |   __|   _| |_              --'
        print '--             |__|  |__|__|__|__|_____|_____|  |_____|             --'
        print '--                                                                  --'
        print '--            Goals: * Handle movement in a small circle            --'
        print '--                   * Use heading outside of [-360, 360]           --'
        print '--                   * Stay connected for 15 seconds                --'
        print '--                                                                  --'
        print '----------------------------------------------------------------------'
        print '----------------------------------------------------------------------'

    def tick(self, task):
        if self.phase == 1:
            x = math.cos(self.t)
            z = math.sin(self.t)
            h = self.t * 180 / math.pi - 450
            self.main.cManager.sendRequest(Constants.CMSG_MOVE, {'x': 0, 'y': 0, 'z': 0, 'h': 0, 'keys': ''})
            self.t += task.getDelay()

            if self.t > 15:
                self.phase = 2
                self.t = 0
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'
                print '--              _____ _____ _____ _____ _____    ____               --'
                print '--             |  _  |  |  |  _  |   __|   __|  |__  |              --'
                print '--             |   __|     |     |__   |   __|  |  __|              --'
                print '--             |__|  |__|__|__|__|_____|_____|  |____|              --'
                print '--                                                                  --'
                print '--            Goals: * Obtain and use 3 powerups                    --'
                print '--                   * Try obtaining and using 6 powerups           --'
                print '--                                                                  --'
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'

        if self.phase == 2:
            if self.t < 3: # obtain 3 powerups
                self.main.cManager.sendRequest(Constants.CMSG_POWER_PICKUP, {'powerId': self.t})
            elif self.t < 6: # use 3 powerups
                self.main.cManager.sendRequest(Constants.CMSG_POWER_UP, {'powerId': self.t - 3})
            elif self.t < 12: # obtain 6 powerups
                self.main.cManager.sendRequest(Constants.CMSG_POWER_PICKUP, {'powerId': self.t - 6})
            elif self.t < 18: # use 6 powerups
                self.main.cManager.sendRequest(Constants.CMSG_POWER_UP, {'powerId': self.t - 12})
            else:
                self.phase = 3
                self.t = 0
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'
                print '--              _____ _____ _____ _____ _____    ____               --'
                print '--             |  _  |  |  |  _  |   __|   __|  |__  |              --'
                print '--             |   __|     |     |__   |   __|  |__  |              --'
                print '--             |__|  |__|__|__|__|_____|_____|  |____|              --'
                print '--                                                                  --'
                print '--            Goals: * Change health                                --'
                print '--                   * Collide (optional; requires other players)   --'
                print '--                                                                  --'
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'

            self.t += 1

        if self.phase == 3:
            if len(self.characters) < 1:
                print ''
                print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                print '!!                                                                  !!'
                print '!!    SUPPORT FOR OTHER PLAYERS MUST BE IMPLEMENTED FOR PHASE 3!    !!'
                print '!!                                                                  !!'
                print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                print ''
                self.t = 999

            if self.t < 10: # change health
                self.main.cManager.sendRequest(Constants.CMSG_HEALTH, {'carId': self.characters[0], 'healthChange': self.t - 10})
            elif self.t < 20: # collide
                # TODO playerId is pretty meaningless here? everything else uses username
                self.main.cManager.sendRequest(Constants.CMSG_COLLISION, {'playerId': 0, 'damage': self.t - 30})
            else:
                self.phase = 4
                self.t = 0
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'
                print '--              _____ _____ _____ _____ _____    __ __              --'
                print '--             |  _  |  |  |  _  |   __|   __|  |  |  |             --'
                print '--             |   __|     |     |__   |   __|  |__   |             --'
                print '--             |__|  |__|__|__|__|_____|_____|     |__|             --'
                print '--                                                                  --'
                print '--            Goals: * Die                                          --'
                print '--                   * Get results and prize                        --'
                print '--                   * Disconnect                                   --'
                print '--                                                                  --'
                print '----------------------------------------------------------------------'
                print '----------------------------------------------------------------------'

            self.t += 1

        if self.phase == 4:
            # TODO gameId is meaningless for these tests; we must simulate lobby to know id
            # TODO likewise, we do not know our own username
            # TODO is RequestRankings for game or lobby?
            if self.t == 0: # die
                self.main.cManager.sendRequest(Constants.CMSG_DEAD, {'gameId': 0})
            elif self.t == 1: # rankings
                self.main.cManager.sendRequest(Constants.CMSG_RESULTS, {'gameId': 0})
            elif self.t == 2: # prize
                self.main.cManager.sendRequest(Constants.CMSG_PRIZES, {'username': 'User'})
            else:
                self.main.cManager.sendRequest(Constants.CMSG_DISCONNECT)
                return task.done

            self.t += 1

        return task.again

    def onRenderCharacter(self, data):
        self.characters.append(data['username'])
        print '[TEST] ResponseRenderCharacter: ' + str(data)

    def onRemoveUser(self, data):
        self.characters = [user for user in self.characters if user != data['username']]
        print '[TEST] ResponseRemoveUser: ' + str(data)

    def onMove(self, data):
        print '[TEST] ResponseMove: ' + str(data)

    def onPowerUpPickUp(self, data):
        print '[TEST] ResponsePowerUpPickUp: ' + str(data)

    def onPowerUpUse(self, data):
        print '[TEST] ResponsePowerUpUse: ' + str(data)

    def onChangeHealth(self, data):
        print '[TEST] ResponseChangeHealth: ' + str(data)

    def onCollision(self, data):
        print '[TEST] ResponseCollision: ' + str(data)

    def onDead(self, data):
        print '[TEST] ResponseDead: ' + str(data)

    def onResults(self, data):
        print '[TEST] ResponseResults: ' + str(data)

    def onPrizes(self, data):
        print '[TEST] ResponsePrizes: ' + str(data)

    def onLogout(self, data):
        print '[TEST] ResponseLogout: ' + str(data)



class EventEmitter(object):
    """Very basic EventEmitter (see nodejs) for testing purposes."""
    def __init__(self):
        self.hooks = {}

    def on(self, event, hook):
        if event in self.hooks:
            self.hooks[event].append(hook)
        else:
            self.hooks[event] = [hook]

    def emit(self, event, data = {}):
        if event in self.hooks:
            for hook in self.hooks[event]:
                hook(data)



class Main(ShowBase):
    def __init__(self):
        self.emitter = EventEmitter()
        self.cManager = ConnectionManager(self)

        self.tester = Tester(self)

        if self.startConnection():
            loadPrcFileData("", "window-type none") # disable graphics
            loadPrcFileData("", "audio-library-name null") # disable audio
            ShowBase.__init__(self)
            self.cManager.initTasks()
            self.emitter.emit('connection')
            self.run()

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            print 'Connecting...'
            if not self.cManager.startConnection():
                print 'Connection failed!'
                answer = raw_input('Reconnect? (Y/N): ').lower()
                if answer == 'y':
                    return self.startConnection()
                else:
                    return False

        return True

    def emit(event, data = {}): # terrible alias but I already wrote protocol code
        self.emitter.emit(event, data)

if __name__ == '__main__':
    app = Main()
