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


class OportunidadePersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OportunidadePersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_tipo_oportunidade': 'int',
            'id_status_oportunidade': 'int',
            'numero_receita_federal': 'str',
            'data_inicio_vigencia': 'datetime',
            'data_fim_vigencia': 'datetime',
            'flag_ativo': 'bool',
            'detalhes': 'list[DetalheOportunidadePersist]'
        }

        self.attribute_map = {
            'id_tipo_oportunidade': 'idTipoOportunidade',
            'id_status_oportunidade': 'idStatusOportunidade',
            'numero_receita_federal': 'numeroReceitaFederal',
            'data_inicio_vigencia': 'dataInicioVigencia',
            'data_fim_vigencia': 'dataFimVigencia',
            'flag_ativo': 'flagAtivo',
            'detalhes': 'detalhes'
        }

        self._id_tipo_oportunidade = None
        self._id_status_oportunidade = None
        self._numero_receita_federal = None
        self._data_inicio_vigencia = None
        self._data_fim_vigencia = None
        self._flag_ativo = None
        self._detalhes = None

    @property
    def id_tipo_oportunidade(self):
        """
        Gets the id_tipo_oportunidade of this OportunidadePersist.
        C\u00C3\u00B3digo identificador do tipo oportunidade

        :return: The id_tipo_oportunidade of this OportunidadePersist.
        :rtype: int
        """
        return self._id_tipo_oportunidade

    @id_tipo_oportunidade.setter
    def id_tipo_oportunidade(self, id_tipo_oportunidade):
        """
        Sets the id_tipo_oportunidade of this OportunidadePersist.
        C\u00C3\u00B3digo identificador do tipo oportunidade

        :param id_tipo_oportunidade: The id_tipo_oportunidade of this OportunidadePersist.
        :type: int
        """
        self._id_tipo_oportunidade = id_tipo_oportunidade

    @property
    def id_status_oportunidade(self):
        """
        Gets the id_status_oportunidade of this OportunidadePersist.
        C\u00C3\u00B3digo identificador do status oportunidade

        :return: The id_status_oportunidade of this OportunidadePersist.
        :rtype: int
        """
        return self._id_status_oportunidade

    @id_status_oportunidade.setter
    def id_status_oportunidade(self, id_status_oportunidade):
        """
        Sets the id_status_oportunidade of this OportunidadePersist.
        C\u00C3\u00B3digo identificador do status oportunidade

        :param id_status_oportunidade: The id_status_oportunidade of this OportunidadePersist.
        :type: int
        """
        self._id_status_oportunidade = id_status_oportunidade

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this OportunidadePersist.
        N\u00C3\u00BAmero receita federal do cliente

        :return: The numero_receita_federal of this OportunidadePersist.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this OportunidadePersist.
        N\u00C3\u00BAmero receita federal do cliente

        :param numero_receita_federal: The numero_receita_federal of this OportunidadePersist.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def data_inicio_vigencia(self):
        """
        Gets the data_inicio_vigencia of this OportunidadePersist.
        Date de in\u00C3\u00ADcio da vig\u00C3\u00AAncia da oportunidade

        :return: The data_inicio_vigencia of this OportunidadePersist.
        :rtype: datetime
        """
        return self._data_inicio_vigencia

    @data_inicio_vigencia.setter
    def data_inicio_vigencia(self, data_inicio_vigencia):
        """
        Sets the data_inicio_vigencia of this OportunidadePersist.
        Date de in\u00C3\u00ADcio da vig\u00C3\u00AAncia da oportunidade

        :param data_inicio_vigencia: The data_inicio_vigencia of this OportunidadePersist.
        :type: datetime
        """
        self._data_inicio_vigencia = data_inicio_vigencia

    @property
    def data_fim_vigencia(self):
        """
        Gets the data_fim_vigencia of this OportunidadePersist.
        Data do fim da vig\u00C3\u00AAncia da oportunidade

        :return: The data_fim_vigencia of this OportunidadePersist.
        :rtype: datetime
        """
        return self._data_fim_vigencia

    @data_fim_vigencia.setter
    def data_fim_vigencia(self, data_fim_vigencia):
        """
        Sets the data_fim_vigencia of this OportunidadePersist.
        Data do fim da vig\u00C3\u00AAncia da oportunidade

        :param data_fim_vigencia: The data_fim_vigencia of this OportunidadePersist.
        :type: datetime
        """
        self._data_fim_vigencia = data_fim_vigencia

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this OportunidadePersist.
        Atributo que indica se a oportunidade est\u00C3\u00A1 ativa

        :return: The flag_ativo of this OportunidadePersist.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this OportunidadePersist.
        Atributo que indica se a oportunidade est\u00C3\u00A1 ativa

        :param flag_ativo: The flag_ativo of this OportunidadePersist.
        :type: bool
        """
        self._flag_ativo = flag_ativo

    @property
    def detalhes(self):
        """
        Gets the detalhes of this OportunidadePersist.
        Lista de detalhes

        :return: The detalhes of this OportunidadePersist.
        :rtype: list[DetalheOportunidadePersist]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this OportunidadePersist.
        Lista de detalhes

        :param detalhes: The detalhes of this OportunidadePersist.
        :type: list[DetalheOportunidadePersist]
        """
        self._detalhes = detalhes

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
