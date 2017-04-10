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


class PessoaDetalheResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PessoaDetalheResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'list[PessoaDetalheResponse]',
            'first': 'bool',
            'first_page': 'bool',
            'has_content': 'bool',
            'has_next_page': 'bool',
            'has_previous_page': 'bool',
            'id_pessoa': 'int',
            'last': 'bool',
            'next_page': 'int',
            'number': 'int',
            'number_of_elements': 'int',
            'previous_page': 'int',
            'size': 'int',
            'total_elements': 'int',
            'total_pages': 'int',
            'nome_mae': 'str',
            'id_estado_civil': 'int',
            'profissao': 'str',
            'id_natureza_ocupacao': 'int',
            'id_nacionalidade': 'int',
            'numero_agencia': 'int',
            'numero_conta_corrente': 'str',
            'email': 'str',
            'nome_empresa': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'first': 'first',
            'first_page': 'firstPage',
            'has_content': 'hasContent',
            'has_next_page': 'hasNextPage',
            'has_previous_page': 'hasPreviousPage',
            'id_pessoa': 'idPessoa',
            'last': 'last',
            'next_page': 'nextPage',
            'number': 'number',
            'number_of_elements': 'numberOfElements',
            'previous_page': 'previousPage',
            'size': 'size',
            'total_elements': 'totalElements',
            'total_pages': 'totalPages',
            'nome_mae': 'nomeMae',
            'id_estado_civil': 'idEstadoCivil',
            'profissao': 'profissao',
            'id_natureza_ocupacao': 'idNaturezaOcupacao',
            'id_nacionalidade': 'idNacionalidade',
            'numero_agencia': 'numeroAgencia',
            'numero_conta_corrente': 'numeroContaCorrente',
            'email': 'email',
            'nome_empresa': 'nomeEmpresa'
        }

        self._content = None
        self._first = None
        self._first_page = None
        self._has_content = None
        self._has_next_page = None
        self._has_previous_page = None
        self._id_pessoa = None
        self._last = None
        self._next_page = None
        self._number = None
        self._number_of_elements = None
        self._previous_page = None
        self._size = None
        self._total_elements = None
        self._total_pages = None
        self._nome_mae = None
        self._id_estado_civil = None
        self._profissao = None
        self._id_natureza_ocupacao = None
        self._id_nacionalidade = None
        self._numero_agencia = None
        self._numero_conta_corrente = None
        self._email = None
        self._nome_empresa = None

    @property
    def content(self):
        """
        Gets the content of this PessoaDetalheResponse.


        :return: The content of this PessoaDetalheResponse.
        :rtype: list[PessoaDetalheResponse]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this PessoaDetalheResponse.


        :param content: The content of this PessoaDetalheResponse.
        :type: list[PessoaDetalheResponse]
        """
        self._content = content

    @property
    def first(self):
        """
        Gets the first of this PessoaDetalheResponse.


        :return: The first of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this PessoaDetalheResponse.


        :param first: The first of this PessoaDetalheResponse.
        :type: bool
        """
        self._first = first

    @property
    def first_page(self):
        """
        Gets the first_page of this PessoaDetalheResponse.


        :return: The first_page of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """
        Sets the first_page of this PessoaDetalheResponse.


        :param first_page: The first_page of this PessoaDetalheResponse.
        :type: bool
        """
        self._first_page = first_page

    @property
    def has_content(self):
        """
        Gets the has_content of this PessoaDetalheResponse.


        :return: The has_content of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._has_content

    @has_content.setter
    def has_content(self, has_content):
        """
        Sets the has_content of this PessoaDetalheResponse.


        :param has_content: The has_content of this PessoaDetalheResponse.
        :type: bool
        """
        self._has_content = has_content

    @property
    def has_next_page(self):
        """
        Gets the has_next_page of this PessoaDetalheResponse.


        :return: The has_next_page of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, has_next_page):
        """
        Sets the has_next_page of this PessoaDetalheResponse.


        :param has_next_page: The has_next_page of this PessoaDetalheResponse.
        :type: bool
        """
        self._has_next_page = has_next_page

    @property
    def has_previous_page(self):
        """
        Gets the has_previous_page of this PessoaDetalheResponse.


        :return: The has_previous_page of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._has_previous_page

    @has_previous_page.setter
    def has_previous_page(self, has_previous_page):
        """
        Sets the has_previous_page of this PessoaDetalheResponse.


        :param has_previous_page: The has_previous_page of this PessoaDetalheResponse.
        :type: bool
        """
        self._has_previous_page = has_previous_page

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this PessoaDetalheResponse.
        C\u00C3\u00B3digo identificador da pessoa

        :return: The id_pessoa of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this PessoaDetalheResponse.
        C\u00C3\u00B3digo identificador da pessoa

        :param id_pessoa: The id_pessoa of this PessoaDetalheResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def last(self):
        """
        Gets the last of this PessoaDetalheResponse.


        :return: The last of this PessoaDetalheResponse.
        :rtype: bool
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this PessoaDetalheResponse.


        :param last: The last of this PessoaDetalheResponse.
        :type: bool
        """
        self._last = last

    @property
    def next_page(self):
        """
        Gets the next_page of this PessoaDetalheResponse.


        :return: The next_page of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """
        Sets the next_page of this PessoaDetalheResponse.


        :param next_page: The next_page of this PessoaDetalheResponse.
        :type: int
        """
        self._next_page = next_page

    @property
    def number(self):
        """
        Gets the number of this PessoaDetalheResponse.


        :return: The number of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this PessoaDetalheResponse.


        :param number: The number of this PessoaDetalheResponse.
        :type: int
        """
        self._number = number

    @property
    def number_of_elements(self):
        """
        Gets the number_of_elements of this PessoaDetalheResponse.


        :return: The number_of_elements of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """
        Sets the number_of_elements of this PessoaDetalheResponse.


        :param number_of_elements: The number_of_elements of this PessoaDetalheResponse.
        :type: int
        """
        self._number_of_elements = number_of_elements

    @property
    def previous_page(self):
        """
        Gets the previous_page of this PessoaDetalheResponse.


        :return: The previous_page of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """
        Sets the previous_page of this PessoaDetalheResponse.


        :param previous_page: The previous_page of this PessoaDetalheResponse.
        :type: int
        """
        self._previous_page = previous_page

    @property
    def size(self):
        """
        Gets the size of this PessoaDetalheResponse.


        :return: The size of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this PessoaDetalheResponse.


        :param size: The size of this PessoaDetalheResponse.
        :type: int
        """
        self._size = size

    @property
    def total_elements(self):
        """
        Gets the total_elements of this PessoaDetalheResponse.


        :return: The total_elements of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """
        Sets the total_elements of this PessoaDetalheResponse.


        :param total_elements: The total_elements of this PessoaDetalheResponse.
        :type: int
        """
        self._total_elements = total_elements

    @property
    def total_pages(self):
        """
        Gets the total_pages of this PessoaDetalheResponse.


        :return: The total_pages of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this PessoaDetalheResponse.


        :param total_pages: The total_pages of this PessoaDetalheResponse.
        :type: int
        """
        self._total_pages = total_pages

    @property
    def nome_mae(self):
        """
        Gets the nome_mae of this PessoaDetalheResponse.
        Apresenta o nome da m\u00C3\u00A3e da pessoa fisica

        :return: The nome_mae of this PessoaDetalheResponse.
        :rtype: str
        """
        return self._nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae):
        """
        Sets the nome_mae of this PessoaDetalheResponse.
        Apresenta o nome da m\u00C3\u00A3e da pessoa fisica

        :param nome_mae: The nome_mae of this PessoaDetalheResponse.
        :type: str
        """
        self._nome_mae = nome_mae

    @property
    def id_estado_civil(self):
        """
        Gets the id_estado_civil of this PessoaDetalheResponse.
        Id Estado civil da pessoa fisica

        :return: The id_estado_civil of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._id_estado_civil

    @id_estado_civil.setter
    def id_estado_civil(self, id_estado_civil):
        """
        Sets the id_estado_civil of this PessoaDetalheResponse.
        Id Estado civil da pessoa fisica

        :param id_estado_civil: The id_estado_civil of this PessoaDetalheResponse.
        :type: int
        """
        self._id_estado_civil = id_estado_civil

    @property
    def profissao(self):
        """
        Gets the profissao of this PessoaDetalheResponse.
        Profiss\u00C3\u00A3o da pessoa fisica

        :return: The profissao of this PessoaDetalheResponse.
        :rtype: str
        """
        return self._profissao

    @profissao.setter
    def profissao(self, profissao):
        """
        Sets the profissao of this PessoaDetalheResponse.
        Profiss\u00C3\u00A3o da pessoa fisica

        :param profissao: The profissao of this PessoaDetalheResponse.
        :type: str
        """
        self._profissao = profissao

    @property
    def id_natureza_ocupacao(self):
        """
        Gets the id_natureza_ocupacao of this PessoaDetalheResponse.
        Id Natureza Ocupa\u00C3\u00A7\u00C3\u00A3o da pessoa fisica

        :return: The id_natureza_ocupacao of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._id_natureza_ocupacao

    @id_natureza_ocupacao.setter
    def id_natureza_ocupacao(self, id_natureza_ocupacao):
        """
        Sets the id_natureza_ocupacao of this PessoaDetalheResponse.
        Id Natureza Ocupa\u00C3\u00A7\u00C3\u00A3o da pessoa fisica

        :param id_natureza_ocupacao: The id_natureza_ocupacao of this PessoaDetalheResponse.
        :type: int
        """
        self._id_natureza_ocupacao = id_natureza_ocupacao

    @property
    def id_nacionalidade(self):
        """
        Gets the id_nacionalidade of this PessoaDetalheResponse.
        Id Nacionalidade da pessoa fisica

        :return: The id_nacionalidade of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._id_nacionalidade

    @id_nacionalidade.setter
    def id_nacionalidade(self, id_nacionalidade):
        """
        Sets the id_nacionalidade of this PessoaDetalheResponse.
        Id Nacionalidade da pessoa fisica

        :param id_nacionalidade: The id_nacionalidade of this PessoaDetalheResponse.
        :type: int
        """
        self._id_nacionalidade = id_nacionalidade

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this PessoaDetalheResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :return: The numero_agencia of this PessoaDetalheResponse.
        :rtype: int
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this PessoaDetalheResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :param numero_agencia: The numero_agencia of this PessoaDetalheResponse.
        :type: int
        """
        self._numero_agencia = numero_agencia

    @property
    def numero_conta_corrente(self):
        """
        Gets the numero_conta_corrente of this PessoaDetalheResponse.
        N\u00C3\u00BAmero da conta corrente.

        :return: The numero_conta_corrente of this PessoaDetalheResponse.
        :rtype: str
        """
        return self._numero_conta_corrente

    @numero_conta_corrente.setter
    def numero_conta_corrente(self, numero_conta_corrente):
        """
        Sets the numero_conta_corrente of this PessoaDetalheResponse.
        N\u00C3\u00BAmero da conta corrente.

        :param numero_conta_corrente: The numero_conta_corrente of this PessoaDetalheResponse.
        :type: str
        """
        self._numero_conta_corrente = numero_conta_corrente

    @property
    def email(self):
        """
        Gets the email of this PessoaDetalheResponse.
        Email da pessoa fisica

        :return: The email of this PessoaDetalheResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PessoaDetalheResponse.
        Email da pessoa fisica

        :param email: The email of this PessoaDetalheResponse.
        :type: str
        """
        self._email = email

    @property
    def nome_empresa(self):
        """
        Gets the nome_empresa of this PessoaDetalheResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :return: The nome_empresa of this PessoaDetalheResponse.
        :rtype: str
        """
        return self._nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        """
        Sets the nome_empresa of this PessoaDetalheResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :param nome_empresa: The nome_empresa of this PessoaDetalheResponse.
        :type: str
        """
        self._nome_empresa = nome_empresa

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

