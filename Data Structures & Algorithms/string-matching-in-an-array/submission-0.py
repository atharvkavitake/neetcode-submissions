class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []

        for word in words:
            for other in words:
                if word != other and word in other:
                    answer.append(word)
                    break

        return answer