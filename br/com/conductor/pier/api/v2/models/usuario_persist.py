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


class UsuarioPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UsuarioPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nome': 'str',
            'login': 'str',
            'cpf': 'str',
            'email': 'str',
            'senha': 'str'
        }

        self.attribute_map = {
            'nome': 'nome',
            'login': 'login',
            'cpf': 'cpf',
            'email': 'email',
            'senha': 'senha'
        }

        self._nome = None
        self._login = None
        self._cpf = None
        self._email = None
        self._senha = None

    @property
    def nome(self):
        """
        Gets the nome of this UsuarioPersist.
        Apresenta o nome do usu\u00C3\u00A1rio.

        :return: The nome of this UsuarioPersist.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this UsuarioPersist.
        Apresenta o nome do usu\u00C3\u00A1rio.

        :param nome: The nome of this UsuarioPersist.
        :type: str
        """
        self._nome = nome

    @property
    def login(self):
        """
        Gets the login of this UsuarioPersist.
        Apresenta o login do usu\u00C3\u00A1rio.

        :return: The login of this UsuarioPersist.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """
        Sets the login of this UsuarioPersist.
        Apresenta o login do usu\u00C3\u00A1rio.

        :param login: The login of this UsuarioPersist.
        :type: str
        """
        self._login = login

    @property
    def cpf(self):
        """
        Gets the cpf of this UsuarioPersist.
        N\u00C3\u00BAmero do CPF.

        :return: The cpf of this UsuarioPersist.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this UsuarioPersist.
        N\u00C3\u00BAmero do CPF.

        :param cpf: The cpf of this UsuarioPersist.
        :type: str
        """
        self._cpf = cpf

    @property
    def email(self):
        """
        Gets the email of this UsuarioPersist.
        Apresenta o email do usu\u00C3\u00A1rio.

        :return: The email of this UsuarioPersist.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UsuarioPersist.
        Apresenta o email do usu\u00C3\u00A1rio.

        :param email: The email of this UsuarioPersist.
        :type: str
        """
        self._email = email

    @property
    def senha(self):
        """
        Gets the senha of this UsuarioPersist.
        Apresenta a senha do usu\u00C3\u00A1rio.

        :return: The senha of this UsuarioPersist.
        :rtype: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """
        Sets the senha of this UsuarioPersist.
        Apresenta a senha do usu\u00C3\u00A1rio.

        :param senha: The senha of this UsuarioPersist.
        :type: str
        """
        self._senha = senha

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

