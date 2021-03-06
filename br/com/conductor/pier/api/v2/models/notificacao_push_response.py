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


class NotificacaoPushResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NotificacaoPushResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_envio': 'str',
            'id_emissor': 'int',
            'tipo_evento': 'str',
            'status': 'str',
            'id_pessoa': 'int',
            'id_conta': 'int',
            'token_dispositivo': 'str',
            'titulo': 'str',
            'conteudo': 'str',
            'plataforma': 'str',
            'protocolo': 'str'
        }

        self.attribute_map = {
            'data_envio': 'dataEnvio',
            'id_emissor': 'idEmissor',
            'tipo_evento': 'tipoEvento',
            'status': 'status',
            'id_pessoa': 'idPessoa',
            'id_conta': 'idConta',
            'token_dispositivo': 'tokenDispositivo',
            'titulo': 'titulo',
            'conteudo': 'conteudo',
            'plataforma': 'plataforma',
            'protocolo': 'protocolo'
        }

        self._data_envio = None
        self._id_emissor = None
        self._tipo_evento = None
        self._status = None
        self._id_pessoa = None
        self._id_conta = None
        self._token_dispositivo = None
        self._titulo = None
        self._conteudo = None
        self._plataforma = None
        self._protocolo = None

    @property
    def data_envio(self):
        """
        Gets the data_envio of this NotificacaoPushResponse.
        {{{notificacao_push_response_data_envio_value}}}

        :return: The data_envio of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._data_envio

    @data_envio.setter
    def data_envio(self, data_envio):
        """
        Sets the data_envio of this NotificacaoPushResponse.
        {{{notificacao_push_response_data_envio_value}}}

        :param data_envio: The data_envio of this NotificacaoPushResponse.
        :type: str
        """
        self._data_envio = data_envio

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_emissor_value}}}

        :return: The id_emissor of this NotificacaoPushResponse.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_emissor_value}}}

        :param id_emissor: The id_emissor of this NotificacaoPushResponse.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this NotificacaoPushResponse.
        {{{notificacao_push_response_tipo_evento_value}}}

        :return: The tipo_evento of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this NotificacaoPushResponse.
        {{{notificacao_push_response_tipo_evento_value}}}

        :param tipo_evento: The tipo_evento of this NotificacaoPushResponse.
        :type: str
        """
        allowed_values = ["RISCO_FRAUDE", "CODIGO_SEGURANCA", "OUTROS", "OTP_3D_SECURE"]
        if tipo_evento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_evento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_evento = tipo_evento

    @property
    def status(self):
        """
        Gets the status of this NotificacaoPushResponse.
        {{{notificacao_push_response_status_value}}}

        :return: The status of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NotificacaoPushResponse.
        {{{notificacao_push_response_status_value}}}

        :param status: The status of this NotificacaoPushResponse.
        :type: str
        """
        allowed_values = ["PENDENTE", "ENCAMINHADO", "ENVIADO", "RESPONDIDO", "ERRO", "ERRO_RESPOSTA", "SUCESSO_RESPOSTA"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_pessoa_value}}}

        :return: The id_pessoa of this NotificacaoPushResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_pessoa_value}}}

        :param id_pessoa: The id_pessoa of this NotificacaoPushResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_conta(self):
        """
        Gets the id_conta of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_conta_value}}}

        :return: The id_conta of this NotificacaoPushResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this NotificacaoPushResponse.
        {{{notificacao_push_response_id_conta_value}}}

        :param id_conta: The id_conta of this NotificacaoPushResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def token_dispositivo(self):
        """
        Gets the token_dispositivo of this NotificacaoPushResponse.
        {{{notificacao_push_response_token_dispositivo_value}}}

        :return: The token_dispositivo of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._token_dispositivo

    @token_dispositivo.setter
    def token_dispositivo(self, token_dispositivo):
        """
        Sets the token_dispositivo of this NotificacaoPushResponse.
        {{{notificacao_push_response_token_dispositivo_value}}}

        :param token_dispositivo: The token_dispositivo of this NotificacaoPushResponse.
        :type: str
        """
        self._token_dispositivo = token_dispositivo

    @property
    def titulo(self):
        """
        Gets the titulo of this NotificacaoPushResponse.
        {{{notificacao_push_response_titulo_value}}}

        :return: The titulo of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        """
        Sets the titulo of this NotificacaoPushResponse.
        {{{notificacao_push_response_titulo_value}}}

        :param titulo: The titulo of this NotificacaoPushResponse.
        :type: str
        """
        self._titulo = titulo

    @property
    def conteudo(self):
        """
        Gets the conteudo of this NotificacaoPushResponse.
        {{{notificacao_push_response_conteudo_value}}}

        :return: The conteudo of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        """
        Sets the conteudo of this NotificacaoPushResponse.
        {{{notificacao_push_response_conteudo_value}}}

        :param conteudo: The conteudo of this NotificacaoPushResponse.
        :type: str
        """
        self._conteudo = conteudo

    @property
    def plataforma(self):
        """
        Gets the plataforma of this NotificacaoPushResponse.
        {{{notificacao_push_response_plataforma_value}}}

        :return: The plataforma of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._plataforma

    @plataforma.setter
    def plataforma(self, plataforma):
        """
        Sets the plataforma of this NotificacaoPushResponse.
        {{{notificacao_push_response_plataforma_value}}}

        :param plataforma: The plataforma of this NotificacaoPushResponse.
        :type: str
        """
        allowed_values = ["APNS", "FCM", "GCM"]
        if plataforma not in allowed_values:
            raise ValueError(
                "Invalid value for `plataforma`, must be one of {0}"
                .format(allowed_values)
            )
        self._plataforma = plataforma

    @property
    def protocolo(self):
        """
        Gets the protocolo of this NotificacaoPushResponse.
        {{{notificacao_push_response_protocolo_value}}}

        :return: The protocolo of this NotificacaoPushResponse.
        :rtype: str
        """
        return self._protocolo

    @protocolo.setter
    def protocolo(self, protocolo):
        """
        Sets the protocolo of this NotificacaoPushResponse.
        {{{notificacao_push_response_protocolo_value}}}

        :param protocolo: The protocolo of this NotificacaoPushResponse.
        :type: str
        """
        self._protocolo = protocolo

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

