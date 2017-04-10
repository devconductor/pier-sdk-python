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


class OportunidadeAUDResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OportunidadeAUDResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_tipo_oportunidade': 'int',
            'id_status_oportunidade': 'int',
            'data_cadastro': 'datetime',
            'data_atualizacao': 'datetime',
            'numero_receita_federal': 'str',
            'data_inicio_vigencia': 'datetime',
            'data_fim_vigencia': 'datetime',
            'flag_ativo': 'bool',
            'detalhes': 'list[CdtDetalheOportunidadeAUD]',
            'rev_date': 'datetime',
            'rev_type': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_tipo_oportunidade': 'idTipoOportunidade',
            'id_status_oportunidade': 'idStatusOportunidade',
            'data_cadastro': 'dataCadastro',
            'data_atualizacao': 'dataAtualizacao',
            'numero_receita_federal': 'numeroReceitaFederal',
            'data_inicio_vigencia': 'dataInicioVigencia',
            'data_fim_vigencia': 'dataFimVigencia',
            'flag_ativo': 'flagAtivo',
            'detalhes': 'detalhes',
            'rev_date': 'revDate',
            'rev_type': 'revType'
        }

        self._id = None
        self._id_tipo_oportunidade = None
        self._id_status_oportunidade = None
        self._data_cadastro = None
        self._data_atualizacao = None
        self._numero_receita_federal = None
        self._data_inicio_vigencia = None
        self._data_fim_vigencia = None
        self._flag_ativo = None
        self._detalhes = None
        self._rev_date = None
        self._rev_type = None

    @property
    def id(self):
        """
        Gets the id of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador da oportunidade

        :return: The id of this OportunidadeAUDResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador da oportunidade

        :param id: The id of this OportunidadeAUDResponse.
        :type: int
        """
        self._id = id

    @property
    def id_tipo_oportunidade(self):
        """
        Gets the id_tipo_oportunidade of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador do tipo oportunidade

        :return: The id_tipo_oportunidade of this OportunidadeAUDResponse.
        :rtype: int
        """
        return self._id_tipo_oportunidade

    @id_tipo_oportunidade.setter
    def id_tipo_oportunidade(self, id_tipo_oportunidade):
        """
        Sets the id_tipo_oportunidade of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador do tipo oportunidade

        :param id_tipo_oportunidade: The id_tipo_oportunidade of this OportunidadeAUDResponse.
        :type: int
        """
        self._id_tipo_oportunidade = id_tipo_oportunidade

    @property
    def id_status_oportunidade(self):
        """
        Gets the id_status_oportunidade of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador do status oportunidade

        :return: The id_status_oportunidade of this OportunidadeAUDResponse.
        :rtype: int
        """
        return self._id_status_oportunidade

    @id_status_oportunidade.setter
    def id_status_oportunidade(self, id_status_oportunidade):
        """
        Sets the id_status_oportunidade of this OportunidadeAUDResponse.
        C\u00C3\u00B3digo identificador do status oportunidade

        :param id_status_oportunidade: The id_status_oportunidade of this OportunidadeAUDResponse.
        :type: int
        """
        self._id_status_oportunidade = id_status_oportunidade

    @property
    def data_cadastro(self):
        """
        Gets the data_cadastro of this OportunidadeAUDResponse.
        Data cadastro da oportunidade.

        :return: The data_cadastro of this OportunidadeAUDResponse.
        :rtype: datetime
        """
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        """
        Sets the data_cadastro of this OportunidadeAUDResponse.
        Data cadastro da oportunidade.

        :param data_cadastro: The data_cadastro of this OportunidadeAUDResponse.
        :type: datetime
        """
        self._data_cadastro = data_cadastro

    @property
    def data_atualizacao(self):
        """
        Gets the data_atualizacao of this OportunidadeAUDResponse.
        Data atualiza\u00C3\u00A7\u00C3\u00A3o da oportunidade.

        :return: The data_atualizacao of this OportunidadeAUDResponse.
        :rtype: datetime
        """
        return self._data_atualizacao

    @data_atualizacao.setter
    def data_atualizacao(self, data_atualizacao):
        """
        Sets the data_atualizacao of this OportunidadeAUDResponse.
        Data atualiza\u00C3\u00A7\u00C3\u00A3o da oportunidade.

        :param data_atualizacao: The data_atualizacao of this OportunidadeAUDResponse.
        :type: datetime
        """
        self._data_atualizacao = data_atualizacao

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this OportunidadeAUDResponse.
        N\u00C3\u00BAmero receita federal do cliente ao qual ser\u00C3\u00A1 ofertada a oportunidade

        :return: The numero_receita_federal of this OportunidadeAUDResponse.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this OportunidadeAUDResponse.
        N\u00C3\u00BAmero receita federal do cliente ao qual ser\u00C3\u00A1 ofertada a oportunidade

        :param numero_receita_federal: The numero_receita_federal of this OportunidadeAUDResponse.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def data_inicio_vigencia(self):
        """
        Gets the data_inicio_vigencia of this OportunidadeAUDResponse.
        In\u00C3\u00ADcio da vig\u00C3\u00AAncia da oportunidade

        :return: The data_inicio_vigencia of this OportunidadeAUDResponse.
        :rtype: datetime
        """
        return self._data_inicio_vigencia

    @data_inicio_vigencia.setter
    def data_inicio_vigencia(self, data_inicio_vigencia):
        """
        Sets the data_inicio_vigencia of this OportunidadeAUDResponse.
        In\u00C3\u00ADcio da vig\u00C3\u00AAncia da oportunidade

        :param data_inicio_vigencia: The data_inicio_vigencia of this OportunidadeAUDResponse.
        :type: datetime
        """
        self._data_inicio_vigencia = data_inicio_vigencia

    @property
    def data_fim_vigencia(self):
        """
        Gets the data_fim_vigencia of this OportunidadeAUDResponse.
        fim da vig\u00C3\u00AAncia da oportunidade

        :return: The data_fim_vigencia of this OportunidadeAUDResponse.
        :rtype: datetime
        """
        return self._data_fim_vigencia

    @data_fim_vigencia.setter
    def data_fim_vigencia(self, data_fim_vigencia):
        """
        Sets the data_fim_vigencia of this OportunidadeAUDResponse.
        fim da vig\u00C3\u00AAncia da oportunidade

        :param data_fim_vigencia: The data_fim_vigencia of this OportunidadeAUDResponse.
        :type: datetime
        """
        self._data_fim_vigencia = data_fim_vigencia

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this OportunidadeAUDResponse.
        Flag de verifica\u00C3\u00A7\u00C3\u00A3o se a oportunidade est\u00C3\u00A1 ativa

        :return: The flag_ativo of this OportunidadeAUDResponse.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this OportunidadeAUDResponse.
        Flag de verifica\u00C3\u00A7\u00C3\u00A3o se a oportunidade est\u00C3\u00A1 ativa

        :param flag_ativo: The flag_ativo of this OportunidadeAUDResponse.
        :type: bool
        """
        self._flag_ativo = flag_ativo

    @property
    def detalhes(self):
        """
        Gets the detalhes of this OportunidadeAUDResponse.
        Lista de detalhes da oportunidade

        :return: The detalhes of this OportunidadeAUDResponse.
        :rtype: list[CdtDetalheOportunidadeAUD]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this OportunidadeAUDResponse.
        Lista de detalhes da oportunidade

        :param detalhes: The detalhes of this OportunidadeAUDResponse.
        :type: list[CdtDetalheOportunidadeAUD]
        """
        self._detalhes = detalhes

    @property
    def rev_date(self):
        """
        Gets the rev_date of this OportunidadeAUDResponse.
        Data da auditoria

        :return: The rev_date of this OportunidadeAUDResponse.
        :rtype: datetime
        """
        return self._rev_date

    @rev_date.setter
    def rev_date(self, rev_date):
        """
        Sets the rev_date of this OportunidadeAUDResponse.
        Data da auditoria

        :param rev_date: The rev_date of this OportunidadeAUDResponse.
        :type: datetime
        """
        self._rev_date = rev_date

    @property
    def rev_type(self):
        """
        Gets the rev_type of this OportunidadeAUDResponse.
        Tipo da auditoria

        :return: The rev_type of this OportunidadeAUDResponse.
        :rtype: int
        """
        return self._rev_type

    @rev_type.setter
    def rev_type(self, rev_type):
        """
        Sets the rev_type of this OportunidadeAUDResponse.
        Tipo da auditoria

        :param rev_type: The rev_type of this OportunidadeAUDResponse.
        :type: int
        """
        self._rev_type = rev_type

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

