def main():
    try:
        a = int(input("Hiiii , Enter a number : "))
        print(a)
        return

    except Exception as e :
        print(e)
        return

    # Finally chalta hi chalta hai , its usecase is clearly visible in function when we are using retirn also .
    finally:
        print("I am inside finally")

main()