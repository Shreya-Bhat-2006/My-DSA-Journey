def rot(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in s1+s2
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(rot(s1, s2))