import random
opp=['a','c','v','y','t','j','k','l','o','p']
num_values_to_select = 3
selected_values = random.sample(opp, num_values_to_select)
# out_put="".join(selected_values)
stro=input("Type the secret thing:")
words=stro.split(" ")
koka=input("type 1 for coding and 0 for decoding")
coding=True if (koka=='1') else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r2="".join(random.sample(opp, num_values_to_select))
            r1="".join(random.sample(opp, num_values_to_select))
            strnew=r1+word[1:]+word[0]+r2
            nwords.append(strnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))


else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            strnew=word[3:-3]
            strnew=strnew[-1]+strnew[:-1]
            nwords.append(strnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))         
    