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


class LinkHistoricoAssessoriaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LinkHistoricoAssessoriaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_hora_historico': 'datetime',
            'tipo_historico': 'str',
            'nome_assessoria': 'str'
        }

        self.attribute_map = {
            'data_hora_historico': 'dataHoraHistorico',
            'tipo_historico': 'tipoHistorico',
            'nome_assessoria': 'nomeAssessoria'
        }

        self._data_hora_historico = None
        self._tipo_historico = None
        self._nome_assessoria = None

    @property
    def data_hora_historico(self):
        """
        Gets the data_hora_historico of this LinkHistoricoAssessoriaResponse.
        Apresenta a data e hora do hist\u00C3\u00B3rico

        :return: The data_hora_historico of this LinkHistoricoAssessoriaResponse.
        :rtype: datetime
        """
        return self._data_hora_historico

    @data_hora_historico.setter
    def data_hora_historico(self, data_hora_historico):
        """
        Sets the data_hora_historico of this LinkHistoricoAssessoriaResponse.
        Apresenta a data e hora do hist\u00C3\u00B3rico

        :param data_hora_historico: The data_hora_historico of this LinkHistoricoAssessoriaResponse.
        :type: datetime
        """
        self._data_hora_historico = data_hora_historico

    @property
    def tipo_historico(self):
        """
        Gets the tipo_historico of this LinkHistoricoAssessoriaResponse.
        Apresenta o tipo do hist\u00C3\u00B3rico podendo ser ENTRADA ou SAIDA

        :return: The tipo_historico of this LinkHistoricoAssessoriaResponse.
        :rtype: str
        """
        return self._tipo_historico

    @tipo_historico.setter
    def tipo_historico(self, tipo_historico):
        """
        Sets the tipo_historico of this LinkHistoricoAssessoriaResponse.
        Apresenta o tipo do hist\u00C3\u00B3rico podendo ser ENTRADA ou SAIDA

        :param tipo_historico: The tipo_historico of this LinkHistoricoAssessoriaResponse.
        :type: str
        """
        self._tipo_historico = tipo_historico

    @property
    def nome_assessoria(self):
        """
        Gets the nome_assessoria of this LinkHistoricoAssessoriaResponse.
        Apresenta o nome da Assessoria de Cobran\u00C3\u00A7a relacionada ao hist\u00C3\u00B3rico

        :return: The nome_assessoria of this LinkHistoricoAssessoriaResponse.
        :rtype: str
        """
        return self._nome_assessoria

    @nome_assessoria.setter
    def nome_assessoria(self, nome_assessoria):
        """
        Sets the nome_assessoria of this LinkHistoricoAssessoriaResponse.
        Apresenta o nome da Assessoria de Cobran\u00C3\u00A7a relacionada ao hist\u00C3\u00B3rico

        :param nome_assessoria: The nome_assessoria of this LinkHistoricoAssessoriaResponse.
        :type: str
        """
        self._nome_assessoria = nome_assessoria

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

