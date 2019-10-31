from Session import Session
'''
    This is the Main Class (our View). Right now, it is rather bland.
    It instantiates a session (our controller). It then listens for the users input and passes this input to the session to compute a reply.
    Connectable to a GUI if anyone wants to do that...
'''
#TODO: GUI?


class quote_main(object):
    def __init__(self):
        session = Session()
        self.convo(session)


    def convo (self, session):
        print("START")
        print('[QUOTE QUEEN]:', session.current.getPrompt())

        inp = ""
        while inp != "end":
            inp = input('[User]: ')
            print('[QUOTE QUEEN]:', session.reply(inp))

if __name__ == "__main__":
    qm = quote_main()