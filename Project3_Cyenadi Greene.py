#Cyenadi Greene
#project 3
#10/31/2024
#Goals:practice Python data structures



def task1():
    print("Task 1 Test: \n")
    print("Opening filename.txt and printing it's content")
    #open the file
    with open("filename.txt", "r") as theFile:
    #read the file
        print("Reading the file:")
        data =theFile.read()
        print(data)
        print("-" * 50)

        #removing punctions from theFile, except " ' " because words with ' are still proper english words
        cleaned_data = ""
        for char in data:
            if char not in ".,!?-":
                cleaned_data +=char

        #creating list of theFile
        theFile_list=cleaned_data.split()
        
    print("The text file turned into a list")
    print(theFile_list)
    print( "the amount of words in the list is:", len(theFile_list))

    print("-" * 50)
    # Create a dictionary that counts word frequency, i.e. freq[“happy”] = 12 means the word “happy” appears 12 times in the text file.
    print("Word Frequency")
    frequency ={}
    for word in theFile_list:
        word = word.lower()
        if word in frequency:
            frequency[word] = frequency[word]+1
        else:
            frequency[word]=1
    for word, count in frequency.items():
        print("%s = %d" % (word,count))
    print("-" * 50)
    # Remove all conjunction words ( for, and, nor, but, or, yet, so -- the 7 FANBOYS) plus (‘a’, ‘an’,'to', 'in', 'at') from the word list. Sort the list in alphabetical order and print out the first 100 words with 20 words in a line.
    #remove all conjucntion words
    print("The list with these words removed: 'a', 'an', 'to', 'in', 'at','for', 'and' , 'nor', 'but', 'or', 'yet', 'so' ")
    toRemove = ['a', 'an', 'to', 'in', 'at','for', 'and',  'nor', 'but', 'or', 'yet', 'so']
    theFile_list=[word for word in theFile_list if word.lower() not in toRemove]
    print(theFile_list)
    print("-" * 50)
    #Sort the list in alphabetical order
    #print("The list in alphebitcal order:")
    print("")
    sorted_list =sorted(theFile_list)
    # print out the first 100 words with 20 words in a line.
    for i in range(100):
        print(sorted_list[i], end=" ")
        if (i+1)%20 ==0:
            print("\n")
    print("-" * 50) 

    #(7) Remove the words described in (6) from the dictionary. Print out 50 most frequent words in the form of tuples, i.e. (word, frequency) in descending order of frequency with 10 tuples per line.
    # Remove the words described in (6) from the dictionary.
    print("Removing: 'a', 'an', 'to', 'in', 'at','for', 'and' , 'nor', 'but', 'or', 'yet', 'so' ")
    print("Printing out 50 most frequent words in form of tuples")
    for key in toRemove:
        del frequency[key]

    
    #Print out 50 most frequent words in the form of tuples, i.e. (word, frequency) in descending order of frequency with 10 tuples per line.
    sorted_frequency = sorted(frequency.items(), key = lambda x: x[1], reverse =True)
    for i in range(50):
        word, count = sorted_frequency[i]
        print(f"({word},{count})", end=" ")

        if (i+1) % 10 ==0:
            print("\n")
    print("-" * 50)


import math

# A function setup() takes the above two lists as parameters and returns two values, a list of (name, score) tuples (i.e. [(“Andy”, 88), (“Ben”, 92), ...] and a dictionary with name as key and score as value (i.e. {“Andy” : 88, “Ben” : 92, ...}
def setup(list1, list2):
        names_scores_tuple = list(zip(list1, list2))
        
        # Create the dictionary with names as keys and scores as values
        names_scores_dict = dict(zip(list1, list2))
        
        # Return both values
        return names_scores_tuple, names_scores_dict

#A function score_update() that will take three parameters, a dictionary as returned by the setup() function, a student’s name, and a new score. It will update the student’s score with the new score if the student’s name is in the dictionary. Once update successful, it will return “Done” Otherwise it returns None (you design proper message if update unsuccessful.)
def scoreUpdate( dictionary, name, newscore):
        
    if name in dictionary:
        dictionary[name]= newscore
        return print("Done")
    else:
         return print("Name is not in the dictionary, failed to update")
    
#A function get_stat() that takes the dictionary as parameter, returns multiple values, the class average score, the standard deviation, and the student with highest score in the form of (name,highest_score).

def get_stat(dictionary):
    scores = list(dictionary.values())
    average= sum(scores)/ len(scores)

    summation= sum((score-average)**2 for score in scores)
    standardDev= math.sqrt(summation/ len(scores))

    highestStudent= max( dictionary, key=dictionary.get)
    highestScore = dictionary [ highestStudent]

    return {
         "average" : average,
         "Standard Devation" : standardDev,
         "highest" : (highestStudent, highestScore)
    }
def task2():
    print("Task 2:")
    print("Printing the first tuple list and dictionary using the list given in instructions:")
    names = ["Andy", "Ben", "Cathy", "Dave", "Edward", "Fanny", "George", "Hana", "Jess", "Karen", "Nancy", "Pedro"]
    scores = [88, 92, 85, 76, 85, 96, 77, 82, 90, 72, 98, 82]
    namescoretuple, namescoredict = setup(names, scores)
    print("List of (name, score) tuples:", namescoretuple)
    print("Dictionary with name as key and score as value:", namescoredict)
    print()
    print("-" * 50)
    print("Change score of Cathy to 0")
    scoreUpdate(namescoredict, 'Cathy',0 )
    print(namescoredict)
    print("Showing the fail update message by trying to change the score of 'Sally'")
    scoreUpdate(namescoredict, 'Sally',10)
    print("-" * 50)
    stats=get_stat(namescoredict)
    print("Class Average:", stats["average"])
    print("Standard Deviation:", stats["Standard Devation"])
    print("Highest Scorer:", stats["highest"])
    print("-" * 50)




    print("Printing the first tuple list and dictionary using the list I created")
    names1 =[ 'Sam', 'Dean', 'Crowley', 'Bobby', 'Ruby', 'Castiel', 'Kate', 'Sarah', 'Kia','Sophia', 'Mia', 'Cade','Kevin', 'Tony', 'Bella', 'Cory', 'Star','Ellen','Jo', 'Jack']
    scores1 =[65, 70, 75, 77, 83, 82, 55, 100, 85, 90, 80, 45, 73, 22, 50, 88, 95, 100, 40, 76]
    namescoretuple, namescoredict = setup(names1, scores1)
    print("List of (name, score) tuples:", namescoretuple)
    print("Dictionary with name as key and score as value:", namescoredict)
    print("-" * 50)
    print("Change score of Crowley to 0")
    scoreUpdate(namescoredict, 'Crowley',0 )
    print(namescoredict)
    print("Showing the fail update message by trying to change the score of 'Sally'")
    scoreUpdate(namescoredict, 'Sally',10)
    print("-" * 50)
    stats=get_stat(namescoredict)
    print("Class Average:", stats["average"])
    print("Standard Deviation:", stats["Standard Devation"])
    print("Highest Scorer:", stats["highest"])
    print("-" * 50)
    

