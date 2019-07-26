_g_repo = None


def set(repo):
    global _g_repo
    _g_repo = repo


def get():
    return _g_repo