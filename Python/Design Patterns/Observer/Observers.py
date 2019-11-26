
class HexFormatterObs:
    def notify(self,publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")

class BinaryFormatterObs:
    def notify(self,publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin data = {value}")

def main():
    df = DefaultFormatter('test1')
    print(df)
    print()

    hf = HexFormatterObs()
    df.add(hf)
    df.data = 3
    print(df)
    print()

    bf = BinaryFormatterObs()
    df.add(bf)
    df.data = 21
    print(df)
    print()

    df.remove(hf)
    df.data = 40
    print(df)
    print()

    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)
    print()
    
    df.data = 15.8
    print(df)


if __name__ == "__main__":
    from DefaultFormatter import DefaultFormatter
    main()