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


class TerminalPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TerminalPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_estabelecimento': 'int',
            'flag_consulta_extrato': 'bool',
            'flag_terminal_virtual': 'bool'
        }

        self.attribute_map = {
            'id_estabelecimento': 'idEstabelecimento',
            'flag_consulta_extrato': 'flagConsultaExtrato',
            'flag_terminal_virtual': 'flagTerminalVirtual'
        }

        self._id_estabelecimento = None
        self._flag_consulta_extrato = None
        self._flag_terminal_virtual = None

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this TerminalPersist.
        {{{terminal_persist_id_estabelecimento_value}}}

        :return: The id_estabelecimento of this TerminalPersist.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this TerminalPersist.
        {{{terminal_persist_id_estabelecimento_value}}}

        :param id_estabelecimento: The id_estabelecimento of this TerminalPersist.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def flag_consulta_extrato(self):
        """
        Gets the flag_consulta_extrato of this TerminalPersist.
        {{{terminal_persist_flag_consulta_extrato_value}}}

        :return: The flag_consulta_extrato of this TerminalPersist.
        :rtype: bool
        """
        return self._flag_consulta_extrato

    @flag_consulta_extrato.setter
    def flag_consulta_extrato(self, flag_consulta_extrato):
        """
        Sets the flag_consulta_extrato of this TerminalPersist.
        {{{terminal_persist_flag_consulta_extrato_value}}}

        :param flag_consulta_extrato: The flag_consulta_extrato of this TerminalPersist.
        :type: bool
        """
        self._flag_consulta_extrato = flag_consulta_extrato

    @property
    def flag_terminal_virtual(self):
        """
        Gets the flag_terminal_virtual of this TerminalPersist.
        {{{terminal_persist_flag_terminal_virtual_value}}}

        :return: The flag_terminal_virtual of this TerminalPersist.
        :rtype: bool
        """
        return self._flag_terminal_virtual

    @flag_terminal_virtual.setter
    def flag_terminal_virtual(self, flag_terminal_virtual):
        """
        Sets the flag_terminal_virtual of this TerminalPersist.
        {{{terminal_persist_flag_terminal_virtual_value}}}

        :param flag_terminal_virtual: The flag_terminal_virtual of this TerminalPersist.
        :type: bool
        """
        self._flag_terminal_virtual = flag_terminal_virtual

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

