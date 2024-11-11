# Write a recursive function reverse(sentence) for reversing a sentence. For example,
# reverse('Who let the dogs out?') will return '?tuo sgod eht tel ohW'. The idea is to remove
# the first or last letter, reverse the shortened sentence, and then combine the two parts

def reverse(sentence):
  if len(sentence)==1:
    return sentence
  else:
    return sentence[-1] + reverse(sentence[1:-1]) + sentence[0]
  
print(reverse("Who let the dogs out?"))
