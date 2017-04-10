# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class PageHistoricoAtraso(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PageHistoricoAtraso - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'list[HistoricoAtrasoFaturaResponse]',
            'first': 'bool',
            'first_page': 'bool',
            'has_content': 'bool',
            'has_next_page': 'bool',
            'has_previous_page': 'bool',
            'last': 'bool',
            'next_page': 'int',
            'number': 'int',
            'number_of_elements': 'int',
            'previous_page': 'int',
            'size': 'int',
            'total_elements': 'int',
            'total_pages': 'int'
        }

        self.attribute_map = {
            'content': 'content',
            'first': 'first',
            'first_page': 'firstPage',
            'has_content': 'hasContent',
            'has_next_page': 'hasNextPage',
            'has_previous_page': 'hasPreviousPage',
            'last': 'last',
            'next_page': 'nextPage',
            'number': 'number',
            'number_of_elements': 'numberOfElements',
            'previous_page': 'previousPage',
            'size': 'size',
            'total_elements': 'totalElements',
            'total_pages': 'totalPages'
        }

        self._content = None
        self._first = None
        self._first_page = None
        self._has_content = None
        self._has_next_page = None
        self._has_previous_page = None
        self._last = None
        self._next_page = None
        self._number = None
        self._number_of_elements = None
        self._previous_page = None
        self._size = None
        self._total_elements = None
        self._total_pages = None

    @property
    def content(self):
        """
        Gets the content of this PageHistoricoAtraso.


        :return: The content of this PageHistoricoAtraso.
        :rtype: list[HistoricoAtrasoFaturaResponse]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this PageHistoricoAtraso.


        :param content: The content of this PageHistoricoAtraso.
        :type: list[HistoricoAtrasoFaturaResponse]
        """
        self._content = content

    @property
    def first(self):
        """
        Gets the first of this PageHistoricoAtraso.


        :return: The first of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this PageHistoricoAtraso.


        :param first: The first of this PageHistoricoAtraso.
        :type: bool
        """
        self._first = first

    @property
    def first_page(self):
        """
        Gets the first_page of this PageHistoricoAtraso.


        :return: The first_page of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """
        Sets the first_page of this PageHistoricoAtraso.


        :param first_page: The first_page of this PageHistoricoAtraso.
        :type: bool
        """
        self._first_page = first_page

    @property
    def has_content(self):
        """
        Gets the has_content of this PageHistoricoAtraso.


        :return: The has_content of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._has_content

    @has_content.setter
    def has_content(self, has_content):
        """
        Sets the has_content of this PageHistoricoAtraso.


        :param has_content: The has_content of this PageHistoricoAtraso.
        :type: bool
        """
        self._has_content = has_content

    @property
    def has_next_page(self):
        """
        Gets the has_next_page of this PageHistoricoAtraso.


        :return: The has_next_page of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, has_next_page):
        """
        Sets the has_next_page of this PageHistoricoAtraso.


        :param has_next_page: The has_next_page of this PageHistoricoAtraso.
        :type: bool
        """
        self._has_next_page = has_next_page

    @property
    def has_previous_page(self):
        """
        Gets the has_previous_page of this PageHistoricoAtraso.


        :return: The has_previous_page of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._has_previous_page

    @has_previous_page.setter
    def has_previous_page(self, has_previous_page):
        """
        Sets the has_previous_page of this PageHistoricoAtraso.


        :param has_previous_page: The has_previous_page of this PageHistoricoAtraso.
        :type: bool
        """
        self._has_previous_page = has_previous_page

    @property
    def last(self):
        """
        Gets the last of this PageHistoricoAtraso.


        :return: The last of this PageHistoricoAtraso.
        :rtype: bool
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this PageHistoricoAtraso.


        :param last: The last of this PageHistoricoAtraso.
        :type: bool
        """
        self._last = last

    @property
    def next_page(self):
        """
        Gets the next_page of this PageHistoricoAtraso.


        :return: The next_page of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """
        Sets the next_page of this PageHistoricoAtraso.


        :param next_page: The next_page of this PageHistoricoAtraso.
        :type: int
        """
        self._next_page = next_page

    @property
    def number(self):
        """
        Gets the number of this PageHistoricoAtraso.


        :return: The number of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this PageHistoricoAtraso.


        :param number: The number of this PageHistoricoAtraso.
        :type: int
        """
        self._number = number

    @property
    def number_of_elements(self):
        """
        Gets the number_of_elements of this PageHistoricoAtraso.


        :return: The number_of_elements of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """
        Sets the number_of_elements of this PageHistoricoAtraso.


        :param number_of_elements: The number_of_elements of this PageHistoricoAtraso.
        :type: int
        """
        self._number_of_elements = number_of_elements

    @property
    def previous_page(self):
        """
        Gets the previous_page of this PageHistoricoAtraso.


        :return: The previous_page of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """
        Sets the previous_page of this PageHistoricoAtraso.


        :param previous_page: The previous_page of this PageHistoricoAtraso.
        :type: int
        """
        self._previous_page = previous_page

    @property
    def size(self):
        """
        Gets the size of this PageHistoricoAtraso.


        :return: The size of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this PageHistoricoAtraso.


        :param size: The size of this PageHistoricoAtraso.
        :type: int
        """
        self._size = size

    @property
    def total_elements(self):
        """
        Gets the total_elements of this PageHistoricoAtraso.


        :return: The total_elements of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """
        Sets the total_elements of this PageHistoricoAtraso.


        :param total_elements: The total_elements of this PageHistoricoAtraso.
        :type: int
        """
        self._total_elements = total_elements

    @property
    def total_pages(self):
        """
        Gets the total_pages of this PageHistoricoAtraso.


        :return: The total_pages of this PageHistoricoAtraso.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this PageHistoricoAtraso.


        :param total_pages: The total_pages of this PageHistoricoAtraso.
        :type: int
        """
        self._total_pages = total_pages

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

