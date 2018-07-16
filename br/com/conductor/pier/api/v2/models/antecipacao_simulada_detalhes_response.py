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


class AntecipacaoSimuladaDetalhesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoSimuladaDetalhesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'quantidade_parcelas': 'int',
            'valor_parcelas': 'float',
            'valor_desconto': 'float',
            'valor_parcelas_desconto': 'float'
        }

        self.attribute_map = {
            'quantidade_parcelas': 'quantidadeParcelas',
            'valor_parcelas': 'valorParcelas',
            'valor_desconto': 'valorDesconto',
            'valor_parcelas_desconto': 'valorParcelasDesconto'
        }

        self._quantidade_parcelas = None
        self._valor_parcelas = None
        self._valor_desconto = None
        self._valor_parcelas_desconto = None

    @property
    def quantidade_parcelas(self):
        """
        Gets the quantidade_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_quantidade_parcelas_value}}}

        :return: The quantidade_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        :rtype: int
        """
        return self._quantidade_parcelas

    @quantidade_parcelas.setter
    def quantidade_parcelas(self, quantidade_parcelas):
        """
        Sets the quantidade_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_quantidade_parcelas_value}}}

        :param quantidade_parcelas: The quantidade_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        :type: int
        """
        self._quantidade_parcelas = quantidade_parcelas

    @property
    def valor_parcelas(self):
        """
        Gets the valor_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_parcelas_value}}}

        :return: The valor_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        :rtype: float
        """
        return self._valor_parcelas

    @valor_parcelas.setter
    def valor_parcelas(self, valor_parcelas):
        """
        Sets the valor_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_parcelas_value}}}

        :param valor_parcelas: The valor_parcelas of this AntecipacaoSimuladaDetalhesResponse.
        :type: float
        """
        self._valor_parcelas = valor_parcelas

    @property
    def valor_desconto(self):
        """
        Gets the valor_desconto of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_desconto_value}}}

        :return: The valor_desconto of this AntecipacaoSimuladaDetalhesResponse.
        :rtype: float
        """
        return self._valor_desconto

    @valor_desconto.setter
    def valor_desconto(self, valor_desconto):
        """
        Sets the valor_desconto of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_desconto_value}}}

        :param valor_desconto: The valor_desconto of this AntecipacaoSimuladaDetalhesResponse.
        :type: float
        """
        self._valor_desconto = valor_desconto

    @property
    def valor_parcelas_desconto(self):
        """
        Gets the valor_parcelas_desconto of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_parcelas_desconto_value}}}

        :return: The valor_parcelas_desconto of this AntecipacaoSimuladaDetalhesResponse.
        :rtype: float
        """
        return self._valor_parcelas_desconto

    @valor_parcelas_desconto.setter
    def valor_parcelas_desconto(self, valor_parcelas_desconto):
        """
        Sets the valor_parcelas_desconto of this AntecipacaoSimuladaDetalhesResponse.
        {{{antecipacao_simulada_detalhes_response_valor_parcelas_desconto_value}}}

        :param valor_parcelas_desconto: The valor_parcelas_desconto of this AntecipacaoSimuladaDetalhesResponse.
        :type: float
        """
        self._valor_parcelas_desconto = valor_parcelas_desconto

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

