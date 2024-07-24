number_words={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
num=input("enter your mark:")
for x in num:
    if x in number_words:
        print(f'{number_words[x]}',end=' ')
    