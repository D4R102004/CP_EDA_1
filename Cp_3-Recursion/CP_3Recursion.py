

class CP3:
    @staticmethod
    def minimum(pos: int, elements: list[int]):
        if pos == len(elements):
            return float('inf')
        return min(elements[pos], CP3.minimum(pos + 1, elements))