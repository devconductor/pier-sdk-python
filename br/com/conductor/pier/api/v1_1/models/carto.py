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


class Carto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Carto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'arquivo_impressao': 'str',
            'codigo_desbloqueio': 'str',
            'data_estagio_cartao': 'datetime',
            'data_geracao': 'datetime',
            'data_impressao': 'datetime',
            'data_status_cartao': 'datetime',
            'data_validade': 'datetime',
            'flag_impressao_origem_comercial': 'int',
            'flag_provisorio': 'int',
            'id': 'int',
            'id_conta': 'int',
            'id_estagio_cartao': 'int',
            'id_pessoa': 'int',
            'id_produto': 'int',
            'id_status_cartao': 'int',
            'nome_impresso': 'str',
            'numero_cartao': 'str',
            'portador': 'int'
        }

        self.attribute_map = {
            'arquivo_impressao': 'arquivoImpressao',
            'codigo_desbloqueio': 'codigoDesbloqueio',
            'data_estagio_cartao': 'dataEstagioCartao',
            'data_geracao': 'dataGeracao',
            'data_impressao': 'dataImpressao',
            'data_status_cartao': 'dataStatusCartao',
            'data_validade': 'dataValidade',
            'flag_impressao_origem_comercial': 'flagImpressaoOrigemComercial',
            'flag_provisorio': 'flagProvisorio',
            'id': 'id',
            'id_conta': 'idConta',
            'id_estagio_cartao': 'idEstagioCartao',
            'id_pessoa': 'idPessoa',
            'id_produto': 'idProduto',
            'id_status_cartao': 'idStatusCartao',
            'nome_impresso': 'nomeImpresso',
            'numero_cartao': 'numeroCartao',
            'portador': 'portador'
        }

        self._arquivo_impressao = None
        self._codigo_desbloqueio = None
        self._data_estagio_cartao = None
        self._data_geracao = None
        self._data_impressao = None
        self._data_status_cartao = None
        self._data_validade = None
        self._flag_impressao_origem_comercial = None
        self._flag_provisorio = None
        self._id = None
        self._id_conta = None
        self._id_estagio_cartao = None
        self._id_pessoa = None
        self._id_produto = None
        self._id_status_cartao = None
        self._nome_impresso = None
        self._numero_cartao = None
        self._portador = None

    @property
    def arquivo_impressao(self):
        """
        Gets the arquivo_impressao of this Carto.
        Apresenta o nome do arquivo onde o cart\u00C3\u00A3o fora inclu\u00C3\u00ADdo para impress\u00C3\u00A3o por uma gr\u00C3\u00A1fica, quando houver.

        :return: The arquivo_impressao of this Carto.
        :rtype: str
        """
        return self._arquivo_impressao

    @arquivo_impressao.setter
    def arquivo_impressao(self, arquivo_impressao):
        """
        Sets the arquivo_impressao of this Carto.
        Apresenta o nome do arquivo onde o cart\u00C3\u00A3o fora inclu\u00C3\u00ADdo para impress\u00C3\u00A3o por uma gr\u00C3\u00A1fica, quando houver.

        :param arquivo_impressao: The arquivo_impressao of this Carto.
        :type: str
        """
        self._arquivo_impressao = arquivo_impressao

    @property
    def codigo_desbloqueio(self):
        """
        Gets the codigo_desbloqueio of this Carto.
        Apresenta um c\u00C3\u00B3digo espec\u00C3\u00ADfico para ser utilizado como vari\u00C3\u00A1vel no processo de desbloqueio do cart\u00C3\u00A3o para emissores que querem usar esta funcionalidade.

        :return: The codigo_desbloqueio of this Carto.
        :rtype: str
        """
        return self._codigo_desbloqueio

    @codigo_desbloqueio.setter
    def codigo_desbloqueio(self, codigo_desbloqueio):
        """
        Sets the codigo_desbloqueio of this Carto.
        Apresenta um c\u00C3\u00B3digo espec\u00C3\u00ADfico para ser utilizado como vari\u00C3\u00A1vel no processo de desbloqueio do cart\u00C3\u00A3o para emissores que querem usar esta funcionalidade.

        :param codigo_desbloqueio: The codigo_desbloqueio of this Carto.
        :type: str
        """
        self._codigo_desbloqueio = codigo_desbloqueio

    @property
    def data_estagio_cartao(self):
        """
        Gets the data_estagio_cartao of this Carto.
        Apresenta a data em que o idEstagioCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :return: The data_estagio_cartao of this Carto.
        :rtype: datetime
        """
        return self._data_estagio_cartao

    @data_estagio_cartao.setter
    def data_estagio_cartao(self, data_estagio_cartao):
        """
        Sets the data_estagio_cartao of this Carto.
        Apresenta a data em que o idEstagioCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :param data_estagio_cartao: The data_estagio_cartao of this Carto.
        :type: datetime
        """
        self._data_estagio_cartao = data_estagio_cartao

    @property
    def data_geracao(self):
        """
        Gets the data_geracao of this Carto.
        Apresenta a data em que o cart\u00C3\u00A3o foi gerado.

        :return: The data_geracao of this Carto.
        :rtype: datetime
        """
        return self._data_geracao

    @data_geracao.setter
    def data_geracao(self, data_geracao):
        """
        Sets the data_geracao of this Carto.
        Apresenta a data em que o cart\u00C3\u00A3o foi gerado.

        :param data_geracao: The data_geracao of this Carto.
        :type: datetime
        """
        self._data_geracao = data_geracao

    @property
    def data_impressao(self):
        """
        Gets the data_impressao of this Carto.
        Apresenta a data em que o cart\u00C3\u00A3o fora impresso, caso impress\u00C3\u00A3o em loja, ou a data em que ele fora inclu\u00C3\u00ADdo no arquivo para impress\u00C3\u00A3o via gr\u00C3\u00A1fica.

        :return: The data_impressao of this Carto.
        :rtype: datetime
        """
        return self._data_impressao

    @data_impressao.setter
    def data_impressao(self, data_impressao):
        """
        Sets the data_impressao of this Carto.
        Apresenta a data em que o cart\u00C3\u00A3o fora impresso, caso impress\u00C3\u00A3o em loja, ou a data em que ele fora inclu\u00C3\u00ADdo no arquivo para impress\u00C3\u00A3o via gr\u00C3\u00A1fica.

        :param data_impressao: The data_impressao of this Carto.
        :type: datetime
        """
        self._data_impressao = data_impressao

    @property
    def data_status_cartao(self):
        """
        Gets the data_status_cartao of this Carto.
        Apresenta a data em que o idStatusCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :return: The data_status_cartao of this Carto.
        :rtype: datetime
        """
        return self._data_status_cartao

    @data_status_cartao.setter
    def data_status_cartao(self, data_status_cartao):
        """
        Sets the data_status_cartao of this Carto.
        Apresenta a data em que o idStatusCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.

        :param data_status_cartao: The data_status_cartao of this Carto.
        :type: datetime
        """
        self._data_status_cartao = data_status_cartao

    @property
    def data_validade(self):
        """
        Gets the data_validade of this Carto.
        Apresenta a data de validade do cart\u00C3\u00A3o em formato MMAAAA, quando houver.

        :return: The data_validade of this Carto.
        :rtype: datetime
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this Carto.
        Apresenta a data de validade do cart\u00C3\u00A3o em formato MMAAAA, quando houver.

        :param data_validade: The data_validade of this Carto.
        :type: datetime
        """
        self._data_validade = data_validade

    @property
    def flag_impressao_origem_comercial(self):
        """
        Gets the flag_impressao_origem_comercial of this Carto.
        Quando ativa, indica que o cart\u00C3\u00A3o fora impresso na Origem Comercial.

        :return: The flag_impressao_origem_comercial of this Carto.
        :rtype: int
        """
        return self._flag_impressao_origem_comercial

    @flag_impressao_origem_comercial.setter
    def flag_impressao_origem_comercial(self, flag_impressao_origem_comercial):
        """
        Sets the flag_impressao_origem_comercial of this Carto.
        Quando ativa, indica que o cart\u00C3\u00A3o fora impresso na Origem Comercial.

        :param flag_impressao_origem_comercial: The flag_impressao_origem_comercial of this Carto.
        :type: int
        """
        self._flag_impressao_origem_comercial = flag_impressao_origem_comercial

    @property
    def flag_provisorio(self):
        """
        Gets the flag_provisorio of this Carto.
        Quando ativa, indica que o cart\u00C3\u00A3o \u00C3\u00A9 provis\u00C3\u00B3rio. Ou seja, \u00C3\u00A9 um cart\u00C3\u00A3o para uso tempor\u00C3\u00A1rio quando se deseja permitir que o cliente transacione sem que ele tenha recebido um cart\u00C3\u00A3o definitivo.

        :return: The flag_provisorio of this Carto.
        :rtype: int
        """
        return self._flag_provisorio

    @flag_provisorio.setter
    def flag_provisorio(self, flag_provisorio):
        """
        Sets the flag_provisorio of this Carto.
        Quando ativa, indica que o cart\u00C3\u00A3o \u00C3\u00A9 provis\u00C3\u00B3rio. Ou seja, \u00C3\u00A9 um cart\u00C3\u00A3o para uso tempor\u00C3\u00A1rio quando se deseja permitir que o cliente transacione sem que ele tenha recebido um cart\u00C3\u00A3o definitivo.

        :param flag_provisorio: The flag_provisorio of this Carto.
        :type: int
        """
        self._flag_provisorio = flag_provisorio

    @property
    def id(self):
        """
        Gets the id of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o (id).

        :return: The id of this Carto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o (id).

        :param id: The id of this Carto.
        :type: int
        """
        self._id = id

    @property
    def id_conta(self):
        """
        Gets the id_conta of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o cart\u00C3\u00A3o pertence (id).

        :return: The id_conta of this Carto.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o cart\u00C3\u00A3o pertence (id).

        :param id_conta: The id_conta of this Carto.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_estagio_cartao(self):
        """
        Gets the id_estagio_cartao of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o (id).

        :return: The id_estagio_cartao of this Carto.
        :rtype: int
        """
        return self._id_estagio_cartao

    @id_estagio_cartao.setter
    def id_estagio_cartao(self, id_estagio_cartao):
        """
        Sets the id_estagio_cartao of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o (id).

        :param id_estagio_cartao: The id_estagio_cartao of this Carto.
        :type: int
        """
        self._id_estagio_cartao = id_estagio_cartao

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa a qual o cart\u00C3\u00A3o pertence (id)

        :return: The id_pessoa of this Carto.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa a qual o cart\u00C3\u00A3o pertence (id)

        :param id_pessoa: The id_pessoa of this Carto.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_produto(self):
        """
        Gets the id_produto of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto a qual o cart\u00C3\u00A3o pertence (id).

        :return: The id_produto of this Carto.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto a qual o cart\u00C3\u00A3o pertence (id).

        :param id_produto: The id_produto of this Carto.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def id_status_cartao(self):
        """
        Gets the id_status_cartao of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o (id).

        :return: The id_status_cartao of this Carto.
        :rtype: int
        """
        return self._id_status_cartao

    @id_status_cartao.setter
    def id_status_cartao(self, id_status_cartao):
        """
        Sets the id_status_cartao of this Carto.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o (id).

        :param id_status_cartao: The id_status_cartao of this Carto.
        :type: int
        """
        self._id_status_cartao = id_status_cartao

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this Carto.
        Apresenta o nome impresso no cart\u00C3\u00A3o.

        :return: The nome_impresso of this Carto.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this Carto.
        Apresenta o nome impresso no cart\u00C3\u00A3o.

        :param nome_impresso: The nome_impresso of this Carto.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this Carto.
        Apresenta o n\u00C3\u00BAmero do cart\u00C3\u00A3o.

        :return: The numero_cartao of this Carto.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this Carto.
        Apresenta o n\u00C3\u00BAmero do cart\u00C3\u00A3o.

        :param numero_cartao: The numero_cartao of this Carto.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def portador(self):
        """
        Gets the portador of this Carto.
        Indica qual \u00C3\u00A9 a rela\u00C3\u00A7\u00C3\u00A3o do portador do cart\u00C3\u00A3o com a conta. Quando \u00E2\u0080\u00981\u00E2\u0080\u0099, corresponde ao seu titular. Quando diferente disso, corresponde a um cart\u00C3\u00A3o adicional.

        :return: The portador of this Carto.
        :rtype: int
        """
        return self._portador

    @portador.setter
    def portador(self, portador):
        """
        Sets the portador of this Carto.
        Indica qual \u00C3\u00A9 a rela\u00C3\u00A7\u00C3\u00A3o do portador do cart\u00C3\u00A3o com a conta. Quando \u00E2\u0080\u00981\u00E2\u0080\u0099, corresponde ao seu titular. Quando diferente disso, corresponde a um cart\u00C3\u00A3o adicional.

        :param portador: The portador of this Carto.
        :type: int
        """
        self._portador = portador

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
