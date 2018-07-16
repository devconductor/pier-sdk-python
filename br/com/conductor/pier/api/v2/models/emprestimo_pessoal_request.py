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


class EmprestimoPessoalRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EmprestimoPessoalRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'valor_solicitado': 'float',
            'numero_parcelas': 'int',
            'taxa_juros': 'float',
            'periodo_taxa': 'str',
            'sistema_amortizacao': 'str',
            'numero_meses_carencia': 'int'
        }

        self.attribute_map = {
            'valor_solicitado': 'valorSolicitado',
            'numero_parcelas': 'numeroParcelas',
            'taxa_juros': 'taxaJuros',
            'periodo_taxa': 'periodoTaxa',
            'sistema_amortizacao': 'sistemaAmortizacao',
            'numero_meses_carencia': 'numeroMesesCarencia'
        }

        self._valor_solicitado = None
        self._numero_parcelas = None
        self._taxa_juros = None
        self._periodo_taxa = None
        self._sistema_amortizacao = None
        self._numero_meses_carencia = None

    @property
    def valor_solicitado(self):
        """
        Gets the valor_solicitado of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_valor_solicitado_value}}}

        :return: The valor_solicitado of this EmprestimoPessoalRequest.
        :rtype: float
        """
        return self._valor_solicitado

    @valor_solicitado.setter
    def valor_solicitado(self, valor_solicitado):
        """
        Sets the valor_solicitado of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_valor_solicitado_value}}}

        :param valor_solicitado: The valor_solicitado of this EmprestimoPessoalRequest.
        :type: float
        """
        self._valor_solicitado = valor_solicitado

    @property
    def numero_parcelas(self):
        """
        Gets the numero_parcelas of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_numero_parcelas_value}}}

        :return: The numero_parcelas of this EmprestimoPessoalRequest.
        :rtype: int
        """
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas):
        """
        Sets the numero_parcelas of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_numero_parcelas_value}}}

        :param numero_parcelas: The numero_parcelas of this EmprestimoPessoalRequest.
        :type: int
        """
        self._numero_parcelas = numero_parcelas

    @property
    def taxa_juros(self):
        """
        Gets the taxa_juros of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_taxa_juros_value}}}

        :return: The taxa_juros of this EmprestimoPessoalRequest.
        :rtype: float
        """
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        """
        Sets the taxa_juros of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_taxa_juros_value}}}

        :param taxa_juros: The taxa_juros of this EmprestimoPessoalRequest.
        :type: float
        """
        self._taxa_juros = taxa_juros

    @property
    def periodo_taxa(self):
        """
        Gets the periodo_taxa of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_periodo_taxa_value}}}

        :return: The periodo_taxa of this EmprestimoPessoalRequest.
        :rtype: str
        """
        return self._periodo_taxa

    @periodo_taxa.setter
    def periodo_taxa(self, periodo_taxa):
        """
        Sets the periodo_taxa of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_periodo_taxa_value}}}

        :param periodo_taxa: The periodo_taxa of this EmprestimoPessoalRequest.
        :type: str
        """
        self._periodo_taxa = periodo_taxa

    @property
    def sistema_amortizacao(self):
        """
        Gets the sistema_amortizacao of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_sistema_amortizacao_value}}}

        :return: The sistema_amortizacao of this EmprestimoPessoalRequest.
        :rtype: str
        """
        return self._sistema_amortizacao

    @sistema_amortizacao.setter
    def sistema_amortizacao(self, sistema_amortizacao):
        """
        Sets the sistema_amortizacao of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_sistema_amortizacao_value}}}

        :param sistema_amortizacao: The sistema_amortizacao of this EmprestimoPessoalRequest.
        :type: str
        """
        self._sistema_amortizacao = sistema_amortizacao

    @property
    def numero_meses_carencia(self):
        """
        Gets the numero_meses_carencia of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_numero_meses_carencia_value}}}

        :return: The numero_meses_carencia of this EmprestimoPessoalRequest.
        :rtype: int
        """
        return self._numero_meses_carencia

    @numero_meses_carencia.setter
    def numero_meses_carencia(self, numero_meses_carencia):
        """
        Sets the numero_meses_carencia of this EmprestimoPessoalRequest.
        {{{emprestimo_pessoal_request_numero_meses_carencia_value}}}

        :param numero_meses_carencia: The numero_meses_carencia of this EmprestimoPessoalRequest.
        :type: int
        """
        self._numero_meses_carencia = numero_meses_carencia

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

