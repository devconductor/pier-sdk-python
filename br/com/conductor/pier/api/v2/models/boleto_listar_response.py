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


class BoletoListarResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BoletoListarResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_conta': 'int',
            'nosso_numero': 'str',
            'data_vencimento': 'str',
            'valor_boleto': 'float',
            'id_tipo_boleto': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_conta': 'idConta',
            'nosso_numero': 'nossoNumero',
            'data_vencimento': 'dataVencimento',
            'valor_boleto': 'valorBoleto',
            'id_tipo_boleto': 'idTipoBoleto'
        }

        self._id = None
        self._id_conta = None
        self._nosso_numero = None
        self._data_vencimento = None
        self._valor_boleto = None
        self._id_tipo_boleto = None

    @property
    def id(self):
        """
        Gets the id of this BoletoListarResponse.
        {{{boleto_response_id_value}}}

        :return: The id of this BoletoListarResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BoletoListarResponse.
        {{{boleto_response_id_value}}}

        :param id: The id of this BoletoListarResponse.
        :type: int
        """
        self._id = id

    @property
    def id_conta(self):
        """
        Gets the id_conta of this BoletoListarResponse.
        {{{boleto_response_id_conta_value}}}

        :return: The id_conta of this BoletoListarResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this BoletoListarResponse.
        {{{boleto_response_id_conta_value}}}

        :param id_conta: The id_conta of this BoletoListarResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def nosso_numero(self):
        """
        Gets the nosso_numero of this BoletoListarResponse.
        {{{boleto_response_nosso_numero_value}}}

        :return: The nosso_numero of this BoletoListarResponse.
        :rtype: str
        """
        return self._nosso_numero

    @nosso_numero.setter
    def nosso_numero(self, nosso_numero):
        """
        Sets the nosso_numero of this BoletoListarResponse.
        {{{boleto_response_nosso_numero_value}}}

        :param nosso_numero: The nosso_numero of this BoletoListarResponse.
        :type: str
        """
        self._nosso_numero = nosso_numero

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this BoletoListarResponse.
        {{{boleto_response_data_vencimento_value}}}

        :return: The data_vencimento of this BoletoListarResponse.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this BoletoListarResponse.
        {{{boleto_response_data_vencimento_value}}}

        :param data_vencimento: The data_vencimento of this BoletoListarResponse.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def valor_boleto(self):
        """
        Gets the valor_boleto of this BoletoListarResponse.
        {{{boleto_response_valor_boleto_value}}}

        :return: The valor_boleto of this BoletoListarResponse.
        :rtype: float
        """
        return self._valor_boleto

    @valor_boleto.setter
    def valor_boleto(self, valor_boleto):
        """
        Sets the valor_boleto of this BoletoListarResponse.
        {{{boleto_response_valor_boleto_value}}}

        :param valor_boleto: The valor_boleto of this BoletoListarResponse.
        :type: float
        """
        self._valor_boleto = valor_boleto

    @property
    def id_tipo_boleto(self):
        """
        Gets the id_tipo_boleto of this BoletoListarResponse.
        {{{boleto_response_id_tipo_boleto_value}}}

        :return: The id_tipo_boleto of this BoletoListarResponse.
        :rtype: int
        """
        return self._id_tipo_boleto

    @id_tipo_boleto.setter
    def id_tipo_boleto(self, id_tipo_boleto):
        """
        Sets the id_tipo_boleto of this BoletoListarResponse.
        {{{boleto_response_id_tipo_boleto_value}}}

        :param id_tipo_boleto: The id_tipo_boleto of this BoletoListarResponse.
        :type: int
        """
        self._id_tipo_boleto = id_tipo_boleto

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

