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


class FaturaDetalheResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FaturaDetalheResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_conta': 'int',
            'situacao_processamento': 'str',
            'pagamento_efetuado': 'bool',
            'data_vencimento_fatura': 'str',
            'data_vencimento_real': 'str',
            'data_fechamento': 'str',
            'valor_total': 'float',
            'valor_pagamento_minimo': 'float',
            'lancamentos_fatura_response': 'list[LancamentoFaturaResponse]',
            'saldo_anterior': 'float'
        }

        self.attribute_map = {
            'id_conta': 'idConta',
            'situacao_processamento': 'situacaoProcessamento',
            'pagamento_efetuado': 'pagamentoEfetuado',
            'data_vencimento_fatura': 'dataVencimentoFatura',
            'data_vencimento_real': 'dataVencimentoReal',
            'data_fechamento': 'dataFechamento',
            'valor_total': 'valorTotal',
            'valor_pagamento_minimo': 'valorPagamentoMinimo',
            'lancamentos_fatura_response': 'lancamentosFaturaResponse',
            'saldo_anterior': 'saldoAnterior'
        }

        self._id_conta = None
        self._situacao_processamento = None
        self._pagamento_efetuado = None
        self._data_vencimento_fatura = None
        self._data_vencimento_real = None
        self._data_fechamento = None
        self._valor_total = None
        self._valor_pagamento_minimo = None
        self._lancamentos_fatura_response = None
        self._saldo_anterior = None

    @property
    def id_conta(self):
        """
        Gets the id_conta of this FaturaDetalheResponse.
        {{{fatura_response_id_conta_value}}}

        :return: The id_conta of this FaturaDetalheResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this FaturaDetalheResponse.
        {{{fatura_response_id_conta_value}}}

        :param id_conta: The id_conta of this FaturaDetalheResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def situacao_processamento(self):
        """
        Gets the situacao_processamento of this FaturaDetalheResponse.
        {{{fatura_response_situacao_processamento_value}}}

        :return: The situacao_processamento of this FaturaDetalheResponse.
        :rtype: str
        """
        return self._situacao_processamento

    @situacao_processamento.setter
    def situacao_processamento(self, situacao_processamento):
        """
        Sets the situacao_processamento of this FaturaDetalheResponse.
        {{{fatura_response_situacao_processamento_value}}}

        :param situacao_processamento: The situacao_processamento of this FaturaDetalheResponse.
        :type: str
        """
        allowed_values = ["ABERTA", "FECHADA", "TODAS"]
        if situacao_processamento not in allowed_values:
            raise ValueError(
                "Invalid value for `situacao_processamento`, must be one of {0}"
                .format(allowed_values)
            )
        self._situacao_processamento = situacao_processamento

    @property
    def pagamento_efetuado(self):
        """
        Gets the pagamento_efetuado of this FaturaDetalheResponse.
        {{{fatura_response_pagamento_efetuado_value}}}

        :return: The pagamento_efetuado of this FaturaDetalheResponse.
        :rtype: bool
        """
        return self._pagamento_efetuado

    @pagamento_efetuado.setter
    def pagamento_efetuado(self, pagamento_efetuado):
        """
        Sets the pagamento_efetuado of this FaturaDetalheResponse.
        {{{fatura_response_pagamento_efetuado_value}}}

        :param pagamento_efetuado: The pagamento_efetuado of this FaturaDetalheResponse.
        :type: bool
        """
        self._pagamento_efetuado = pagamento_efetuado

    @property
    def data_vencimento_fatura(self):
        """
        Gets the data_vencimento_fatura of this FaturaDetalheResponse.
        {{{fatura_response_data_vencimento_fatura_value}}}

        :return: The data_vencimento_fatura of this FaturaDetalheResponse.
        :rtype: str
        """
        return self._data_vencimento_fatura

    @data_vencimento_fatura.setter
    def data_vencimento_fatura(self, data_vencimento_fatura):
        """
        Sets the data_vencimento_fatura of this FaturaDetalheResponse.
        {{{fatura_response_data_vencimento_fatura_value}}}

        :param data_vencimento_fatura: The data_vencimento_fatura of this FaturaDetalheResponse.
        :type: str
        """
        self._data_vencimento_fatura = data_vencimento_fatura

    @property
    def data_vencimento_real(self):
        """
        Gets the data_vencimento_real of this FaturaDetalheResponse.
        {{{fatura_response_data_vencimento_real_value}}}

        :return: The data_vencimento_real of this FaturaDetalheResponse.
        :rtype: str
        """
        return self._data_vencimento_real

    @data_vencimento_real.setter
    def data_vencimento_real(self, data_vencimento_real):
        """
        Sets the data_vencimento_real of this FaturaDetalheResponse.
        {{{fatura_response_data_vencimento_real_value}}}

        :param data_vencimento_real: The data_vencimento_real of this FaturaDetalheResponse.
        :type: str
        """
        self._data_vencimento_real = data_vencimento_real

    @property
    def data_fechamento(self):
        """
        Gets the data_fechamento of this FaturaDetalheResponse.
        {{{fatura_response_data_fechamento_value}}}

        :return: The data_fechamento of this FaturaDetalheResponse.
        :rtype: str
        """
        return self._data_fechamento

    @data_fechamento.setter
    def data_fechamento(self, data_fechamento):
        """
        Sets the data_fechamento of this FaturaDetalheResponse.
        {{{fatura_response_data_fechamento_value}}}

        :param data_fechamento: The data_fechamento of this FaturaDetalheResponse.
        :type: str
        """
        self._data_fechamento = data_fechamento

    @property
    def valor_total(self):
        """
        Gets the valor_total of this FaturaDetalheResponse.
        {{{fatura_response_valor_total_value}}}

        :return: The valor_total of this FaturaDetalheResponse.
        :rtype: float
        """
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        """
        Sets the valor_total of this FaturaDetalheResponse.
        {{{fatura_response_valor_total_value}}}

        :param valor_total: The valor_total of this FaturaDetalheResponse.
        :type: float
        """
        self._valor_total = valor_total

    @property
    def valor_pagamento_minimo(self):
        """
        Gets the valor_pagamento_minimo of this FaturaDetalheResponse.
        {{{fatura_response_valor_pagamento_minimo_value}}}

        :return: The valor_pagamento_minimo of this FaturaDetalheResponse.
        :rtype: float
        """
        return self._valor_pagamento_minimo

    @valor_pagamento_minimo.setter
    def valor_pagamento_minimo(self, valor_pagamento_minimo):
        """
        Sets the valor_pagamento_minimo of this FaturaDetalheResponse.
        {{{fatura_response_valor_pagamento_minimo_value}}}

        :param valor_pagamento_minimo: The valor_pagamento_minimo of this FaturaDetalheResponse.
        :type: float
        """
        self._valor_pagamento_minimo = valor_pagamento_minimo

    @property
    def lancamentos_fatura_response(self):
        """
        Gets the lancamentos_fatura_response of this FaturaDetalheResponse.
        {{{fatura_detalhe_response_lancamentos_fatura_response_value}}}

        :return: The lancamentos_fatura_response of this FaturaDetalheResponse.
        :rtype: list[LancamentoFaturaResponse]
        """
        return self._lancamentos_fatura_response

    @lancamentos_fatura_response.setter
    def lancamentos_fatura_response(self, lancamentos_fatura_response):
        """
        Sets the lancamentos_fatura_response of this FaturaDetalheResponse.
        {{{fatura_detalhe_response_lancamentos_fatura_response_value}}}

        :param lancamentos_fatura_response: The lancamentos_fatura_response of this FaturaDetalheResponse.
        :type: list[LancamentoFaturaResponse]
        """
        self._lancamentos_fatura_response = lancamentos_fatura_response

    @property
    def saldo_anterior(self):
        """
        Gets the saldo_anterior of this FaturaDetalheResponse.
        {{{fatura_response_saldo_anterior_value}}}

        :return: The saldo_anterior of this FaturaDetalheResponse.
        :rtype: float
        """
        return self._saldo_anterior

    @saldo_anterior.setter
    def saldo_anterior(self, saldo_anterior):
        """
        Sets the saldo_anterior of this FaturaDetalheResponse.
        {{{fatura_response_saldo_anterior_value}}}

        :param saldo_anterior: The saldo_anterior of this FaturaDetalheResponse.
        :type: float
        """
        self._saldo_anterior = saldo_anterior

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

