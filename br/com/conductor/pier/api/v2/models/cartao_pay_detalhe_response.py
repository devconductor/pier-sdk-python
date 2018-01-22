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


class CartaoPayDetalheResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CartaoPayDetalheResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'numero_cartao': 'str',
            'data_validade_cartao': 'str',
            'nome_impresso': 'str',
            'id_entidade': 'int',
            'nome_entidade': 'str',
            'status': 'str',
            'cvv': 'str',
            'data_validade_chave_criptograma': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'numero_cartao': 'numeroCartao',
            'data_validade_cartao': 'dataValidadeCartao',
            'nome_impresso': 'nomeImpresso',
            'id_entidade': 'idEntidade',
            'nome_entidade': 'nomeEntidade',
            'status': 'status',
            'cvv': 'cvv',
            'data_validade_chave_criptograma': 'dataValidadeChaveCriptograma'
        }

        self._id = None
        self._numero_cartao = None
        self._data_validade_cartao = None
        self._nome_impresso = None
        self._id_entidade = None
        self._nome_entidade = None
        self._status = None
        self._cvv = None
        self._data_validade_chave_criptograma = None

    @property
    def id(self):
        """
        Gets the id of this CartaoPayDetalheResponse.
        Id do cart\u00C3\u00A3o

        :return: The id of this CartaoPayDetalheResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CartaoPayDetalheResponse.
        Id do cart\u00C3\u00A3o

        :param id: The id of this CartaoPayDetalheResponse.
        :type: int
        """
        self._id = id

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this CartaoPayDetalheResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o real criptografado

        :return: The numero_cartao of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this CartaoPayDetalheResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o real criptografado

        :param numero_cartao: The numero_cartao of this CartaoPayDetalheResponse.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def data_validade_cartao(self):
        """
        Gets the data_validade_cartao of this CartaoPayDetalheResponse.
        Data de validade do cart\u00C3\u00A3o

        :return: The data_validade_cartao of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._data_validade_cartao

    @data_validade_cartao.setter
    def data_validade_cartao(self, data_validade_cartao):
        """
        Sets the data_validade_cartao of this CartaoPayDetalheResponse.
        Data de validade do cart\u00C3\u00A3o

        :param data_validade_cartao: The data_validade_cartao of this CartaoPayDetalheResponse.
        :type: str
        """
        self._data_validade_cartao = data_validade_cartao

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this CartaoPayDetalheResponse.
        Nome impresso no cart\u00C3\u00A3o criptografado

        :return: The nome_impresso of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this CartaoPayDetalheResponse.
        Nome impresso no cart\u00C3\u00A3o criptografado

        :param nome_impresso: The nome_impresso of this CartaoPayDetalheResponse.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def id_entidade(self):
        """
        Gets the id_entidade of this CartaoPayDetalheResponse.
        Identificador do emissor do cart\u00C3\u00A3o

        :return: The id_entidade of this CartaoPayDetalheResponse.
        :rtype: int
        """
        return self._id_entidade

    @id_entidade.setter
    def id_entidade(self, id_entidade):
        """
        Sets the id_entidade of this CartaoPayDetalheResponse.
        Identificador do emissor do cart\u00C3\u00A3o

        :param id_entidade: The id_entidade of this CartaoPayDetalheResponse.
        :type: int
        """
        self._id_entidade = id_entidade

    @property
    def nome_entidade(self):
        """
        Gets the nome_entidade of this CartaoPayDetalheResponse.
        Nome do emissor do cart\u00C3\u00A3o

        :return: The nome_entidade of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._nome_entidade

    @nome_entidade.setter
    def nome_entidade(self, nome_entidade):
        """
        Sets the nome_entidade of this CartaoPayDetalheResponse.
        Nome do emissor do cart\u00C3\u00A3o

        :param nome_entidade: The nome_entidade of this CartaoPayDetalheResponse.
        :type: str
        """
        self._nome_entidade = nome_entidade

    @property
    def status(self):
        """
        Gets the status of this CartaoPayDetalheResponse.
        Status do cart\u00C3\u00A3o

        :return: The status of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CartaoPayDetalheResponse.
        Status do cart\u00C3\u00A3o

        :param status: The status of this CartaoPayDetalheResponse.
        :type: str
        """
        allowed_values = ["ATIVO", "INATIVO", "BLOQUEADO"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def cvv(self):
        """
        Gets the cvv of this CartaoPayDetalheResponse.
        CVV do cart\u00C3\u00A3o criptografado

        :return: The cvv of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """
        Sets the cvv of this CartaoPayDetalheResponse.
        CVV do cart\u00C3\u00A3o criptografado

        :param cvv: The cvv of this CartaoPayDetalheResponse.
        :type: str
        """
        self._cvv = cvv

    @property
    def data_validade_chave_criptograma(self):
        """
        Gets the data_validade_chave_criptograma of this CartaoPayDetalheResponse.
        Data de validade da chave do criptograma

        :return: The data_validade_chave_criptograma of this CartaoPayDetalheResponse.
        :rtype: str
        """
        return self._data_validade_chave_criptograma

    @data_validade_chave_criptograma.setter
    def data_validade_chave_criptograma(self, data_validade_chave_criptograma):
        """
        Sets the data_validade_chave_criptograma of this CartaoPayDetalheResponse.
        Data de validade da chave do criptograma

        :param data_validade_chave_criptograma: The data_validade_chave_criptograma of this CartaoPayDetalheResponse.
        :type: str
        """
        self._data_validade_chave_criptograma = data_validade_chave_criptograma

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

