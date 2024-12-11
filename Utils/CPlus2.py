from typing import List


class CPlus2:
    @staticmethod
    def resize(vector: List, new_size: int, default):
        current_size = len(vector)

        if new_size > current_size:
            vector.extend([default] * (new_size - current_size))
        elif new_size < current_size:
            vector[:] = vector[:new_size]
