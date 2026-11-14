import copy
import pathlib
import unittest

from nlupp.data_loader import DataLoader


class CrossDomainIsolationTest(unittest.TestCase):
    def test_cross_domain_loading_preserves_original_annotations(self):
        loader = DataLoader(pathlib.Path(__file__).parent / "data")
        original = copy.deepcopy(loader._data)
        for domain in ("banking-hotels", "hotels-banking"):
            experiment = loader.get_data_for_experiment(domain)[0]
            self.assertEqual(loader._data, original)
            for examples in experiment.values():
                for example in examples:
                    for intent in example.get("intents", []):
                        self.assertIn("general", loader.ontology["intents"][intent]["domain"])
                    for slot in example.get("slots", {}):
                        self.assertIn("general", loader.ontology["slots"][slot]["domain"])
        self.assertEqual(loader._data, original)


if __name__ == "__main__":
    unittest.main()
