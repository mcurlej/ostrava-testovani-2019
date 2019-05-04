import rsp_lib

# 1. nacita tah uzivatela DONE
# 2. validovat vstup uzivatela DONE
# 3. zahrat nahodny tah DONE
# 4. informovat hraca o tahu DONE
# 5. vyhodnotit haty DONE
# 6. informovat hraca o vysledku DONE

def main():
    valid = False
    while not valid:
        choice = input("Rock, Paper, Scissors?")
        choice = choice.lower()
        valid = rsp_lib.is_valid_choice(choice)

    print("Human choice: ", choice)

    pc_choice = rsp_lib.random_choice()

    print("Computer choice: ", pc_choice)

    result = rsp_lib.get_game_results(choice, pc_choice)

    if result == 1:
        print("Human won!")
    elif result == -1:
        print("Human lost!")
    else:
        print("Tie")

if __name__ == '__main__':
    main()