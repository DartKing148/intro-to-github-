from math import ceil, log
import argparse


def diff_payment(p, i, n):
    count = 0
    i = count_interest(i)
    for m in range(1, n + 1):
        d = p - ((p * (m - 1)) / n)
        d = ceil(p / n + i * d)
        count += d
        print(f"Month {m}: payment is {d}")
    print(f"\nOverpayment = {int(count - p)}")


def count_month(payment, i, loan):
    i = count_interest(i)
    time = payment / (payment - i * loan)
    time = ceil(log(time, 1 + i))
    if time % 12 == 0:
        print(f"It will take {time // 12 } years to repay this loan!")
    elif time < 12:
        print(f"It will take {time} months to repay this loan!")
    else:
        print(f"It will take {time // 12} years and {time % 12} months to repay this loan!")
    print(f"Overpayment = {int(time * payment - loan)}")


def monthly_pay(i, loan, n):
    i = count_interest(i)
    payment = loan * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    payment = ceil(payment)
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {int(payment * n - loan)}")


def count_principal(p, n, i):
    i = count_interest(i)
    principal = (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    principal = p // principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {int(p * n - principal)}")


def count_interest(i):
    loan_interest = i / (12 * 100)
    return loan_interest


def check(parameters):
    c = 0

    for x in parameters:
        if x is not None:
            c += 1

    for f in parameters[1:4]:
        if f is not None:
            if float(f) < 0:
                print("Incorrect parameters")
                exit()

    if parameters[0] != "annuity" and parameters[0] != "diff" or parameters[2] is None:
        print("Incorrect parameters")
        exit()
    elif c < 4:
        print("Incorrect parameters")
        exit()
    elif parameters[0] == "diff" and parameters[4] is not None:
        print("Incorrect parameters")
        exit()


arguments = argparse.ArgumentParser()
arguments.add_argument("-t", "--type", choices=["diff", "annuity"])
arguments.add_argument("-p", "--principal")
arguments.add_argument("-i", "--interest")
arguments.add_argument("-n", "--periods")
arguments.add_argument("-y", "--payment")
args = arguments.parse_args()

all_parameters = [args.type, args.principal, args.interest, args.periods, args.payment]
check(all_parameters)

if args.type == "diff":
    diff_payment(int(args.principal), float(args.interest), int(args.periods))

if args.type == "annuity":
    if args.principal is None:
        count_principal(int(args.payment), int(args.periods), float(args.interest))
    elif args.periods is None:
        count_month(int(args.payment), float(args.interest), int(args.principal))
    elif args.payment is None:
        monthly_pay(float(args.interest), int(args.principal), int(args.periods))
