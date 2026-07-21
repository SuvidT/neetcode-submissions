class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcounts = [0] * 26
        for char in chars:
            charcounts[ord(char) - ord('a')] += 1

        totalvalidchars = 0

        for word in words:
            is_good = True
            wordcounts = [0] * 26
            word_len = 0

            for char in word:
                word_len += 1
                idx = ord(char) - ord('a')
                wordcounts[idx] += 1

                if wordcounts[idx] > charcounts[idx]:
                    is_good = False
                    break

            if is_good:
                totalvalidchars += word_len

        return totalvalidchars