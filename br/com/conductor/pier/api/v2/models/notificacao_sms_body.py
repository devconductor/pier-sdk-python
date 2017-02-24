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


class NotificacaoSMSBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NotificacaoSMSBody - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nsu': 'int',
            'id_pessoa': 'int',
            'id_conta': 'int',
            'celular': 'str',
            'conteudo': 'str',
            'data_agendamento': 'datetime',
            'tipo_evento': 'str'
        }

        self.attribute_map = {
            'nsu': 'nsu',
            'id_pessoa': 'idPessoa',
            'id_conta': 'idConta',
            'celular': 'celular',
            'conteudo': 'conteudo',
            'data_agendamento': 'dataAgendamento',
            'tipo_evento': 'tipoEvento'
        }

        self._nsu = None
        self._id_pessoa = None
        self._id_conta = None
        self._celular = None
        self._conteudo = None
        self._data_agendamento = None
        self._tipo_evento = None

    @property
    def nsu(self):
        """
        Gets the nsu of this NotificacaoSMSBody.
        N\u00C3\u00BAmero sequencial \u00C3\u00BAnico

        :return: The nsu of this NotificacaoSMSBody.
        :rtype: int
        """
        return self._nsu

    @nsu.setter
    def nsu(self, nsu):
        """
        Sets the nsu of this NotificacaoSMSBody.
        N\u00C3\u00BAmero sequencial \u00C3\u00BAnico

        :param nsu: The nsu of this NotificacaoSMSBody.
        :type: int
        """
        self._nsu = nsu

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this NotificacaoSMSBody.
        C\u00C3\u00B3digo identificado da pessoa

        :return: The id_pessoa of this NotificacaoSMSBody.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this NotificacaoSMSBody.
        C\u00C3\u00B3digo identificado da pessoa

        :param id_pessoa: The id_pessoa of this NotificacaoSMSBody.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_conta(self):
        """
        Gets the id_conta of this NotificacaoSMSBody.
        C\u00C3\u00B3digo identificador da conta

        :return: The id_conta of this NotificacaoSMSBody.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this NotificacaoSMSBody.
        C\u00C3\u00B3digo identificador da conta

        :param id_conta: The id_conta of this NotificacaoSMSBody.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def celular(self):
        """
        Gets the celular of this NotificacaoSMSBody.
        Apresenta o celular a ser eviado o SMS no formato 5588999999999 ou 5588999999999.

        :return: The celular of this NotificacaoSMSBody.
        :rtype: str
        """
        return self._celular

    @celular.setter
    def celular(self, celular):
        """
        Sets the celular of this NotificacaoSMSBody.
        Apresenta o celular a ser eviado o SMS no formato 5588999999999 ou 5588999999999.

        :param celular: The celular of this NotificacaoSMSBody.
        :type: str
        """
        self._celular = celular

    @property
    def conteudo(self):
        """
        Gets the conteudo of this NotificacaoSMSBody.
        Apresenta o texto do SMS a ser enviado

        :return: The conteudo of this NotificacaoSMSBody.
        :rtype: str
        """
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        """
        Sets the conteudo of this NotificacaoSMSBody.
        Apresenta o texto do SMS a ser enviado

        :param conteudo: The conteudo of this NotificacaoSMSBody.
        :type: str
        """
        self._conteudo = conteudo

    @property
    def data_agendamento(self):
        """
        Gets the data_agendamento of this NotificacaoSMSBody.
        Apresenta a data e hora em que ser\u00C3\u00A1 enviado a notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The data_agendamento of this NotificacaoSMSBody.
        :rtype: datetime
        """
        return self._data_agendamento

    @data_agendamento.setter
    def data_agendamento(self, data_agendamento):
        """
        Sets the data_agendamento of this NotificacaoSMSBody.
        Apresenta a data e hora em que ser\u00C3\u00A1 enviado a notifica\u00C3\u00A7\u00C3\u00A3o

        :param data_agendamento: The data_agendamento of this NotificacaoSMSBody.
        :type: datetime
        """
        self._data_agendamento = data_agendamento

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this NotificacaoSMSBody.
        Apresenta o tipoEvento a qual pertence a notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The tipo_evento of this NotificacaoSMSBody.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this NotificacaoSMSBody.
        Apresenta o tipoEvento a qual pertence a notifica\u00C3\u00A7\u00C3\u00A3o

        :param tipo_evento: The tipo_evento of this NotificacaoSMSBody.
        :type: str
        """
        allowed_values = ["RISCO_FRAUDE", "OUTROS"]
        if tipo_evento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_evento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_evento = tipo_evento

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

