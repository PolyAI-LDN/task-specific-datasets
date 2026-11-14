import pathlib
import unittest

from nlupp.data_loader import DataLoader


class FoldKeyTest(unittest.TestCase):
    def test_fold_keys_are_integers_in_every_regime(self):
        loader = DataLoader(pathlib.Path(__file__).parent / "data")
        for regime, count in (("low", 20), ("mid", 10), ("large", 10)):
            folds = loader.get_data_for_experiment("banking", regime)
            self.assertEqual(list(folds), list(range(count)))
            self.assertTrue(all(type(key) is int for key in folds))
            self.assertTrue(all(isinstance(key, int) for key in folds))


if __name__ == "__main__":
    unittest.main()
