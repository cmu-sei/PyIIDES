"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE
MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO
WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER
INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL.
CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT
TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact
permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release
and unlimited distribution.  Please see Copyright notice for non-US Government
use and distribution.
DM24-1597
"""
from pyiides.utils.helper_functions import *

class Sentence:
    """
    Initializes a Sentence instance
    
    Args:
        id (required) (string) : Unique identifier for the sentence. Defaults to a new UUIDv4 string if not provided.
        sentence_type (required) (string) : The type of sentence that was ordered.
            A constant from `sentence-type-vocab <./vocab/sentence-type-vocab.html>`_.
        quantity (integer) : The quantity of the sentence type imposed. MUST be used with the metric property if used.
            Required if metric exists.
        metric (string) : The measurement type of the sentence imposed. MUST be used with the quantity property if used.
            A constant from `sentence-metric-vocab <./vocab/sentence-metric-vocab.html>`_.
            Required if quantity exists.
        concurrency (boolean) : Whether the sentence is to run concurrently (at the same time as) other sentences within the same case.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import Sentence
        >>> sentence = Sentence(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     sentence_type="9",
        ...     quantity=5,
        ...     metric="Years",
        ...     concurrency=True
        ... )
        >>> print(sentence.sentence_type)
        9
        >>> print(sentence.quantity)
        5
    """
    def __init__(self, sentence_type, id=None, quantity=None, metric=None, concurrency=None) -> None:
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(sentence_type, str)
        check_vocab(sentence_type, 'sentence-type-vocab')
        self._sentence_type = sentence_type

        if (quantity == None and metric != None or quantity != None and metric == None):
            raise ReferenceError("Either quantity and metric must coexist, or they are both None")
        
        check_type(quantity, int)
        self._quantity = quantity

        check_type(metric, str)
        check_vocab(metric, 'sentence-metric-vocab')
        self._metric = metric

        check_type(concurrency, bool)
        self._concurrency = concurrency

        # relationships
        self._court_case = None

    def __repr__(self):
        return (f"Sentence(id={self.id}, "
                f"sentence_type={self.sentence_type}, "
                f"quantity={self.quantity}, "
                f"metric={self.metric}, "
                f"concurrency={self.concurrency})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_court_case'}
        class_dict_copy["_id"] = f"sentence--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def sentence_type(self):
        return self._sentence_type
    
    @sentence_type.setter
    def sentence_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'sentence-type-vocab')
        self._sentence_type = value

    @sentence_type.deleter
    def sentence_type(self):
        self._sentence_type = None

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        check_type(value, int, allow_none=False)
        self._quantity = value

        if self._metric == None:
            val = input("Please enter an input for metric:\n")
            check_type(val, str)
            check_vocab(val, 'sentence-metric-vocab')
            self._metric = val
            if (self._metric == None):
                raise ReferenceError("Either quantity and metric must coexist, or they are both None")

    @quantity.deleter
    def quantity(self):
        self._quantity = None
        self._metric = None

    @property
    def metric(self):
        return self._metric
    
    @metric.setter
    def metric(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'sentence-metric-vocab')
        self._metric = value

        if self._quantity == None:
            val = input("Please enter an input for quantity:\n")
            check_type(val, int)
            self._quantity = val
            if (self._quantity == None):
                raise ReferenceError("Either quantity and metric must coexist, or they are both None")

    @metric.deleter
    def metric(self):
        self._metric = None
        self._quantity = None

    @property
    def concurrency(self):
        return self._concurrency
    
    @concurrency.setter
    def concurrency(self, value):
        check_type(value, bool, allow_none=True)
        self._concurrency = value

    @concurrency.deleter
    def concurrency(self):
        self._concurrency = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def court_case(self):
        return self._court_case
    
    @court_case.setter
    def court_case(self, value):
        
        check_type(value, CourtCase, allow_none=False)
        
        # set the court case
        # making sure to remove old relationships
        if self._court_case != None:
            self._court_case.sentences.remove(self)
        self._court_case = value

        # add it to the court case's sentence list
        if value.sentences == None:
            value.sentences = [self]
        elif self not in value.sentences: 
            value.sentences.append(self)
    
    @court_case.deleter
    def court_case(self):
        if self._court_case != None:
            self._court_case.sentences.remove(self)
            self._court_case = None
