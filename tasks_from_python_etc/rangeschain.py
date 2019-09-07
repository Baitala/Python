import unittest
from itertools import chain
from typing import List, Iterable, Optional, Generator, TypeVar, Type


RangesChainType = TypeVar('RangesChainType', bound='RangesChain')


class RangesChain:
    def __init__(self, ranges: Iterable[range]) -> None:
        self._ranges: Iterable[range] = ranges

    @classmethod
    def from_iterable(
        cls: Type[RangesChainType],
        iterable: Iterable[int],
    ) -> RangesChainType:
        ranges: List[range] = []

        start: Optional[int] = None
        prev: Optional[int] = None
        current: Optional[int] = None
        for current in iterable:
            if start is None or prev is None:
                start = current
            elif current - 1 != prev:
                ranges.append(range(start, prev + 1))
                start = current
            prev = current

        if current is not None and start is not None:
            ranges.append(range(start, current + 1))

        return cls(ranges)

    def __iter__(self) -> Generator[int, None, None]:
        yield from chain(*self._ranges)


class RangesChainTestCase(unittest.TestCase):
    def test_from_iterable__empty(self):
        ranges_chain = RangesChain.from_iterable([])
        self.assertListEqual(list(ranges_chain._ranges), [])

    def test_from_iterable(self):
        ranges_chain = RangesChain.from_iterable([
            1, 2, 3,
            100,
            5, 6, 7,
        ])

        ranges = list(ranges_chain._ranges)
        self.assertEqual(len(ranges), 3)
        self.assertListEqual(list(ranges[0]), [1, 2, 3])
        self.assertListEqual(list(ranges[1]), [100])
        self.assertListEqual(list(ranges[2]), [5, 6, 7])

    def test_iter(self):
        self.assertListEqual(
            list(RangesChain([range(2), range(3)])),
            [0, 1, 0, 1, 2],
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
