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


class Pessoa(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Pessoa - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'nome': 'str',
            'tipo': 'str',
            'cpf': 'str',
            'cnpj': 'str',
            'data_nascimento': 'datetime',
            'numero_identidade': 'str',
            'orgao_expedidor_identidade': 'str',
            'sexo': 'str',
            'unidade_federativa_identidade': 'str',
            'data_emissao_identidade': 'date'
        }

        self.attribute_map = {
            'id': 'id',
            'nome': 'nome',
            'tipo': 'tipo',
            'cpf': 'cpf',
            'cnpj': 'cnpj',
            'data_nascimento': 'dataNascimento',
            'numero_identidade': 'numeroIdentidade',
            'orgao_expedidor_identidade': 'orgaoExpedidorIdentidade',
            'sexo': 'sexo',
            'unidade_federativa_identidade': 'unidadeFederativaIdentidade',
            'data_emissao_identidade': 'dataEmissaoIdentidade'
        }

        self._id = None
        self._nome = None
        self._tipo = None
        self._cpf = None
        self._cnpj = None
        self._data_nascimento = None
        self._numero_identidade = None
        self._orgao_expedidor_identidade = None
        self._sexo = None
        self._unidade_federativa_identidade = None
        self._data_emissao_identidade = None

    @property
    def id(self):
        """
        Gets the id of this Pessoa.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa (id).

        :return: The id of this Pessoa.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Pessoa.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa (id).

        :param id: The id of this Pessoa.
        :type: int
        """
        self._id = id

    @property
    def nome(self):
        """
        Gets the nome of this Pessoa.
        Apresenta o 'Nome Completo da PF' ou o 'Nome Completo da Raz\u00C3\u00A3o Social (Nome Empresarial)'.

        :return: The nome of this Pessoa.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this Pessoa.
        Apresenta o 'Nome Completo da PF' ou o 'Nome Completo da Raz\u00C3\u00A3o Social (Nome Empresarial)'.

        :param nome: The nome of this Pessoa.
        :type: str
        """
        self._nome = nome

    @property
    def tipo(self):
        """
        Gets the tipo of this Pessoa.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo da Pessoa, sendo: (\"PF\": Pessoa F\u00C3\u00ADsica), (\"PJ\": Pessoa Jur\u00C3\u00ADdica).

        :return: The tipo of this Pessoa.
        :rtype: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        """
        Sets the tipo of this Pessoa.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo da Pessoa, sendo: (\"PF\": Pessoa F\u00C3\u00ADsica), (\"PJ\": Pessoa Jur\u00C3\u00ADdica).

        :param tipo: The tipo of this Pessoa.
        :type: str
        """
        self._tipo = tipo

    @property
    def cpf(self):
        """
        Gets the cpf of this Pessoa.
        N\u00C3\u00BAmero do CPF, quando PF.

        :return: The cpf of this Pessoa.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this Pessoa.
        N\u00C3\u00BAmero do CPF, quando PF.

        :param cpf: The cpf of this Pessoa.
        :type: str
        """
        self._cpf = cpf

    @property
    def cnpj(self):
        """
        Gets the cnpj of this Pessoa.
        N\u00C3\u00BAmero do CNPJ, quando PJ.

        :return: The cnpj of this Pessoa.
        :rtype: str
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        """
        Sets the cnpj of this Pessoa.
        N\u00C3\u00BAmero do CNPJ, quando PJ.

        :param cnpj: The cnpj of this Pessoa.
        :type: str
        """
        self._cnpj = cnpj

    @property
    def data_nascimento(self):
        """
        Gets the data_nascimento of this Pessoa.
        Data de Nascimento da Pessoa, quando PF, ou a Data de Abertura da Empresa, quando PJ.

        :return: The data_nascimento of this Pessoa.
        :rtype: datetime
        """
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        """
        Sets the data_nascimento of this Pessoa.
        Data de Nascimento da Pessoa, quando PF, ou a Data de Abertura da Empresa, quando PJ.

        :param data_nascimento: The data_nascimento of this Pessoa.
        :type: datetime
        """
        self._data_nascimento = data_nascimento

    @property
    def numero_identidade(self):
        """
        Gets the numero_identidade of this Pessoa.
        N\u00C3\u00BAmero da Identidade

        :return: The numero_identidade of this Pessoa.
        :rtype: str
        """
        return self._numero_identidade

    @numero_identidade.setter
    def numero_identidade(self, numero_identidade):
        """
        Sets the numero_identidade of this Pessoa.
        N\u00C3\u00BAmero da Identidade

        :param numero_identidade: The numero_identidade of this Pessoa.
        :type: str
        """
        self._numero_identidade = numero_identidade

    @property
    def orgao_expedidor_identidade(self):
        """
        Gets the orgao_expedidor_identidade of this Pessoa.
        Org\u00C3\u00A3o expedidor do RG.

        :return: The orgao_expedidor_identidade of this Pessoa.
        :rtype: str
        """
        return self._orgao_expedidor_identidade

    @orgao_expedidor_identidade.setter
    def orgao_expedidor_identidade(self, orgao_expedidor_identidade):
        """
        Sets the orgao_expedidor_identidade of this Pessoa.
        Org\u00C3\u00A3o expedidor do RG.

        :param orgao_expedidor_identidade: The orgao_expedidor_identidade of this Pessoa.
        :type: str
        """
        self._orgao_expedidor_identidade = orgao_expedidor_identidade

    @property
    def sexo(self):
        """
        Gets the sexo of this Pessoa.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).

        :return: The sexo of this Pessoa.
        :rtype: str
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """
        Sets the sexo of this Pessoa.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).

        :param sexo: The sexo of this Pessoa.
        :type: str
        """
        self._sexo = sexo

    @property
    def unidade_federativa_identidade(self):
        """
        Gets the unidade_federativa_identidade of this Pessoa.
        Sigla da Unidade Federativa de onde foi expedido a Identidade

        :return: The unidade_federativa_identidade of this Pessoa.
        :rtype: str
        """
        return self._unidade_federativa_identidade

    @unidade_federativa_identidade.setter
    def unidade_federativa_identidade(self, unidade_federativa_identidade):
        """
        Sets the unidade_federativa_identidade of this Pessoa.
        Sigla da Unidade Federativa de onde foi expedido a Identidade

        :param unidade_federativa_identidade: The unidade_federativa_identidade of this Pessoa.
        :type: str
        """
        self._unidade_federativa_identidade = unidade_federativa_identidade

    @property
    def data_emissao_identidade(self):
        """
        Gets the data_emissao_identidade of this Pessoa.
        Data emiss\u00C3\u00A3o da identidade no formato aaaa-MM-dd

        :return: The data_emissao_identidade of this Pessoa.
        :rtype: date
        """
        return self._data_emissao_identidade

    @data_emissao_identidade.setter
    def data_emissao_identidade(self, data_emissao_identidade):
        """
        Sets the data_emissao_identidade of this Pessoa.
        Data emiss\u00C3\u00A3o da identidade no formato aaaa-MM-dd

        :param data_emissao_identidade: The data_emissao_identidade of this Pessoa.
        :type: date
        """
        self._data_emissao_identidade = data_emissao_identidade

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

