# Write a program to generate names in sequence

# Command to create a file
cmd = "touch "

for i in range(1, 11):
    cmd += "set_{:02d}.py ".format(i)

print(cmd)
