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


class TipoFaturamentoPorContaPersistValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoFaturamentoPorContaPersistValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_conta': 'int',
            'id_tipo_faturamento': 'int'
        }

        self.attribute_map = {
            'id_conta': 'idConta',
            'id_tipo_faturamento': 'idTipoFaturamento'
        }

        self._id_conta = None
        self._id_tipo_faturamento = None

    @property
    def id_conta(self):
        """
        Gets the id_conta of this TipoFaturamentoPorContaPersistValue.
        {{{tipo_faturamento_por_conta_persist_id_conta_value}}}

        :return: The id_conta of this TipoFaturamentoPorContaPersistValue.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this TipoFaturamentoPorContaPersistValue.
        {{{tipo_faturamento_por_conta_persist_id_conta_value}}}

        :param id_conta: The id_conta of this TipoFaturamentoPorContaPersistValue.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_tipo_faturamento(self):
        """
        Gets the id_tipo_faturamento of this TipoFaturamentoPorContaPersistValue.
        {{{tipo_faturamento_por_conta_persist_id_tipo_faturamento_value}}}

        :return: The id_tipo_faturamento of this TipoFaturamentoPorContaPersistValue.
        :rtype: int
        """
        return self._id_tipo_faturamento

    @id_tipo_faturamento.setter
    def id_tipo_faturamento(self, id_tipo_faturamento):
        """
        Sets the id_tipo_faturamento of this TipoFaturamentoPorContaPersistValue.
        {{{tipo_faturamento_por_conta_persist_id_tipo_faturamento_value}}}

        :param id_tipo_faturamento: The id_tipo_faturamento of this TipoFaturamentoPorContaPersistValue.
        :type: int
        """
        self._id_tipo_faturamento = id_tipo_faturamento

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
