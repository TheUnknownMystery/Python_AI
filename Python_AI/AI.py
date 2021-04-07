import webbrowser
import random


class AI(object):

    def __init__(A_I, UserName):
        A_I.UserName = UserName

    def Introduce(A_I):
        print("Hello " + A_I.UserName)

    def OpenLink(A_I):
        Input_Link = input("Please Enter Link")
        url = Input_Link
        webbrowser.open(url)

    def Add(A_I, n1, n2):
        print(n1 + n2)

    def Substract(A_I, n1, n2):
        print(n1 + n2)

    def Multiply(A_I, n1, n2):
        print(n1 * n2)

    def Create_A_Random_Number(A_I, n1, n2):
        print(random.randint(n1, n2))

    def Help(A_I):
        print('''

1.Introduce - Tells the AI to introduce them self
2.Add - Takes Two Argument And Adds Them
3.OpenLink  - Opens Any Link
4.Multiply  - Takes two number and multiply
5.Substract - Takes two number and substract

      ''')

#Run this to see all the functions
AI_1 = AI("Sauhardo")
AI_1.Help()