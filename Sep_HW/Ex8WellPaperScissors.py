


def WellPaperScissors(Player1, Player2):
    if Player1 == Player2:
        return "Draw"
    elif Player1 == "W" and Player2 == "P":
        return "P2"
    elif Player1 == "W" and Player2 == "S":
        return "P1"
    elif Player1 == "P" and Player2 == "W":
        return "P1"
    elif Player1 == "P" and Player2 == "S":
        return "P1"
    elif Player1 == "S" and Player2 == "W":
        return "P2"
    elif Player1 == "S" and Player2 == "P":
        return "P1"
    else:
        raise ValueError






if __name__ == "__main__":
    print("Pass1" if WellPaperScissors("W", "W")=="Draw" else "Error1")
    print("Pass2" if WellPaperScissors("W", "P")=="P2" else "Error2")
    print("Pass3" if WellPaperScissors("W", "S")=="P1" else "Error3")
    print("Pass4" if WellPaperScissors("P", "W")=="P1" else "Error4")
    print("Pass5" if WellPaperScissors("P", "P")=="Draw" else "Error5")
    print("Pass6" if WellPaperScissors("P", "S")=="P1" else "Error6")
    print("Pass7" if WellPaperScissors("S", "W")=="P2" else "Error7")
    print("Pass8" if WellPaperScissors("S", "P")=="P1" else "Error8")
    print("Pass9" if WellPaperScissors("S", "S")=="Draw" else "Error9")
    
    # print("Pass2" if WellPaperScissors("W", "S")=="Draw" else "Error2")
    # print("Pass3" if WellPaperScissors("S", "P")=="Draw" else "Error3")
    # print("Pass4" if WellPaperScissors("P", "W")=="Draw" else "Error4")