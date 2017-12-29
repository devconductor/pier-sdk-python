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


class ConfiguracaoRegistroCobrancaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConfiguracaoRegistroCobrancaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_emissor': 'int',
            'codigo_banco': 'int',
            'uri': 'str',
            'key_store_name': 'str',
            'key_store_password': 'str',
            'keystore_alias': 'str',
            'key_store_private_key_password': 'str',
            'type_keystore': 'str',
            'trust_store_name': 'str',
            'trust_store_password': 'str',
            'truststore_alias': 'str',
            'type_truststore': 'str',
            'uri_adicional': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_emissor': 'idEmissor',
            'codigo_banco': 'codigoBanco',
            'uri': 'uri',
            'key_store_name': 'keyStoreName',
            'key_store_password': 'keyStorePassword',
            'keystore_alias': 'keystoreAlias',
            'key_store_private_key_password': 'keyStorePrivateKeyPassword',
            'type_keystore': 'typeKeystore',
            'trust_store_name': 'trustStoreName',
            'trust_store_password': 'trustStorePassword',
            'truststore_alias': 'truststoreAlias',
            'type_truststore': 'typeTruststore',
            'uri_adicional': 'uriAdicional',
            'status': 'status'
        }

        self._id = None
        self._id_emissor = None
        self._codigo_banco = None
        self._uri = None
        self._key_store_name = None
        self._key_store_password = None
        self._keystore_alias = None
        self._key_store_private_key_password = None
        self._type_keystore = None
        self._trust_store_name = None
        self._trust_store_password = None
        self._truststore_alias = None
        self._type_truststore = None
        self._uri_adicional = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo identificador da configura\u00C3\u00A7\u00C3\u00A3o.

        :return: The id of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo identificador da configura\u00C3\u00A7\u00C3\u00A3o.

        :param id: The id of this ConfiguracaoRegistroCobrancaResponse.
        :type: int
        """
        self._id = id

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo do emissor.

        :return: The id_emissor of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo do emissor.

        :param id_emissor: The id_emissor of this ConfiguracaoRegistroCobrancaResponse.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def codigo_banco(self):
        """
        Gets the codigo_banco of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo do Banco.

        :return: The codigo_banco of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: int
        """
        return self._codigo_banco

    @codigo_banco.setter
    def codigo_banco(self, codigo_banco):
        """
        Sets the codigo_banco of this ConfiguracaoRegistroCobrancaResponse.
        C\u00C3\u00B3digo do Banco.

        :param codigo_banco: The codigo_banco of this ConfiguracaoRegistroCobrancaResponse.
        :type: int
        """
        self._codigo_banco = codigo_banco

    @property
    def uri(self):
        """
        Gets the uri of this ConfiguracaoRegistroCobrancaResponse.
        URL de acesso ao banco.

        :return: The uri of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ConfiguracaoRegistroCobrancaResponse.
        URL de acesso ao banco.

        :param uri: The uri of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._uri = uri

    @property
    def key_store_name(self):
        """
        Gets the key_store_name of this ConfiguracaoRegistroCobrancaResponse.
        Caminho do certificado digital do emissor.

        :return: The key_store_name of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._key_store_name

    @key_store_name.setter
    def key_store_name(self, key_store_name):
        """
        Sets the key_store_name of this ConfiguracaoRegistroCobrancaResponse.
        Caminho do certificado digital do emissor.

        :param key_store_name: The key_store_name of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._key_store_name = key_store_name

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha do certificado digital do emissor.

        :return: The key_store_password of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha do certificado digital do emissor.

        :param key_store_password: The key_store_password of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._key_store_password = key_store_password

    @property
    def keystore_alias(self):
        """
        Gets the keystore_alias of this ConfiguracaoRegistroCobrancaResponse.
        Alias do certificado digital do emissor.

        :return: The keystore_alias of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._keystore_alias

    @keystore_alias.setter
    def keystore_alias(self, keystore_alias):
        """
        Sets the keystore_alias of this ConfiguracaoRegistroCobrancaResponse.
        Alias do certificado digital do emissor.

        :param keystore_alias: The keystore_alias of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._keystore_alias = keystore_alias

    @property
    def key_store_private_key_password(self):
        """
        Gets the key_store_private_key_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha da chave privada do certificado digital do emissor.

        :return: The key_store_private_key_password of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._key_store_private_key_password

    @key_store_private_key_password.setter
    def key_store_private_key_password(self, key_store_private_key_password):
        """
        Sets the key_store_private_key_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha da chave privada do certificado digital do emissor.

        :param key_store_private_key_password: The key_store_private_key_password of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._key_store_private_key_password = key_store_private_key_password

    @property
    def type_keystore(self):
        """
        Gets the type_keystore of this ConfiguracaoRegistroCobrancaResponse.
        Tipo do certificado digital do emissor.

        :return: The type_keystore of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._type_keystore

    @type_keystore.setter
    def type_keystore(self, type_keystore):
        """
        Sets the type_keystore of this ConfiguracaoRegistroCobrancaResponse.
        Tipo do certificado digital do emissor.

        :param type_keystore: The type_keystore of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._type_keystore = type_keystore

    @property
    def trust_store_name(self):
        """
        Gets the trust_store_name of this ConfiguracaoRegistroCobrancaResponse.
        Caminho do certificado digital do banco.

        :return: The trust_store_name of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._trust_store_name

    @trust_store_name.setter
    def trust_store_name(self, trust_store_name):
        """
        Sets the trust_store_name of this ConfiguracaoRegistroCobrancaResponse.
        Caminho do certificado digital do banco.

        :param trust_store_name: The trust_store_name of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._trust_store_name = trust_store_name

    @property
    def trust_store_password(self):
        """
        Gets the trust_store_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha do certificado digital do banco.

        :return: The trust_store_password of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """
        Sets the trust_store_password of this ConfiguracaoRegistroCobrancaResponse.
        Senha do certificado digital do banco.

        :param trust_store_password: The trust_store_password of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._trust_store_password = trust_store_password

    @property
    def truststore_alias(self):
        """
        Gets the truststore_alias of this ConfiguracaoRegistroCobrancaResponse.
        Alias do certificado digital do banco.

        :return: The truststore_alias of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._truststore_alias

    @truststore_alias.setter
    def truststore_alias(self, truststore_alias):
        """
        Sets the truststore_alias of this ConfiguracaoRegistroCobrancaResponse.
        Alias do certificado digital do banco.

        :param truststore_alias: The truststore_alias of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._truststore_alias = truststore_alias

    @property
    def type_truststore(self):
        """
        Gets the type_truststore of this ConfiguracaoRegistroCobrancaResponse.
        Tipo do certificado digital do banco.

        :return: The type_truststore of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._type_truststore

    @type_truststore.setter
    def type_truststore(self, type_truststore):
        """
        Sets the type_truststore of this ConfiguracaoRegistroCobrancaResponse.
        Tipo do certificado digital do banco.

        :param type_truststore: The type_truststore of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._type_truststore = type_truststore

    @property
    def uri_adicional(self):
        """
        Gets the uri_adicional of this ConfiguracaoRegistroCobrancaResponse.
        URL adicional de acesso ao banco.

        :return: The uri_adicional of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._uri_adicional

    @uri_adicional.setter
    def uri_adicional(self, uri_adicional):
        """
        Sets the uri_adicional of this ConfiguracaoRegistroCobrancaResponse.
        URL adicional de acesso ao banco.

        :param uri_adicional: The uri_adicional of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        self._uri_adicional = uri_adicional

    @property
    def status(self):
        """
        Gets the status of this ConfiguracaoRegistroCobrancaResponse.
        Status indicador se a configura\u00C3\u00A7\u00C3\u00A3o est\u00C3\u00A1 ativa.

        :return: The status of this ConfiguracaoRegistroCobrancaResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConfiguracaoRegistroCobrancaResponse.
        Status indicador se a configura\u00C3\u00A7\u00C3\u00A3o est\u00C3\u00A1 ativa.

        :param status: The status of this ConfiguracaoRegistroCobrancaResponse.
        :type: str
        """
        allowed_values = ["INATIVO", "ATIVO"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
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

