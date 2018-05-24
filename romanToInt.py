def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        len_roman = len(s)
        final_sum = 0

        for i in range(len_roman):
            if s[i] not in roman_dict:
                return "Please use only roman charcters"
            else:
                
                if s[i] == 'I':
                    if i+1 != len_roman and (s[i+1] == 'V' or s[i+1] == 'X'):
                        final_sum = final_sum - roman_dict[s[i]]
                    else:
                        final_sum = final_sum + roman_dict[s[i]]
                elif s[i] == 'X':
                    if i+1 != len_roman and (s[i+1] == 'L' or s[i+1] == 'C'):
                        final_sum = final_sum - roman_dict[s[i]]
                    else:
                        final_sum = final_sum + roman_dict[s[i]]
                elif s[i] == 'C':
                    if i+1 != len_roman and (s[i+1] == 'D' or s[i+1] == 'M'):
                        final_sum = final_sum - roman_dict[s[i]]
                    else:
                        final_sum = final_sum + roman_dict[s[i]]
                else:
                    final_sum = final_sum + roman_dict[s[i]]
        return final_sum

c = 'Y'
while c != 'N':
    
    print("Enter the number roman number: ")
    s = input()
    print(romanToInt(s))
    print("Press Y for continue and N for exit")
    c = (input().upper())