def main():
    task1()
    task2()

if __name__ == "__main__":
    main()

"""
Task 1 Test: 

Opening filename.txt and printing it's content
Reading the file:
1609

THE SONNETS

by William Shakespeare



                     1
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee.


                     2
  When forty winters shall besiege thy brow,
  And dig deep trenches in thy beauty's field,
  Thy youth's proud livery so gazed on now,
  Will be a tattered weed of small worth held:
  Then being asked, where all thy beauty lies,
  Where all the treasure of thy lusty days;
  To say within thine own deep sunken eyes,
  Were an all-eating shame, and thriftless praise.
  How much more praise deserved thy beauty's use,
  If thou couldst answer 'This fair child of mine
  Shall sum my count, and make my old excuse'
  Proving his beauty by succession thine.
    This were to be new made when thou art old,
    And see thy blood warm when thou feel'st it cold.


                     3
  Look in thy glass and tell the face thou viewest,
  Now is the time that face should form another,
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose uneared womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime,
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live remembered not to be,
    Die single and thine image dies with thee.


                     4
  Unthrifty loveliness why dost thou spend,
  Upon thy self thy beauty's legacy?
  Nature's bequest gives nothing but doth lend,
  And being frank she lends to those are free:
  Then beauteous niggard why dost thou abuse,
  The bounteous largess given thee to give?
  Profitless usurer why dost thou use
  So great a sum of sums yet canst not live?
  For having traffic with thy self alone,
  Thou of thy self thy sweet self dost deceive,
  Then how when nature calls thee to be gone,
  What acceptable audit canst thou leave?
    Thy unused beauty must be tombed with thee,
    Which used lives th' executor to be.


                     5
  Those hours that with gentle work did frame
  The lovely gaze where every eye doth dwell
  Will play the tyrants to the very same,
  And that unfair which fairly doth excel:
  For never-resting time leads summer on
  To hideous winter and confounds him there,
  Sap checked with frost and lusty leaves quite gone,
  Beauty o'er-snowed and bareness every where:
  Then were not summer's distillation left
  A liquid prisoner pent in walls of glass,
  Beauty's effect with beauty were bereft,
  Nor it nor no remembrance what it was.
    But flowers distilled though they with winter meet,
    Leese but their show, their substance still lives sweet.


                     6
  Then let not winter's ragged hand deface,
  In thee thy summer ere thou be distilled:
  Make sweet some vial; treasure thou some place,
  With beauty's treasure ere it be self-killed:
  That use is not forbidden usury,
  Which happies those that pay the willing loan;
  That's for thy self to breed another thee,
  Or ten times happier be it ten for one,
  Ten times thy self were happier than thou art,
  If ten of thine ten times refigured thee:
  Then what could death do if thou shouldst depart,
  Leaving thee living in posterity?
    Be not self-willed for thou art much too fair,
    To be death's conquest and make worms thine heir.


                     7
  Lo in the orient when the gracious light
  Lifts up his burning head, each under eye
  Doth homage to his new-appearing sight,
  Serving with looks his sacred majesty,
  And having climbed the steep-up heavenly hill,
  Resembling strong youth in his middle age,
  Yet mortal looks adore his beauty still,
  Attending on his golden pilgrimage:
  But when from highmost pitch with weary car,
  Like feeble age he reeleth from the day,
  The eyes (fore duteous) now converted are
  From his low tract and look another way:
    So thou, thy self out-going in thy noon:
    Unlooked on diest unless thou get a son.


                     8
  Music to hear, why hear'st thou music sadly?
  Sweets with sweets war not, joy delights in joy:
  Why lov'st thou that which thou receiv'st not gladly,
  Or else receiv'st with pleasure thine annoy?
  If the true concord of well-tuned sounds,
  By unions married do offend thine ear,
  They do but sweetly chide thee, who confounds
  In singleness the parts that thou shouldst bear:
  Mark how one string sweet husband to another,
  Strikes each in each by mutual ordering;
  Resembling sire, and child, and happy mother,
  Who all in one, one pleasing note do sing:
    Whose speechless song being many, seeming one,
    Sings this to thee, 'Thou single wilt prove none'.


                     9
  Is it for fear to wet a widow's eye,
  That thou consum'st thy self in single life?
  Ah, if thou issueless shalt hap to die,
  The world will wail thee like a makeless wife,
  The world will be thy widow and still weep,
  That thou no form of thee hast left behind,
  When every private widow well may keep,
  By children's eyes, her husband's shape in mind:
  Look what an unthrift in the world doth spend
  Shifts but his place, for still the world enjoys it;
  But beauty's waste hath in the world an end,
  And kept unused the user so destroys it:
    No love toward others in that bosom sits
    That on himself such murd'rous shame commits.


                     10
  For shame deny that thou bear'st love to any
  Who for thy self art so unprovident.
  Grant if thou wilt, thou art beloved of many,
  But that thou none lov'st is most evident:
  For thou art so possessed with murd'rous hate,
  That 'gainst thy self thou stick'st not to conspire,
  Seeking that beauteous roof to ruinate
  Which to repair should be thy chief desire:
  O change thy thought, that I may change my mind,
  Shall hate be fairer lodged than gentle love?
  Be as thy presence is gracious and kind,
  Or to thy self at least kind-hearted prove,
    Make thee another self for love of me,
    That beauty still may live in thine or thee.

--------------------------------------------------
The text file turned into a list
['1609', 'THE', 'SONNETS', 'by', 'William', 'Shakespeare', '1', 'From', 'fairest', 'creatures', 'we', 'desire', 'increase', 'That', 'thereby', "beauty's", 'rose', 'might', 'never', 'die', 'But', 'as', 'the', 'riper', 'should', 'by', 'time', 'decease', 'His', 'tender', 'heir', 'might', 'bear', 'his', 'memory:', 'But', 'thou', 'contracted', 'to', 'thine', 'own', 'bright', 'eyes', "Feed'st", 'thy', "light's", 'flame', 'with', 'selfsubstantial', 'fuel', 'Making', 'a', 'famine', 'where', 'abundance', 'lies', 'Thy', 'self', 'thy', 'foe', 'to', 'thy', 'sweet', 'self', 'too', 'cruel:', 'Thou', 'that', 'art', 'now', 'the', "world's", 'fresh', 'ornament', 'And', 'only', 'herald', 'to', 'the', 'gaudy', 'spring', 'Within', 'thine', 'own', 'bud', 'buriest', 'thy', 'content', 'And', 'tender', 'churl', "mak'st", 'waste', 'in', 'niggarding:', 'Pity', 'the', 'world', 'or', 'else', 'this', 'glutton', 'be', 'To', 'eat', 'the', "world's", 'due', 'by', 'the', 'grave', 'and', 'thee', '2', 'When', 'forty', 'winters', 'shall', 'besiege', 'thy', 'brow', 'And', 'dig', 'deep', 'trenches', 'in', 'thy', "beauty's", 'field', 'Thy', "youth's", 'proud', 'livery', 'so', 'gazed', 'on', 'now', 'Will', 'be', 'a', 'tattered', 'weed', 'of', 'small', 'worth', 'held:', 'Then', 'being', 'asked', 'where', 'all', 'thy', 'beauty', 'lies', 'Where', 'all', 'the', 'treasure', 'of', 'thy', 'lusty', 'days;', 'To', 'say', 'within', 'thine', 'own', 'deep', 'sunken', 'eyes', 'Were', 'an', 'alleating', 'shame', 'and', 'thriftless', 'praise', 'How', 'much', 'more', 'praise', 'deserved', 'thy', "beauty's", 'use', 'If', 'thou', 'couldst', 'answer', "'This", 'fair', 'child', 'of', 'mine', 'Shall', 'sum', 'my', 'count', 'and', 'make', 'my', 'old', "excuse'", 'Proving', 'his', 'beauty', 'by', 'succession', 'thine', 'This', 'were', 'to', 'be', 'new', 'made', 'when', 'thou', 'art', 'old', 'And', 'see', 'thy', 'blood', 'warm', 'when', 'thou', "feel'st", 'it', 'cold', '3', 'Look', 'in', 'thy', 'glass', 'and', 'tell', 'the', 'face', 'thou', 'viewest', 'Now', 'is', 'the', 'time', 'that', 'face', 'should', 'form', 'another', 'Whose', 
'fresh', 'repair', 'if', 'now', 'thou', 'not', 'renewest', 'Thou', 'dost', 'beguile', 'the', 'world', 'unbless', 'some', 'mother', 'For', 'where', 'is', 'she', 'so', 'fair', 'whose', 'uneared', 'womb', 'Disdains', 'the', 'tillage', 'of', 'thy', 'husbandry', 'Or', 'who', 'is', 'he', 'so', 'fond', 'will', 'be', 'the', 'tomb', 'Of', 'his', 'selflove', 'to', 'stop', 'posterity', 'Thou', 'art', 'thy', "mother's", 'glass', 'and', 'she', 'in', 'thee', 'Calls', 'back', 'the', 'lovely', 'April', 'of', 'her', 'prime', 'So', 'thou', 'through', 'windows', 'of', 'thine', 'age', 'shalt', 'see', 'Despite', 'of', 'wrinkles', 'this', 'thy', 'golden', 'time', 'But', 'if', 'thou', 'live', 'remembered', 'not', 'to', 'be', 'Die', 'single', 'and', 'thine', 'image', 'dies', 'with', 'thee', '4', 'Unthrifty', 'loveliness', 
'why', 'dost', 'thou', 'spend', 'Upon', 'thy', 'self', 'thy', "beauty's", 'legacy', "Nature's", 'bequest', 'gives', 'nothing', 'but', 'doth', 'lend', 'And', 'being', 'frank', 'she', 'lends', 'to', 'those', 'are', 'free:', 'Then', 'beauteous', 'niggard', 'why', 'dost', 'thou', 'abuse', 'The', 'bounteous', 'largess', 'given', 'thee', 'to', 'give', 'Profitless', 'usurer', 'why', 'dost', 'thou', 'use', 'So', 'great', 'a', 'sum', 'of', 'sums', 'yet', 'canst', 'not', 'live', 'For', 'having', 'traffic', 'with', 'thy', 'self', 'alone', 'Thou', 'of', 'thy', 'self', 'thy', 'sweet', 'self', 'dost', 'deceive', 'Then', 'how', 'when', 'nature', 'calls', 
'thee', 'to', 'be', 'gone', 'What', 'acceptable', 'audit', 'canst', 'thou', 'leave', 'Thy', 'unused', 'beauty', 'must', 'be', 'tombed', 'with', 'thee', 'Which', 'used', 'lives', "th'", 'executor', 'to', 'be', '5', 'Those', 'hours', 'that', 'with', 'gentle', 'work', 'did', 'frame', 'The', 'lovely', 'gaze', 'where', 'every', 'eye', 'doth', 'dwell', 'Will', 'play', 'the', 'tyrants', 'to', 'the', 'very', 'same', 'And', 'that', 'unfair', 'which', 'fairly', 'doth', 'excel:', 'For', 'neverresting', 'time', 'leads', 'summer', 'on', 'To', 'hideous', 'winter', 'and', 'confounds', 'him', 'there', 'Sap', 'checked', 'with', 'frost', 'and', 'lusty', 'leaves', 'quite', 'gone', 'Beauty', "o'ersnowed", 'and', 'bareness', 'every', 'where:', 'Then', 'were', 'not', "summer's", 'distillation', 'left', 'A', 'liquid', 'prisoner', 'pent', 'in', 'walls', 'of', 'glass', "Beauty's", 'effect', 'with', 'beauty', 'were', 'bereft', 'Nor', 'it', 'nor', 'no', 'remembrance', 'what', 'it', 'was', 'But', 'flowers', 'distilled', 'though', 'they', 'with', 'winter', 'meet', 'Leese', 'but', 'their', 'show', 'their', 'substance', 'still', 'lives', 'sweet', 
'6', 'Then', 'let', 'not', "winter's", 'ragged', 'hand', 'deface', 'In', 'thee', 'thy', 'summer', 'ere', 'thou', 'be', 'distilled:', 'Make', 'sweet', 'some', 'vial;', 'treasure', 'thou', 'some', 'place', 'With', "beauty's", 'treasure', 'ere', 'it', 'be', 'selfkilled:', 'That', 'use', 'is', 'not', 'forbidden', 'usury', 'Which', 'happies', 'those', 'that', 'pay', 'the', 'willing', 'loan;', "That's", 'for', 'thy', 'self', 'to', 'breed', 'another', 'thee', 'Or', 'ten', 'times', 'happier', 'be', 'it', 'ten', 'for', 'one', 'Ten', 'times', 'thy', 'self', 'were', 'happier', 'than', 'thou', 'art', 'If', 'ten', 'of', 'thine', 'ten', 'times', 'refigured', 'thee:', 'Then', 'what', 'could', 'death', 'do', 'if', 'thou', 'shouldst', 'depart', 'Leaving', 'thee', 'living', 'in', 'posterity', 'Be', 'not', 'selfwilled', 'for', 'thou', 'art', 'much', 'too', 'fair', 'To', 'be', "death's", 'conquest', 'and', 'make', 'worms', 'thine', 'heir', '7', 'Lo', 'in', 'the', 'orient', 'when', 'the', 'gracious', 'light', 'Lifts', 'up', 'his', 'burning', 'head', 'each', 'under', 'eye', 'Doth', 'homage', 'to', 'his', 'newappearing', 'sight', 'Serving', 'with', 'looks', 'his', 'sacred', 'majesty', 'And', 'having', 'climbed', 'the', 'steepup', 'heavenly', 'hill', 'Resembling', 'strong', 'youth', 'in', 'his', 'middle', 'age', 'Yet', 'mortal', 'looks', 'adore', 'his', 'beauty', 'still', 'Attending', 'on', 'his', 'golden', 'pilgrimage:', 'But', 'when', 'from', 'highmost', 'pitch', 'with', 'weary', 'car', 'Like', 'feeble', 'age', 'he', 'reeleth', 'from', 'the', 'day', 'The', 'eyes', '(fore', 'duteous)', 'now', 'converted', 'are', 'From', 'his', 'low', 'tract', 'and', 'look', 'another', 'way:', 'So', 'thou', 'thy', 'self', 'outgoing', 'in', 'thy', 'noon:', 'Unlooked', 'on', 'diest', 'unless', 
'thou', 'get', 'a', 'son', '8', 'Music', 'to', 'hear', 'why', "hear'st", 'thou', 'music', 'sadly', 'Sweets', 'with', 'sweets', 'war', 'not', 'joy', 'delights', 'in', 'joy:', 'Why', "lov'st", 'thou', 'that', 'which', 'thou', "receiv'st", 'not', 'gladly', 'Or', 'else', "receiv'st", 'with', 'pleasure', 'thine', 'annoy', 'If', 'the', 'true', 'concord', 'of', 'welltuned', 'sounds', 'By', 'unions', 'married', 'do', 'offend', 'thine', 'ear', 'They', 'do', 'but', 'sweetly', 'chide', 'thee', 'who', 'confounds', 'In', 'singleness', 'the', 'parts', 'that', 'thou', 'shouldst', 'bear:', 'Mark', 'how', 'one', 'string', 'sweet', 'husband', 'to', 'another', 'Strikes', 'each', 'in', 'each', 'by', 'mutual', 'ordering;', 'Resembling', 'sire', 'and', 'child', 'and', 'happy', 'mother', 'Who', 'all', 'in', 'one', 'one', 
'pleasing', 'note', 'do', 'sing:', 'Whose', 'speechless', 'song', 'being', 'many', 'seeming', 'one', 'Sings', 'this', 'to', 'thee', "'Thou", 'single', 'wilt', 'prove', "none'", '9', 'Is', 'it', 'for', 'fear', 'to', 'wet', 'a', "widow's", 'eye', 'That', 'thou', "consum'st", 'thy', 'self', 'in', 'single', 'life', 'Ah', 'if', 'thou', 'issueless', 'shalt', 'hap', 'to', 'die', 'The', 'world', 'will', 'wail', 'thee', 'like', 'a', 'makeless', 'wife', 'The', 'world', 'will', 'be', 'thy', 'widow', 'and', 'still', 'weep', 'That', 'thou', 'no', 'form', 'of', 'thee', 'hast', 'left', 'behind', 'When', 'every', 'private', 'widow', 'well', 'may', 'keep', 
'By', "children's", 'eyes', 'her', "husband's", 'shape', 'in', 'mind:', 'Look', 'what', 'an', 'unthrift', 'in', 'the', 'world', 'doth', 'spend', 'Shifts', 'but', 
'his', 'place', 'for', 'still', 'the', 'world', 'enjoys', 'it;', 'But', "beauty's", 'waste', 'hath', 'in', 'the', 'world', 'an', 'end', 'And', 'kept', 'unused', 'the', 'user', 'so', 'destroys', 'it:', 'No', 'love', 'toward', 'others', 'in', 'that', 'bosom', 'sits', 'That', 'on', 'himself', 'such', "murd'rous", 'shame', 'commits', '10', 'For', 'shame', 'deny', 'that', 'thou', "bear'st", 'love', 'to', 'any', 'Who', 'for', 'thy', 'self', 'art', 'so', 'unprovident', 'Grant', 'if', 'thou', 'wilt', 'thou', 'art', 'beloved', 'of', 'many', 'But', 'that', 'thou', 'none', "lov'st", 'is', 'most', 'evident:', 'For', 'thou', 'art', 'so', 'possessed', 'with', "murd'rous", 'hate', 'That', "'gainst", 'thy', 'self', 'thou', "stick'st", 'not', 'to', 'conspire', 'Seeking', 'that', 'beauteous', 'roof', 'to', 'ruinate', 'Which', 'to', 'repair', 'should', 'be', 'thy', 'chief', 'desire:', 'O', 'change', 'thy', 'thought', 'that', 'I', 'may', 'change', 'my', 'mind', 'Shall', 'hate', 'be', 'fairer', 'lodged', 'than', 'gentle', 'love', 'Be', 'as', 'thy', 'presence', 'is', 'gracious', 'and', 'kind', 'Or', 'to', 'thy', 'self', 'at', 'least', 'kindhearted', 'prove', 'Make', 'thee', 'another', 'self', 'for', 'love', 'of', 'me', 'That', 'beauty', 'still', 'may', 'live', 'in', 'thine', 'or', 'thee']
the amount of words in the list is: 1114
--------------------------------------------------
Word Frequency
1609 = 1
the = 32
sonnets = 1
by = 7
william = 1
shakespeare = 1
1 = 1
from = 4
fairest = 1
creatures = 1
we = 1
desire = 1
increase = 1
that = 19
thereby = 1
beauty's = 7
rose = 1
might = 2
never = 1
die = 3
but = 11
as = 2
riper = 1
should = 3
time = 4
decease = 1
his = 12
tender = 2
heir = 2
bear = 1
memory: = 1
thou = 36
contracted = 1
to = 27
thine = 11
own = 3
bright = 1
eyes = 4
feed'st = 1
thy = 35
light's = 1
flame = 1
with = 14
selfsubstantial = 1
fuel = 1
making = 1
a = 7
famine = 1
where = 5
abundance = 1
lies = 2
self = 14
foe = 1
sweet = 5
too = 2
cruel: = 1
art = 8
now = 5
world's = 2
fresh = 2
ornament = 1
and = 23
only = 1
herald = 1
gaudy = 1
spring = 1
within = 2
bud = 1
buriest = 1
content = 1
churl = 1
mak'st = 1
waste = 2
in = 20
niggarding: = 1
pity = 1
world = 7
or = 6
else = 2
this = 4
glutton = 1
be = 17
eat = 1
due = 1
grave = 1
thee = 15
2 = 1
when = 7
forty = 1
winters = 1
shall = 3
besiege = 1
brow = 1
dig = 1
deep = 2
trenches = 1
field = 1
youth's = 1
proud = 1
livery = 1
so = 9
gazed = 1
on = 5
will = 5
tattered = 1
weed = 1
of = 16
small = 1
worth = 1
held: = 1
then = 6
being = 3
asked = 1
all = 3
beauty = 7
treasure = 3
lusty = 2
days; = 1
say = 1
sunken = 1
were = 5
an = 3
alleating = 1
shame = 3
thriftless = 1
praise = 2
how = 3
much = 2
more = 1
deserved = 1
use = 3
if = 8
couldst = 1
answer = 1
'this = 1
fair = 3
child = 2
mine = 1
sum = 2
my = 3
count = 1
make = 4
old = 2
excuse' = 1
proving = 1
succession = 1
new = 1
made = 1
see = 2
blood = 1
warm = 1
feel'st = 1
it = 6
cold = 1
3 = 1
look = 3
glass = 3
tell = 1
face = 2
viewest = 1
is = 7
form = 2
another = 5
whose = 3
repair = 2
not = 10
renewest = 1
dost = 5
beguile = 1
unbless = 1
some = 3
mother = 2
for = 12
she = 3
uneared = 1
womb = 1
disdains = 1
tillage = 1
husbandry = 1
who = 4
he = 2
fond = 1
tomb = 1
selflove = 1
stop = 1
posterity = 2
mother's = 1
calls = 2
back = 1
lovely = 2
april = 1
her = 2
prime = 1
through = 1
windows = 1
age = 3
shalt = 2
despite = 1
wrinkles = 1
golden = 2
live = 3
remembered = 1
single = 3
image = 1
dies = 1
4 = 1
unthrifty = 1
loveliness = 1
why = 5
spend = 2
upon = 1
legacy = 1
nature's = 1
bequest = 1
gives = 1
nothing = 1
doth = 5
lend = 1
frank = 1
lends = 1
those = 3
are = 2
free: = 1
beauteous = 2
niggard = 1
abuse = 1
bounteous = 1
largess = 1
given = 1
give = 1
profitless = 1
usurer = 1
great = 1
sums = 1
yet = 2
canst = 2
having = 2
traffic = 1
alone = 1
deceive = 1
nature = 1
gone = 2
what = 4
acceptable = 1
audit = 1
leave = 1
unused = 2
must = 1
tombed = 1
which = 5
used = 1
lives = 2
th' = 1
executor = 1
5 = 1
hours = 1
gentle = 2
work = 1
did = 1
frame = 1
gaze = 1
every = 3
eye = 3
dwell = 1
play = 1
tyrants = 1
very = 1
same = 1
unfair = 1
fairly = 1
excel: = 1
neverresting = 1
leads = 1
summer = 2
hideous = 1
winter = 2
confounds = 2
him = 1
there = 1
sap = 1
checked = 1
frost = 1
leaves = 1
quite = 1
o'ersnowed = 1
bareness = 1
where: = 1
summer's = 1
distillation = 1
left = 2
liquid = 1
prisoner = 1
pent = 1
walls = 1
effect = 1
bereft = 1
nor = 2
no = 3
remembrance = 1
was = 1
flowers = 1
distilled = 1
though = 1
they = 2
meet = 1
leese = 1
their = 2
show = 1
substance = 1
still = 5
6 = 1
let = 1
winter's = 1
ragged = 1
hand = 1
deface = 1
ere = 2
distilled: = 1
vial; = 1
place = 2
selfkilled: = 1
forbidden = 1
usury = 1
happies = 1
pay = 1
willing = 1
loan; = 1
that's = 1
breed = 1
ten = 5
times = 3
happier = 2
one = 5
than = 2
refigured = 1
thee: = 1
could = 1
death = 1
do = 4
shouldst = 2
depart = 1
leaving = 1
living = 1
selfwilled = 1
death's = 1
conquest = 1
worms = 1
7 = 1
lo = 1
orient = 1
gracious = 2
light = 1
lifts = 1
up = 1
burning = 1
head = 1
each = 3
under = 1
homage = 1
newappearing = 1
sight = 1
serving = 1
looks = 2
sacred = 1
majesty = 1
climbed = 1
steepup = 1
heavenly = 1
hill = 1
resembling = 2
strong = 1
youth = 1
middle = 1
mortal = 1
adore = 1
attending = 1
pilgrimage: = 1
highmost = 1
pitch = 1
weary = 1
car = 1
like = 2
feeble = 1
reeleth = 1
day = 1
(fore = 1
duteous) = 1
converted = 1
low = 1
tract = 1
way: = 1
outgoing = 1
noon: = 1
unlooked = 1
diest = 1
unless = 1
get = 1
son = 1
8 = 1
music = 2
hear = 1
hear'st = 1
sadly = 1
sweets = 2
war = 1
joy = 1
delights = 1
joy: = 1
lov'st = 2
receiv'st = 2
gladly = 1
pleasure = 1
annoy = 1
true = 1
concord = 1
welltuned = 1
sounds = 1
unions = 1
married = 1
offend = 1
ear = 1
sweetly = 1
chide = 1
singleness = 1
parts = 1
bear: = 1
mark = 1
string = 1
husband = 1
strikes = 1
mutual = 1
ordering; = 1
sire = 1
happy = 1
pleasing = 1
note = 1
sing: = 1
speechless = 1
song = 1
many = 2
seeming = 1
sings = 1
'thou = 1
wilt = 2
prove = 2
none' = 1
9 = 1
fear = 1
wet = 1
widow's = 1
consum'st = 1
life = 1
ah = 1
issueless = 1
hap = 1
wail = 1
makeless = 1
wife = 1
widow = 2
weep = 1
hast = 1
behind = 1
private = 1
well = 1
may = 3
keep = 1
children's = 1
husband's = 1
shape = 1
mind: = 1
unthrift = 1
shifts = 1
enjoys = 1
it; = 1
hath = 1
end = 1
kept = 1
user = 1
destroys = 1
it: = 1
love = 4
toward = 1
others = 1
bosom = 1
sits = 1
himself = 1
such = 1
murd'rous = 2
commits = 1
10 = 1
deny = 1
bear'st = 1
any = 1
unprovident = 1
grant = 1
beloved = 1
none = 1
most = 1
evident: = 1
possessed = 1
hate = 2
'gainst = 1
stick'st = 1
conspire = 1
seeking = 1
roof = 1
ruinate = 1
chief = 1
desire: = 1
o = 1
change = 2
thought = 1
i = 1
mind = 1
fairer = 1
lodged = 1
presence = 1
kind = 1
at = 1
least = 1
kindhearted = 1
me = 1
--------------------------------------------------
The list with these words removed: 'a', 'an', 'to', 'in', 'at','for', 'and' , 'nor', 'but', 'or', 'yet', 'so'
['1609', 'THE', 'SONNETS', 'by', 'William', 'Shakespeare', '1', 'From', 'fairest', 'creatures', 'we', 'desire', 'increase', 'That', 'thereby', "beauty's", 'rose', 'might', 'never', 'die', 'as', 'the', 'riper', 'should', 'by', 'time', 'decease', 'His', 'tender', 'heir', 'might', 'bear', 'his', 'memory:', 'thou', 'contracted', 'thine', 'own', 'bright', 'eyes', "Feed'st", 'thy', "light's", 'flame', 'with', 'selfsubstantial', 'fuel', 'Making', 'famine', 'where', 'abundance', 'lies', 'Thy', 'self', 'thy', 'foe', 'thy', 'sweet', 'self', 'too', 'cruel:', 'Thou', 'that', 'art', 'now', 'the', "world's", 'fresh', 'ornament', 'only', 'herald', 'the', 
'gaudy', 'spring', 'Within', 'thine', 'own', 'bud', 'buriest', 'thy', 'content', 'tender', 'churl', "mak'st", 'waste', 'niggarding:', 'Pity', 'the', 'world', 'else', 'this', 'glutton', 'be', 'eat', 'the', "world's", 'due', 'by', 'the', 'grave', 'thee', '2', 'When', 'forty', 'winters', 'shall', 'besiege', 'thy', 'brow', 'dig', 'deep', 'trenches', 'thy', "beauty's", 'field', 'Thy', "youth's", 'proud', 'livery', 'gazed', 'on', 'now', 'Will', 'be', 'tattered', 'weed', 'of', 'small', 'worth', 'held:', 'Then', 'being', 'asked', 'where', 'all', 'thy', 'beauty', 'lies', 'Where', 'all', 'the', 'treasure', 'of', 'thy', 'lusty', 'days;', 'say', 'within', 'thine', 'own', 'deep', 'sunken', 'eyes', 'Were', 'alleating', 'shame', 'thriftless', 'praise', 'How', 'much', 'more', 'praise', 'deserved', 'thy', "beauty's", 'use', 'If', 'thou', 'couldst', 'answer', "'This", 'fair', 'child', 'of', 'mine', 'Shall', 'sum', 'my', 'count', 'make', 'my', 'old', "excuse'", 'Proving', 'his', 'beauty', 'by', 'succession', 'thine', 'This', 'were', 'be', 'new', 'made', 'when', 'thou', 'art', 'old', 'see', 'thy', 'blood', 'warm', 'when', 'thou', "feel'st", 'it', 'cold', '3', 'Look', 'thy', 'glass', 'tell', 'the', 'face', 'thou', 'viewest', 'Now', 'is', 'the', 'time', 'that', 'face', 'should', 'form', 'another', 'Whose', 'fresh', 'repair', 'if', 'now', 'thou', 'not', 'renewest', 'Thou', 'dost', 'beguile', 'the', 'world', 'unbless', 'some', 'mother', 'where', 'is', 'she', 'fair', 'whose', 'uneared', 'womb', 'Disdains', 'the', 'tillage', 'of', 'thy', 'husbandry', 'who', 'is', 'he', 'fond', 'will', 'be', 'the', 'tomb', 'Of', 'his', 
'selflove', 'stop', 'posterity', 'Thou', 'art', 'thy', "mother's", 'glass', 'she', 'thee', 'Calls', 'back', 'the', 'lovely', 'April', 'of', 'her', 'prime', 'thou', 'through', 'windows', 'of', 'thine', 'age', 'shalt', 'see', 'Despite', 'of', 'wrinkles', 'this', 'thy', 'golden', 'time', 'if', 'thou', 'live', 'remembered', 'not', 'be', 'Die', 'single', 'thine', 'image', 'dies', 'with', 'thee', '4', 'Unthrifty', 'loveliness', 'why', 'dost', 'thou', 'spend', 'Upon', 'thy', 'self', 'thy', "beauty's", 'legacy', "Nature's", 'bequest', 'gives', 'nothing', 'doth', 'lend', 'being', 'frank', 'she', 'lends', 'those', 'are', 'free:', 'Then', 'beauteous', 'niggard', 'why', 'dost', 'thou', 'abuse', 'The', 'bounteous', 'largess', 'given', 'thee', 'give', 'Profitless', 'usurer', 'why', 'dost', 'thou', 'use', 'great', 'sum', 'of', 'sums', 'canst', 'not', 'live', 'having', 'traffic', 'with', 'thy', 'self', 'alone', 'Thou', 'of', 'thy', 'self', 'thy', 'sweet', 'self', 'dost', 'deceive', 'Then', 'how', 'when', 'nature', 'calls', 'thee', 'be', 'gone', 'What', 'acceptable', 'audit', 'canst', 'thou', 'leave', 'Thy', 'unused', 'beauty', 'must', 'be', 'tombed', 'with', 'thee', 'Which', 'used', 'lives', "th'", 'executor', 'be', '5', 'Those', 'hours', 'that', 'with', 'gentle', 'work', 'did', 'frame', 'The', 'lovely', 'gaze', 'where', 'every', 'eye', 'doth', 'dwell', 'Will', 'play', 'the', 'tyrants', 'the', 'very', 'same', 'that', 'unfair', 'which', 'fairly', 'doth', 'excel:', 'neverresting', 'time', 'leads', 'summer', 'on', 'hideous', 'winter', 'confounds', 'him', 'there', 'Sap', 'checked', 'with', 'frost', 'lusty', 'leaves', 'quite', 'gone', 'Beauty', "o'ersnowed", 'bareness', 'every', 'where:', 'Then', 'were', 'not', "summer's", 'distillation', 'left', 'liquid', 'prisoner', 'pent', 'walls', 'of', 'glass', "Beauty's", 'effect', 'with', 'beauty', 'were', 'bereft', 'it', 'no', 'remembrance', 'what', 'it', 'was', 'flowers', 'distilled', 'though', 'they', 'with', 'winter', 'meet', 'Leese', 'their', 'show', 'their', 'substance', 'still', 'lives', 'sweet', '6', 'Then', 'let', 'not', "winter's", 'ragged', 'hand', 'deface', 'thee', 'thy', 'summer', 'ere', 'thou', 'be', 'distilled:', 'Make', 'sweet', 'some', 'vial;', 'treasure', 'thou', 'some', 'place', 'With', "beauty's", 'treasure', 'ere', 'it', 'be', 'selfkilled:', 'That', 'use', 'is', 'not', 'forbidden', 'usury', 'Which', 'happies', 'those', 'that', 'pay', 'the', 'willing', 'loan;', "That's", 'thy', 'self', 'breed', 'another', 'thee', 'ten', 'times', 'happier', 'be', 'it', 'ten', 'one', 'Ten', 'times', 'thy', 'self', 'were', 'happier', 'than', 'thou', 'art', 'If', 'ten', 'of', 'thine', 'ten', 'times', 'refigured', 'thee:', 'Then', 'what', 'could', 'death', 'do', 'if', 'thou', 'shouldst', 'depart', 'Leaving', 'thee', 'living', 'posterity', 'Be', 'not', 'selfwilled', 'thou', 'art', 'much', 'too', 'fair', 'be', "death's", 'conquest', 'make', 'worms', 'thine', 'heir', '7', 'Lo', 'the', 'orient', 'when', 'the', 'gracious', 'light', 'Lifts', 'up', 'his', 'burning', 'head', 'each', 'under', 'eye', 'Doth', 'homage', 'his', 'newappearing', 'sight', 'Serving', 'with', 'looks', 'his', 'sacred', 'majesty', 'having', 'climbed', 'the', 'steepup', 'heavenly', 'hill', 'Resembling', 'strong', 'youth', 'his', 'middle', 'age', 'mortal', 'looks', 'adore', 'his', 'beauty', 'still', 'Attending', 'on', 'his', 'golden', 'pilgrimage:', 'when', 'from', 'highmost', 'pitch', 'with', 'weary', 'car', 'Like', 'feeble', 'age', 'he', 'reeleth', 'from', 'the', 'day', 'The', 'eyes', '(fore', 'duteous)', 'now', 'converted', 'are', 'From', 'his', 'low', 'tract', 'look', 'another', 'way:', 'thou', 'thy', 'self', 'outgoing', 'thy', 'noon:', 'Unlooked', 'on', 'diest', 'unless', 'thou', 'get', 'son', '8', 'Music', 'hear', 'why', "hear'st", 'thou', 'music', 'sadly', 'Sweets', 'with', 'sweets', 'war', 'not', 'joy', 'delights', 'joy:', 'Why', "lov'st", 'thou', 'that', 'which', 'thou', "receiv'st", 'not', 'gladly', 'else', "receiv'st", 'with', 'pleasure', 'thine', 'annoy', 'If', 'the', 'true', 'concord', 'of', 'welltuned', 'sounds', 'By', 'unions', 'married', 'do', 'offend', 'thine', 'ear', 'They', 'do', 'sweetly', 'chide', 'thee', 'who', 'confounds', 'singleness', 'the', 'parts', 'that', 'thou', 'shouldst', 'bear:', 'Mark', 'how', 'one', 'string', 'sweet', 'husband', 'another', 'Strikes', 'each', 'each', 'by', 'mutual', 'ordering;', 'Resembling', 'sire', 'child', 'happy', 'mother', 'Who', 'all', 'one', 'one', 'pleasing', 'note', 'do', 'sing:', 'Whose', 'speechless', 'song', 'being', 'many', 'seeming', 'one', 'Sings', 'this', 'thee', "'Thou", 'single', 'wilt', 'prove', "none'", '9', 'Is', 'it', 'fear', 'wet', "widow's", 'eye', 'That', 'thou', "consum'st", 'thy', 'self', 'single', 'life', 'Ah', 'if', 'thou', 'issueless', 'shalt', 'hap', 'die', 'The', 'world', 'will', 'wail', 'thee', 'like', 'makeless', 'wife', 'The', 'world', 'will', 'be', 'thy', 'widow', 'still', 'weep', 'That', 'thou', 'no', 'form', 'of', 'thee', 'hast', 'left', 'behind', 'When', 'every', 'private', 'widow', 'well', 'may', 'keep', 'By', "children's", 'eyes', 'her', "husband's", 'shape', 'mind:', 'Look', 'what', 'unthrift', 'the', 'world', 'doth', 'spend', 'Shifts', 'his', 'place', 'still', 'the', 'world', 'enjoys', 'it;', "beauty's", 'waste', 'hath', 'the', 'world', 'end', 'kept', 'unused', 'the', 'user', 'destroys', 'it:', 'No', 'love', 'toward', 'others', 'that', 'bosom', 'sits', 'That', 'on', 'himself', 'such', "murd'rous", 'shame', 'commits', '10', 'shame', 'deny', 'that', 'thou', "bear'st", 'love', 'any', 'Who', 'thy', 'self', 'art', 'unprovident', 'Grant', 'if', 'thou', 'wilt', 'thou', 'art', 'beloved', 'of', 'many', 'that', 'thou', 'none', "lov'st", 'is', 'most', 'evident:', 'thou', 'art', 'possessed', 'with', "murd'rous", 'hate', 'That', "'gainst", 'thy', 'self', 'thou', "stick'st", 'not', 'conspire', 'Seeking', 'that', 'beauteous', 'roof', 'ruinate', 'Which', 'repair', 'should', 'be', 'thy', 'chief', 'desire:', 'O', 'change', 'thy', 'thought', 'that', 'I', 'may', 'change', 'my', 'mind', 'Shall', 'hate', 'be', 'fairer', 'lodged', 'than', 'gentle', 'love', 'Be', 'as', 'thy', 'presence', 'is', 'gracious', 'kind', 'thy', 'self', 'least', 'kindhearted', 'prove', 'Make', 'thee', 'another', 'self', 'love', 'of', 'me', 'That', 'beauty', 'still', 'may', 'live', 'thine', 'thee']
--------------------------------------------------

'This 'Thou 'gainst (fore 1 10 1609 2 3 4 5 6 7 8 9 Ah April Attending Be Be

Beauty Beauty's By By Calls Despite Die Disdains Doth Feed'st From From Grant His How I If If If Is

Leaving Leese Lifts Like Lo Look Look Make Make Making Mark Music Nature's No Now O Of Pity Profitless Proving

Resembling Resembling SONNETS Sap Seeking Serving Shakespeare Shall Shall Shifts Sings Strikes Sweets THE Ten That That That That That

That That That's The The The The The Then Then Then Then Then Then They This Those Thou Thou Thou

--------------------------------------------------
Removing: 'a', 'an', 'to', 'in', 'at','for', 'and' , 'nor', 'but', 'or', 'yet', 'so'
Printing out 50 most frequent words in form of tuples
(thou,36) (thy,35) (the,32) (that,19) (be,17) (of,16) (thee,15) (with,14) (self,14) (his,12)

(thine,11) (not,10) (art,8) (if,8) (by,7) (beauty's,7) (world,7) (when,7) (beauty,7) (is,7)

(then,6) (it,6) (where,5) (sweet,5) (now,5) (on,5) (will,5) (were,5) (another,5) (dost,5)

(why,5) (doth,5) (which,5) (still,5) (ten,5) (one,5) (from,4) (time,4) (eyes,4) (this,4)

(make,4) (who,4) (what,4) (do,4) (love,4) (die,3) (should,3) (own,3) (shall,3) (being,3)

--------------------------------------------------
Task 2:
Printing the first tuple list and dictionary using the list given in instructions:
List of (name, score) tuples: [('Andy', 88), ('Ben', 92), ('Cathy', 85), ('Dave', 76), ('Edward', 85), ('Fanny', 96), ('George', 77), ('Hana', 82), ('Jess', 90), 
('Karen', 72), ('Nancy', 98), ('Pedro', 82)]
Dictionary with name as key and score as value: {'Andy': 88, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 
'Karen': 72, 'Nancy': 98, 'Pedro': 82}

--------------------------------------------------
Change score of Cathy to 0
Done
{'Andy': 88, 'Ben': 92, 'Cathy': 0, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}
Showing the fail update message by trying to change the score of 'Sally'
Name is not in the dictionary, failed to update
--------------------------------------------------
Class Average: 78.16666666666667
Standard Deviation: 24.781825777954474
Highest Scorer: ('Nancy', 98)
--------------------------------------------------
Printing the first tuple list and dictionary using the list I created
List of (name, score) tuples: [('Sam', 65), ('Dean', 70), ('Crowley', 75), ('Bobby', 77), ('Ruby', 83), ('Castiel', 82), ('Kate', 55), ('Sarah', 100), ('Kia', 85), ('Sophia', 90), ('Mia', 80), ('Cade', 45), ('Kevin', 73), ('Tony', 22), ('Bella', 50), ('Cory', 88), ('Star', 95), ('Ellen', 100), ('Jo', 40), ('Jack', 76)]    
Dictionary with name as key and score as value: {'Sam': 65, 'Dean': 70, 'Crowley': 75, 'Bobby': 77, 'Ruby': 83, 'Castiel': 82, 'Kate': 55, 'Sarah': 100, 'Kia': 85, 'Sophia': 90, 'Mia': 80, 'Cade': 45, 'Kevin': 73, 'Tony': 22, 'Bella': 50, 'Cory': 88, 'Star': 95, 'Ellen': 100, 'Jo': 40, 'Jack': 76}
--------------------------------------------------
Change score of Crowley to 0
Done
{'Sam': 65, 'Dean': 70, 'Crowley': 0, 'Bobby': 77, 'Ruby': 83, 'Castiel': 82, 'Kate': 55, 'Sarah': 100, 'Kia': 85, 'Sophia': 90, 'Mia': 80, 'Cade': 45, 'Kevin': 73, 'Tony': 22, 'Bella': 50, 'Cory': 88, 'Star': 95, 'Ellen': 100, 'Jo': 40, 'Jack': 76}
Showing the fail update message by trying to change the score of 'Sally'
Name is not in the dictionary, failed to update
--------------------------------------------------
Class Average: 68.8
Standard Deviation: 25.720808696462093
Highest Scorer: ('Sarah', 100)
--------------------------------------------------
"""