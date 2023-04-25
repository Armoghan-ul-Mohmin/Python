# 2-7. Stripping Names:
##############################
#       Use a variable to represent a person’s name, and include
#   some whitespace characters at the beginning and end of the name. Make sure
#   you use each character combination, "\t" and "\n", at least once.
#   Print the name once, so the whitespace around the name is displayed.
#   Then print the name using each of the three stripping functions, lstrip(),
#   rstrip(), and strip().

name = input("Enter your Name: ")
print("\t\n   " + name + "  \n\t")

# Print name with surrounding whitespace
print("Name with surrounding whitespace:")
print(name)

# Print name using lstrip()
print("\nName using lstrip():")
print(name.lstrip())

# Print name using rstrip()
print("\nName using rstrip():")
print(name.rstrip())

# Print name using strip()
print("\nName using strip():")
print(name.strip())
