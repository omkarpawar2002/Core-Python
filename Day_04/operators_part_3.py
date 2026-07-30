# 5.Membership operators :

"""
1.in :
        1.in operator is used to check whether the object occurs in specified object.
        2.It return True if object is found in specified object or return False if not found.
"""

name = "Aakit Shrivastv"
print("v" in name)
print("Z" in name)

"""
2.not in :
        1.not in operator is used to check whether the object does not occurs in specified object.
        2.It return True if object is not found in specified object or return False if found.
"""

name = "Aakit Shrivastv"
print("v" not in name)
print("Z" not in name)

print(
    "=================================================================================================="
)

# 6.Identity Operators :

"""
1.is :
        1.is operator is used to check whether both objects are point to same memory location.
        2.It return True if they point same memory location otherwise they return False.
"""

a = 10
b = 10
c = 101
print(a is b)
print(a is c)

"""
2.is not :
        1.is not operator is used to check whether both objects are not point to same memory location.
        2.It return True if they are not point to same memory location otherwise they return False.
"""

a = 10
b = 10
c = 101
print(a is not b)
print(a is not c)