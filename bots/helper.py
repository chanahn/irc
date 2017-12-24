from irc import IRCBot, run_bot


class HelperBot(IRCBot):

    helpers = []
    finds = []

    def register(self, nick, message, channel, address):
        helper = {
                'nick': nick,
                'address': address,
                'timestamp': time()
                }
        helpers.append(helper)
        return '%s registered as helper', nick
                

    def find(self, nick, message, channel, address):
        find = {
                'id': len(finds) + 1,
                'nick': nick,
                'address': address,
                'timestamp': time()
                }
        finds.append(find)
        return '[%s] %s needs help at %s', len(finds), nick, address


    def accept(self, nick, message, channel, find_id):
        for find in finds:
            if find['id'] == find_id:
                finds.remove(find)
                return '%s accepted request %s', nick, find['id']
        return 'find_id not valid'

    def list(self, nick, message, channel):
        return finds

    def command_patterns(self):
        return (
            self.ping('^register (?P<address>\S+)', self.register),
            self.ping('^find (?P<address>\S+)', self.find),
            self.ping('^accept (?P<find_id>\S+)', self.accept),
            self.ping('^list', self.list),
        )


host = 'irc.freenode.net'
port = 6667
nick = 'helper'

run_bot(HelperBot, host, port, nick, ['#findhelper'])
