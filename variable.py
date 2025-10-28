# Variables are dynamicly typed
n = 0
print('n =',n)

n = "abc"
print('n =',n)

# Multiple assignments
n, m = 0, "abc"
n, m, z = 3.14, "abc", False

print(f"n = {n} m = {m} z = {z}")

# Increment
n = n + 1   #good
n += 1      #good
# n++       #bad

# None is null (absence of value)

n = 4
n = None
print("n =", n)