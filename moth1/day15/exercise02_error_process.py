
def get_score():
    score = int(input("Please input score: "))
    print (score)
    return score


while True:
    try:
        score = get_score()
    except Exception:
        print ("input error~ please input again.")
        continue
    # else:
    #     if 1<= score<=100:
    #         break
    break

