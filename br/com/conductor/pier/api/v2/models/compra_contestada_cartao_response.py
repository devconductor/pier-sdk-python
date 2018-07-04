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


class CompraContestadaCartaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CompraContestadaCartaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_cartao': 'int',
            'aging_contestacao': 'int',
            'cartao': 'str',
            'nome': 'str',
            'bandeira': 'str'
        }

        self.attribute_map = {
            'id_cartao': 'idCartao',
            'aging_contestacao': 'agingContestacao',
            'cartao': 'cartao',
            'nome': 'nome',
            'bandeira': 'bandeira'
        }

        self._id_cartao = None
        self._aging_contestacao = None
        self._cartao = None
        self._nome = None
        self._bandeira = None

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_id_cartao_value}}}

        :return: The id_cartao of this CompraContestadaCartaoResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_id_cartao_value}}}

        :param id_cartao: The id_cartao of this CompraContestadaCartaoResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def aging_contestacao(self):
        """
        Gets the aging_contestacao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_aging_contestacao_value}}}

        :return: The aging_contestacao of this CompraContestadaCartaoResponse.
        :rtype: int
        """
        return self._aging_contestacao

    @aging_contestacao.setter
    def aging_contestacao(self, aging_contestacao):
        """
        Sets the aging_contestacao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_aging_contestacao_value}}}

        :param aging_contestacao: The aging_contestacao of this CompraContestadaCartaoResponse.
        :type: int
        """
        self._aging_contestacao = aging_contestacao

    @property
    def cartao(self):
        """
        Gets the cartao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_cartao_value}}}

        :return: The cartao of this CompraContestadaCartaoResponse.
        :rtype: str
        """
        return self._cartao

    @cartao.setter
    def cartao(self, cartao):
        """
        Sets the cartao of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_cartao_value}}}

        :param cartao: The cartao of this CompraContestadaCartaoResponse.
        :type: str
        """
        self._cartao = cartao

    @property
    def nome(self):
        """
        Gets the nome of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_nome_value}}}

        :return: The nome of this CompraContestadaCartaoResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_nome_value}}}

        :param nome: The nome of this CompraContestadaCartaoResponse.
        :type: str
        """
        self._nome = nome

    @property
    def bandeira(self):
        """
        Gets the bandeira of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_bandeira_value}}}

        :return: The bandeira of this CompraContestadaCartaoResponse.
        :rtype: str
        """
        return self._bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        """
        Sets the bandeira of this CompraContestadaCartaoResponse.
        {{{compra_contestada_cartao_response_bandeira_value}}}

        :param bandeira: The bandeira of this CompraContestadaCartaoResponse.
        :type: str
        """
        self._bandeira = bandeira

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
