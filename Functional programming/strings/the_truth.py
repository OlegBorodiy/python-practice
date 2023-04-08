def decode_test(message, step):
    decode_step_1 = ''
    decode_step_2 = ''
    decode_step_3 = ''
    for i in message:
        if i in all_sym:
            num = all_sym.find(i)
            decode_step_1 += all_sym[num - step]
        else:
            decode_step_1 += i
    replace_index = 3
    for word in decode_step_1.split(' '):
        new_word = ''
        for index in range(len(word)):
            new_word += word[index - replace_index % len(word)]
        if new_word.endswith('/'):
            replace_index += 1
        decode_step_2 += new_word + ' '
    decode_step_2 = decode_step_2.replace('"', '!')
    decode_step_2 = decode_step_2.replace('(', "'")
    for word in decode_step_2.split(' '):
        new_word = ''
        for i in word:
            if i.isalpha() or i == '!' or i == "'" or i == '/':
                new_word += i
        decode_step_3 += new_word + ' '
    decode_step_3 = decode_step_3.replace('/', '.''\n')
    return decode_step_3


all_sym = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo' \
          ' jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt c' \
          'fuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq' \
          ' jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft' \
          ' (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu' \
          ' zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm' \
          ' omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf' \
          ' fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe' \
          ' sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi' \
          ' uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf' \
          ' sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu' \
          ' cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq' \
          ' tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb' \
          ' cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj' \
          ' .. fu(tm pe psfn gp tf"uip'

print('', decode_test(text, 1))