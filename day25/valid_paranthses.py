import re


class Solution:
    def isValid(self, s: str) -> bool:
        for i in s:
            s = re.sub("\(\)|\[\]|\{\}", "", s)
        return s == ""
