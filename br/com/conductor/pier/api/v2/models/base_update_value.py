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


class BaseUpdateValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BaseUpdateValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'servidor': 'str',
            'usuario': 'str',
            'senha': 'str',
            'nome_base': 'str',
            'alterado_por': 'str',
            'domain': 'str',
            'senha_criptografada': 'bool',
            'nome_base_controle_acesso': 'str',
            'id_emissor': 'int',
            'servidor_controle_acesso': 'str',
            'nome_base_usuarios': 'str',
            'servidor_usuarios': 'str',
            'flag_cluster': 'bool'
        }

        self.attribute_map = {
            'servidor': 'servidor',
            'usuario': 'usuario',
            'senha': 'senha',
            'nome_base': 'nomeBase',
            'alterado_por': 'alteradoPor',
            'domain': 'domain',
            'senha_criptografada': 'senhaCriptografada',
            'nome_base_controle_acesso': 'nomeBaseControleAcesso',
            'id_emissor': 'idEmissor',
            'servidor_controle_acesso': 'servidorControleAcesso',
            'nome_base_usuarios': 'nomeBaseUsuarios',
            'servidor_usuarios': 'servidorUsuarios',
            'flag_cluster': 'flagCluster'
        }

        self._servidor = None
        self._usuario = None
        self._senha = None
        self._nome_base = None
        self._alterado_por = None
        self._domain = None
        self._senha_criptografada = None
        self._nome_base_controle_acesso = None
        self._id_emissor = None
        self._servidor_controle_acesso = None
        self._nome_base_usuarios = None
        self._servidor_usuarios = None
        self._flag_cluster = None

    @property
    def servidor(self):
        """
        Gets the servidor of this BaseUpdateValue.
        {{{base_update_servidor_value}}}

        :return: The servidor of this BaseUpdateValue.
        :rtype: str
        """
        return self._servidor

    @servidor.setter
    def servidor(self, servidor):
        """
        Sets the servidor of this BaseUpdateValue.
        {{{base_update_servidor_value}}}

        :param servidor: The servidor of this BaseUpdateValue.
        :type: str
        """
        self._servidor = servidor

    @property
    def usuario(self):
        """
        Gets the usuario of this BaseUpdateValue.
        {{{base_update_usuario_value}}}

        :return: The usuario of this BaseUpdateValue.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this BaseUpdateValue.
        {{{base_update_usuario_value}}}

        :param usuario: The usuario of this BaseUpdateValue.
        :type: str
        """
        self._usuario = usuario

    @property
    def senha(self):
        """
        Gets the senha of this BaseUpdateValue.
        {{{base_update_senha_value}}}

        :return: The senha of this BaseUpdateValue.
        :rtype: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """
        Sets the senha of this BaseUpdateValue.
        {{{base_update_senha_value}}}

        :param senha: The senha of this BaseUpdateValue.
        :type: str
        """
        self._senha = senha

    @property
    def nome_base(self):
        """
        Gets the nome_base of this BaseUpdateValue.
        {{{base_update_nome_base_value}}}

        :return: The nome_base of this BaseUpdateValue.
        :rtype: str
        """
        return self._nome_base

    @nome_base.setter
    def nome_base(self, nome_base):
        """
        Sets the nome_base of this BaseUpdateValue.
        {{{base_update_nome_base_value}}}

        :param nome_base: The nome_base of this BaseUpdateValue.
        :type: str
        """
        self._nome_base = nome_base

    @property
    def alterado_por(self):
        """
        Gets the alterado_por of this BaseUpdateValue.
        {{{base_update_alterado_por_value}}}

        :return: The alterado_por of this BaseUpdateValue.
        :rtype: str
        """
        return self._alterado_por

    @alterado_por.setter
    def alterado_por(self, alterado_por):
        """
        Sets the alterado_por of this BaseUpdateValue.
        {{{base_update_alterado_por_value}}}

        :param alterado_por: The alterado_por of this BaseUpdateValue.
        :type: str
        """
        self._alterado_por = alterado_por

    @property
    def domain(self):
        """
        Gets the domain of this BaseUpdateValue.
        {{{base_update_domain_value}}}

        :return: The domain of this BaseUpdateValue.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this BaseUpdateValue.
        {{{base_update_domain_value}}}

        :param domain: The domain of this BaseUpdateValue.
        :type: str
        """
        self._domain = domain

    @property
    def senha_criptografada(self):
        """
        Gets the senha_criptografada of this BaseUpdateValue.
        {{{base_update_senha_criptografada_value}}}

        :return: The senha_criptografada of this BaseUpdateValue.
        :rtype: bool
        """
        return self._senha_criptografada

    @senha_criptografada.setter
    def senha_criptografada(self, senha_criptografada):
        """
        Sets the senha_criptografada of this BaseUpdateValue.
        {{{base_update_senha_criptografada_value}}}

        :param senha_criptografada: The senha_criptografada of this BaseUpdateValue.
        :type: bool
        """
        self._senha_criptografada = senha_criptografada

    @property
    def nome_base_controle_acesso(self):
        """
        Gets the nome_base_controle_acesso of this BaseUpdateValue.
        {{{base_update_nome_base_controle_acesso_value}}}

        :return: The nome_base_controle_acesso of this BaseUpdateValue.
        :rtype: str
        """
        return self._nome_base_controle_acesso

    @nome_base_controle_acesso.setter
    def nome_base_controle_acesso(self, nome_base_controle_acesso):
        """
        Sets the nome_base_controle_acesso of this BaseUpdateValue.
        {{{base_update_nome_base_controle_acesso_value}}}

        :param nome_base_controle_acesso: The nome_base_controle_acesso of this BaseUpdateValue.
        :type: str
        """
        self._nome_base_controle_acesso = nome_base_controle_acesso

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this BaseUpdateValue.
        {{{base_update_id_emissor_value}}}

        :return: The id_emissor of this BaseUpdateValue.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this BaseUpdateValue.
        {{{base_update_id_emissor_value}}}

        :param id_emissor: The id_emissor of this BaseUpdateValue.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def servidor_controle_acesso(self):
        """
        Gets the servidor_controle_acesso of this BaseUpdateValue.
        {{{base_update_servidor_controle_acesso_value}}}

        :return: The servidor_controle_acesso of this BaseUpdateValue.
        :rtype: str
        """
        return self._servidor_controle_acesso

    @servidor_controle_acesso.setter
    def servidor_controle_acesso(self, servidor_controle_acesso):
        """
        Sets the servidor_controle_acesso of this BaseUpdateValue.
        {{{base_update_servidor_controle_acesso_value}}}

        :param servidor_controle_acesso: The servidor_controle_acesso of this BaseUpdateValue.
        :type: str
        """
        self._servidor_controle_acesso = servidor_controle_acesso

    @property
    def nome_base_usuarios(self):
        """
        Gets the nome_base_usuarios of this BaseUpdateValue.
        {{{base_update_nome_base_usuarios_value}}}

        :return: The nome_base_usuarios of this BaseUpdateValue.
        :rtype: str
        """
        return self._nome_base_usuarios

    @nome_base_usuarios.setter
    def nome_base_usuarios(self, nome_base_usuarios):
        """
        Sets the nome_base_usuarios of this BaseUpdateValue.
        {{{base_update_nome_base_usuarios_value}}}

        :param nome_base_usuarios: The nome_base_usuarios of this BaseUpdateValue.
        :type: str
        """
        self._nome_base_usuarios = nome_base_usuarios

    @property
    def servidor_usuarios(self):
        """
        Gets the servidor_usuarios of this BaseUpdateValue.
        {{{base_update_servidor_usuarios_value}}}

        :return: The servidor_usuarios of this BaseUpdateValue.
        :rtype: str
        """
        return self._servidor_usuarios

    @servidor_usuarios.setter
    def servidor_usuarios(self, servidor_usuarios):
        """
        Sets the servidor_usuarios of this BaseUpdateValue.
        {{{base_update_servidor_usuarios_value}}}

        :param servidor_usuarios: The servidor_usuarios of this BaseUpdateValue.
        :type: str
        """
        self._servidor_usuarios = servidor_usuarios

    @property
    def flag_cluster(self):
        """
        Gets the flag_cluster of this BaseUpdateValue.
        {{{base_update_flag_cluster_value}}}

        :return: The flag_cluster of this BaseUpdateValue.
        :rtype: bool
        """
        return self._flag_cluster

    @flag_cluster.setter
    def flag_cluster(self, flag_cluster):
        """
        Sets the flag_cluster of this BaseUpdateValue.
        {{{base_update_flag_cluster_value}}}

        :param flag_cluster: The flag_cluster of this BaseUpdateValue.
        :type: bool
        """
        self._flag_cluster = flag_cluster

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

