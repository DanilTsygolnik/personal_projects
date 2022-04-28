def w_duration(T, R, nW, nR):
    if nW == nR:
        W = T/nR - R
    else:
        W = (T + R*(1-nW))/nW
    return round(W)

def str_to_list(string):
    hh = ""
    mm = ""
    check = ""
    for s in string:
        if s == ":":
            check = ":"
            continue
        else:
            if check != ":":
                hh += s
            else:
                mm += s
    return [int(hh), int(mm)]

def t_str(t_list):
    string = ""
    if t_list[0] < 10:
        string += "0" + str(t_list[0]) + ":"
    else:
        string += str(t_list[0]) + ":"
    if t_list[1] < 10:
        string += "0" + str(t_list[1])
    else:
        string += str(t_list[1])
    return string


def schedule(start, nW, W, R, even=True):
    p_start = str_to_list(start)
    cnt = 0
    print("Schedule")
    while cnt < nW:
        if cnt == nW-1 and even == False:
            WRsum = W
        else:
            WRsum = W+R
        hsum = p_start[0] + WRsum//60
        msum = p_start[1] + WRsum%60
        if msum >= 60:
            hsum += 1
            msum -= 60
        p_finish = [hsum, msum]
        

        print(str(cnt+1)+". "+t_str(p_start)+" - "+t_str(p_finish))
        p_start = p_finish
        cnt += 1

# values = [T, m, n (рабочие подходы по M)]
def timing(T, even=True):
    plan_cnt = 1
    for s in range(5, 7):
        if even == True:
            nW = nR = s
        else:
            nW = s
            nR = s-1
        print("\n== Plan number "+str(plan_cnt)+" ==")
        print("\nTotal working sets:", nW)
        print("Total rest sets:", nR)
        print("-----------------")
        for R in range(10, 24):
            print("Work -", w_duration(T, R, nW, nR), "minutes; rest -", R, "minutes")
        plan_cnt += 1

#timing(9*60)
#timing(9*60, False)

schedule("6:00", 6, 75, 18, False)
schedule("16:00", 3, 88, 18, False)
