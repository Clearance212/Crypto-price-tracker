
coins = ["Sol", "Tron", "Lite", "Algo", "Rvn", "Zcash", "Eth"]

with open("cryptoorg.txt", "a") as file:
    d = input("Date today: \n")
    file.write(d)
    file.write('\n')
    file.write("------------------\n")
    for i in coins:
        a = input(i + ": ")
        file.write(i + ": ")
        file.write(a)
        file.write('\n')

    file.write('\n')
