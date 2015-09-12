__author__ = 'veradocs-web'


def inNext(number):
    if 500<number<=1000:
        return 1000
    if 100 < number<=500:
        return 500
    if 50 < number<=100:
        return 100
    if  20< number<=50:
        return 50
    if 10 < number<=20:
        return 20
    if  5 < number <= 10:
        return 10
    if 2< number<= 5:
        return 5
    if number==2:
        return 2
    if number ==1:
        return 1

def correctTransaction(number,togive):
    if number==0:
       return
    number=togive-number
    togive=inNext(number)
    number=togive-number
    print number,togive
    correctTransaction(number,togive)



correctTransaction(427,500)



     #find the range in between number
     #find cashier return
    # userReturn()
      #number =


