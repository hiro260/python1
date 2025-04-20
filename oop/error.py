def split_bill(price):
    num = input("how many people?")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("you cannnot devide by 0. Please input correct value")
        print(e)
    except ValueError:
        print("please input number.")
    else:
        print(f"each person pays {each}.")
    finally:
        print("thank you")
    

if __name__ == "__main__":
    split_bill(10000)

