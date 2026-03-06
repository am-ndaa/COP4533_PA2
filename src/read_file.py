def read_file(filename):
    filename = '../data/' + filename
    with open(filename, "r") as file:
        content = file.read().split()
    
    k = int(content[0])
    m = int(content[1])
    what_would_you_do_if_when_you_okay_so_he_said_yes_would_go = [int(x) for x in content[2:2+m]]
    return k,  what_would_you_do_if_when_you_okay_so_he_said_yes_would_go

if __name__ == "__main__":
    fn = input("Enter a file name: ")
    k, what_would_you_do_if_when_you_okay_so_he_said_yes_would_go = read_file(fn)
    print(f"Contents of {fn}:\n")
    print(k)
    print(what_would_you_do_if_when_you_okay_so_he_said_yes_would_go)