class CP2Complexity:
    @staticmethod
    def average(arr: list[int]) -> int:
        s = 0              # O(1)
        if len(arr) == 0:  # { O(1)
            return 0       # }
        for x in arr:      # { O(n)
            s += x         # }  |_ O(1) = O(n)
        return s           #

    def __repr__(self):
        return f"Class: CPComplexity"
