class wordChecker(object):
    def __init__(self, limitToCharset, fontChars, requiredLetters, requiredGroups, bannedLetters, banRepetitions, minLength, maxLength):
        self.limitToCharset = limitToCharset
        self.fontChars = fontChars
        self.requiredLetters = requiredLetters
        self.requiredGroups = requiredGroups
        self.bannedLetters = bannedLetters
        self.banRepetitions = banRepetitions
        self.minLength = minLength
        self.maxLength = maxLength

    def excludedAll(self, word, charList):
        for c in charList:
            if c in word:
                return False
        return True

    def includedAll(self, word, charList):
        for c in charList:
            if not c in word:
                return False
        return True

    def includedAny(self, word, charList):
        if len(charList):
            for c in charList:
                if c in word:
                    return True
            return False
        else:
            return True

    def includedGroups(self, word, charListList):
        for charList in charListList:
            if not self.includedAny(word, charList):
                return False
        return True

    def limitedTo(self, word, charList, condition):
        if condition:
            for c in word:
                if not c in charList:
                    return False
            return True
        else:
            return True

    def uniqueChars(self, word, condition):
        if condition:
            wordChars = []
            for c in word:
                if c in wordChars:
                    return False
                wordChars.append(c)
            return True
        else:
            return True

    def checkLength(self, word):
        return self.minLength <= len(word) <= self.maxLength

    def checkExisting(self, word, outputList):
        return not word in outputList

    def checkWord(self, word, outputWords):
        requirements = [
            (self.checkExisting, [outputWords]),    
            (self.limitedTo, [self.fontChars, self.limitToCharset]),
            (self.checkLength, []),
            (self.includedAll, [self.requiredLetters]),
            (self.includedGroups, [self.requiredGroups]),
            (self.excludedAll, [self.bannedLetters]),
            (self.uniqueChars, [self.banRepetitions]),
        ]
        for reqFunc, args in requirements:
            if not reqFunc(word, *args):
                return False
        return True