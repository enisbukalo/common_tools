from typing import Any


class MergeSort:
    def __init__(self) -> None:
        """Merge sorting object for sorting as list of Integers.

        Ability to override _compare to compare anything you wish."""
        pass

    def _merge(self, left: list[Any], right: list[Any]) -> list[Any]:
        """
        Merge two lists in sorted order from lowest to highest.

        Args:
            left (list[Any]): The first list to merge.
            right (list[Any]): The second list to merge.

        Returns:
            list[Any]: The merged list in sorted order from lowest to highest.
        """
        result = []

        while len(left) != 0 and len(right) != 0:
            if left <= right:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while len(left) != 0:
            result.append(left.pop(0))

        while len(right) != 0:
            result.append(right.pop(0))

        return result

    def merge_sort(self, items: list[Any]) -> list[Any]:
        """
        Sorts a list of items using the merge sort algorithm.

        Parameters:
            items (list[Any]): The list of items to be sorted.

        Returns:
            list[Any]: The sorted list of items.
        """
        if len(items) <= 1:
            return items

        mid_point = len(items) // 2
        L = items[:mid_point]
        R = items[mid_point:]

        return self._merge(self.merge_sort(L), self.merge_sort(R))
