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
from pyiides.utils.helper_functions import check_type, check_vocab


class Person:
    """
    Initialize a Person instance.

    Args:
        first_name (str): The first, or given, name of the individual.
        middle_name (str): The middle name of the individual.
        last_name (str): The last, or family, name of the individual.
        suffix (str): The name suffix of the individual. A constant from 
                      `suffix-vocab <./vocab/suffix-vocab.html>`_.
        alias (list): A list of aliases (other names) the individual has used, and/or 
                      the anonymized names of the individual in court records. One or more string values.
        city (str): The city (or county/district) that the person resided in at the time of the incident.
        state (str): The state (or region) that the person resided in at the time of the incident.
        country (str): The country that the person resided in at the time of the incident. 
                       Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
        postal_code (int): The postal code that the person resided in at the time of the incident.
        country_of_citizenship (list): Citizenship(s) of the person. Public implementations 
                                       should use the standard codes provided by ISO 3166-1 alpha-2. One or more string values.
        nationality (list): The nationality or nationalities of the person. Public implementations 
                            should use the standard codes provided by ISO 3166-1 alpha-2. One or more string values.
        residency (str): Residency status if the person was not a citizen of the country where 
                         they resided during the incident. A constant from 
                         `residency-vocab <./vocab/residency-vocab.html>`_.
        gender (str): Sex or gender at the time of the incident. A constant from 
                      `gender-vocab <./vocab/gender-vocab.html>`_.
        age (int): Age at the time that the incident began.
        education (str): Highest level of education at the time the incident began. A constant from 
                         `education-vocab <./vocab/education-vocab.html>`_.
        marital_status (str): The marital status at the time of the incident. A constant from 
                              `marital-status-vocab <./vocab/marital-status-vocab.html>`_.
        number_of_children (int): The number of children that the person is responsible for, at the time of the incident.
        comment (str): Comments or clarifications regarding any of the Person properties.
        **kwargs (dict): Additional attributes for the person.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> from pyiides import Person
        >>> person = Person(first_name="John", last_name="Doe", city="New York", country="US")
        >>> print(person.first_name)
        John
        >>> print(person.city)
        New York
    """
    def __init__(self, first_name=None, middle_name=None, last_name=None, suffix=None, alias=None, city=None, state=None, country=None, postal_code=None, country_of_citizenship=None, nationality=None, residency=None, gender=None, age=None, education=None, marital_status=None, number_of_children=None, comment=None, **kwargs):
        check_type(first_name, str)
        self._first_name = first_name

        check_type(middle_name, str)
        self._middle_name = middle_name

        check_type(last_name, str)
        self._last_name = last_name

        check_type(suffix, str)
        check_vocab(suffix, 'suffix-vocab')
        self._suffix = suffix

        check_type(alias, list)
        if alias != None:
            for s in alias:
                check_type(s, str)
        self._alias = alias

        check_type(city, str)
        self._city = city

        check_type(state, str)
        check_vocab(state, 'state-vocab-us')
        self._state = state

        check_type(country, str)
        check_vocab(kwargs.get("country"), 'country-vocab')
        self._country = country

        check_type(postal_code, int)
        self._postal_code = postal_code

        check_type(country_of_citizenship, list)
        if country_of_citizenship != None:
            for s in country_of_citizenship:
                check_type(s, str)
        self._country_of_citizenship = country_of_citizenship

        check_type(nationality, list)
        if nationality != None:
            for s in nationality:
                check_type(s, str)
        self._nationality = nationality

        check_type(residency, str)
        check_vocab(residency, 'residency-vocab')
        self._residency = residency

        check_type(gender, str)
        check_vocab(gender, 'gender-vocab')
        self._gender = gender

        check_type(age, int)
        self._age = age

        check_type(education, str)
        check_vocab(education, 'education-vocab')
        self._education = education

        check_type(marital_status, str)
        check_vocab(marital_status, 'marital-status-vocab')
        self._marital_status = marital_status

        check_type(number_of_children, int)
        self._number_of_children = number_of_children

        check_type(comment, str)
        self._comment = comment

    def __repr__(self):
        return (f"Person("
                f"first_name={self.first_name}, "
                f"middle_name={self.middle_name}, "
                f"last_name={self.last_name}, "
                f"suffix={self.suffix}, "
                f"alias={self.alias}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"country={self.country}, "
                f"postal_code={self.postal_code}, "
                f"country_of_citizenship={self.country_of_citizenship}, "
                f"nationality={self.nationality}, "
                f"residency={self.residency}, "
                f"gender={self.gender}, "
                f"age={self.age}, "
                f"education={self.education}, "
                f"marital_status={self.marital_status}, "
                f"number_of_children={self.number_of_children}, "
                f"comment={self.comment})")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        return ({
                    key.lstrip('_'): value for key, value in class_dict_copy.items()
                }, None)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        check_type(value, str, allow_none=False)
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        self._first_name = None

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        check_type(value, str, allow_none=False)
        self._middle_name = value

    @middle_name.deleter
    def middle_name(self):
        self._middle_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        check_type(value, str, allow_none=False)
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        self._last_name = None

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'suffix-vocab')
        self._suffix = value

    @suffix.deleter
    def suffix(self):
        self._suffix = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._alias = value

    def append_alias(self, item):
        check_type(item, str, allow_none=False)
        self._alias.append(item)

    @alias.deleter
    def alias(self):
        self._alias = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        check_type(value, str, allow_none=False)
        self._city = value

    @city.deleter
    def city(self):
        self._city = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._state = value

    @state.deleter
    def state(self):
        self._state = None

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._country = value

    @country.deleter
    def country(self):
        self._country = None

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        check_type(value, int, allow_none=False)
        self._postal_code = value

    @postal_code.deleter
    def postal_code(self):
        self._postal_code = None

    @property
    def country_of_citizenship(self):
        return self._country_of_citizenship

    @country_of_citizenship.setter
    def country_of_citizenship(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._country_of_citizenship = value

    def append_country_of_citizenship(self, item):
        check_type(item, str, allow_none=False)
        self._country_of_citizenship.append(item)

    @country_of_citizenship.deleter
    def country_of_citizenship(self):
        self._country_of_citizenship = None

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._nationality = value

    def append_nationality(self, item):
        check_type(item, str, allow_none=False)
        self._nationality.append(item)

    @nationality.deleter
    def nationality(self):
        self._nationality = None

    @property
    def residency(self):
        return self._residency

    @residency.setter
    def residency(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'residency-vocab')
        self._residency = value

    @residency.deleter
    def residency(self):
        self._residency = None

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'gender-vocab')
        self._gender = value

    @gender.deleter
    def gender(self):
        self._gender = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        check_type(value, int, allow_none=False)
        self._age = value

    @age.deleter
    def age(self):
        self._age = None

    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'education-vocab')
        self._education = value

    @education.deleter
    def education(self):
        self._education = None

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'marital-status-vocab')
        self._marital_status = value

    @marital_status.deleter
    def marital_status(self):
        self._marital_status = None

    @property
    def number_of_children(self):
        return self._number_of_children

    @number_of_children.setter
    def number_of_children(self, value):
        check_type(value, int, allow_none=False)
        self._number_of_children = value

    @number_of_children.deleter
    def number_of_children(self):
        self._number_of_children = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None
