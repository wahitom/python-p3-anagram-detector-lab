# your code goes here!

# your code goes here!
 #init this class 
    # pass in  params
        # for the word we are comparing with
        # for the empty list match = []
        
    # get the name for  anagram
        # we will need a method that iterates over the items in the list and 
        # also compares it to the word passed as an argument 
    # compare it to other words in and array

class Anagram:

   

    def __init__(self, anagram=""):
        if isinstance(anagram, str):
            self._anagram = anagram
            #self._match = match
        else:
            print ("Input a word")
    
    def match(self, match=[]):
        result = []
        for word in match:
            if sorted(word) == sorted(self._anagram): #this method iterates through a list to find sth
                result.append(word)
        if result:
            return result
        else:
            return []
            

listen = Anagram("listen")
listen.match = listen.match(["enlist", "silent", "hello", "world"])

print(listen.match)