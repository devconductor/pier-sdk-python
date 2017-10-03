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


class ControleVencimentoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ControleVencimentoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_vencimento': 'str',
            'data_prevista_corte': 'str',
            'data_hora_realizacao_corte': 'str',
            'data_prevista_faturamento': 'str',
            'data_hora_realizacao_faturamento': 'str',
            'data_real_vencimento': 'str'
        }

        self.attribute_map = {
            'data_vencimento': 'dataVencimento',
            'data_prevista_corte': 'dataPrevistaCorte',
            'data_hora_realizacao_corte': 'dataHoraRealizacaoCorte',
            'data_prevista_faturamento': 'dataPrevistaFaturamento',
            'data_hora_realizacao_faturamento': 'dataHoraRealizacaoFaturamento',
            'data_real_vencimento': 'dataRealVencimento'
        }

        self._data_vencimento = None
        self._data_prevista_corte = None
        self._data_hora_realizacao_corte = None
        self._data_prevista_faturamento = None
        self._data_hora_realizacao_faturamento = None
        self._data_real_vencimento = None

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this ControleVencimentoResponse.
         Indica a data de vencimento das faturas

        :return: The data_vencimento of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this ControleVencimentoResponse.
         Indica a data de vencimento das faturas

        :param data_vencimento: The data_vencimento of this ControleVencimentoResponse.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def data_prevista_corte(self):
        """
        Gets the data_prevista_corte of this ControleVencimentoResponse.
         Indica a data prevista para a realiza\u00C3\u00A7\u00C3\u00A3o do Corte das faturas

        :return: The data_prevista_corte of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_prevista_corte

    @data_prevista_corte.setter
    def data_prevista_corte(self, data_prevista_corte):
        """
        Sets the data_prevista_corte of this ControleVencimentoResponse.
         Indica a data prevista para a realiza\u00C3\u00A7\u00C3\u00A3o do Corte das faturas

        :param data_prevista_corte: The data_prevista_corte of this ControleVencimentoResponse.
        :type: str
        """
        self._data_prevista_corte = data_prevista_corte

    @property
    def data_hora_realizacao_corte(self):
        """
        Gets the data_hora_realizacao_corte of this ControleVencimentoResponse.
        Indica a data e a hora que fora realizada a realiza\u00C3\u00A7\u00C3\u00A3o do Corte das faturas

        :return: The data_hora_realizacao_corte of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_hora_realizacao_corte

    @data_hora_realizacao_corte.setter
    def data_hora_realizacao_corte(self, data_hora_realizacao_corte):
        """
        Sets the data_hora_realizacao_corte of this ControleVencimentoResponse.
        Indica a data e a hora que fora realizada a realiza\u00C3\u00A7\u00C3\u00A3o do Corte das faturas

        :param data_hora_realizacao_corte: The data_hora_realizacao_corte of this ControleVencimentoResponse.
        :type: str
        """
        self._data_hora_realizacao_corte = data_hora_realizacao_corte

    @property
    def data_prevista_faturamento(self):
        """
        Gets the data_prevista_faturamento of this ControleVencimentoResponse.
        Indica a data prevista para a realiza\u00C3\u00A7\u00C3\u00A3o do faturamento

        :return: The data_prevista_faturamento of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_prevista_faturamento

    @data_prevista_faturamento.setter
    def data_prevista_faturamento(self, data_prevista_faturamento):
        """
        Sets the data_prevista_faturamento of this ControleVencimentoResponse.
        Indica a data prevista para a realiza\u00C3\u00A7\u00C3\u00A3o do faturamento

        :param data_prevista_faturamento: The data_prevista_faturamento of this ControleVencimentoResponse.
        :type: str
        """
        self._data_prevista_faturamento = data_prevista_faturamento

    @property
    def data_hora_realizacao_faturamento(self):
        """
        Gets the data_hora_realizacao_faturamento of this ControleVencimentoResponse.
        Indica a data e a hora que fora realizado o faturamento

        :return: The data_hora_realizacao_faturamento of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_hora_realizacao_faturamento

    @data_hora_realizacao_faturamento.setter
    def data_hora_realizacao_faturamento(self, data_hora_realizacao_faturamento):
        """
        Sets the data_hora_realizacao_faturamento of this ControleVencimentoResponse.
        Indica a data e a hora que fora realizado o faturamento

        :param data_hora_realizacao_faturamento: The data_hora_realizacao_faturamento of this ControleVencimentoResponse.
        :type: str
        """
        self._data_hora_realizacao_faturamento = data_hora_realizacao_faturamento

    @property
    def data_real_vencimento(self):
        """
        Gets the data_real_vencimento of this ControleVencimentoResponse.
        Indica o dia \u00C3\u00BAtil que ser\u00C3\u00A1 considerado como a data de vencimento

        :return: The data_real_vencimento of this ControleVencimentoResponse.
        :rtype: str
        """
        return self._data_real_vencimento

    @data_real_vencimento.setter
    def data_real_vencimento(self, data_real_vencimento):
        """
        Sets the data_real_vencimento of this ControleVencimentoResponse.
        Indica o dia \u00C3\u00BAtil que ser\u00C3\u00A1 considerado como a data de vencimento

        :param data_real_vencimento: The data_real_vencimento of this ControleVencimentoResponse.
        :type: str
        """
        self._data_real_vencimento = data_real_vencimento

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
