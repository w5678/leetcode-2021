"""
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

思路：
绕不开先对原数组进行排序
精髓在于， sorted(words,key=lambda x: (-len(x),x))
这种可以排序出长度越长对排在前面，若长度相等值越小的排在前面
"""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ""
        set_words=set(words)
        for key in sorted(words,key=lambda x: (-len(x),x)):
            idx=len(key)-1
            while idx>0:
                if key[:idx] not in set_words:
                    break
                idx-=1
            else:
                return key
        return ""



if __name__ == '__main__':
    # words=["t","ti","tig","tige","tiger","e","en","eng","engl","engli","englis","english","h","hi","his","hist","histo","histor","history"]
    # words=["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
    words=["gbra","jy","pl","zn","gb","j","jyh","jyhm","plr","znicn","p","gbr","zni","znic","aq"]
    s=Solution().longestWord(words)
    print(s)
