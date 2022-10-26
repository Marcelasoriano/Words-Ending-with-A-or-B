#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: 21 October 2022
#Program #24: prints words ending with a or b, number of words ending with a or b and the fraction of words ending with a or b

wordList=input("Enter a list of words: ")
ending=0
for word in wordList.split():
  if (word[-1]=="a") or (word[-1]=="b"):
    ending+=1
print("number of words:",len(wordList.split()))
print("number of words ending with a or b: " +str(ending))
print("fraction of words starting with a or b: ",round(ending/len(wordList.split()),2))