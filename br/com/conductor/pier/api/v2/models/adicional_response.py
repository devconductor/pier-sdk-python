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


class AdicionalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AdicionalResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_conta': 'int',
            'id_pessoa': 'int',
            'nome': 'str',
            'nome_impresso': 'str',
            'numero_receita_federal': 'str',
            'data_nascimento': 'str',
            'sexo': 'str',
            'numero_identidade': 'str',
            'orgao_expedidor_identidade': 'str',
            'unidade_federativa_identidade': 'str',
            'data_emissao_identidade': 'str',
            'id_parentesco': 'int',
            'flag_ativo': 'int',
            'data_cadastro_portador': 'str',
            'data_cancelamento_portador': 'str'
        }

        self.attribute_map = {
            'id_conta': 'idConta',
            'id_pessoa': 'idPessoa',
            'nome': 'nome',
            'nome_impresso': 'nomeImpresso',
            'numero_receita_federal': 'numeroReceitaFederal',
            'data_nascimento': 'dataNascimento',
            'sexo': 'sexo',
            'numero_identidade': 'numeroIdentidade',
            'orgao_expedidor_identidade': 'orgaoExpedidorIdentidade',
            'unidade_federativa_identidade': 'unidadeFederativaIdentidade',
            'data_emissao_identidade': 'dataEmissaoIdentidade',
            'id_parentesco': 'idParentesco',
            'flag_ativo': 'flagAtivo',
            'data_cadastro_portador': 'dataCadastroPortador',
            'data_cancelamento_portador': 'dataCancelamentoPortador'
        }

        self._id_conta = None
        self._id_pessoa = None
        self._nome = None
        self._nome_impresso = None
        self._numero_receita_federal = None
        self._data_nascimento = None
        self._sexo = None
        self._numero_identidade = None
        self._orgao_expedidor_identidade = None
        self._unidade_federativa_identidade = None
        self._data_emissao_identidade = None
        self._id_parentesco = None
        self._flag_ativo = None
        self._data_cadastro_portador = None
        self._data_cancelamento_portador = None

    @property
    def id_conta(self):
        """
        Gets the id_conta of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da Conta para cadastro do Adicional

        :return: The id_conta of this AdicionalResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da Conta para cadastro do Adicional

        :param id_conta: The id_conta of this AdicionalResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa Adicional

        :return: The id_pessoa of this AdicionalResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa Adicional

        :param id_pessoa: The id_pessoa of this AdicionalResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def nome(self):
        """
        Gets the nome of this AdicionalResponse.
        Nome completo do Adicional

        :return: The nome of this AdicionalResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this AdicionalResponse.
        Nome completo do Adicional

        :param nome: The nome of this AdicionalResponse.
        :type: str
        """
        self._nome = nome

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this AdicionalResponse.
        Nome do Adicional que ser\u00C3\u00A1 gravado no Cart\u00C3\u00A3o

        :return: The nome_impresso of this AdicionalResponse.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this AdicionalResponse.
        Nome do Adicional que ser\u00C3\u00A1 gravado no Cart\u00C3\u00A3o

        :param nome_impresso: The nome_impresso of this AdicionalResponse.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this AdicionalResponse.
        N\u00C3\u00BAmero do CPF ou CNPJ do Adicional

        :return: The numero_receita_federal of this AdicionalResponse.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this AdicionalResponse.
        N\u00C3\u00BAmero do CPF ou CNPJ do Adicional

        :param numero_receita_federal: The numero_receita_federal of this AdicionalResponse.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def data_nascimento(self):
        """
        Gets the data_nascimento of this AdicionalResponse.
        Data de Nascimento do Adicional

        :return: The data_nascimento of this AdicionalResponse.
        :rtype: str
        """
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        """
        Sets the data_nascimento of this AdicionalResponse.
        Data de Nascimento do Adicional

        :param data_nascimento: The data_nascimento of this AdicionalResponse.
        :type: str
        """
        self._data_nascimento = data_nascimento

    @property
    def sexo(self):
        """
        Gets the sexo of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).

        :return: The sexo of this AdicionalResponse.
        :rtype: str
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """
        Sets the sexo of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).

        :param sexo: The sexo of this AdicionalResponse.
        :type: str
        """
        self._sexo = sexo

    @property
    def numero_identidade(self):
        """
        Gets the numero_identidade of this AdicionalResponse.
        N\u00C3\u00BAmero do Documento de Identidade do Adicional

        :return: The numero_identidade of this AdicionalResponse.
        :rtype: str
        """
        return self._numero_identidade

    @numero_identidade.setter
    def numero_identidade(self, numero_identidade):
        """
        Sets the numero_identidade of this AdicionalResponse.
        N\u00C3\u00BAmero do Documento de Identidade do Adicional

        :param numero_identidade: The numero_identidade of this AdicionalResponse.
        :type: str
        """
        self._numero_identidade = numero_identidade

    @property
    def orgao_expedidor_identidade(self):
        """
        Gets the orgao_expedidor_identidade of this AdicionalResponse.
        Nome do Org\u00C3\u00A3o Emissor do Documento de Identidade do Adicional

        :return: The orgao_expedidor_identidade of this AdicionalResponse.
        :rtype: str
        """
        return self._orgao_expedidor_identidade

    @orgao_expedidor_identidade.setter
    def orgao_expedidor_identidade(self, orgao_expedidor_identidade):
        """
        Sets the orgao_expedidor_identidade of this AdicionalResponse.
        Nome do Org\u00C3\u00A3o Emissor do Documento de Identidade do Adicional

        :param orgao_expedidor_identidade: The orgao_expedidor_identidade of this AdicionalResponse.
        :type: str
        """
        self._orgao_expedidor_identidade = orgao_expedidor_identidade

    @property
    def unidade_federativa_identidade(self):
        """
        Gets the unidade_federativa_identidade of this AdicionalResponse.
        Sigla da Unidade Federativa onde o Documento de Identidade do Adicional foi emitido

        :return: The unidade_federativa_identidade of this AdicionalResponse.
        :rtype: str
        """
        return self._unidade_federativa_identidade

    @unidade_federativa_identidade.setter
    def unidade_federativa_identidade(self, unidade_federativa_identidade):
        """
        Sets the unidade_federativa_identidade of this AdicionalResponse.
        Sigla da Unidade Federativa onde o Documento de Identidade do Adicional foi emitido

        :param unidade_federativa_identidade: The unidade_federativa_identidade of this AdicionalResponse.
        :type: str
        """
        self._unidade_federativa_identidade = unidade_federativa_identidade

    @property
    def data_emissao_identidade(self):
        """
        Gets the data_emissao_identidade of this AdicionalResponse.
        Data de emiss\u00C3\u00A3o do Documento de Identidade do Adicional

        :return: The data_emissao_identidade of this AdicionalResponse.
        :rtype: str
        """
        return self._data_emissao_identidade

    @data_emissao_identidade.setter
    def data_emissao_identidade(self, data_emissao_identidade):
        """
        Sets the data_emissao_identidade of this AdicionalResponse.
        Data de emiss\u00C3\u00A3o do Documento de Identidade do Adicional

        :param data_emissao_identidade: The data_emissao_identidade of this AdicionalResponse.
        :type: str
        """
        self._data_emissao_identidade = data_emissao_identidade

    @property
    def id_parentesco(self):
        """
        Gets the id_parentesco of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do Parentesco do Adicional com o Titular

        :return: The id_parentesco of this AdicionalResponse.
        :rtype: int
        """
        return self._id_parentesco

    @id_parentesco.setter
    def id_parentesco(self, id_parentesco):
        """
        Sets the id_parentesco of this AdicionalResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do Parentesco do Adicional com o Titular

        :param id_parentesco: The id_parentesco of this AdicionalResponse.
        :type: int
        """
        self._id_parentesco = id_parentesco

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this AdicionalResponse.
        Indica se o adicional est\u00C3\u00A1 ativo = 1 ou inativo = 0

        :return: The flag_ativo of this AdicionalResponse.
        :rtype: int
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this AdicionalResponse.
        Indica se o adicional est\u00C3\u00A1 ativo = 1 ou inativo = 0

        :param flag_ativo: The flag_ativo of this AdicionalResponse.
        :type: int
        """
        self._flag_ativo = flag_ativo

    @property
    def data_cadastro_portador(self):
        """
        Gets the data_cadastro_portador of this AdicionalResponse.
        Indica a data de cadastro do adicional

        :return: The data_cadastro_portador of this AdicionalResponse.
        :rtype: str
        """
        return self._data_cadastro_portador

    @data_cadastro_portador.setter
    def data_cadastro_portador(self, data_cadastro_portador):
        """
        Sets the data_cadastro_portador of this AdicionalResponse.
        Indica a data de cadastro do adicional

        :param data_cadastro_portador: The data_cadastro_portador of this AdicionalResponse.
        :type: str
        """
        self._data_cadastro_portador = data_cadastro_portador

    @property
    def data_cancelamento_portador(self):
        """
        Gets the data_cancelamento_portador of this AdicionalResponse.
        Indica a data de cancelamento do adicional

        :return: The data_cancelamento_portador of this AdicionalResponse.
        :rtype: str
        """
        return self._data_cancelamento_portador

    @data_cancelamento_portador.setter
    def data_cancelamento_portador(self, data_cancelamento_portador):
        """
        Sets the data_cancelamento_portador of this AdicionalResponse.
        Indica a data de cancelamento do adicional

        :param data_cancelamento_portador: The data_cancelamento_portador of this AdicionalResponse.
        :type: str
        """
        self._data_cancelamento_portador = data_cancelamento_portador

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

