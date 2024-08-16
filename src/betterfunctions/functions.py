class Functions:


    def intput(self,text: str = None):
        inp = input(text)
        try:
            x = int(inp)
            return x
        except Exception as e:
            raise("Please give a number for input.")

    def output(self,value):
        print(value)