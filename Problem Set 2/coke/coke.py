def main():
    print("Amount Due: 50")
    due = 50
    coin = 0
    while True:
        coin_input = int(input("Insert Coin: "))
        if accept_input(coin_input):
            coin = coin + coin_input
            if coin >= due:
                print(f"Change Owed: {coin - due}")
                break
            else:
                print(f"Amount Due: {due - coin}")
        else:
            print(f"Amount Due: {due - coin}")

def accept_input(coin_input):
    return(coin_input in [5,10,25])

main()