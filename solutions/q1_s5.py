def longest_palindromic_substring(s):
    n = len(s)
    max_len = 0 # stores the length of the longest palindromic substring
    result = "" # stores the longest palindromic substring
    
    for i in range(n):
        # Odd length palindrome
        l, r = i, i # left and right pointers
        while l >= 0 and r < n and s[l] == s[r]: # while the pointers are within the bounds of the string and the characters at the pointers are equal
            
            # if the length of the current palindromic substring is greater than the maximum length found so far
            if (r - l + 1) > max_len:
                
                # update the maximum length
                max_len = r - l + 1

                # update the longest palindromic substring
                result = s[l:r+1]

            # move the left pointer to the left
            l -= 1
            
            # move the right pointer to the right
            r += 1
            
        # Even length palindrome
        l, r = i, i + 1 # l and r are the left and right pointers
        while l >= 0 and r < n and s[l] == s[r]: # while the pointers are within the bounds of the string and the characters at the pointers are equal
            
            # if the length of the current palindromic substring is greater than the maximum length found so far
            if (r - l + 1) > max_len:
                
                # update the maximum length
                max_len = r - l + 1

                # update the longest palindromic substring
                result = s[l:r+1]

            # move the left pointer to the left
            l -= 1
            
            # move the right pointer to the right
            r += 1

    if max_len < 2:
        return ""  # If no palindromic substring of length >= 2

    return result