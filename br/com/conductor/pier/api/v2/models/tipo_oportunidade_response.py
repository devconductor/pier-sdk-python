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


class TipoOportunidadeResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoOportunidadeResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'descricao': 'str',
            'flag_ativo': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'descricao': 'descricao',
            'flag_ativo': 'flagAtivo'
        }

        self._id = None
        self._descricao = None
        self._flag_ativo = None

    @property
    def id(self):
        """
        Gets the id of this TipoOportunidadeResponse.
        C\u00C3\u00B3digo identificador do TipoOportunidade

        :return: The id of this TipoOportunidadeResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TipoOportunidadeResponse.
        C\u00C3\u00B3digo identificador do TipoOportunidade

        :param id: The id of this TipoOportunidadeResponse.
        :type: int
        """
        self._id = id

    @property
    def descricao(self):
        """
        Gets the descricao of this TipoOportunidadeResponse.
        Descricao do TipoOportunidade

        :return: The descricao of this TipoOportunidadeResponse.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this TipoOportunidadeResponse.
        Descricao do TipoOportunidade

        :param descricao: The descricao of this TipoOportunidadeResponse.
        :type: str
        """
        self._descricao = descricao

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this TipoOportunidadeResponse.
        Flag que representa se o tipo oportunidade est\u00C3\u00A1 ativo

        :return: The flag_ativo of this TipoOportunidadeResponse.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this TipoOportunidadeResponse.
        Flag que representa se o tipo oportunidade est\u00C3\u00A1 ativo

        :param flag_ativo: The flag_ativo of this TipoOportunidadeResponse.
        :type: bool
        """
        self._flag_ativo = flag_ativo

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

