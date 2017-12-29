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


class CartaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CartaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'flag_titular': 'int',
            'id_pessoa': 'int',
            'sequencial_cartao': 'int',
            'id_conta': 'int',
            'id_status': 'int',
            'data_status': 'str',
            'id_estagio': 'int',
            'data_estagio': 'str',
            'numero_bin': 'int',
            'numero_cartao': 'str',
            'numero_cartao_hash': 'int',
            'numero_cartao_criptografado': 'str',
            'data_emissao': 'str',
            'data_validade': 'str',
            'cartao_virtual': 'int',
            'impressao_avulsa': 'int',
            'data_impressao': 'str',
            'nome_arquivo_impressao': 'str',
            'id_produto': 'int',
            'nome_impresso': 'str',
            'codigo_desbloqueio': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'flag_titular': 'flagTitular',
            'id_pessoa': 'idPessoa',
            'sequencial_cartao': 'sequencialCartao',
            'id_conta': 'idConta',
            'id_status': 'idStatus',
            'data_status': 'dataStatus',
            'id_estagio': 'idEstagio',
            'data_estagio': 'dataEstagio',
            'numero_bin': 'numeroBin',
            'numero_cartao': 'numeroCartao',
            'numero_cartao_hash': 'numeroCartaoHash',
            'numero_cartao_criptografado': 'numeroCartaoCriptografado',
            'data_emissao': 'dataEmissao',
            'data_validade': 'dataValidade',
            'cartao_virtual': 'cartaoVirtual',
            'impressao_avulsa': 'impressaoAvulsa',
            'data_impressao': 'dataImpressao',
            'nome_arquivo_impressao': 'nomeArquivoImpressao',
            'id_produto': 'idProduto',
            'nome_impresso': 'nomeImpresso',
            'codigo_desbloqueio': 'codigoDesbloqueio'
        }

        self._id = None
        self._flag_titular = None
        self._id_pessoa = None
        self._sequencial_cartao = None
        self._id_conta = None
        self._id_status = None
        self._data_status = None
        self._id_estagio = None
        self._data_estagio = None
        self._numero_bin = None
        self._numero_cartao = None
        self._numero_cartao_hash = None
        self._numero_cartao_criptografado = None
        self._data_emissao = None
        self._data_validade = None
        self._cartao_virtual = None
        self._impressao_avulsa = None
        self._data_impressao = None
        self._nome_arquivo_impressao = None
        self._id_produto = None
        self._nome_impresso = None
        self._codigo_desbloqueio = None

    @property
    def id(self):
        """
        Gets the id of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o.

        :return: The id of this CartaoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o.

        :param id: The id of this CartaoResponse.
        :type: int
        """
        self._id = id

    @property
    def flag_titular(self):
        """
        Gets the flag_titular of this CartaoResponse.
        Apresenta o tipo do Portador do cart\u00C3\u00A3o, sendo: (1: Titular, 0: Adicional).

        :return: The flag_titular of this CartaoResponse.
        :rtype: int
        """
        return self._flag_titular

    @flag_titular.setter
    def flag_titular(self, flag_titular):
        """
        Sets the flag_titular of this CartaoResponse.
        Apresenta o tipo do Portador do cart\u00C3\u00A3o, sendo: (1: Titular, 0: Adicional).

        :param flag_titular: The flag_titular of this CartaoResponse.
        :type: int
        """
        self._flag_titular = flag_titular

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa a qual o cart\u00C3\u00A3o pertence

        :return: The id_pessoa of this CartaoResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa a qual o cart\u00C3\u00A3o pertence

        :param id_pessoa: The id_pessoa of this CartaoResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def sequencial_cartao(self):
        """
        Gets the sequencial_cartao of this CartaoResponse.
        N\u00C3\u00BAmero sequencial do cart\u00C3\u00A3o

        :return: The sequencial_cartao of this CartaoResponse.
        :rtype: int
        """
        return self._sequencial_cartao

    @sequencial_cartao.setter
    def sequencial_cartao(self, sequencial_cartao):
        """
        Sets the sequencial_cartao of this CartaoResponse.
        N\u00C3\u00BAmero sequencial do cart\u00C3\u00A3o

        :param sequencial_cartao: The sequencial_cartao of this CartaoResponse.
        :type: int
        """
        self._sequencial_cartao = sequencial_cartao

    @property
    def id_conta(self):
        """
        Gets the id_conta of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o cart\u00C3\u00A3o pertence.

        :return: The id_conta of this CartaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o cart\u00C3\u00A3o pertence.

        :param id_conta: The id_conta of this CartaoResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_status(self):
        """
        Gets the id_status of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o.

        :return: The id_status of this CartaoResponse.
        :rtype: int
        """
        return self._id_status

    @id_status.setter
    def id_status(self, id_status):
        """
        Sets the id_status of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o.

        :param id_status: The id_status of this CartaoResponse.
        :type: int
        """
        self._id_status = id_status

    @property
    def data_status(self):
        """
        Gets the data_status of this CartaoResponse.
        Apresenta a data em que o idStatusCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :return: The data_status of this CartaoResponse.
        :rtype: str
        """
        return self._data_status

    @data_status.setter
    def data_status(self, data_status):
        """
        Sets the data_status of this CartaoResponse.
        Apresenta a data em que o idStatusCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :param data_status: The data_status of this CartaoResponse.
        :type: str
        """
        self._data_status = data_status

    @property
    def id_estagio(self):
        """
        Gets the id_estagio of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o.

        :return: The id_estagio of this CartaoResponse.
        :rtype: int
        """
        return self._id_estagio

    @id_estagio.setter
    def id_estagio(self, id_estagio):
        """
        Sets the id_estagio of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o.

        :param id_estagio: The id_estagio of this CartaoResponse.
        :type: int
        """
        self._id_estagio = id_estagio

    @property
    def data_estagio(self):
        """
        Gets the data_estagio of this CartaoResponse.
        Apresenta a data em que o idEstagio atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :return: The data_estagio of this CartaoResponse.
        :rtype: str
        """
        return self._data_estagio

    @data_estagio.setter
    def data_estagio(self, data_estagio):
        """
        Sets the data_estagio of this CartaoResponse.
        Apresenta a data em que o idEstagio atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :param data_estagio: The data_estagio of this CartaoResponse.
        :type: str
        """
        self._data_estagio = data_estagio

    @property
    def numero_bin(self):
        """
        Gets the numero_bin of this CartaoResponse.
        N\u00C3\u00BAmero do bin do cart\u00C3\u00A3o.

        :return: The numero_bin of this CartaoResponse.
        :rtype: int
        """
        return self._numero_bin

    @numero_bin.setter
    def numero_bin(self, numero_bin):
        """
        Sets the numero_bin of this CartaoResponse.
        N\u00C3\u00BAmero do bin do cart\u00C3\u00A3o.

        :param numero_bin: The numero_bin of this CartaoResponse.
        :type: int
        """
        self._numero_bin = numero_bin

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this CartaoResponse.
        Apresenta o n\u00C3\u00BAmero do cart\u00C3\u00A3o.

        :return: The numero_cartao of this CartaoResponse.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this CartaoResponse.
        Apresenta o n\u00C3\u00BAmero do cart\u00C3\u00A3o.

        :param numero_cartao: The numero_cartao of this CartaoResponse.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def numero_cartao_hash(self):
        """
        Gets the numero_cartao_hash of this CartaoResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o hash.

        :return: The numero_cartao_hash of this CartaoResponse.
        :rtype: int
        """
        return self._numero_cartao_hash

    @numero_cartao_hash.setter
    def numero_cartao_hash(self, numero_cartao_hash):
        """
        Sets the numero_cartao_hash of this CartaoResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o hash.

        :param numero_cartao_hash: The numero_cartao_hash of this CartaoResponse.
        :type: int
        """
        self._numero_cartao_hash = numero_cartao_hash

    @property
    def numero_cartao_criptografado(self):
        """
        Gets the numero_cartao_criptografado of this CartaoResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o criptografado.

        :return: The numero_cartao_criptografado of this CartaoResponse.
        :rtype: str
        """
        return self._numero_cartao_criptografado

    @numero_cartao_criptografado.setter
    def numero_cartao_criptografado(self, numero_cartao_criptografado):
        """
        Sets the numero_cartao_criptografado of this CartaoResponse.
        N\u00C3\u00BAmero do cart\u00C3\u00A3o criptografado.

        :param numero_cartao_criptografado: The numero_cartao_criptografado of this CartaoResponse.
        :type: str
        """
        self._numero_cartao_criptografado = numero_cartao_criptografado

    @property
    def data_emissao(self):
        """
        Gets the data_emissao of this CartaoResponse.
        Apresenta a data de emiss\u00C3\u00A3o do cart\u00C3\u00A3o.

        :return: The data_emissao of this CartaoResponse.
        :rtype: str
        """
        return self._data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao):
        """
        Sets the data_emissao of this CartaoResponse.
        Apresenta a data de emiss\u00C3\u00A3o do cart\u00C3\u00A3o.

        :param data_emissao: The data_emissao of this CartaoResponse.
        :type: str
        """
        self._data_emissao = data_emissao

    @property
    def data_validade(self):
        """
        Gets the data_validade of this CartaoResponse.
        Apresenta a data de validade do cart\u00C3\u00A3o em formato yyyy-MM, quando houver.

        :return: The data_validade of this CartaoResponse.
        :rtype: str
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this CartaoResponse.
        Apresenta a data de validade do cart\u00C3\u00A3o em formato yyyy-MM, quando houver.

        :param data_validade: The data_validade of this CartaoResponse.
        :type: str
        """
        self._data_validade = data_validade

    @property
    def cartao_virtual(self):
        """
        Gets the cartao_virtual of this CartaoResponse.
        Apresenta o status que informa se o cart\u00C3\u00A3o \u00C3\u00A9 virtual. Sendo: (1: True, 0: False).

        :return: The cartao_virtual of this CartaoResponse.
        :rtype: int
        """
        return self._cartao_virtual

    @cartao_virtual.setter
    def cartao_virtual(self, cartao_virtual):
        """
        Sets the cartao_virtual of this CartaoResponse.
        Apresenta o status que informa se o cart\u00C3\u00A3o \u00C3\u00A9 virtual. Sendo: (1: True, 0: False).

        :param cartao_virtual: The cartao_virtual of this CartaoResponse.
        :type: int
        """
        self._cartao_virtual = cartao_virtual

    @property
    def impressao_avulsa(self):
        """
        Gets the impressao_avulsa of this CartaoResponse.
        Quando ativa, indica que o cart\u00C3\u00A3o fora impresso na Origem Comercial.

        :return: The impressao_avulsa of this CartaoResponse.
        :rtype: int
        """
        return self._impressao_avulsa

    @impressao_avulsa.setter
    def impressao_avulsa(self, impressao_avulsa):
        """
        Sets the impressao_avulsa of this CartaoResponse.
        Quando ativa, indica que o cart\u00C3\u00A3o fora impresso na Origem Comercial.

        :param impressao_avulsa: The impressao_avulsa of this CartaoResponse.
        :type: int
        """
        self._impressao_avulsa = impressao_avulsa

    @property
    def data_impressao(self):
        """
        Gets the data_impressao of this CartaoResponse.
        Apresenta a data em que o cart\u00C3\u00A3o fora impresso, caso impress\u00C3\u00A3o em loja, ou a data em que ele fora inclu\u00C3\u00ADdo no arquivo para impress\u00C3\u00A3o via gr\u00C3\u00A1fica.

        :return: The data_impressao of this CartaoResponse.
        :rtype: str
        """
        return self._data_impressao

    @data_impressao.setter
    def data_impressao(self, data_impressao):
        """
        Sets the data_impressao of this CartaoResponse.
        Apresenta a data em que o cart\u00C3\u00A3o fora impresso, caso impress\u00C3\u00A3o em loja, ou a data em que ele fora inclu\u00C3\u00ADdo no arquivo para impress\u00C3\u00A3o via gr\u00C3\u00A1fica.

        :param data_impressao: The data_impressao of this CartaoResponse.
        :type: str
        """
        self._data_impressao = data_impressao

    @property
    def nome_arquivo_impressao(self):
        """
        Gets the nome_arquivo_impressao of this CartaoResponse.
        Apresenta o nome do arquivo onde o cart\u00C3\u00A3o fora inclu\u00C3\u00ADdo para impress\u00C3\u00A3o por uma gr\u00C3\u00A1fica, quando houver.

        :return: The nome_arquivo_impressao of this CartaoResponse.
        :rtype: str
        """
        return self._nome_arquivo_impressao

    @nome_arquivo_impressao.setter
    def nome_arquivo_impressao(self, nome_arquivo_impressao):
        """
        Sets the nome_arquivo_impressao of this CartaoResponse.
        Apresenta o nome do arquivo onde o cart\u00C3\u00A3o fora inclu\u00C3\u00ADdo para impress\u00C3\u00A3o por uma gr\u00C3\u00A1fica, quando houver.

        :param nome_arquivo_impressao: The nome_arquivo_impressao of this CartaoResponse.
        :type: str
        """
        self._nome_arquivo_impressao = nome_arquivo_impressao

    @property
    def id_produto(self):
        """
        Gets the id_produto of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto a qual o cart\u00C3\u00A3o pertence.

        :return: The id_produto of this CartaoResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this CartaoResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto a qual o cart\u00C3\u00A3o pertence.

        :param id_produto: The id_produto of this CartaoResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this CartaoResponse.
        Apresenta o nome impresso no cart\u00C3\u00A3o.

        :return: The nome_impresso of this CartaoResponse.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this CartaoResponse.
        Apresenta o nome impresso no cart\u00C3\u00A3o.

        :param nome_impresso: The nome_impresso of this CartaoResponse.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def codigo_desbloqueio(self):
        """
        Gets the codigo_desbloqueio of this CartaoResponse.
        Apresenta um c\u00C3\u00B3digo espec\u00C3\u00ADfico para ser utilizado como vari\u00C3\u00A1vel no processo de desbloqueio do cart\u00C3\u00A3o para emissores que querem usar esta funcionalidade.

        :return: The codigo_desbloqueio of this CartaoResponse.
        :rtype: str
        """
        return self._codigo_desbloqueio

    @codigo_desbloqueio.setter
    def codigo_desbloqueio(self, codigo_desbloqueio):
        """
        Sets the codigo_desbloqueio of this CartaoResponse.
        Apresenta um c\u00C3\u00B3digo espec\u00C3\u00ADfico para ser utilizado como vari\u00C3\u00A1vel no processo de desbloqueio do cart\u00C3\u00A3o para emissores que querem usar esta funcionalidade.

        :param codigo_desbloqueio: The codigo_desbloqueio of this CartaoResponse.
        :type: str
        """
        self._codigo_desbloqueio = codigo_desbloqueio

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

