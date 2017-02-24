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


class FaturaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FaturaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'descricao': 'str',
            'banco': 'int',
            'faixa_nosso_numero': 'int',
            'min_nosso_numero': 'float',
            'max_nosso_numero': 'float',
            'tam_nosso_numero': 'int',
            'ultimo_nosso_numero': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'descricao': 'descricao',
            'banco': 'banco',
            'faixa_nosso_numero': 'faixaNossoNumero',
            'min_nosso_numero': 'minNossoNumero',
            'max_nosso_numero': 'maxNossoNumero',
            'tam_nosso_numero': 'tamNossoNumero',
            'ultimo_nosso_numero': 'ultimoNossoNumero'
        }

        self._id = None
        self._descricao = None
        self._banco = None
        self._faixa_nosso_numero = None
        self._min_nosso_numero = None
        self._max_nosso_numero = None
        self._tam_nosso_numero = None
        self._ultimo_nosso_numero = None

    @property
    def id(self):
        """
        Gets the id of this FaturaResponse.
        C\u00C3\u00B3digo identificador do tipo de boleto.

        :return: The id of this FaturaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FaturaResponse.
        C\u00C3\u00B3digo identificador do tipo de boleto.

        :param id: The id of this FaturaResponse.
        :type: int
        """
        self._id = id

    @property
    def descricao(self):
        """
        Gets the descricao of this FaturaResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do tipo de boleto.

        :return: The descricao of this FaturaResponse.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this FaturaResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do tipo de boleto.

        :param descricao: The descricao of this FaturaResponse.
        :type: str
        """
        self._descricao = descricao

    @property
    def banco(self):
        """
        Gets the banco of this FaturaResponse.
        C\u00C3\u00B3digo identificador do banco.

        :return: The banco of this FaturaResponse.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this FaturaResponse.
        C\u00C3\u00B3digo identificador do banco.

        :param banco: The banco of this FaturaResponse.
        :type: int
        """
        self._banco = banco

    @property
    def faixa_nosso_numero(self):
        """
        Gets the faixa_nosso_numero of this FaturaResponse.
        Faixa permitida para cria\u00C3\u00A7\u00C3\u00A3o do nosso n\u00C3\u00BAmero.

        :return: The faixa_nosso_numero of this FaturaResponse.
        :rtype: int
        """
        return self._faixa_nosso_numero

    @faixa_nosso_numero.setter
    def faixa_nosso_numero(self, faixa_nosso_numero):
        """
        Sets the faixa_nosso_numero of this FaturaResponse.
        Faixa permitida para cria\u00C3\u00A7\u00C3\u00A3o do nosso n\u00C3\u00BAmero.

        :param faixa_nosso_numero: The faixa_nosso_numero of this FaturaResponse.
        :type: int
        """
        self._faixa_nosso_numero = faixa_nosso_numero

    @property
    def min_nosso_numero(self):
        """
        Gets the min_nosso_numero of this FaturaResponse.
        N\u00C3\u00BAmero minimo para o nosso n\u00C3\u00BAmero.

        :return: The min_nosso_numero of this FaturaResponse.
        :rtype: float
        """
        return self._min_nosso_numero

    @min_nosso_numero.setter
    def min_nosso_numero(self, min_nosso_numero):
        """
        Sets the min_nosso_numero of this FaturaResponse.
        N\u00C3\u00BAmero minimo para o nosso n\u00C3\u00BAmero.

        :param min_nosso_numero: The min_nosso_numero of this FaturaResponse.
        :type: float
        """
        self._min_nosso_numero = min_nosso_numero

    @property
    def max_nosso_numero(self):
        """
        Gets the max_nosso_numero of this FaturaResponse.
        N\u00C3\u00BAmero m\u00C3\u00A1ximo para o nosso n\u00C3\u00BAmero.

        :return: The max_nosso_numero of this FaturaResponse.
        :rtype: float
        """
        return self._max_nosso_numero

    @max_nosso_numero.setter
    def max_nosso_numero(self, max_nosso_numero):
        """
        Sets the max_nosso_numero of this FaturaResponse.
        N\u00C3\u00BAmero m\u00C3\u00A1ximo para o nosso n\u00C3\u00BAmero.

        :param max_nosso_numero: The max_nosso_numero of this FaturaResponse.
        :type: float
        """
        self._max_nosso_numero = max_nosso_numero

    @property
    def tam_nosso_numero(self):
        """
        Gets the tam_nosso_numero of this FaturaResponse.
        Tamanho do nosso n\u00C3\u00BAmero.

        :return: The tam_nosso_numero of this FaturaResponse.
        :rtype: int
        """
        return self._tam_nosso_numero

    @tam_nosso_numero.setter
    def tam_nosso_numero(self, tam_nosso_numero):
        """
        Sets the tam_nosso_numero of this FaturaResponse.
        Tamanho do nosso n\u00C3\u00BAmero.

        :param tam_nosso_numero: The tam_nosso_numero of this FaturaResponse.
        :type: int
        """
        self._tam_nosso_numero = tam_nosso_numero

    @property
    def ultimo_nosso_numero(self):
        """
        Gets the ultimo_nosso_numero of this FaturaResponse.
        \u00C3\u009Altimo nosso n\u00C3\u00BAmero utilizado.

        :return: The ultimo_nosso_numero of this FaturaResponse.
        :rtype: float
        """
        return self._ultimo_nosso_numero

    @ultimo_nosso_numero.setter
    def ultimo_nosso_numero(self, ultimo_nosso_numero):
        """
        Sets the ultimo_nosso_numero of this FaturaResponse.
        \u00C3\u009Altimo nosso n\u00C3\u00BAmero utilizado.

        :param ultimo_nosso_numero: The ultimo_nosso_numero of this FaturaResponse.
        :type: float
        """
        self._ultimo_nosso_numero = ultimo_nosso_numero

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

