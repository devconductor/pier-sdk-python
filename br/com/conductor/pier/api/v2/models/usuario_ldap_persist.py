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


class UsuarioLdapPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UsuarioLdapPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cpf': 'str',
            'email': 'str',
            'id_emissor': 'int',
            'login': 'str',
            'nome': 'str',
            'perfis': 'list[ReferenciaIdPersist]'
        }

        self.attribute_map = {
            'cpf': 'cpf',
            'email': 'email',
            'id_emissor': 'idEmissor',
            'login': 'login',
            'nome': 'nome',
            'perfis': 'perfis'
        }

        self._cpf = None
        self._email = None
        self._id_emissor = None
        self._login = None
        self._nome = None
        self._perfis = None

    @property
    def cpf(self):
        """
        Gets the cpf of this UsuarioLdapPersist.


        :return: The cpf of this UsuarioLdapPersist.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this UsuarioLdapPersist.


        :param cpf: The cpf of this UsuarioLdapPersist.
        :type: str
        """
        self._cpf = cpf

    @property
    def email(self):
        """
        Gets the email of this UsuarioLdapPersist.


        :return: The email of this UsuarioLdapPersist.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UsuarioLdapPersist.


        :param email: The email of this UsuarioLdapPersist.
        :type: str
        """
        self._email = email

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this UsuarioLdapPersist.


        :return: The id_emissor of this UsuarioLdapPersist.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this UsuarioLdapPersist.


        :param id_emissor: The id_emissor of this UsuarioLdapPersist.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def login(self):
        """
        Gets the login of this UsuarioLdapPersist.


        :return: The login of this UsuarioLdapPersist.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """
        Sets the login of this UsuarioLdapPersist.


        :param login: The login of this UsuarioLdapPersist.
        :type: str
        """
        self._login = login

    @property
    def nome(self):
        """
        Gets the nome of this UsuarioLdapPersist.


        :return: The nome of this UsuarioLdapPersist.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this UsuarioLdapPersist.


        :param nome: The nome of this UsuarioLdapPersist.
        :type: str
        """
        self._nome = nome

    @property
    def perfis(self):
        """
        Gets the perfis of this UsuarioLdapPersist.


        :return: The perfis of this UsuarioLdapPersist.
        :rtype: list[ReferenciaIdPersist]
        """
        return self._perfis

    @perfis.setter
    def perfis(self, perfis):
        """
        Sets the perfis of this UsuarioLdapPersist.


        :param perfis: The perfis of this UsuarioLdapPersist.
        :type: list[ReferenciaIdPersist]
        """
        self._perfis = perfis

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

