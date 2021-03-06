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


class ConsultaCadastroEstabelecimentoDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConsultaCadastroEstabelecimentoDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_hora_consulta': 'str',
            'status': 'str',
            'tipo_entidade': 'str'
        }

        self.attribute_map = {
            'data_hora_consulta': 'dataHoraConsulta',
            'status': 'status',
            'tipo_entidade': 'tipoEntidade'
        }

        self._data_hora_consulta = None
        self._status = None
        self._tipo_entidade = None

    @property
    def data_hora_consulta(self):
        """
        Gets the data_hora_consulta of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_data_hora_consulta_value}}}

        :return: The data_hora_consulta of this ConsultaCadastroEstabelecimentoDTO.
        :rtype: str
        """
        return self._data_hora_consulta

    @data_hora_consulta.setter
    def data_hora_consulta(self, data_hora_consulta):
        """
        Sets the data_hora_consulta of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_data_hora_consulta_value}}}

        :param data_hora_consulta: The data_hora_consulta of this ConsultaCadastroEstabelecimentoDTO.
        :type: str
        """
        self._data_hora_consulta = data_hora_consulta

    @property
    def status(self):
        """
        Gets the status of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_status_value}}}

        :return: The status of this ConsultaCadastroEstabelecimentoDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_status_value}}}

        :param status: The status of this ConsultaCadastroEstabelecimentoDTO.
        :type: str
        """
        allowed_values = ["OK", "NOK"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def tipo_entidade(self):
        """
        Gets the tipo_entidade of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_tipo_entidade_value}}}

        :return: The tipo_entidade of this ConsultaCadastroEstabelecimentoDTO.
        :rtype: str
        """
        return self._tipo_entidade

    @tipo_entidade.setter
    def tipo_entidade(self, tipo_entidade):
        """
        Sets the tipo_entidade of this ConsultaCadastroEstabelecimentoDTO.
        {{{consulta_cadastro_estabelecimento_d_t_o_tipo_entidade_value}}}

        :param tipo_entidade: The tipo_entidade of this ConsultaCadastroEstabelecimentoDTO.
        :type: str
        """
        allowed_values = ["ATIVO", "BLOQUEADO"]
        if tipo_entidade not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_entidade`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_entidade = tipo_entidade

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

