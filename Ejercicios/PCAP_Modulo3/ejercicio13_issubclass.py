
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C,B))#True
print(issubclass(B,C))#False
print(issubclass(C,A))#True