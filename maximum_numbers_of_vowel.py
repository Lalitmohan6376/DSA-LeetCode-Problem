#1456. Maximum Number of Vowels in a Substring of Given Length

def vowel(s, k):
    count = 0
    vowel = "aeiou"
    max_vowel = 0

    for i in range(k):
        if s[i] in vowel:
            count+=1

        max_vowel = count

        for i in range(k,len(s)):
            if s[i-k] in vowel:
                count-=1
            
            if s[i] in vowel:
                count+=1

            max_vowel = max(max_vowel, count)
    return max_vowel
        

        

print(vowel("aeiou", 2))


    #     for j in sliding:
    #         if j in vowel:
    #             count+=1
    #     max_vowel = max(max_vowel, count) #2
    #     count= 0
    # return max_vowel
