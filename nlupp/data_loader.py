"""Methods for loading the different data setups"""
import json
import os

_LOW, _MID, _LARGE = "low", "mid", "large"  # Data regimes
_BANKING, _HOTELS, _ALL, _HOTELS_BANKING, _BANKING_HOTELS = (
    "banking", "hotels", "all", "hotels-banking", "banking-hotels")  # Domains


class DataLoader:
    def __init__(self, data_dir):
        """Loader for the NLU++ data

        Args:
            data_dir: directory with the NLU++ data (i.e. https://github.com/
            PolyAI-LDN/task-specific-datasets/tree/master/nlupp/data)
        """
        self._data = self._read_data(data_dir)
        with open(os.path.join(data_dir, f"ontology.json")) as f:
            self.ontology = json.load(f)

    @staticmethod
    def _read_data(data_dir):
        data = {}
        for domain in [_BANKING, _HOTELS]:
            data[domain] = {}
            for fold in range(20):
                with open(os.path.join(
                        data_dir, domain, f"fold{fold}.json")) as f:
                    data[domain][fold] = json.load(f)
        return data

    def _get_cross_domain_data(self, source_domain, target_domain):
        train_examples, test_examples = [], []
        for fold_i in range(20):
            train_examples += self._data[source_domain][fold_i]
            test_examples += self._data[target_domain][fold_i]

        # delete non-generic slots and values
        generic_intents = []
        generic_slots = []
        for intent, metadata in self.ontology["intents"].items():
            if "general" in metadata["domain"]:
                generic_intents.append(intent)
        for slot, metadata in self.ontology["slots"].items():
            if "general" in metadata["domain"]:
                generic_slots.append(slot)
        for example in train_examples + test_examples:
            if "intents" in example:
                example["intents"] = [
                    intent for intent in example["intents"]
                    if intent in generic_intents]
            if "slots" in example:
                example["slots"] = {
                    slot: data for slot, data in example["slots"].items()
                    if slot in generic_slots}

        experiment_data = {
            0: {"train": train_examples,
                "test": test_examples}
        }  # keeping the same structure as other experiments, even if there is
           # only 1 fold
        return experiment_data

    def get_data_for_experiment(self, domain, regime=None):
        """Load the data folds following the structure used in the experiments

        https://arxiv.org/pdf/2204.13021.pdf

        Args:
            domain: (str) 'banking', 'hotels', 'all', 'hotels-banking'
                or 'banking-hotels
            regime: (str) 'low', 'mid' or 'large' (or None for cross domain
                experiments)

        Returns:
            Dict with the folds ready for the experiment
        """
        if domain in [_HOTELS_BANKING, _BANKING_HOTELS]:
            source_domain, target_domain = domain.split("-")
            return self._get_cross_domain_data(source_domain, target_domain)

        assert regime in [_LOW, _MID, _LARGE], (
            "regime must be 'low', 'mid', 'large'")
        assert domain in [_BANKING, _HOTELS, _ALL], (
            "regime must be 'banking', 'hotels', 'all', 'hotels-banking' or "
            "'banking-hotels'")
        if regime == _LOW:
            folds = range(20)
        else:
            folds = range(0, 20, 2)
        experiment_data = {}
        for fold_i in folds:
            if regime == _LOW:
                train_folds = [fold_i]
            elif regime == _MID:
                train_folds = [fold_i, fold_i + 1]
            else:
                train_folds = [j for j in range(20)
                               if j not in [fold_i, fold_i+1]]
            test_folds = [j for j in range(20) if j not in train_folds]
            train_examples, test_examples = [], []
            for fold_j in train_folds:
                if domain in [_BANKING, _ALL]:
                    train_examples += self._data[_BANKING][fold_j]
                if domain in [_HOTELS, _ALL]:
                    train_examples += self._data[_HOTELS][fold_j]
            for fold_j in test_folds:
                if domain in [_BANKING, _ALL]:
                    test_examples += self._data[_BANKING][fold_j]
                if domain in [_HOTELS, _ALL]:
                    test_examples += self._data[_HOTELS][fold_j]
            fold_key = fold_i if regime == _LOW else fold_i / 2
            experiment_data[fold_key] = {"train": train_examples,
                                         "test": test_examples}
        return experiment_data


