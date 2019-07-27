class Response:

    def __init__(self):
        self.is_failed = True


def send_transfer_to_protocol_msg(from_id, to_id, amount):
    pass


def wait_protocol_resp():
    ok = Response()
    ok.is_failed = False
    return ok
