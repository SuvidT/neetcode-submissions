class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sen = list(senate)

        r = 0
        d = 0

        i = -1
        while True:
            i += 1
            i %= len(sen)

            if sen[i] == 'R':
                if d > 0:
                    sen[i] = '_'
                else:
                    r += 1
            
            if sen[i] == 'D':
                if r > 0:
                    sen[i] = '_'
                else:
                    d += 1
            
            if sen.count('R') == 0:
                return 'Dire'
            if sen.count('D') == 0:
                return 'Radiant'