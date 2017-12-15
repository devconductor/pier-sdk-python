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


class AntecipacaoSimuladaLoteResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoSimuladaLoteResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'valor_total_antecipado': 'float',
            'valor_total_desconto': 'float',
            'valor_total_com_desconto': 'float',
            'antecipacoes_simuladas': 'list[AntecipacaoSimuladaResponse]'
        }

        self.attribute_map = {
            'valor_total_antecipado': 'valorTotalAntecipado',
            'valor_total_desconto': 'valorTotalDesconto',
            'valor_total_com_desconto': 'valorTotalComDesconto',
            'antecipacoes_simuladas': 'antecipacoesSimuladas'
        }

        self._valor_total_antecipado = None
        self._valor_total_desconto = None
        self._valor_total_com_desconto = None
        self._antecipacoes_simuladas = None

    @property
    def valor_total_antecipado(self):
        """
        Gets the valor_total_antecipado of this AntecipacaoSimuladaLoteResponse.
        Valor total antecipado.

        :return: The valor_total_antecipado of this AntecipacaoSimuladaLoteResponse.
        :rtype: float
        """
        return self._valor_total_antecipado

    @valor_total_antecipado.setter
    def valor_total_antecipado(self, valor_total_antecipado):
        """
        Sets the valor_total_antecipado of this AntecipacaoSimuladaLoteResponse.
        Valor total antecipado.

        :param valor_total_antecipado: The valor_total_antecipado of this AntecipacaoSimuladaLoteResponse.
        :type: float
        """
        self._valor_total_antecipado = valor_total_antecipado

    @property
    def valor_total_desconto(self):
        """
        Gets the valor_total_desconto of this AntecipacaoSimuladaLoteResponse.
        Valor total do desconto.

        :return: The valor_total_desconto of this AntecipacaoSimuladaLoteResponse.
        :rtype: float
        """
        return self._valor_total_desconto

    @valor_total_desconto.setter
    def valor_total_desconto(self, valor_total_desconto):
        """
        Sets the valor_total_desconto of this AntecipacaoSimuladaLoteResponse.
        Valor total do desconto.

        :param valor_total_desconto: The valor_total_desconto of this AntecipacaoSimuladaLoteResponse.
        :type: float
        """
        self._valor_total_desconto = valor_total_desconto

    @property
    def valor_total_com_desconto(self):
        """
        Gets the valor_total_com_desconto of this AntecipacaoSimuladaLoteResponse.
        Valor total antecipado com o desconto.

        :return: The valor_total_com_desconto of this AntecipacaoSimuladaLoteResponse.
        :rtype: float
        """
        return self._valor_total_com_desconto

    @valor_total_com_desconto.setter
    def valor_total_com_desconto(self, valor_total_com_desconto):
        """
        Sets the valor_total_com_desconto of this AntecipacaoSimuladaLoteResponse.
        Valor total antecipado com o desconto.

        :param valor_total_com_desconto: The valor_total_com_desconto of this AntecipacaoSimuladaLoteResponse.
        :type: float
        """
        self._valor_total_com_desconto = valor_total_com_desconto

    @property
    def antecipacoes_simuladas(self):
        """
        Gets the antecipacoes_simuladas of this AntecipacaoSimuladaLoteResponse.
        Antecipa\u00C3\u00A7\u00C3\u00B5es Simuladas.

        :return: The antecipacoes_simuladas of this AntecipacaoSimuladaLoteResponse.
        :rtype: list[AntecipacaoSimuladaResponse]
        """
        return self._antecipacoes_simuladas

    @antecipacoes_simuladas.setter
    def antecipacoes_simuladas(self, antecipacoes_simuladas):
        """
        Sets the antecipacoes_simuladas of this AntecipacaoSimuladaLoteResponse.
        Antecipa\u00C3\u00A7\u00C3\u00B5es Simuladas.

        :param antecipacoes_simuladas: The antecipacoes_simuladas of this AntecipacaoSimuladaLoteResponse.
        :type: list[AntecipacaoSimuladaResponse]
        """
        self._antecipacoes_simuladas = antecipacoes_simuladas

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
