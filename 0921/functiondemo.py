# Call by reference , mutable type
def change(target):
    target[0] =10000
    print(f"in the change target = {target}")

original = [1,2,3]
print(f"Before change Original = {original}")
change(original)
print(f"After change Original = {original}")
