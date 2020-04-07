print("\n\n---------------------8Madlib----------------------\n")

def main():
    while True:
        word_one = input("Enter a verb: ")
        word_two = input("Enter a noun: ")
        word_three = input("Enter an adjective: ")
        word_four = input("Enter an adverb: \n")

        print(f"Here is your madlib: \n \n The day I saw the Tiger King {word_one} was one of the most interesting days of the year. After he did that, the king played chess on at his friend's {word_two} and then combed his {word_three} hair with a comb made out of old fish bones. Later that same day, I saw the Tiger King dance {word_four} in front of an audience of kangaroos and wombats.\n")

        play_again = input("Would you like to play again? y/n: ")
        if play_again != 'y':
            print('Goodbye')
            break
        else: 
            print('okay, lets play again')

main()