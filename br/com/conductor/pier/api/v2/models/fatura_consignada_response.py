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


class FaturaConsignadaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FaturaConsignadaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_conta': 'int',
            'flag_emite_fatura': 'int',
            'data_vencimento_fatura': 'str',
            'valor_total_fatura': 'float',
            'valor_fatura_anterior': 'float',
            'valor_pagamento_minimo': 'float',
            'valor_pagamento_consignado': 'float',
            'valor_pagamento_complementar': 'float',
            'total_compras_nacionais': 'float',
            'total_compras_internacionas': 'float',
            'total_saques_nacionais': 'float',
            'total_saques_internacionais': 'float',
            'total_debitos_nacionais': 'float',
            'total_debitos_recorrentes': 'float',
            'total_debitos_internacionais': 'float',
            'total_debitos_diversos_nacionais': 'float',
            'total_debitos_opcionais': 'float',
            'total_pagamentos': 'float',
            'total_creditos_nacionais': 'float',
            'total_ajustes': 'float',
            'total_tarifas': 'float',
            'total_multa': 'float',
            'total_juros': 'float',
            'taxa_rotativo': 'float',
            'taxa_saque': 'float',
            'taxa_maxima_proximo_periodo': 'float',
            'total_servicos': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'id_conta': 'idConta',
            'flag_emite_fatura': 'flagEmiteFatura',
            'data_vencimento_fatura': 'dataVencimentoFatura',
            'valor_total_fatura': 'valorTotalFatura',
            'valor_fatura_anterior': 'valorFaturaAnterior',
            'valor_pagamento_minimo': 'valorPagamentoMinimo',
            'valor_pagamento_consignado': 'valorPagamentoConsignado',
            'valor_pagamento_complementar': 'valorPagamentoComplementar',
            'total_compras_nacionais': 'totalComprasNacionais',
            'total_compras_internacionas': 'totalComprasInternacionas',
            'total_saques_nacionais': 'totalSaquesNacionais',
            'total_saques_internacionais': 'totalSaquesInternacionais',
            'total_debitos_nacionais': 'totalDebitosNacionais',
            'total_debitos_recorrentes': 'totalDebitosRecorrentes',
            'total_debitos_internacionais': 'totalDebitosInternacionais',
            'total_debitos_diversos_nacionais': 'totalDebitosDiversosNacionais',
            'total_debitos_opcionais': 'totalDebitosOpcionais',
            'total_pagamentos': 'totalPagamentos',
            'total_creditos_nacionais': 'totalCreditosNacionais',
            'total_ajustes': 'totalAjustes',
            'total_tarifas': 'totalTarifas',
            'total_multa': 'totalMulta',
            'total_juros': 'totalJuros',
            'taxa_rotativo': 'taxaRotativo',
            'taxa_saque': 'taxaSaque',
            'taxa_maxima_proximo_periodo': 'taxaMaximaProximoPeriodo',
            'total_servicos': 'totalServicos'
        }

        self._id = None
        self._id_conta = None
        self._flag_emite_fatura = None
        self._data_vencimento_fatura = None
        self._valor_total_fatura = None
        self._valor_fatura_anterior = None
        self._valor_pagamento_minimo = None
        self._valor_pagamento_consignado = None
        self._valor_pagamento_complementar = None
        self._total_compras_nacionais = None
        self._total_compras_internacionas = None
        self._total_saques_nacionais = None
        self._total_saques_internacionais = None
        self._total_debitos_nacionais = None
        self._total_debitos_recorrentes = None
        self._total_debitos_internacionais = None
        self._total_debitos_diversos_nacionais = None
        self._total_debitos_opcionais = None
        self._total_pagamentos = None
        self._total_creditos_nacionais = None
        self._total_ajustes = None
        self._total_tarifas = None
        self._total_multa = None
        self._total_juros = None
        self._taxa_rotativo = None
        self._taxa_saque = None
        self._taxa_maxima_proximo_periodo = None
        self._total_servicos = None

    @property
    def id(self):
        """
        Gets the id of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da fatura.

        :return: The id of this FaturaConsignadaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da fatura.

        :param id: The id of this FaturaConsignadaResponse.
        :type: int
        """
        self._id = id

    @property
    def id_conta(self):
        """
        Gets the id_conta of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da conta (id).

        :return: The id_conta of this FaturaConsignadaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da conta (id).

        :param id_conta: The id_conta of this FaturaConsignadaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def flag_emite_fatura(self):
        """
        Gets the flag_emite_fatura of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da conta a qual a fatura se refere.

        :return: The flag_emite_fatura of this FaturaConsignadaResponse.
        :rtype: int
        """
        return self._flag_emite_fatura

    @flag_emite_fatura.setter
    def flag_emite_fatura(self, flag_emite_fatura):
        """
        Sets the flag_emite_fatura of this FaturaConsignadaResponse.
        C\u00C3\u00B3digo identificador da conta a qual a fatura se refere.

        :param flag_emite_fatura: The flag_emite_fatura of this FaturaConsignadaResponse.
        :type: int
        """
        self._flag_emite_fatura = flag_emite_fatura

    @property
    def data_vencimento_fatura(self):
        """
        Gets the data_vencimento_fatura of this FaturaConsignadaResponse.
        Data de vencimento da fatura.

        :return: The data_vencimento_fatura of this FaturaConsignadaResponse.
        :rtype: str
        """
        return self._data_vencimento_fatura

    @data_vencimento_fatura.setter
    def data_vencimento_fatura(self, data_vencimento_fatura):
        """
        Sets the data_vencimento_fatura of this FaturaConsignadaResponse.
        Data de vencimento da fatura.

        :param data_vencimento_fatura: The data_vencimento_fatura of this FaturaConsignadaResponse.
        :type: str
        """
        self._data_vencimento_fatura = data_vencimento_fatura

    @property
    def valor_total_fatura(self):
        """
        Gets the valor_total_fatura of this FaturaConsignadaResponse.
        Valor para pagamento total da fatura.

        :return: The valor_total_fatura of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._valor_total_fatura

    @valor_total_fatura.setter
    def valor_total_fatura(self, valor_total_fatura):
        """
        Sets the valor_total_fatura of this FaturaConsignadaResponse.
        Valor para pagamento total da fatura.

        :param valor_total_fatura: The valor_total_fatura of this FaturaConsignadaResponse.
        :type: float
        """
        self._valor_total_fatura = valor_total_fatura

    @property
    def valor_fatura_anterior(self):
        """
        Gets the valor_fatura_anterior of this FaturaConsignadaResponse.
        Valor total da fatura anterior.

        :return: The valor_fatura_anterior of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._valor_fatura_anterior

    @valor_fatura_anterior.setter
    def valor_fatura_anterior(self, valor_fatura_anterior):
        """
        Sets the valor_fatura_anterior of this FaturaConsignadaResponse.
        Valor total da fatura anterior.

        :param valor_fatura_anterior: The valor_fatura_anterior of this FaturaConsignadaResponse.
        :type: float
        """
        self._valor_fatura_anterior = valor_fatura_anterior

    @property
    def valor_pagamento_minimo(self):
        """
        Gets the valor_pagamento_minimo of this FaturaConsignadaResponse.
        Valor m\u00C3\u00ADnimo para pagamento da fatura.

        :return: The valor_pagamento_minimo of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._valor_pagamento_minimo

    @valor_pagamento_minimo.setter
    def valor_pagamento_minimo(self, valor_pagamento_minimo):
        """
        Sets the valor_pagamento_minimo of this FaturaConsignadaResponse.
        Valor m\u00C3\u00ADnimo para pagamento da fatura.

        :param valor_pagamento_minimo: The valor_pagamento_minimo of this FaturaConsignadaResponse.
        :type: float
        """
        self._valor_pagamento_minimo = valor_pagamento_minimo

    @property
    def valor_pagamento_consignado(self):
        """
        Gets the valor_pagamento_consignado of this FaturaConsignadaResponse.
        Valor da fatura pago atrav\u00C3\u00A9s de desconto em folha.

        :return: The valor_pagamento_consignado of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._valor_pagamento_consignado

    @valor_pagamento_consignado.setter
    def valor_pagamento_consignado(self, valor_pagamento_consignado):
        """
        Sets the valor_pagamento_consignado of this FaturaConsignadaResponse.
        Valor da fatura pago atrav\u00C3\u00A9s de desconto em folha.

        :param valor_pagamento_consignado: The valor_pagamento_consignado of this FaturaConsignadaResponse.
        :type: float
        """
        self._valor_pagamento_consignado = valor_pagamento_consignado

    @property
    def valor_pagamento_complementar(self):
        """
        Gets the valor_pagamento_complementar of this FaturaConsignadaResponse.
        Valor complementar para considerar o pagamento m\u00C3\u00ADnimo da fatura.

        :return: The valor_pagamento_complementar of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._valor_pagamento_complementar

    @valor_pagamento_complementar.setter
    def valor_pagamento_complementar(self, valor_pagamento_complementar):
        """
        Sets the valor_pagamento_complementar of this FaturaConsignadaResponse.
        Valor complementar para considerar o pagamento m\u00C3\u00ADnimo da fatura.

        :param valor_pagamento_complementar: The valor_pagamento_complementar of this FaturaConsignadaResponse.
        :type: float
        """
        self._valor_pagamento_complementar = valor_pagamento_complementar

    @property
    def total_compras_nacionais(self):
        """
        Gets the total_compras_nacionais of this FaturaConsignadaResponse.
        Valor total das compras nacionais lan\u00C3\u00A7adas na fatura.

        :return: The total_compras_nacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_compras_nacionais

    @total_compras_nacionais.setter
    def total_compras_nacionais(self, total_compras_nacionais):
        """
        Sets the total_compras_nacionais of this FaturaConsignadaResponse.
        Valor total das compras nacionais lan\u00C3\u00A7adas na fatura.

        :param total_compras_nacionais: The total_compras_nacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_compras_nacionais = total_compras_nacionais

    @property
    def total_compras_internacionas(self):
        """
        Gets the total_compras_internacionas of this FaturaConsignadaResponse.
        Valor total das compras internacionais lan\u00C3\u00A7adas na fatura.

        :return: The total_compras_internacionas of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_compras_internacionas

    @total_compras_internacionas.setter
    def total_compras_internacionas(self, total_compras_internacionas):
        """
        Sets the total_compras_internacionas of this FaturaConsignadaResponse.
        Valor total das compras internacionais lan\u00C3\u00A7adas na fatura.

        :param total_compras_internacionas: The total_compras_internacionas of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_compras_internacionas = total_compras_internacionas

    @property
    def total_saques_nacionais(self):
        """
        Gets the total_saques_nacionais of this FaturaConsignadaResponse.
        Valor total dos saques nacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_saques_nacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_saques_nacionais

    @total_saques_nacionais.setter
    def total_saques_nacionais(self, total_saques_nacionais):
        """
        Sets the total_saques_nacionais of this FaturaConsignadaResponse.
        Valor total dos saques nacionais lan\u00C3\u00A7ados na fatura.

        :param total_saques_nacionais: The total_saques_nacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_saques_nacionais = total_saques_nacionais

    @property
    def total_saques_internacionais(self):
        """
        Gets the total_saques_internacionais of this FaturaConsignadaResponse.
        Valor total dos saques internacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_saques_internacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_saques_internacionais

    @total_saques_internacionais.setter
    def total_saques_internacionais(self, total_saques_internacionais):
        """
        Sets the total_saques_internacionais of this FaturaConsignadaResponse.
        Valor total dos saques internacionais lan\u00C3\u00A7ados na fatura.

        :param total_saques_internacionais: The total_saques_internacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_saques_internacionais = total_saques_internacionais

    @property
    def total_debitos_nacionais(self):
        """
        Gets the total_debitos_nacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos nacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_debitos_nacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_debitos_nacionais

    @total_debitos_nacionais.setter
    def total_debitos_nacionais(self, total_debitos_nacionais):
        """
        Sets the total_debitos_nacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos nacionais lan\u00C3\u00A7ados na fatura.

        :param total_debitos_nacionais: The total_debitos_nacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_debitos_nacionais = total_debitos_nacionais

    @property
    def total_debitos_recorrentes(self):
        """
        Gets the total_debitos_recorrentes of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos recorrentes lan\u00C3\u00A7ados na fatura.

        :return: The total_debitos_recorrentes of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_debitos_recorrentes

    @total_debitos_recorrentes.setter
    def total_debitos_recorrentes(self, total_debitos_recorrentes):
        """
        Sets the total_debitos_recorrentes of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos recorrentes lan\u00C3\u00A7ados na fatura.

        :param total_debitos_recorrentes: The total_debitos_recorrentes of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_debitos_recorrentes = total_debitos_recorrentes

    @property
    def total_debitos_internacionais(self):
        """
        Gets the total_debitos_internacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos internacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_debitos_internacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_debitos_internacionais

    @total_debitos_internacionais.setter
    def total_debitos_internacionais(self, total_debitos_internacionais):
        """
        Sets the total_debitos_internacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos internacionais lan\u00C3\u00A7ados na fatura.

        :param total_debitos_internacionais: The total_debitos_internacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_debitos_internacionais = total_debitos_internacionais

    @property
    def total_debitos_diversos_nacionais(self):
        """
        Gets the total_debitos_diversos_nacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos diversos nacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_debitos_diversos_nacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_debitos_diversos_nacionais

    @total_debitos_diversos_nacionais.setter
    def total_debitos_diversos_nacionais(self, total_debitos_diversos_nacionais):
        """
        Sets the total_debitos_diversos_nacionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos diversos nacionais lan\u00C3\u00A7ados na fatura.

        :param total_debitos_diversos_nacionais: The total_debitos_diversos_nacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_debitos_diversos_nacionais = total_debitos_diversos_nacionais

    @property
    def total_debitos_opcionais(self):
        """
        Gets the total_debitos_opcionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos diversos opcionais lan\u00C3\u00A7ados na fatura.

        :return: The total_debitos_opcionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_debitos_opcionais

    @total_debitos_opcionais.setter
    def total_debitos_opcionais(self, total_debitos_opcionais):
        """
        Sets the total_debitos_opcionais of this FaturaConsignadaResponse.
        Valor total dos d\u00C3\u00A9bitos diversos opcionais lan\u00C3\u00A7ados na fatura.

        :param total_debitos_opcionais: The total_debitos_opcionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_debitos_opcionais = total_debitos_opcionais

    @property
    def total_pagamentos(self):
        """
        Gets the total_pagamentos of this FaturaConsignadaResponse.
        Valor total dos pagamentos lan\u00C3\u00A7ados na fatura.

        :return: The total_pagamentos of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_pagamentos

    @total_pagamentos.setter
    def total_pagamentos(self, total_pagamentos):
        """
        Sets the total_pagamentos of this FaturaConsignadaResponse.
        Valor total dos pagamentos lan\u00C3\u00A7ados na fatura.

        :param total_pagamentos: The total_pagamentos of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_pagamentos = total_pagamentos

    @property
    def total_creditos_nacionais(self):
        """
        Gets the total_creditos_nacionais of this FaturaConsignadaResponse.
        Valor total dos cr\u00C3\u00A9ditos nacionais lan\u00C3\u00A7ados na fatura.

        :return: The total_creditos_nacionais of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_creditos_nacionais

    @total_creditos_nacionais.setter
    def total_creditos_nacionais(self, total_creditos_nacionais):
        """
        Sets the total_creditos_nacionais of this FaturaConsignadaResponse.
        Valor total dos cr\u00C3\u00A9ditos nacionais lan\u00C3\u00A7ados na fatura.

        :param total_creditos_nacionais: The total_creditos_nacionais of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_creditos_nacionais = total_creditos_nacionais

    @property
    def total_ajustes(self):
        """
        Gets the total_ajustes of this FaturaConsignadaResponse.
        Valor total dos ajustes lan\u00C3\u00A7ados na fatura.

        :return: The total_ajustes of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_ajustes

    @total_ajustes.setter
    def total_ajustes(self, total_ajustes):
        """
        Sets the total_ajustes of this FaturaConsignadaResponse.
        Valor total dos ajustes lan\u00C3\u00A7ados na fatura.

        :param total_ajustes: The total_ajustes of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_ajustes = total_ajustes

    @property
    def total_tarifas(self):
        """
        Gets the total_tarifas of this FaturaConsignadaResponse.
        Valor total das tarifas lan\u00C3\u00A7adas na fatura.

        :return: The total_tarifas of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_tarifas

    @total_tarifas.setter
    def total_tarifas(self, total_tarifas):
        """
        Sets the total_tarifas of this FaturaConsignadaResponse.
        Valor total das tarifas lan\u00C3\u00A7adas na fatura.

        :param total_tarifas: The total_tarifas of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_tarifas = total_tarifas

    @property
    def total_multa(self):
        """
        Gets the total_multa of this FaturaConsignadaResponse.
        Valor total da multa lan\u00C3\u00A7ada na fatura.

        :return: The total_multa of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_multa

    @total_multa.setter
    def total_multa(self, total_multa):
        """
        Sets the total_multa of this FaturaConsignadaResponse.
        Valor total da multa lan\u00C3\u00A7ada na fatura.

        :param total_multa: The total_multa of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_multa = total_multa

    @property
    def total_juros(self):
        """
        Gets the total_juros of this FaturaConsignadaResponse.
        Valor total dos juros de mora lan\u00C3\u00A7ados na fatura.

        :return: The total_juros of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_juros

    @total_juros.setter
    def total_juros(self, total_juros):
        """
        Sets the total_juros of this FaturaConsignadaResponse.
        Valor total dos juros de mora lan\u00C3\u00A7ados na fatura.

        :param total_juros: The total_juros of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_juros = total_juros

    @property
    def taxa_rotativo(self):
        """
        Gets the taxa_rotativo of this FaturaConsignadaResponse.
        Valor percentual da taxa de juros rotativos.

        :return: The taxa_rotativo of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._taxa_rotativo

    @taxa_rotativo.setter
    def taxa_rotativo(self, taxa_rotativo):
        """
        Sets the taxa_rotativo of this FaturaConsignadaResponse.
        Valor percentual da taxa de juros rotativos.

        :param taxa_rotativo: The taxa_rotativo of this FaturaConsignadaResponse.
        :type: float
        """
        self._taxa_rotativo = taxa_rotativo

    @property
    def taxa_saque(self):
        """
        Gets the taxa_saque of this FaturaConsignadaResponse.
        Valor percentual da taxa de saque.

        :return: The taxa_saque of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._taxa_saque

    @taxa_saque.setter
    def taxa_saque(self, taxa_saque):
        """
        Sets the taxa_saque of this FaturaConsignadaResponse.
        Valor percentual da taxa de saque.

        :param taxa_saque: The taxa_saque of this FaturaConsignadaResponse.
        :type: float
        """
        self._taxa_saque = taxa_saque

    @property
    def taxa_maxima_proximo_periodo(self):
        """
        Gets the taxa_maxima_proximo_periodo of this FaturaConsignadaResponse.
        Valor m\u00C3\u00A1ximo percentual da taxa de encargos para o pr\u00C3\u00B3ximo per\u00C3\u00ADodo.

        :return: The taxa_maxima_proximo_periodo of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._taxa_maxima_proximo_periodo

    @taxa_maxima_proximo_periodo.setter
    def taxa_maxima_proximo_periodo(self, taxa_maxima_proximo_periodo):
        """
        Sets the taxa_maxima_proximo_periodo of this FaturaConsignadaResponse.
        Valor m\u00C3\u00A1ximo percentual da taxa de encargos para o pr\u00C3\u00B3ximo per\u00C3\u00ADodo.

        :param taxa_maxima_proximo_periodo: The taxa_maxima_proximo_periodo of this FaturaConsignadaResponse.
        :type: float
        """
        self._taxa_maxima_proximo_periodo = taxa_maxima_proximo_periodo

    @property
    def total_servicos(self):
        """
        Gets the total_servicos of this FaturaConsignadaResponse.
        Apresenta a soma de todos os seguros cobrados na fatura do cliente.

        :return: The total_servicos of this FaturaConsignadaResponse.
        :rtype: float
        """
        return self._total_servicos

    @total_servicos.setter
    def total_servicos(self, total_servicos):
        """
        Sets the total_servicos of this FaturaConsignadaResponse.
        Apresenta a soma de todos os seguros cobrados na fatura do cliente.

        :param total_servicos: The total_servicos of this FaturaConsignadaResponse.
        :type: float
        """
        self._total_servicos = total_servicos

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

