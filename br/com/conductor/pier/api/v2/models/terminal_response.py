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


class TerminalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TerminalResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'terminal': 'str',
            'numero_estabelecimento': 'int',
            'id_estabelecimento': 'int',
            'flag_consulta_extrato': 'bool',
            'flag_terminal_virtual': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'terminal': 'terminal',
            'numero_estabelecimento': 'numeroEstabelecimento',
            'id_estabelecimento': 'idEstabelecimento',
            'flag_consulta_extrato': 'flagConsultaExtrato',
            'flag_terminal_virtual': 'flagTerminalVirtual'
        }

        self._id = None
        self._terminal = None
        self._numero_estabelecimento = None
        self._id_estabelecimento = None
        self._flag_consulta_extrato = None
        self._flag_terminal_virtual = None

    @property
    def id(self):
        """
        Gets the id of this TerminalResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Terminal (id).

        :return: The id of this TerminalResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TerminalResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Terminal (id).

        :param id: The id of this TerminalResponse.
        :type: int
        """
        self._id = id

    @property
    def terminal(self):
        """
        Gets the terminal of this TerminalResponse.
        N\u00C3\u00BAmero \u00C3\u00BAnico do terminal.

        :return: The terminal of this TerminalResponse.
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """
        Sets the terminal of this TerminalResponse.
        N\u00C3\u00BAmero \u00C3\u00BAnico do terminal.

        :param terminal: The terminal of this TerminalResponse.
        :type: str
        """
        self._terminal = terminal

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this TerminalResponse.
        N\u00C3\u00BAmero do estabelecimento a qual o terminal pertence.

        :return: The numero_estabelecimento of this TerminalResponse.
        :rtype: int
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this TerminalResponse.
        N\u00C3\u00BAmero do estabelecimento a qual o terminal pertence.

        :param numero_estabelecimento: The numero_estabelecimento of this TerminalResponse.
        :type: int
        """
        self._numero_estabelecimento = numero_estabelecimento

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this TerminalResponse.
        N\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do estabelecimento a qual o terminal pertence.

        :return: The id_estabelecimento of this TerminalResponse.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this TerminalResponse.
        N\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do estabelecimento a qual o terminal pertence.

        :param id_estabelecimento: The id_estabelecimento of this TerminalResponse.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def flag_consulta_extrato(self):
        """
        Gets the flag_consulta_extrato of this TerminalResponse.
        Flag indicando se o terminal \u00C3\u00A9 f\u00C3\u00ADsico ou virtual, sendo: (true: Sim), (false: N\u00C3\u00A3o)).

        :return: The flag_consulta_extrato of this TerminalResponse.
        :rtype: bool
        """
        return self._flag_consulta_extrato

    @flag_consulta_extrato.setter
    def flag_consulta_extrato(self, flag_consulta_extrato):
        """
        Sets the flag_consulta_extrato of this TerminalResponse.
        Flag indicando se o terminal \u00C3\u00A9 f\u00C3\u00ADsico ou virtual, sendo: (true: Sim), (false: N\u00C3\u00A3o)).

        :param flag_consulta_extrato: The flag_consulta_extrato of this TerminalResponse.
        :type: bool
        """
        self._flag_consulta_extrato = flag_consulta_extrato

    @property
    def flag_terminal_virtual(self):
        """
        Gets the flag_terminal_virtual of this TerminalResponse.
        Flag indicando se o terminal permite consultar extrato, sendo: (true: Sim), (false: N\u00C3\u00A3o)).

        :return: The flag_terminal_virtual of this TerminalResponse.
        :rtype: bool
        """
        return self._flag_terminal_virtual

    @flag_terminal_virtual.setter
    def flag_terminal_virtual(self, flag_terminal_virtual):
        """
        Sets the flag_terminal_virtual of this TerminalResponse.
        Flag indicando se o terminal permite consultar extrato, sendo: (true: Sim), (false: N\u00C3\u00A3o)).

        :param flag_terminal_virtual: The flag_terminal_virtual of this TerminalResponse.
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

