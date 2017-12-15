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


class PlanoParcelamentoTransferenciaCreditoContaBancariaRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PlanoParcelamentoTransferenciaCreditoContaBancariaRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nsu_origem': 'str',
            'valor_transacao': 'float',
            'numero_real_cartao': 'str',
            'data_validade_cartao': 'str',
            'numero_meses_carencia': 'int',
            'numero_estabelecimento': 'int',
            'data_hora_terminal': 'str',
            'terminal_requisitante': 'str'
        }

        self.attribute_map = {
            'nsu_origem': 'nsuOrigem',
            'valor_transacao': 'valorTransacao',
            'numero_real_cartao': 'numeroRealCartao',
            'data_validade_cartao': 'dataValidadeCartao',
            'numero_meses_carencia': 'numeroMesesCarencia',
            'numero_estabelecimento': 'numeroEstabelecimento',
            'data_hora_terminal': 'dataHoraTerminal',
            'terminal_requisitante': 'terminalRequisitante'
        }

        self._nsu_origem = None
        self._valor_transacao = None
        self._numero_real_cartao = None
        self._data_validade_cartao = None
        self._numero_meses_carencia = None
        self._numero_estabelecimento = None
        self._data_hora_terminal = None
        self._terminal_requisitante = None

    @property
    def nsu_origem(self):
        """
        Gets the nsu_origem of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero Sequencial \u00C3\u009Anico que identifica a transa\u00C3\u00A7\u00C3\u00A3o no sistema que a originou.

        :return: The nsu_origem of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: str
        """
        return self._nsu_origem

    @nsu_origem.setter
    def nsu_origem(self, nsu_origem):
        """
        Sets the nsu_origem of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero Sequencial \u00C3\u009Anico que identifica a transa\u00C3\u00A7\u00C3\u00A3o no sistema que a originou.

        :param nsu_origem: The nsu_origem of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: str
        """
        self._nsu_origem = nsu_origem

    @property
    def valor_transacao(self):
        """
        Gets the valor_transacao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Valor da transa\u00C3\u00A7\u00C3\u00A3o com duas casas decimais para os centavos.

        :return: The valor_transacao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: float
        """
        return self._valor_transacao

    @valor_transacao.setter
    def valor_transacao(self, valor_transacao):
        """
        Sets the valor_transacao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Valor da transa\u00C3\u00A7\u00C3\u00A3o com duas casas decimais para os centavos.

        :param valor_transacao: The valor_transacao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: float
        """
        self._valor_transacao = valor_transacao

    @property
    def numero_real_cartao(self):
        """
        Gets the numero_real_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero Real do Cart\u00C3\u00A3o.

        :return: The numero_real_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: str
        """
        return self._numero_real_cartao

    @numero_real_cartao.setter
    def numero_real_cartao(self, numero_real_cartao):
        """
        Sets the numero_real_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero Real do Cart\u00C3\u00A3o.

        :param numero_real_cartao: The numero_real_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: str
        """
        self._numero_real_cartao = numero_real_cartao

    @property
    def data_validade_cartao(self):
        """
        Gets the data_validade_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Data de Validade do Cart\u00C3\u00A3o. Ex: AAMM

        :return: The data_validade_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: str
        """
        return self._data_validade_cartao

    @data_validade_cartao.setter
    def data_validade_cartao(self, data_validade_cartao):
        """
        Sets the data_validade_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Data de Validade do Cart\u00C3\u00A3o. Ex: AAMM

        :param data_validade_cartao: The data_validade_cartao of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: str
        """
        self._data_validade_cartao = data_validade_cartao

    @property
    def numero_meses_carencia(self):
        """
        Gets the numero_meses_carencia of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Representa o N\u00C3\u00BAmero de Meses concedido como car\u00C3\u00AAncia.

        :return: The numero_meses_carencia of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: int
        """
        return self._numero_meses_carencia

    @numero_meses_carencia.setter
    def numero_meses_carencia(self, numero_meses_carencia):
        """
        Sets the numero_meses_carencia of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Representa o N\u00C3\u00BAmero de Meses concedido como car\u00C3\u00AAncia.

        :param numero_meses_carencia: The numero_meses_carencia of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: int
        """
        self._numero_meses_carencia = numero_meses_carencia

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero do Estabelecimento (N\u00C3\u00BAmero+DV).

        :return: The numero_estabelecimento of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: int
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        N\u00C3\u00BAmero do Estabelecimento (N\u00C3\u00BAmero+DV).

        :param numero_estabelecimento: The numero_estabelecimento of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: int
        """
        self._numero_estabelecimento = numero_estabelecimento

    @property
    def data_hora_terminal(self):
        """
        Gets the data_hora_terminal of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Apresenta a data e hora local da consulta yyyy-MM-dd'T'HH:mm:ss.SSSZ. Ex: 2000-10-31T01:30:00.000-05:00

        :return: The data_hora_terminal of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: str
        """
        return self._data_hora_terminal

    @data_hora_terminal.setter
    def data_hora_terminal(self, data_hora_terminal):
        """
        Sets the data_hora_terminal of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Apresenta a data e hora local da consulta yyyy-MM-dd'T'HH:mm:ss.SSSZ. Ex: 2000-10-31T01:30:00.000-05:00

        :param data_hora_terminal: The data_hora_terminal of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: str
        """
        self._data_hora_terminal = data_hora_terminal

    @property
    def terminal_requisitante(self):
        """
        Gets the terminal_requisitante of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Apresenta a identifica\u00C3\u00A7\u00C3\u00A3o do terminal requisitante

        :return: The terminal_requisitante of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :rtype: str
        """
        return self._terminal_requisitante

    @terminal_requisitante.setter
    def terminal_requisitante(self, terminal_requisitante):
        """
        Sets the terminal_requisitante of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        Apresenta a identifica\u00C3\u00A7\u00C3\u00A3o do terminal requisitante

        :param terminal_requisitante: The terminal_requisitante of this PlanoParcelamentoTransferenciaCreditoContaBancariaRequest.
        :type: str
        """
        self._terminal_requisitante = terminal_requisitante

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
