def flip_flop(line):
    if line == "Flip":
        print("Flop")
    elif line == ("Flop"):
        print("Flip")
    else:
        print("")

def flip_flop_tern(line):
    print("Flop" if line == "Flip" else "Flip" if line == "Flop" else "")

def flip_flop_ret(line):
    if line == "Flip":
        return "Flop"
    elif line == ("Flop"):
        return "Flip"
    else:
        return ""

def flip_flop_tern_ret(line):
    return "Flop" if line == "Flip" else "Flip" if line == "Flop" else ""
    
if __name__ == "__main__":
    if flip_flop_ret("Flip") != "Flop":
        print ("ErrorN1")
    else:
        print("Passed1")
    if flip_flop_ret("Flop") != "Flip":
        print("ErrorN2")
    else:
        print("Passed2")
    output = flip_flop_ret("gjdkflgj")
    if output != "":
        print("ErrorN3")
    else:
        print("Passed3")
    
