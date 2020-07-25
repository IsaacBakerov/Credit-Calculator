import math
import sys

try:
    args = sys.argv
    type = args[1]
    if type == "--type=diff":
        p = args[2]
        if p[:12] == "--principal=":
            p = int(p[12:])
            n = args[3]
            if n[:10] == "--periods=":
                n = int(n[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    m = 1
                    D = 0
                    while m <= n:
                        d = (p/n) + (i*(p - (p*(m-1)/n)))
                        print("Month {}: paid out {}".format(m, math.ceil(d)))
                        m += 1
                        D += math.ceil(d)
                    print("Overpayment = {}".format(D - p))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    elif type == "--type=annuity":
        x = args[2]
        if x[:12] == "--principal=":
            p = int(x[12:])
            y = args[3]
            if y[:10] == "--periods=":
                n = int(y[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    a = p * i * pow(1 + i, n) / (pow(1 + i, n) - 1)
                    a = math.ceil(a)
                    print("Your annuity payment = {}!".format(a))
                    print("Overpayment = {}".format(a * n - p))
                else:
                    print("Incorrect Parameters")
            elif y[:10] == "--payment=":
                a = int(y[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    n = math.log(a / (a - i * p), 1 + i)
                    n = math.ceil(n)
                    if n == 1:
                        print("You need 1 month to repay this credit")
                        print("Overpayment = {}".format(a * n - p))
                    elif n < 12:
                        print("You need {} months to repay this credit".format(n))
                        print("Overpayment = {}".format(a * n - p))
                    elif n == 12:
                        print("You need 1 year to repay this credit")
                        print("Overpayment = {}".format(a * n - p))
                    elif 12 < n < 24:
                        year = n // 12
                        month = n - year * 12
                        if month == 0:
                            print("You need {} year to repay this credit".format(year))
                            print("Overpayment = {}".format(a * n - p))
                        else:
                            print("You need {} year and {} months to repay this credit".format(year, month))
                            print("Overpayment = {}".format(a * n - p))
                    elif n >= 24:
                        year = n // 12
                        month = n - year * 12
                        if month == 0:
                            print("You need {} years to repay this credit".format(year))
                            print("Overpayment = {}".format(a * n - p))
                        else:
                            print("You need {} years and {} months to repay this credit".format(year, month))
                            print("Overpayment = {}".format(a * n - p))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        elif x[:10] == "--payment=":
            a = int(x[10:])
            n = args[3]
            if n[:10] == "--periods=":
                n = int(n[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    p = a * (pow(1 + i, n) - 1) / (i * pow(1 + i, n))
                    p = math.floor(p)
                    print("Your credit principal = {}!".format(p))
                    print("Overpayment = {}".format(a * n - p))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    else:
        Exception
except Exception:
    print("Incorrect Parameters")
