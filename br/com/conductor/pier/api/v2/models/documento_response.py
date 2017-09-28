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


class DocumentoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_tipo_documento': 'int',
            'id_template_documento': 'int',
            'nome': 'str',
            'documento': 'str',
            'extensao': 'str',
            'documento_detalhes': 'list[DocumentoDetalheResponse]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_tipo_documento': 'idTipoDocumento',
            'id_template_documento': 'idTemplateDocumento',
            'nome': 'nome',
            'documento': 'documento',
            'extensao': 'extensao',
            'documento_detalhes': 'documentoDetalhes'
        }

        self._id = None
        self._id_tipo_documento = None
        self._id_template_documento = None
        self._nome = None
        self._documento = None
        self._extensao = None
        self._documento_detalhes = None

    @property
    def id(self):
        """
        Gets the id of this DocumentoResponse.
        ID do Documento.

        :return: The id of this DocumentoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DocumentoResponse.
        ID do Documento.

        :param id: The id of this DocumentoResponse.
        :type: int
        """
        self._id = id

    @property
    def id_tipo_documento(self):
        """
        Gets the id_tipo_documento of this DocumentoResponse.
        ID do Tipo de Documento associado.

        :return: The id_tipo_documento of this DocumentoResponse.
        :rtype: int
        """
        return self._id_tipo_documento

    @id_tipo_documento.setter
    def id_tipo_documento(self, id_tipo_documento):
        """
        Sets the id_tipo_documento of this DocumentoResponse.
        ID do Tipo de Documento associado.

        :param id_tipo_documento: The id_tipo_documento of this DocumentoResponse.
        :type: int
        """
        self._id_tipo_documento = id_tipo_documento

    @property
    def id_template_documento(self):
        """
        Gets the id_template_documento of this DocumentoResponse.
        ID do Template de Documento associado.

        :return: The id_template_documento of this DocumentoResponse.
        :rtype: int
        """
        return self._id_template_documento

    @id_template_documento.setter
    def id_template_documento(self, id_template_documento):
        """
        Sets the id_template_documento of this DocumentoResponse.
        ID do Template de Documento associado.

        :param id_template_documento: The id_template_documento of this DocumentoResponse.
        :type: int
        """
        self._id_template_documento = id_template_documento

    @property
    def nome(self):
        """
        Gets the nome of this DocumentoResponse.
        Nome do Documento.

        :return: The nome of this DocumentoResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this DocumentoResponse.
        Nome do Documento.

        :param nome: The nome of this DocumentoResponse.
        :type: str
        """
        self._nome = nome

    @property
    def documento(self):
        """
        Gets the documento of this DocumentoResponse.
        Nome do Documento.

        :return: The documento of this DocumentoResponse.
        :rtype: str
        """
        return self._documento

    @documento.setter
    def documento(self, documento):
        """
        Sets the documento of this DocumentoResponse.
        Nome do Documento.

        :param documento: The documento of this DocumentoResponse.
        :type: str
        """
        self._documento = documento

    @property
    def extensao(self):
        """
        Gets the extensao of this DocumentoResponse.
        Extens\u00C3\u00A3o do Documento.

        :return: The extensao of this DocumentoResponse.
        :rtype: str
        """
        return self._extensao

    @extensao.setter
    def extensao(self, extensao):
        """
        Sets the extensao of this DocumentoResponse.
        Extens\u00C3\u00A3o do Documento.

        :param extensao: The extensao of this DocumentoResponse.
        :type: str
        """
        self._extensao = extensao

    @property
    def documento_detalhes(self):
        """
        Gets the documento_detalhes of this DocumentoResponse.
        Detalhamento do documento.

        :return: The documento_detalhes of this DocumentoResponse.
        :rtype: list[DocumentoDetalheResponse]
        """
        return self._documento_detalhes

    @documento_detalhes.setter
    def documento_detalhes(self, documento_detalhes):
        """
        Sets the documento_detalhes of this DocumentoResponse.
        Detalhamento do documento.

        :param documento_detalhes: The documento_detalhes of this DocumentoResponse.
        :type: list[DocumentoDetalheResponse]
        """
        self._documento_detalhes = documento_detalhes

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

