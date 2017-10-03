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


class ContaHistoricoPagamentoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContaHistoricoPagamentoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_pagamento': 'int',
            'id_estabelecimento': 'int',
            'id_banco': 'int',
            'id_cartao': 'int',
            'valor_pagamento': 'float',
            'data_hora_pagamento': 'str',
            'data_hora_entrada_pagamento': 'str',
            'status': 'int'
        }

        self.attribute_map = {
            'id_pagamento': 'idPagamento',
            'id_estabelecimento': 'idEstabelecimento',
            'id_banco': 'idBanco',
            'id_cartao': 'idCartao',
            'valor_pagamento': 'valorPagamento',
            'data_hora_pagamento': 'dataHoraPagamento',
            'data_hora_entrada_pagamento': 'dataHoraEntradaPagamento',
            'status': 'status'
        }

        self._id_pagamento = None
        self._id_estabelecimento = None
        self._id_banco = None
        self._id_cartao = None
        self._valor_pagamento = None
        self._data_hora_pagamento = None
        self._data_hora_entrada_pagamento = None
        self._status = None

    @property
    def id_pagamento(self):
        """
        Gets the id_pagamento of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Pagamento

        :return: The id_pagamento of this ContaHistoricoPagamentoResponse.
        :rtype: int
        """
        return self._id_pagamento

    @id_pagamento.setter
    def id_pagamento(self, id_pagamento):
        """
        Sets the id_pagamento of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Pagamento

        :param id_pagamento: The id_pagamento of this ContaHistoricoPagamentoResponse.
        :type: int
        """
        self._id_pagamento = id_pagamento

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento onde o Pagamento foi realizado, quando este for o local de pagamento.

        :return: The id_estabelecimento of this ContaHistoricoPagamentoResponse.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento onde o Pagamento foi realizado, quando este for o local de pagamento.

        :param id_estabelecimento: The id_estabelecimento of this ContaHistoricoPagamentoResponse.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def id_banco(self):
        """
        Gets the id_banco of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Institui\u00C3\u00A7\u00C3\u00A3o Banc\u00C3\u00A1ria onde o Pagamento foi realizado, quando este for o local de pagamento

        :return: The id_banco of this ContaHistoricoPagamentoResponse.
        :rtype: int
        """
        return self._id_banco

    @id_banco.setter
    def id_banco(self, id_banco):
        """
        Sets the id_banco of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Institui\u00C3\u00A7\u00C3\u00A3o Banc\u00C3\u00A1ria onde o Pagamento foi realizado, quando este for o local de pagamento

        :param id_banco: The id_banco of this ContaHistoricoPagamentoResponse.
        :type: int
        """
        self._id_banco = id_banco

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o

        :return: The id_cartao of this ContaHistoricoPagamentoResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o

        :param id_cartao: The id_cartao of this ContaHistoricoPagamentoResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def valor_pagamento(self):
        """
        Gets the valor_pagamento of this ContaHistoricoPagamentoResponse.
        Valor do Pagamento

        :return: The valor_pagamento of this ContaHistoricoPagamentoResponse.
        :rtype: float
        """
        return self._valor_pagamento

    @valor_pagamento.setter
    def valor_pagamento(self, valor_pagamento):
        """
        Sets the valor_pagamento of this ContaHistoricoPagamentoResponse.
        Valor do Pagamento

        :param valor_pagamento: The valor_pagamento of this ContaHistoricoPagamentoResponse.
        :type: float
        """
        self._valor_pagamento = valor_pagamento

    @property
    def data_hora_pagamento(self):
        """
        Gets the data_hora_pagamento of this ContaHistoricoPagamentoResponse.
        Data e Hora da realiza\u00C3\u00A7\u00C3\u00A3o do Pagamento. Quando feito em Institui\u00C3\u00A7\u00C3\u00A3o Banc\u00C3\u00A1ria, o hor\u00C3\u00A1rio do pagamento \u00C3\u00A9 exibido com valor zero

        :return: The data_hora_pagamento of this ContaHistoricoPagamentoResponse.
        :rtype: str
        """
        return self._data_hora_pagamento

    @data_hora_pagamento.setter
    def data_hora_pagamento(self, data_hora_pagamento):
        """
        Sets the data_hora_pagamento of this ContaHistoricoPagamentoResponse.
        Data e Hora da realiza\u00C3\u00A7\u00C3\u00A3o do Pagamento. Quando feito em Institui\u00C3\u00A7\u00C3\u00A3o Banc\u00C3\u00A1ria, o hor\u00C3\u00A1rio do pagamento \u00C3\u00A9 exibido com valor zero

        :param data_hora_pagamento: The data_hora_pagamento of this ContaHistoricoPagamentoResponse.
        :type: str
        """
        self._data_hora_pagamento = data_hora_pagamento

    @property
    def data_hora_entrada_pagamento(self):
        """
        Gets the data_hora_entrada_pagamento of this ContaHistoricoPagamentoResponse.
        Data e Hora em que o registro do Pagamento foi cadastrado

        :return: The data_hora_entrada_pagamento of this ContaHistoricoPagamentoResponse.
        :rtype: str
        """
        return self._data_hora_entrada_pagamento

    @data_hora_entrada_pagamento.setter
    def data_hora_entrada_pagamento(self, data_hora_entrada_pagamento):
        """
        Sets the data_hora_entrada_pagamento of this ContaHistoricoPagamentoResponse.
        Data e Hora em que o registro do Pagamento foi cadastrado

        :param data_hora_entrada_pagamento: The data_hora_entrada_pagamento of this ContaHistoricoPagamentoResponse.
        :type: str
        """
        self._data_hora_entrada_pagamento = data_hora_entrada_pagamento

    @property
    def status(self):
        """
        Gets the status of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Pagamento

        :return: The status of this ContaHistoricoPagamentoResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ContaHistoricoPagamentoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Pagamento

        :param status: The status of this ContaHistoricoPagamentoResponse.
        :type: int
        """
        self._status = status

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
