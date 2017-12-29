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


class CredorResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CredorResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_pessoa_juridica': 'int',
            'nome': 'str',
            'periodicidade': 'str',
            'pagamento_semanal': 'str',
            'pagamento_mensal': 'int',
            'pagamento_decendial_primeiro': 'int',
            'pagamento_decendial_segundo': 'int',
            'pagamento_decendial_terceiro': 'int',
            'pagamento_quinzenal_primeiro': 'int',
            'pagamento_quinzenal_segundo': 'int',
            'credor_banco': 'bool',
            'percentual_rav': 'float',
            'recebe_rav': 'str',
            'percentual_multiplica': 'float',
            'taxa_adm': 'float',
            'taxa_banco': 'float',
            'limite_rav': 'float',
            'id_credor_rav': 'int',
            'banco': 'int',
            'agencia': 'int',
            'digito_verificador_agencia': 'str',
            'conta_corrente': 'str',
            'digito_verificador_conta_corrente': 'str',
            'usuario': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_pessoa_juridica': 'idPessoaJuridica',
            'nome': 'nome',
            'periodicidade': 'periodicidade',
            'pagamento_semanal': 'pagamentoSemanal',
            'pagamento_mensal': 'pagamentoMensal',
            'pagamento_decendial_primeiro': 'pagamentoDecendialPrimeiro',
            'pagamento_decendial_segundo': 'pagamentoDecendialSegundo',
            'pagamento_decendial_terceiro': 'pagamentoDecendialTerceiro',
            'pagamento_quinzenal_primeiro': 'pagamentoQuinzenalPrimeiro',
            'pagamento_quinzenal_segundo': 'pagamentoQuinzenalSegundo',
            'credor_banco': 'credorBanco',
            'percentual_rav': 'percentualRAV',
            'recebe_rav': 'recebeRAV',
            'percentual_multiplica': 'percentualMultiplica',
            'taxa_adm': 'taxaAdm',
            'taxa_banco': 'taxaBanco',
            'limite_rav': 'limiteRAV',
            'id_credor_rav': 'idCredorRAV',
            'banco': 'banco',
            'agencia': 'agencia',
            'digito_verificador_agencia': 'digitoVerificadorAgencia',
            'conta_corrente': 'contaCorrente',
            'digito_verificador_conta_corrente': 'digitoVerificadorContaCorrente',
            'usuario': 'usuario'
        }

        self._id = None
        self._id_pessoa_juridica = None
        self._nome = None
        self._periodicidade = None
        self._pagamento_semanal = None
        self._pagamento_mensal = None
        self._pagamento_decendial_primeiro = None
        self._pagamento_decendial_segundo = None
        self._pagamento_decendial_terceiro = None
        self._pagamento_quinzenal_primeiro = None
        self._pagamento_quinzenal_segundo = None
        self._credor_banco = None
        self._percentual_rav = None
        self._recebe_rav = None
        self._percentual_multiplica = None
        self._taxa_adm = None
        self._taxa_banco = None
        self._limite_rav = None
        self._id_credor_rav = None
        self._banco = None
        self._agencia = None
        self._digito_verificador_agencia = None
        self._conta_corrente = None
        self._digito_verificador_conta_corrente = None
        self._usuario = None

    @property
    def id(self):
        """
        Gets the id of this CredorResponse.
        C\u00C3\u00B3digo identificador do credor

        :return: The id of this CredorResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CredorResponse.
        C\u00C3\u00B3digo identificador do credor

        :param id: The id of this CredorResponse.
        :type: int
        """
        self._id = id

    @property
    def id_pessoa_juridica(self):
        """
        Gets the id_pessoa_juridica of this CredorResponse.
        Identificador da pessoa jur\u00C3\u00ADdica do credor

        :return: The id_pessoa_juridica of this CredorResponse.
        :rtype: int
        """
        return self._id_pessoa_juridica

    @id_pessoa_juridica.setter
    def id_pessoa_juridica(self, id_pessoa_juridica):
        """
        Sets the id_pessoa_juridica of this CredorResponse.
        Identificador da pessoa jur\u00C3\u00ADdica do credor

        :param id_pessoa_juridica: The id_pessoa_juridica of this CredorResponse.
        :type: int
        """
        self._id_pessoa_juridica = id_pessoa_juridica

    @property
    def nome(self):
        """
        Gets the nome of this CredorResponse.
        Nome do credor

        :return: The nome of this CredorResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this CredorResponse.
        Nome do credor

        :param nome: The nome of this CredorResponse.
        :type: str
        """
        self._nome = nome

    @property
    def periodicidade(self):
        """
        Gets the periodicidade of this CredorResponse.
        Periodicidade do pagamento

        :return: The periodicidade of this CredorResponse.
        :rtype: str
        """
        return self._periodicidade

    @periodicidade.setter
    def periodicidade(self, periodicidade):
        """
        Sets the periodicidade of this CredorResponse.
        Periodicidade do pagamento

        :param periodicidade: The periodicidade of this CredorResponse.
        :type: str
        """
        allowed_values = ["DIARIO", "SEMANAL", "MENSAL", "DECENDIAL", "QUINZENAL"]
        if periodicidade not in allowed_values:
            raise ValueError(
                "Invalid value for `periodicidade`, must be one of {0}"
                .format(allowed_values)
            )
        self._periodicidade = periodicidade

    @property
    def pagamento_semanal(self):
        """
        Gets the pagamento_semanal of this CredorResponse.
        Dia para pagamento semanal

        :return: The pagamento_semanal of this CredorResponse.
        :rtype: str
        """
        return self._pagamento_semanal

    @pagamento_semanal.setter
    def pagamento_semanal(self, pagamento_semanal):
        """
        Sets the pagamento_semanal of this CredorResponse.
        Dia para pagamento semanal

        :param pagamento_semanal: The pagamento_semanal of this CredorResponse.
        :type: str
        """
        allowed_values = ["SEGUNDA", "TERCA", "QUARTA", "QUINTA", "SEXTA", "SABADO", "DOMINGO"]
        if pagamento_semanal not in allowed_values:
            raise ValueError(
                "Invalid value for `pagamento_semanal`, must be one of {0}"
                .format(allowed_values)
            )
        self._pagamento_semanal = pagamento_semanal

    @property
    def pagamento_mensal(self):
        """
        Gets the pagamento_mensal of this CredorResponse.
        Dia da data para o pagamento mensal

        :return: The pagamento_mensal of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_mensal

    @pagamento_mensal.setter
    def pagamento_mensal(self, pagamento_mensal):
        """
        Sets the pagamento_mensal of this CredorResponse.
        Dia da data para o pagamento mensal

        :param pagamento_mensal: The pagamento_mensal of this CredorResponse.
        :type: int
        """
        self._pagamento_mensal = pagamento_mensal

    @property
    def pagamento_decendial_primeiro(self):
        """
        Gets the pagamento_decendial_primeiro of this CredorResponse.
        Dia da data para o primeiro pagamento decendial

        :return: The pagamento_decendial_primeiro of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_decendial_primeiro

    @pagamento_decendial_primeiro.setter
    def pagamento_decendial_primeiro(self, pagamento_decendial_primeiro):
        """
        Sets the pagamento_decendial_primeiro of this CredorResponse.
        Dia da data para o primeiro pagamento decendial

        :param pagamento_decendial_primeiro: The pagamento_decendial_primeiro of this CredorResponse.
        :type: int
        """
        self._pagamento_decendial_primeiro = pagamento_decendial_primeiro

    @property
    def pagamento_decendial_segundo(self):
        """
        Gets the pagamento_decendial_segundo of this CredorResponse.
        Dia da data para o segundo pagamento decendial

        :return: The pagamento_decendial_segundo of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_decendial_segundo

    @pagamento_decendial_segundo.setter
    def pagamento_decendial_segundo(self, pagamento_decendial_segundo):
        """
        Sets the pagamento_decendial_segundo of this CredorResponse.
        Dia da data para o segundo pagamento decendial

        :param pagamento_decendial_segundo: The pagamento_decendial_segundo of this CredorResponse.
        :type: int
        """
        self._pagamento_decendial_segundo = pagamento_decendial_segundo

    @property
    def pagamento_decendial_terceiro(self):
        """
        Gets the pagamento_decendial_terceiro of this CredorResponse.
        Dia da data para o terceiro pagamento decendial

        :return: The pagamento_decendial_terceiro of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_decendial_terceiro

    @pagamento_decendial_terceiro.setter
    def pagamento_decendial_terceiro(self, pagamento_decendial_terceiro):
        """
        Sets the pagamento_decendial_terceiro of this CredorResponse.
        Dia da data para o terceiro pagamento decendial

        :param pagamento_decendial_terceiro: The pagamento_decendial_terceiro of this CredorResponse.
        :type: int
        """
        self._pagamento_decendial_terceiro = pagamento_decendial_terceiro

    @property
    def pagamento_quinzenal_primeiro(self):
        """
        Gets the pagamento_quinzenal_primeiro of this CredorResponse.
        Dia da data para o primeiro pagamento quinzenal

        :return: The pagamento_quinzenal_primeiro of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_quinzenal_primeiro

    @pagamento_quinzenal_primeiro.setter
    def pagamento_quinzenal_primeiro(self, pagamento_quinzenal_primeiro):
        """
        Sets the pagamento_quinzenal_primeiro of this CredorResponse.
        Dia da data para o primeiro pagamento quinzenal

        :param pagamento_quinzenal_primeiro: The pagamento_quinzenal_primeiro of this CredorResponse.
        :type: int
        """
        self._pagamento_quinzenal_primeiro = pagamento_quinzenal_primeiro

    @property
    def pagamento_quinzenal_segundo(self):
        """
        Gets the pagamento_quinzenal_segundo of this CredorResponse.
        Dia da data para o segundo pagamento quinzenal

        :return: The pagamento_quinzenal_segundo of this CredorResponse.
        :rtype: int
        """
        return self._pagamento_quinzenal_segundo

    @pagamento_quinzenal_segundo.setter
    def pagamento_quinzenal_segundo(self, pagamento_quinzenal_segundo):
        """
        Sets the pagamento_quinzenal_segundo of this CredorResponse.
        Dia da data para o segundo pagamento quinzenal

        :param pagamento_quinzenal_segundo: The pagamento_quinzenal_segundo of this CredorResponse.
        :type: int
        """
        self._pagamento_quinzenal_segundo = pagamento_quinzenal_segundo

    @property
    def credor_banco(self):
        """
        Gets the credor_banco of this CredorResponse.
        Indica se este credor pode ser um Credor RAV de outros credores

        :return: The credor_banco of this CredorResponse.
        :rtype: bool
        """
        return self._credor_banco

    @credor_banco.setter
    def credor_banco(self, credor_banco):
        """
        Sets the credor_banco of this CredorResponse.
        Indica se este credor pode ser um Credor RAV de outros credores

        :param credor_banco: The credor_banco of this CredorResponse.
        :type: bool
        """
        self._credor_banco = credor_banco

    @property
    def percentual_rav(self):
        """
        Gets the percentual_rav of this CredorResponse.
        Valor percentual do RAV do credor

        :return: The percentual_rav of this CredorResponse.
        :rtype: float
        """
        return self._percentual_rav

    @percentual_rav.setter
    def percentual_rav(self, percentual_rav):
        """
        Sets the percentual_rav of this CredorResponse.
        Valor percentual do RAV do credor

        :param percentual_rav: The percentual_rav of this CredorResponse.
        :type: float
        """
        self._percentual_rav = percentual_rav

    @property
    def recebe_rav(self):
        """
        Gets the recebe_rav of this CredorResponse.
        Indica se o credor recebe RAV e o tipo

        :return: The recebe_rav of this CredorResponse.
        :rtype: str
        """
        return self._recebe_rav

    @recebe_rav.setter
    def recebe_rav(self, recebe_rav):
        """
        Sets the recebe_rav of this CredorResponse.
        Indica se o credor recebe RAV e o tipo

        :param recebe_rav: The recebe_rav of this CredorResponse.
        :type: str
        """
        allowed_values = ["NAO_TEM_PERMISSAO_RAV", "CREDITO_RAV", "DEBITO_RAV"]
        if recebe_rav not in allowed_values:
            raise ValueError(
                "Invalid value for `recebe_rav`, must be one of {0}"
                .format(allowed_values)
            )
        self._recebe_rav = recebe_rav

    @property
    def percentual_multiplica(self):
        """
        Gets the percentual_multiplica of this CredorResponse.
        Percentual Multiplica

        :return: The percentual_multiplica of this CredorResponse.
        :rtype: float
        """
        return self._percentual_multiplica

    @percentual_multiplica.setter
    def percentual_multiplica(self, percentual_multiplica):
        """
        Sets the percentual_multiplica of this CredorResponse.
        Percentual Multiplica

        :param percentual_multiplica: The percentual_multiplica of this CredorResponse.
        :type: float
        """
        self._percentual_multiplica = percentual_multiplica

    @property
    def taxa_adm(self):
        """
        Gets the taxa_adm of this CredorResponse.
        Taxa Administrativa

        :return: The taxa_adm of this CredorResponse.
        :rtype: float
        """
        return self._taxa_adm

    @taxa_adm.setter
    def taxa_adm(self, taxa_adm):
        """
        Sets the taxa_adm of this CredorResponse.
        Taxa Administrativa

        :param taxa_adm: The taxa_adm of this CredorResponse.
        :type: float
        """
        self._taxa_adm = taxa_adm

    @property
    def taxa_banco(self):
        """
        Gets the taxa_banco of this CredorResponse.
        Taxa do Banco

        :return: The taxa_banco of this CredorResponse.
        :rtype: float
        """
        return self._taxa_banco

    @taxa_banco.setter
    def taxa_banco(self, taxa_banco):
        """
        Sets the taxa_banco of this CredorResponse.
        Taxa do Banco

        :param taxa_banco: The taxa_banco of this CredorResponse.
        :type: float
        """
        self._taxa_banco = taxa_banco

    @property
    def limite_rav(self):
        """
        Gets the limite_rav of this CredorResponse.
        Valor limite do RAV

        :return: The limite_rav of this CredorResponse.
        :rtype: float
        """
        return self._limite_rav

    @limite_rav.setter
    def limite_rav(self, limite_rav):
        """
        Sets the limite_rav of this CredorResponse.
        Valor limite do RAV

        :param limite_rav: The limite_rav of this CredorResponse.
        :type: float
        """
        self._limite_rav = limite_rav

    @property
    def id_credor_rav(self):
        """
        Gets the id_credor_rav of this CredorResponse.
        C\u00C3\u00B3digo identificador do credor RAV

        :return: The id_credor_rav of this CredorResponse.
        :rtype: int
        """
        return self._id_credor_rav

    @id_credor_rav.setter
    def id_credor_rav(self, id_credor_rav):
        """
        Sets the id_credor_rav of this CredorResponse.
        C\u00C3\u00B3digo identificador do credor RAV

        :param id_credor_rav: The id_credor_rav of this CredorResponse.
        :type: int
        """
        self._id_credor_rav = id_credor_rav

    @property
    def banco(self):
        """
        Gets the banco of this CredorResponse.
        C\u00C3\u00B3digo do banco

        :return: The banco of this CredorResponse.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this CredorResponse.
        C\u00C3\u00B3digo do banco

        :param banco: The banco of this CredorResponse.
        :type: int
        """
        self._banco = banco

    @property
    def agencia(self):
        """
        Gets the agencia of this CredorResponse.
        Raz\u00C3\u00A3o social da pessoa jur\u00C3\u00ADdica

        :return: The agencia of this CredorResponse.
        :rtype: int
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        """
        Sets the agencia of this CredorResponse.
        Raz\u00C3\u00A3o social da pessoa jur\u00C3\u00ADdica

        :param agencia: The agencia of this CredorResponse.
        :type: int
        """
        self._agencia = agencia

    @property
    def digito_verificador_agencia(self):
        """
        Gets the digito_verificador_agencia of this CredorResponse.
        D\u00C3\u00ADgito Verificador da ag\u00C3\u00AAncia

        :return: The digito_verificador_agencia of this CredorResponse.
        :rtype: str
        """
        return self._digito_verificador_agencia

    @digito_verificador_agencia.setter
    def digito_verificador_agencia(self, digito_verificador_agencia):
        """
        Sets the digito_verificador_agencia of this CredorResponse.
        D\u00C3\u00ADgito Verificador da ag\u00C3\u00AAncia

        :param digito_verificador_agencia: The digito_verificador_agencia of this CredorResponse.
        :type: str
        """
        self._digito_verificador_agencia = digito_verificador_agencia

    @property
    def conta_corrente(self):
        """
        Gets the conta_corrente of this CredorResponse.
        C\u00C3\u00B3digo da Conta Corrente

        :return: The conta_corrente of this CredorResponse.
        :rtype: str
        """
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        """
        Sets the conta_corrente of this CredorResponse.
        C\u00C3\u00B3digo da Conta Corrente

        :param conta_corrente: The conta_corrente of this CredorResponse.
        :type: str
        """
        self._conta_corrente = conta_corrente

    @property
    def digito_verificador_conta_corrente(self):
        """
        Gets the digito_verificador_conta_corrente of this CredorResponse.
        D\u00C3\u00ADgito Verificador da Conta Corrente

        :return: The digito_verificador_conta_corrente of this CredorResponse.
        :rtype: str
        """
        return self._digito_verificador_conta_corrente

    @digito_verificador_conta_corrente.setter
    def digito_verificador_conta_corrente(self, digito_verificador_conta_corrente):
        """
        Sets the digito_verificador_conta_corrente of this CredorResponse.
        D\u00C3\u00ADgito Verificador da Conta Corrente

        :param digito_verificador_conta_corrente: The digito_verificador_conta_corrente of this CredorResponse.
        :type: str
        """
        self._digito_verificador_conta_corrente = digito_verificador_conta_corrente

    @property
    def usuario(self):
        """
        Gets the usuario of this CredorResponse.
        Login do usu\u00C3\u00A1rio para registro da inser\u00C3\u00A7\u00C3\u00A3o

        :return: The usuario of this CredorResponse.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this CredorResponse.
        Login do usu\u00C3\u00A1rio para registro da inser\u00C3\u00A7\u00C3\u00A3o

        :param usuario: The usuario of this CredorResponse.
        :type: str
        """
        self._usuario = usuario

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

