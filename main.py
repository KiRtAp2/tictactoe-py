import logic

while True:
    izbira = input("Ali želiš začeti (n)ovo igro ali (k)ončati? ")
    if izbira.strip() == 'k': break

    logic.igra()
