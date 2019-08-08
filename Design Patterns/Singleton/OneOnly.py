class OneOnly:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(
                OneOnly, cls).__new__(cls,*args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    
    o = OneOnly()
    e = OneOnly()

    boole = o is e
    print(boole)