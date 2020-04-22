paragraph = "Buck did not read the newspapers, or he would have known that trouble was brewing, not alone for himself, but for every tide-water dog, strong of muscle and with warm, long hair, from Puget Sound to San Diego. Because men, groping in the Arctic darkness, had found a yellow metal, and because steamship and transportation companies were booming the find, thousands of men were rushing into the Northland. These men wanted dogs, and the dogs they wanted were heavy dogs, with strong muscles by which to toil, and furry coats to protect them from the frost. Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Millerâ€™s place, it was called. It stood back from the road, half hidden among the trees, through which glimpses could be caught of the wide cool veranda that ran around its four sides. The house was approached by gravelled driveways which wound about through wide-spreading lawns and under the interlacing boughs of tall poplars. At the rear things were on even a more spacious scale than at the front. There were great stables, where a dozen grooms and boys held forth, rows of vine-clad servantsâ€™ cottages, an endless and orderly array of outhouses, long grape arbors, green pastures, orchards, and berry patches. Then there was the pumping plant for the artesian well, and the big cement tank where Judge Millerâ€™s boys took their morning plunge and kept cool in the hot afternoon. And over this great demesne Buck ruled. Here he was born, and here he had lived the four years of his life. It was true, there were other dogs, There could not but be other dogs on so vast a place, but they did not count. They came and went, resided in the populous kennels, or lived obscurely in the recesses of the house after the fashion of Toots, the Japanese pug, or Ysabel, the Mexican hairless,â€”strange creatures that rarely put nose out of doors or set foot to ground. On the other hand, there were the fox terriers, a score of them at least, who yelped fearful promises at Toots and Ysabel looking out of the  windows at them and protected by a legion of housemaids armed with brooms and mops."

#import requests
import string
not_a_letter = "`~-!@#$%^&*()_+=?:;,.\"”[]}{â€1234567890™"
dict_words = dict()

# response  = requests.get('www.gutenberg.org/files/215/215-0.txt')

#text = response.text
text = paragraph


def list_of_words(text):
    word_list = []
    #text = text.strip(not_a_letter)
    text = text.replace('â€™', '\'')
    for letter in not_a_letter:
        text = text.replace(letter, ' ')
    # print(text)
    # exit()
    words = text.lower().split()
    for word in words:
        word_list.append(word)
    for i in range(len(words)):
        words[i] = words[i].strip(not_a_letter)
    #print(word_list)
    return word_list


words = list_of_words(text)
print(words)

## specific_word = input("Enter a specific word, and I'll tell you how often it occurs: ")