[![PolyAI](polyai-logo.png)](https://poly-ai.com/)

# task-specific-datasets

*A collection of NLU datasets in constrained domains.*

## Datasets

### Banking

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

When using the banking dataset in your work, please cite [Efficient Intent Detection with Dual Sentence Encoders](https://arxiv.org/abs/2003.04807).

```bibtex
@inproceedings{Casanueva2020,
    author      = {I{\~{n}}igo Casanueva and Tadas Temcinas and Daniela Gerz and Matthew Henderson and Ivan Vulic},
    title       = {Efficient Intent Detection with Dual Sentence Encoders},
    year        = {2020},
    month       = {mar},
    note        = {Data available at https://github.com/PolyAI-LDN/task-specific-datasets},
    url         = {https://arxiv.org/abs/2003.04807},
    booktitle   = {Arxiv},
}

```
