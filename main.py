class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"   
        


obj1 = A(12)
obj2 = A(6)

print(obj1 < obj2)
print("passed values are", obj1.a , obj2.a,"check whether they are less than or greater than", obj1 < obj2) 

obj3 = A(5)
obj4 = A(5)

print("passed values are", obj3.a , obj4.a,"check whether they are equal or not equal ", obj3 == obj4)



   
            
