import unittest
from src.randomTree import RandomTree, functions


class TestRandomTree(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_add_child(self):
        root = RandomTree("root")
        child = RandomTree("child")
        root.add_child(child)

        self.assertEqual(root.get_children(), [child])

    def test_exec_function_with_callable_content(self):
        tree = RandomTree(functions.arithmetic_average)
        result = tree.exec_function([1, 2, 3])

        self.assertEqual(result, 2.0)

    def test_exec_function_with_non_callable_content(self):
        tree = RandomTree(42)

        with self.assertRaises(TypeError):
            tree.exec_function()

    def test_serialize_and_deserialize_tree(self):
        tree = RandomTree("root")
        child1 = RandomTree("child1")
        child2 = RandomTree("child2")
        tree.add_child(child1)
        tree.add_child(child2)


        tree.serialize()


        deserialized_trees = RandomTree.deserialize_all()

        self.assertEqual(len(deserialized_trees), 1)
        deserialized_tree = deserialized_trees[0]
        self.assertEqual(deserialized_tree.get_content(), "root")
        self.assertEqual(len(deserialized_tree.get_children()), 2)
        self.assertEqual(deserialized_tree.get_children()[0].get_content(), "child1")
        self.assertEqual(deserialized_tree.get_children()[1].get_content(), "child2")

    def test_remove_last_level(self):
        root = RandomTree("root")
        child1 = RandomTree("child1")
        child2 = RandomTree("child2")
        root.add_child(child1)
        root.add_child(child2)


        root.remove_last_level()

        self.assertEqual(root.get_children(), [])

    def test_generate_random_tree(self):
        random_tree = RandomTree.generate_random_tree()

        self.assertIsInstance(random_tree, RandomTree)

    def test_get_tree_result(self):
        root = RandomTree("arithmetic_average")
        child1 = RandomTree(2.0)
        child2 = RandomTree(3.0)
        root.add_child(child1)
        root.add_child(child2)

        result = root.get_tree_result()

        self.assertEqual(result, 2.5)


if __name__ == '__main__':
    unittest.main()