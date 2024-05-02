import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    _tree: Tree
    def setUp(self) -> None:
        super().setUp()
        self._tree = Tree()
        self._tree.add(3)
        self._tree.add(4)
        self._tree.add(0)
        self._tree.add(8)
        self._tree.add(2)

    def test__find1(self):
        self.assertTrue((find3 := self._tree.find(3)) and find3.data == 3)
        self.assertTrue((find4 := self._tree.find(4)) is not None and find4.data == 4)
        self.assertTrue((find0 := self._tree.find(0)) is not None and find0.data == 0)
        self.assertTrue((find8 := self._tree.find(8)) is not None and find8.data == 8)
        self.assertTrue((find2 := self._tree.find(2)) is not None and find2.data == 2)

    def test__find2(self):
        self.assertTrue(self._tree.find(1) is None)
        self.assertTrue(self._tree.find(5) is None)

