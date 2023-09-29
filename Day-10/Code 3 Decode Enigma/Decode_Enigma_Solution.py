# Enter your code here. Read input from STDIN. Print output to STDOUT
def enigma(command):
    command = command.replace("S", "send ").replace("[]", "the ").replace("[sps]", "ships ")
    words = command.split()
    word = " ".join(words)
    return word

# Read the input
command = input()

# Get the interpretation and print it
interpretation = enigma(command)
print(interpretation)
