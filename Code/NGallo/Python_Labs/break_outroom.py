from datetime import datetime

def time():
    now = datetime.now()
    time = now.strftime("%I%M")
    print(time)
    return time
now = time()

def breakout(now):

    now_replaced = now.replace(':','')
    now_replaced = int(now_replaced)
    print(f"NOW = {now_replaced}")


    end_time = input("What time would you like to end? ")
    end_time_replaced = end_time.replace(':','')

    print(f"REPLACED users time they want to end at = {end_time_replaced}")

    end_time = int(end_time)

    print(f"users time they want to end at = {end_time}")

    print_time = end_time - now_replaced 
    print(f"print_time = {print_time}")
    checker = print_time - 40
    print(checker)
    if checker > 0:
        print(checker)
    else:
        print(print_time)

breakout(now)