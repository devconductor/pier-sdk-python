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


class TipoEndereco(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoEndereco - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'nome': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'nome': 'nome'
        }

        self._id = None
        self._nome = None

    @property
    def id(self):
        """
        Gets the id of this TipoEndereco.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Tipo do Endere\u00C3\u00A7o (id)

        :return: The id of this TipoEndereco.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TipoEndereco.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Tipo do Endere\u00C3\u00A7o (id)

        :param id: The id of this TipoEndereco.
        :type: int
        """
        self._id = id

    @property
    def nome(self):
        """
        Gets the nome of this TipoEndereco.
        Nome do Tipo do Endere\u00C3\u00A7o

        :return: The nome of this TipoEndereco.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this TipoEndereco.
        Nome do Tipo do Endere\u00C3\u00A7o

        :param nome: The nome of this TipoEndereco.
        :type: str
        """
        self._nome = nome

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
