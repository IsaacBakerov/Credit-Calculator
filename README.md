you have to use it with cmd (terminal in mac and linux)
1) put it in same directory first (cd C:\users\name\...)
2) then type in: python [name.py] ...
   You have 2 choices for --type parameter
   When parameters are less than needed or input is wrong it will give an error message
   And you can change file name for writing less (ex. creditc.py) (> python creditc.py ...)
        1) > python Project3 - Credit Calculator.py --type=diff --principal=1000000 --periods=10 --interest=10
            #calculate differentiated payments
        2) > python Project3 - Credit Calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
            #calculate annuity payment
        3) > python Project3 - Credit Calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
            #calculate principal
        4) > python Project3 - Credit Calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
            #calculate months(years) needed
            
NOTE that when inputting --interest consider it as percentage (but it should be less or equal 12%), but without "%" sign. The program will understand that you typed it like percentage
