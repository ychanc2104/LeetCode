class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super().__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print( "enter B")
        super().__init__()
        print ("leave B")

class C(A, B):
    def __init__(self):
        print ("enter C")
        super().__init__()
        print ("leave C")


C()

