from difflib import SequenceMatcher

ALLOWED_MATCH_LEN = 5


def longest_substring_mine(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 == 0 or len2 == 0:
        return 0, 0

    current_longest_match_len = ALLOWED_MATCH_LEN
    total_match_len = 0

    while current_longest_match_len >= ALLOWED_MATCH_LEN:
        seqMatch = SequenceMatcher(None, str1, str2)
        match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
        if match.size != 0:
            longest = str(str1[match.a: match.a + match.size])
            print(longest)
            current_longest_match_len = len(longest.strip())
            total_match_len += current_longest_match_len
            str1 = str1.replace(longest, '')
            str2 = str2.replace(longest, '')
        else:
            current_longest_match_len = 0

    print('str1 ratio', total_match_len / len1)
    print('str2 ratio', total_match_len / len2)

    return (total_match_len*100) / len1, (total_match_len*100) / len2


def longest_substring(str1, str2):
    seqMatch = SequenceMatcher(None, str1, str2)
    print(seqMatch.quick_ratio())
    print(seqMatch.real_quick_ratio())

# if __name__ == "__main__":
#     file1 = open('input1', "r")
#     strx = file1.read()
#
#     file2 = open('input2', "r")
#     stry = file2.read()
#     longest_substring(strx, stry)
#     file1 = open('input1', "r")
#     strx = file1.read()
#
#     file2 = open('input2', "r")
#     stry = file2.read()
#     (x, y) = longest_substring_mine(strx, stry)
