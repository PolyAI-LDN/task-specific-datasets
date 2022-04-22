[![PolyAI](polyai-logo.png)](https://poly-ai.com/)

# NLU++

*A Multi-Label, Slot-Rich, Generalisable Dataset for Natural Language Understanding in Task-Oriented Dialogue*


This dataset presents a challenging evaluation environment for dialogue NLU models. It is divided in 2 domains, 
_banking_ and _hotels_, and provides high quality examples combining a large amount of _multi-label_ intents and slots. 
More details on the dataset can be found in [our publication](https://www.youtube.com/watch?v=dQw4w9WgXcQ). 

| Domain  | Number of examples               |   Number of intents   | Number of slots  |
| ---            |   --- | --- |--- |
| BANKING | 2,071 | 48 | 13 |
| HOTELS | 1,009  | 40 | 14 |
| ALL | 3,080 | 62 | 17 |



|          Example Query      | Intents      | Slots (values)      |
| ---            |   --- |--- |
| I want to change my restaurant reservation| change, booking, room | --- |
| I am trying to make a transfer but it doesn’t let me | make, transfer_payment, not_working | --- |
| Why can’t I amend my booking on tuesday? | why, change, booking, not_working | date (tuesday) |
| How much less did I spend on Amazon during the current year? | how_much, less, transfer_payment  | date_period (current year), company_name (Amazon)|
| Can I make a reservation from the 1st of June to the 7th? | make, booking | date_from (1st of June), date_to (7th) |

## Data structure

The data is divided in 2 domains, _banking_ and _hotels_, each of it in their corresponding directories. 
The data for each of these domains is divided in 20 folds, each of them in a json file named `fold0.json`,
`fold1.json`, etc. The structure of each example is the following:
```json
{
    "text": "How much did I spend in total until May on amazon prime?",
    "intents": [
      "how_much",
      "transfer_payment_deposit"
    ],
    "slots": {
      "date_to": {
        "text": "May",
        "span": [
          36,
          39
        ],
        "value": {
          "day": 31,
          "month": 5,
          "year": 2022
        }
      },
      "company_name": {
        "text": "amazon prime",
        "span": [
          43,
          55
        ],
        "value": "amazon prime"
      }
    }
  }

```

Where the intents (or intent modules) are defined as a list in the field 
`"intents"` and the slot-values in the field `"slots"`. If any of the fields is missing,
then it means that the example has no intents or slot-values. For each slot present, the 
span is defined in the field `"span"` and the canonical value is defined in the field `"value"`.
For relative dates and times, the reference date is set to `2022/3/15` and the 
reference time is set to `09:00 a.m.`, e.g.:

```json
{
    "text": "today",
    "slots": {
      "date": {
        "text": "today",
        "span": [
          0,
          5
        ],
        "value": {
          "day": 15,
          "month": 3,
          "year": 2022
        }
      }
    }
  }
```

```json
{
    "text": "any table free in 2 hours?",
    "intents": [
      "request_info",
      "restaurant",
      "booking"
    ],
    "slots": {
      "time": {
        "text": "in 2 hours",
        "span": [
          15,
          25
        ],
        "value": {
          "hour": 11,
          "minute": 0
        }
      }
    }
  }
```

The values of relative weekdays will be considered to be in the future, e.g.:

```json
{
    "text": "I'm leaving on Wednesday",
    "slots": {
      "date_to": {
        "text": "Wednesday",
        "span": [
          15,
          24
        ],
        "value": {
          "day": 16,
          "month": 3,
          "year": 2022
        }
      }
    }
  }
```

## Experimental setup

For the experiments presented in the paper we adopt 3 data setups:
* **20-fold**: We use 1 fold for training and the other 19 folds for testing, doing this 20 times with a different training fold. Then we report the mean results of each fold.
* **10-fold**: We use 2 folds for training and the other 18 folds for testing, doing this 10 times with 10 pairs of training folds. We use consecutive indices for the training pairs (i.e. `fold0.json` and `fold1.json`, `fold2.json` and `fold3.json`, etc.). Then we report the mean results for each pair of folds.
* **Large**: We use 18 folds for training and the other two for testing, doing this 10 times with 10 pairs of testing folds. This can be seen as "inverse" 10-fold.

These setups are designed to replicate the data setups found in production while not overfitting to a small test set.

We also use 3 domain setups:
* **BANKING**: We train and test on banking data only.
* **HOTELS**: We train and test on hotels data only.
* **ALL**: We train and test on both domains. The folds for each domain are joined for the different data setups (i.e. banking/fold0.json will be joined with hotels/fold0.json and so on)

We also perform additional _cross-domain_ experiments, in where we train the models on all the data from one of the domains, and we test it in the shared intents of the other domain

### Citations

When using the NLU++ dataset in your work, please cite [NLU++: A Multi-Label, Slot-Rich, Generalisable 
Dataset for Natural Language Understanding in Task-Oriented Dialogue](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

```bibtex
@inproceedings{Casanueva2022,
    author      = {I{\~{n}}igo Casanueva and Ivan Vuli\'{c} and Georgios Spithourakis and Pawe\l~Budzianowski},
    title       = {NLU++: A Multi-Label, Slot-Rich, Generalisable Dataset for Natural Language Understanding in Task-Oriented Dialogue},
    year        = {2022},
    month       = {apr},
    note        = {Data available at https://www.youtube.com/watch?v=dQw4w9WgXcQ},
    url         = {https://www.youtube.com/watch?v=dQw4w9WgXcQ},
    booktitle   = {TODO}
}

```

## License
The datasets shared on this repository are licensed under the license found in the LICENSE file.
