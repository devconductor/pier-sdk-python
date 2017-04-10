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


class Estabelecimento(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Estabelecimento - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'numero_estabelecimento': 'str',
            'numero_receita_federal': 'int',
            'nome': 'str',
            'descricao': 'str',
            'nome_fantasia': 'str',
            'cep': 'str',
            'nome_logradouro': 'str',
            'numero_endereco': 'str',
            'complemento': 'str',
            'bairro': 'str',
            'cidade': 'str',
            'uf': 'str',
            'pais': 'str',
            'data_cadastramento': 'datetime',
            'obs': 'str',
            'contato': 'str',
            'email': 'str',
            'flag_arquivo_secr_fazenda': 'int',
            'flag_cartao_digitado': 'int',
            'inativo': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'numero_estabelecimento': 'numeroEstabelecimento',
            'numero_receita_federal': 'numeroReceitaFederal',
            'nome': 'nome',
            'descricao': 'descricao',
            'nome_fantasia': 'nomeFantasia',
            'cep': 'cep',
            'nome_logradouro': 'nomeLogradouro',
            'numero_endereco': 'numeroEndereco',
            'complemento': 'complemento',
            'bairro': 'bairro',
            'cidade': 'cidade',
            'uf': 'uf',
            'pais': 'pais',
            'data_cadastramento': 'dataCadastramento',
            'obs': 'obs',
            'contato': 'contato',
            'email': 'email',
            'flag_arquivo_secr_fazenda': 'flagArquivoSecrFazenda',
            'flag_cartao_digitado': 'flagCartaoDigitado',
            'inativo': 'inativo'
        }

        self._id = None
        self._numero_estabelecimento = None
        self._numero_receita_federal = None
        self._nome = None
        self._descricao = None
        self._nome_fantasia = None
        self._cep = None
        self._nome_logradouro = None
        self._numero_endereco = None
        self._complemento = None
        self._bairro = None
        self._cidade = None
        self._uf = None
        self._pais = None
        self._data_cadastramento = None
        self._obs = None
        self._contato = None
        self._email = None
        self._flag_arquivo_secr_fazenda = None
        self._flag_cartao_digitado = None
        self._inativo = None

    @property
    def id(self):
        """
        Gets the id of this Estabelecimento.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do estabelecimento (id).

        :return: The id of this Estabelecimento.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Estabelecimento.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do estabelecimento (id).

        :param id: The id of this Estabelecimento.
        :type: int
        """
        self._id = id

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this Estabelecimento.
        N\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento na Conductor, com dois d\u00C3\u00ADgitos.

        :return: The numero_estabelecimento of this Estabelecimento.
        :rtype: str
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this Estabelecimento.
        N\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento na Conductor, com dois d\u00C3\u00ADgitos.

        :param numero_estabelecimento: The numero_estabelecimento of this Estabelecimento.
        :type: str
        """
        self._numero_estabelecimento = numero_estabelecimento

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this Estabelecimento.
        Apresenta o n\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento na Receita Federal.

        :return: The numero_receita_federal of this Estabelecimento.
        :rtype: int
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this Estabelecimento.
        Apresenta o n\u00C3\u00BAmero de identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento na Receita Federal.

        :param numero_receita_federal: The numero_receita_federal of this Estabelecimento.
        :type: int
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def nome(self):
        """
        Gets the nome of this Estabelecimento.
        Nome do Estabelecimento.

        :return: The nome of this Estabelecimento.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this Estabelecimento.
        Nome do Estabelecimento.

        :param nome: The nome of this Estabelecimento.
        :type: str
        """
        self._nome = nome

    @property
    def descricao(self):
        """
        Gets the descricao of this Estabelecimento.
        Raz\u00C3\u00A3o Social do Estabelecimento.

        :return: The descricao of this Estabelecimento.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this Estabelecimento.
        Raz\u00C3\u00A3o Social do Estabelecimento.

        :param descricao: The descricao of this Estabelecimento.
        :type: str
        """
        self._descricao = descricao

    @property
    def nome_fantasia(self):
        """
        Gets the nome_fantasia of this Estabelecimento.
        T\u00C3\u00ADtulo Comercial do Estabelecimento.

        :return: The nome_fantasia of this Estabelecimento.
        :rtype: str
        """
        return self._nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        """
        Sets the nome_fantasia of this Estabelecimento.
        T\u00C3\u00ADtulo Comercial do Estabelecimento.

        :param nome_fantasia: The nome_fantasia of this Estabelecimento.
        :type: str
        """
        self._nome_fantasia = nome_fantasia

    @property
    def cep(self):
        """
        Gets the cep of this Estabelecimento.
        C\u00C3\u00B3digo de Endere\u00C3\u00A7amento Postal (CEP).

        :return: The cep of this Estabelecimento.
        :rtype: str
        """
        return self._cep

    @cep.setter
    def cep(self, cep):
        """
        Sets the cep of this Estabelecimento.
        C\u00C3\u00B3digo de Endere\u00C3\u00A7amento Postal (CEP).

        :param cep: The cep of this Estabelecimento.
        :type: str
        """
        self._cep = cep

    @property
    def nome_logradouro(self):
        """
        Gets the nome_logradouro of this Estabelecimento.
        Nome do Logradouro.

        :return: The nome_logradouro of this Estabelecimento.
        :rtype: str
        """
        return self._nome_logradouro

    @nome_logradouro.setter
    def nome_logradouro(self, nome_logradouro):
        """
        Sets the nome_logradouro of this Estabelecimento.
        Nome do Logradouro.

        :param nome_logradouro: The nome_logradouro of this Estabelecimento.
        :type: str
        """
        self._nome_logradouro = nome_logradouro

    @property
    def numero_endereco(self):
        """
        Gets the numero_endereco of this Estabelecimento.
        N\u00C3\u00BAmero do endere\u00C3\u00A7o.

        :return: The numero_endereco of this Estabelecimento.
        :rtype: str
        """
        return self._numero_endereco

    @numero_endereco.setter
    def numero_endereco(self, numero_endereco):
        """
        Sets the numero_endereco of this Estabelecimento.
        N\u00C3\u00BAmero do endere\u00C3\u00A7o.

        :param numero_endereco: The numero_endereco of this Estabelecimento.
        :type: str
        """
        self._numero_endereco = numero_endereco

    @property
    def complemento(self):
        """
        Gets the complemento of this Estabelecimento.
        Descri\u00C3\u00A7\u00C3\u00B5es complementares referente ao endere\u00C3\u00A7o.

        :return: The complemento of this Estabelecimento.
        :rtype: str
        """
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        """
        Sets the complemento of this Estabelecimento.
        Descri\u00C3\u00A7\u00C3\u00B5es complementares referente ao endere\u00C3\u00A7o.

        :param complemento: The complemento of this Estabelecimento.
        :type: str
        """
        self._complemento = complemento

    @property
    def bairro(self):
        """
        Gets the bairro of this Estabelecimento.
        Nome do bairro do endere\u00C3\u00A7o.

        :return: The bairro of this Estabelecimento.
        :rtype: str
        """
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        """
        Sets the bairro of this Estabelecimento.
        Nome do bairro do endere\u00C3\u00A7o.

        :param bairro: The bairro of this Estabelecimento.
        :type: str
        """
        self._bairro = bairro

    @property
    def cidade(self):
        """
        Gets the cidade of this Estabelecimento.
        Nome da cidade do endere\u00C3\u00A7o.

        :return: The cidade of this Estabelecimento.
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """
        Sets the cidade of this Estabelecimento.
        Nome da cidade do endere\u00C3\u00A7o.

        :param cidade: The cidade of this Estabelecimento.
        :type: str
        """
        self._cidade = cidade

    @property
    def uf(self):
        """
        Gets the uf of this Estabelecimento.
        Sigla de identifica\u00C3\u00A7\u00C3\u00A3o da Unidade Federativa do endere\u00C3\u00A7o.

        :return: The uf of this Estabelecimento.
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """
        Sets the uf of this Estabelecimento.
        Sigla de identifica\u00C3\u00A7\u00C3\u00A3o da Unidade Federativa do endere\u00C3\u00A7o.

        :param uf: The uf of this Estabelecimento.
        :type: str
        """
        self._uf = uf

    @property
    def pais(self):
        """
        Gets the pais of this Estabelecimento.
        Nome do pa\u00C3\u00ADs.

        :return: The pais of this Estabelecimento.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais):
        """
        Sets the pais of this Estabelecimento.
        Nome do pa\u00C3\u00ADs.

        :param pais: The pais of this Estabelecimento.
        :type: str
        """
        self._pais = pais

    @property
    def data_cadastramento(self):
        """
        Gets the data_cadastramento of this Estabelecimento.
        Data de Cadastro do Estabelecimento.

        :return: The data_cadastramento of this Estabelecimento.
        :rtype: datetime
        """
        return self._data_cadastramento

    @data_cadastramento.setter
    def data_cadastramento(self, data_cadastramento):
        """
        Sets the data_cadastramento of this Estabelecimento.
        Data de Cadastro do Estabelecimento.

        :param data_cadastramento: The data_cadastramento of this Estabelecimento.
        :type: datetime
        """
        self._data_cadastramento = data_cadastramento

    @property
    def obs(self):
        """
        Gets the obs of this Estabelecimento.
        Detalhes espec\u00C3\u00ADficos quanto ao Cadastro do Estabelecimento.

        :return: The obs of this Estabelecimento.
        :rtype: str
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """
        Sets the obs of this Estabelecimento.
        Detalhes espec\u00C3\u00ADficos quanto ao Cadastro do Estabelecimento.

        :param obs: The obs of this Estabelecimento.
        :type: str
        """
        self._obs = obs

    @property
    def contato(self):
        """
        Gets the contato of this Estabelecimento.
        Nome da pessoa para contato com o Estabelecimento.

        :return: The contato of this Estabelecimento.
        :rtype: str
        """
        return self._contato

    @contato.setter
    def contato(self, contato):
        """
        Sets the contato of this Estabelecimento.
        Nome da pessoa para contato com o Estabelecimento.

        :param contato: The contato of this Estabelecimento.
        :type: str
        """
        self._contato = contato

    @property
    def email(self):
        """
        Gets the email of this Estabelecimento.
        E-mail da pessoa para contato com o Estabelecimento.

        :return: The email of this Estabelecimento.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Estabelecimento.
        E-mail da pessoa para contato com o Estabelecimento.

        :param email: The email of this Estabelecimento.
        :type: str
        """
        self._email = email

    @property
    def flag_arquivo_secr_fazenda(self):
        """
        Gets the flag_arquivo_secr_fazenda of this Estabelecimento.
        Indica se o estabelecimento ser\u00C3\u00A1 inclu\u00C3\u00ADdo no arquivo de registro para a Secretaria da Fazenda Estadual.

        :return: The flag_arquivo_secr_fazenda of this Estabelecimento.
        :rtype: int
        """
        return self._flag_arquivo_secr_fazenda

    @flag_arquivo_secr_fazenda.setter
    def flag_arquivo_secr_fazenda(self, flag_arquivo_secr_fazenda):
        """
        Sets the flag_arquivo_secr_fazenda of this Estabelecimento.
        Indica se o estabelecimento ser\u00C3\u00A1 inclu\u00C3\u00ADdo no arquivo de registro para a Secretaria da Fazenda Estadual.

        :param flag_arquivo_secr_fazenda: The flag_arquivo_secr_fazenda of this Estabelecimento.
        :type: int
        """
        self._flag_arquivo_secr_fazenda = flag_arquivo_secr_fazenda

    @property
    def flag_cartao_digitado(self):
        """
        Gets the flag_cartao_digitado of this Estabelecimento.
        Indica se o estabelecimento poder\u00C3\u00A1 originar transa\u00C3\u00A7\u00C3\u00B5es sem a leitura da tarja ou do chip do cart\u00C3\u00A3o.

        :return: The flag_cartao_digitado of this Estabelecimento.
        :rtype: int
        """
        return self._flag_cartao_digitado

    @flag_cartao_digitado.setter
    def flag_cartao_digitado(self, flag_cartao_digitado):
        """
        Sets the flag_cartao_digitado of this Estabelecimento.
        Indica se o estabelecimento poder\u00C3\u00A1 originar transa\u00C3\u00A7\u00C3\u00B5es sem a leitura da tarja ou do chip do cart\u00C3\u00A3o.

        :param flag_cartao_digitado: The flag_cartao_digitado of this Estabelecimento.
        :type: int
        """
        self._flag_cartao_digitado = flag_cartao_digitado

    @property
    def inativo(self):
        """
        Gets the inativo of this Estabelecimento.
        Indica se o estabelecimento est\u00C3\u00A1 inativo.

        :return: The inativo of this Estabelecimento.
        :rtype: int
        """
        return self._inativo

    @inativo.setter
    def inativo(self, inativo):
        """
        Sets the inativo of this Estabelecimento.
        Indica se o estabelecimento est\u00C3\u00A1 inativo.

        :param inativo: The inativo of this Estabelecimento.
        :type: int
        """
        self._inativo = inativo

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

