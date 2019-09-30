
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D, Exception]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    except Exception:
        print("Exception")