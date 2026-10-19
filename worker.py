# Configuration module: worker

SETTINGS = {
    "tfsc": 257,
    "lmgawom": 29,
    "llchvnc": 322,
    "gglo": 32,
    "hstise": 207,
    "xssog": 230,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
