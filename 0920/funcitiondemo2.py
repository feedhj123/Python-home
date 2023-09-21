def change(target):
    target = 100
    print("Before call change : original = %d" %target)

original = 5
print("Before call change : original = %d" %original)
change(original)
print("After call change : original = %d" %original)
