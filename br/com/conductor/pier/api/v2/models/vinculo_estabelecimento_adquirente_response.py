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


class VinculoEstabelecimentoAdquirenteResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VinculoEstabelecimentoAdquirenteResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_estabelecimento': 'int',
            'id_adquirente': 'int',
            'codigo_estabelecimento_adquirente': 'str',
            'data_hora_cadastro': 'str',
            'mensagem': 'str',
            'status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_estabelecimento': 'idEstabelecimento',
            'id_adquirente': 'idAdquirente',
            'codigo_estabelecimento_adquirente': 'codigoEstabelecimentoAdquirente',
            'data_hora_cadastro': 'dataHoraCadastro',
            'mensagem': 'mensagem',
            'status': 'status'
        }

        self._id = None
        self._id_estabelecimento = None
        self._id_adquirente = None
        self._codigo_estabelecimento_adquirente = None
        self._data_hora_cadastro = None
        self._mensagem = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_value}}}

        :return: The id of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_value}}}

        :param id: The id of this VinculoEstabelecimentoAdquirenteResponse.
        :type: int
        """
        self._id = id

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_estabelecimento_value}}}

        :return: The id_estabelecimento of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_estabelecimento_value}}}

        :param id_estabelecimento: The id_estabelecimento of this VinculoEstabelecimentoAdquirenteResponse.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def id_adquirente(self):
        """
        Gets the id_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_adquirente_value}}}

        :return: The id_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: int
        """
        return self._id_adquirente

    @id_adquirente.setter
    def id_adquirente(self, id_adquirente):
        """
        Sets the id_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_id_adquirente_value}}}

        :param id_adquirente: The id_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        :type: int
        """
        self._id_adquirente = id_adquirente

    @property
    def codigo_estabelecimento_adquirente(self):
        """
        Gets the codigo_estabelecimento_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_codigo_estabelecimento_adquirente_value}}}

        :return: The codigo_estabelecimento_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: str
        """
        return self._codigo_estabelecimento_adquirente

    @codigo_estabelecimento_adquirente.setter
    def codigo_estabelecimento_adquirente(self, codigo_estabelecimento_adquirente):
        """
        Sets the codigo_estabelecimento_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_codigo_estabelecimento_adquirente_value}}}

        :param codigo_estabelecimento_adquirente: The codigo_estabelecimento_adquirente of this VinculoEstabelecimentoAdquirenteResponse.
        :type: str
        """
        self._codigo_estabelecimento_adquirente = codigo_estabelecimento_adquirente

    @property
    def data_hora_cadastro(self):
        """
        Gets the data_hora_cadastro of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_data_hora_cadastro_value}}}

        :return: The data_hora_cadastro of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: str
        """
        return self._data_hora_cadastro

    @data_hora_cadastro.setter
    def data_hora_cadastro(self, data_hora_cadastro):
        """
        Sets the data_hora_cadastro of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_data_hora_cadastro_value}}}

        :param data_hora_cadastro: The data_hora_cadastro of this VinculoEstabelecimentoAdquirenteResponse.
        :type: str
        """
        self._data_hora_cadastro = data_hora_cadastro

    @property
    def mensagem(self):
        """
        Gets the mensagem of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_mensagem_value}}}

        :return: The mensagem of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: str
        """
        return self._mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        """
        Sets the mensagem of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_mensagem_value}}}

        :param mensagem: The mensagem of this VinculoEstabelecimentoAdquirenteResponse.
        :type: str
        """
        self._mensagem = mensagem

    @property
    def status(self):
        """
        Gets the status of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_status_value}}}

        :return: The status of this VinculoEstabelecimentoAdquirenteResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VinculoEstabelecimentoAdquirenteResponse.
        {{{vinculo_estabelecimento_adquirente_response_status_value}}}

        :param status: The status of this VinculoEstabelecimentoAdquirenteResponse.
        :type: int
        """
        self._status = status

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

