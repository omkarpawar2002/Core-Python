# Loop control statement :
"""
We now learn about control statement but we need to control loop so we have loop control statement :
    1.break
    2.continue
    3.pass
"""

# 1.break :
"""
1.break keyword is used when we immedieatly wants to exits from the loop.
2.we mainly used break keyword for searching some value if found then exit.
"""

# Here we see when value 5 fonud so it stop
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 2.continue :
"""
continue keyword is used when we want to skip the current value and jump on the next iteration.
"""

# Here we see when value 5 fonud so it skip it and continue printing other value
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 3.pass :
"""
1.pass keyword is used when we don't want implement any feature for now but later we implement it.
2.So to prevent error we used pass keyword.
3.It acts as a placeholder which does nothing.
"""

# Here we see loop run but it does nothing and after loop next statement execute which is Done.
for i in range(1, 11):
    pass
print("Done")


# Nested Loop :
"""
1.A loop inside another loop is known as a nested loop.
2.Mostly we used nested loop when we work with patterns.
"""

for row in range(5):
    for column in range(5):
        print("* ", end=" ")
    print()
