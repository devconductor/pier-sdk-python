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


class TransferenciaBancariaPersistValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransferenciaBancariaPersistValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'valor_compra': 'float',
            'valor': 'float',
            'documento_favorecido': 'str',
            'banco': 'int',
            'numero_agencia': 'str',
            'digito_agencia': 'str',
            'numero_conta': 'str',
            'digito_conta': 'str',
            'flag_conta_poupanca': 'int',
            'nome_favorecido': 'str'
        }

        self.attribute_map = {
            'valor_compra': 'valorCompra',
            'valor': 'valor',
            'documento_favorecido': 'documentoFavorecido',
            'banco': 'banco',
            'numero_agencia': 'numeroAgencia',
            'digito_agencia': 'digitoAgencia',
            'numero_conta': 'numeroConta',
            'digito_conta': 'digitoConta',
            'flag_conta_poupanca': 'flagContaPoupanca',
            'nome_favorecido': 'nomeFavorecido'
        }

        self._valor_compra = None
        self._valor = None
        self._documento_favorecido = None
        self._banco = None
        self._numero_agencia = None
        self._digito_agencia = None
        self._numero_conta = None
        self._digito_conta = None
        self._flag_conta_poupanca = None
        self._nome_favorecido = None

    @property
    def valor_compra(self):
        """
        Gets the valor_compra of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_valor_compra_value}}}

        :return: The valor_compra of this TransferenciaBancariaPersistValue.
        :rtype: float
        """
        return self._valor_compra

    @valor_compra.setter
    def valor_compra(self, valor_compra):
        """
        Sets the valor_compra of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_valor_compra_value}}}

        :param valor_compra: The valor_compra of this TransferenciaBancariaPersistValue.
        :type: float
        """
        self._valor_compra = valor_compra

    @property
    def valor(self):
        """
        Gets the valor of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_valor_value}}}

        :return: The valor of this TransferenciaBancariaPersistValue.
        :rtype: float
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """
        Sets the valor of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_valor_value}}}

        :param valor: The valor of this TransferenciaBancariaPersistValue.
        :type: float
        """
        self._valor = valor

    @property
    def documento_favorecido(self):
        """
        Gets the documento_favorecido of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_documento_favorecido_value}}}

        :return: The documento_favorecido of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._documento_favorecido

    @documento_favorecido.setter
    def documento_favorecido(self, documento_favorecido):
        """
        Sets the documento_favorecido of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_documento_favorecido_value}}}

        :param documento_favorecido: The documento_favorecido of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._documento_favorecido = documento_favorecido

    @property
    def banco(self):
        """
        Gets the banco of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_banco_value}}}

        :return: The banco of this TransferenciaBancariaPersistValue.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_banco_value}}}

        :param banco: The banco of this TransferenciaBancariaPersistValue.
        :type: int
        """
        self._banco = banco

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_numero_agencia_value}}}

        :return: The numero_agencia of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_numero_agencia_value}}}

        :param numero_agencia: The numero_agencia of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._numero_agencia = numero_agencia

    @property
    def digito_agencia(self):
        """
        Gets the digito_agencia of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_digito_agencia_value}}}

        :return: The digito_agencia of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._digito_agencia

    @digito_agencia.setter
    def digito_agencia(self, digito_agencia):
        """
        Sets the digito_agencia of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_digito_agencia_value}}}

        :param digito_agencia: The digito_agencia of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._digito_agencia = digito_agencia

    @property
    def numero_conta(self):
        """
        Gets the numero_conta of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_numero_conta_value}}}

        :return: The numero_conta of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        """
        Sets the numero_conta of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_numero_conta_value}}}

        :param numero_conta: The numero_conta of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._numero_conta = numero_conta

    @property
    def digito_conta(self):
        """
        Gets the digito_conta of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_digito_conta_value}}}

        :return: The digito_conta of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._digito_conta

    @digito_conta.setter
    def digito_conta(self, digito_conta):
        """
        Sets the digito_conta of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_digito_conta_value}}}

        :param digito_conta: The digito_conta of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._digito_conta = digito_conta

    @property
    def flag_conta_poupanca(self):
        """
        Gets the flag_conta_poupanca of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_flag_conta_poupanca_value}}}

        :return: The flag_conta_poupanca of this TransferenciaBancariaPersistValue.
        :rtype: int
        """
        return self._flag_conta_poupanca

    @flag_conta_poupanca.setter
    def flag_conta_poupanca(self, flag_conta_poupanca):
        """
        Sets the flag_conta_poupanca of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_flag_conta_poupanca_value}}}

        :param flag_conta_poupanca: The flag_conta_poupanca of this TransferenciaBancariaPersistValue.
        :type: int
        """
        self._flag_conta_poupanca = flag_conta_poupanca

    @property
    def nome_favorecido(self):
        """
        Gets the nome_favorecido of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_nome_favorecido_value}}}

        :return: The nome_favorecido of this TransferenciaBancariaPersistValue.
        :rtype: str
        """
        return self._nome_favorecido

    @nome_favorecido.setter
    def nome_favorecido(self, nome_favorecido):
        """
        Sets the nome_favorecido of this TransferenciaBancariaPersistValue.
        {{{transferencia_bancaria_persist_nome_favorecido_value}}}

        :param nome_favorecido: The nome_favorecido of this TransferenciaBancariaPersistValue.
        :type: str
        """
        self._nome_favorecido = nome_favorecido

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

