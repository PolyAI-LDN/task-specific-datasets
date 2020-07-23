[![PolyAI](polyai-logo.png)](https://poly-ai.com/)

# task-specific-datasets

*A collection of NLU datasets in constrained domains.*

## Datasets

## Banking

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


### Citations

When using the banking dataset in your work, please cite [Efficient Intent Detection with Dual Sentence Encoders](https://arxiv.org/abs/2003.04807).

```bibtex
@inproceedings{Casanueva2020,
    author      = {I{\~{n}}igo Casanueva and Tadas Temcinas and Daniela Gerz and Matthew Henderson and Ivan Vulic},
    title       = {Efficient Intent Detection with Dual Sentence Encoders},
    year        = {2020},
    month       = {mar},
    note        = {Data available at https://github.com/PolyAI-LDN/task-specific-datasets},
    url         = {https://arxiv.org/abs/2003.04807},
    booktitle   = {Proceedings of the 2nd Workshop on NLP for ConvAI - ACL 2020}
}

```

## Span Extraction
The directory `span_extraction` contains the data used for the SpanConvert paper.

A training example looks like:
```
{
    "userInput": {
        "text": "I would like a table for one person"
    },
    "labels": [
        {
            "slot": "people",
            "valueSpan": {
                "startIndex": 25,
                "endIndex": 35
            }
        }
    ]
}
```

In the above example, the span "one person" is the value for the `people` slot.

The datasets have a structure like this:
```
ls span_extraction/restaurant8k

test.json
train_0.json
train_1.json
train_2.json
...
```
Where:
* `test.json` contains the examples for evaluation
* `train_0.json` contains all of the training examples
* `train_{i}.json` contains `1/(2^i)`th of the training data.


#### Exploring the Span Extraction Datasets
Here's a quick command line demo to explore some of the datasets (requires `jq` and `parallel`)
```

# Calculate the number of examples in each json file.
cd span_extraction

ls -d restaurant8k/*.json | parallel -k 'echo -n "{}," && cat {} | jq length'

restaurant8k/test.json,3731
restaurant8k/train_0.json,8198
restaurant8k/train_1.json,4099
restaurant8k/train_2.json,2049
restaurant8k/train_3.json,1024
restaurant8k/train_4.json,512
restaurant8k/train_5.json,256
restaurant8k/train_6.json,128
restaurant8k/train_7.json,64
restaurant8k/train_8.json,32

ls -d dstc8/*/*.json | parallel -k 'echo -n "{}," && cat {} | jq length'
dstc8/Buses_1/test.json,377
dstc8/Buses_1/train_0.json,1133
dstc8/Buses_1/train_1.json,566
dstc8/Buses_1/train_2.json,283
dstc8/Buses_1/train_3.json,141
dstc8/Buses_1/train_4.json,70
dstc8/Events_1/test.json,521
dstc8/Events_1/train_0.json,1498
dstc8/Events_1/train_1.json,749
dstc8/Events_1/train_2.json,374
dstc8/Events_1/train_3.json,187
dstc8/Events_1/train_4.json,93
dstc8/Homes_1/test.json,587
dstc8/Homes_1/train_0.json,2064
dstc8/Homes_1/train_1.json,1032
dstc8/Homes_1/train_2.json,516
dstc8/Homes_1/train_3.json,258
dstc8/Homes_1/train_4.json,129
dstc8/RentalCars_1/test.json,328
dstc8/RentalCars_1/train_0.json,874
dstc8/RentalCars_1/train_1.json,437
dstc8/RentalCars_1/train_2.json,218
dstc8/RentalCars_1/train_3.json,109
dstc8/RentalCars_1/train_4.json,54
```
### Citations

When using the datasets in your work, please cite [the Span-ConveRT paper](https://arxiv.org/abs/2005.08866).

```bibtex
@inproceedings{CoopeFarghly2020,
    Author      = {Sam Coope and Tyler Farghly and Daniela Gerz and Ivan Vulić and Matthew Henderson},
    Title       = {Span-ConveRT: Few-shot Span Extraction for Dialog with Pretrained Conversational Representations},
    Year        = {2020},
    url         = {https://arxiv.org/abs/2005.08866},
    publisher   = {ACL},
}

```


## License
The datasets shared on this repository are licensed under the license found in the LICENSE file.
