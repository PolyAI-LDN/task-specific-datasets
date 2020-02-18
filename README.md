[![PolyAI](polyai-logo.png)](https://poly-ai.com/)

# task-specific-datasets

*A collection of NLU datasets in constrained domains.*

## Datasets

###Banking

Dataset composed of online banking queries annotated with their corresponding intents.

| Dataset statistics               |      |
| ---            |   --- |
| Train examples | 10003 |
| Test examples | 3080 |
| Number of intents | 77 |

|          Example Query      | Intent      |
| ---            |   --- |
| Is there a way to know when my card will arrive?| card_arrival |
| I think my card is broken | card_not_working |
| I made a mistake and need to cancel a transaction | cancel_transfer |
| Is my card usable anywhere? | card_acceptance |


## Citations

When using the banking dataset in your work, please cite INTENT_DETECTION_PAPER:

```bibtex
@inproceedings{Casanueva2020,
    author      = {I{\~{n}}igo Casanueva and Tadas Temcinas and Matthew Henderson and Daniela Gerz and Ivan Vulic},
    title       = {TODO},
    year        = {2020},
    month       = {jul},
    note        = {Data available at TODO},
    url         = {TODO},
    booktitle   = {Arxiv},
}

```