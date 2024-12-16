from six import moves

from googlevoice import Voice


def run():
    voice = Voice()
    voice.login()

    outgoingNumber = moves.input('Number to call: ')
    forwardingNumber = moves.input('Number to call from [optional]: ') or None

    voice.call(outgoingNumber, forwardingNumber)

    if moves.input('Calling now... cancel?[y/N] ').lower() == 'y':
        voice.cancel(outgoingNumber, forwardingNumber)


__name__ == '__main__' and run()
