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


class LimiteDisponibilidade(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LimiteDisponibilidade - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'limite_compra': 'float',
            'limite_consignado': 'float',
            'limite_externo': 'float',
            'limite_extra': 'float',
            'limite_global': 'float',
            'limite_internacional_compra': 'float',
            'limite_internacional_parcelado': 'float',
            'limite_internacional_parcelas': 'float',
            'limite_internacional_saque_global': 'float',
            'limite_internacional_saque_periodo': 'float',
            'limite_mensal': 'float',
            'limite_parcelado': 'float',
            'limite_parcelas': 'float',
            'limite_saque_global': 'float',
            'limite_saque_periodo': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'limite_compra': 'limiteCompra',
            'limite_consignado': 'limiteConsignado',
            'limite_externo': 'limiteExterno',
            'limite_extra': 'limiteExtra',
            'limite_global': 'limiteGlobal',
            'limite_internacional_compra': 'limiteInternacionalCompra',
            'limite_internacional_parcelado': 'limiteInternacionalParcelado',
            'limite_internacional_parcelas': 'limiteInternacionalParcelas',
            'limite_internacional_saque_global': 'limiteInternacionalSaqueGlobal',
            'limite_internacional_saque_periodo': 'limiteInternacionalSaquePeriodo',
            'limite_mensal': 'limiteMensal',
            'limite_parcelado': 'limiteParcelado',
            'limite_parcelas': 'limiteParcelas',
            'limite_saque_global': 'limiteSaqueGlobal',
            'limite_saque_periodo': 'limiteSaquePeriodo'
        }

        self._id = None
        self._limite_compra = None
        self._limite_consignado = None
        self._limite_externo = None
        self._limite_extra = None
        self._limite_global = None
        self._limite_internacional_compra = None
        self._limite_internacional_parcelado = None
        self._limite_internacional_parcelas = None
        self._limite_internacional_saque_global = None
        self._limite_internacional_saque_periodo = None
        self._limite_mensal = None
        self._limite_parcelado = None
        self._limite_parcelas = None
        self._limite_saque_global = None
        self._limite_saque_periodo = None

    @property
    def id(self):
        """
        Gets the id of this LimiteDisponibilidade.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Limite Disponibilidade (id).

        :return: The id of this LimiteDisponibilidade.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LimiteDisponibilidade.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Limite Disponibilidade (id).

        :param id: The id of this LimiteDisponibilidade.
        :type: int
        """
        self._id = id

    @property
    def limite_compra(self):
        """
        Gets the limite_compra of this LimiteDisponibilidade.


        :return: The limite_compra of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_compra

    @limite_compra.setter
    def limite_compra(self, limite_compra):
        """
        Sets the limite_compra of this LimiteDisponibilidade.


        :param limite_compra: The limite_compra of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_compra = limite_compra

    @property
    def limite_consignado(self):
        """
        Gets the limite_consignado of this LimiteDisponibilidade.


        :return: The limite_consignado of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_consignado

    @limite_consignado.setter
    def limite_consignado(self, limite_consignado):
        """
        Sets the limite_consignado of this LimiteDisponibilidade.


        :param limite_consignado: The limite_consignado of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_consignado = limite_consignado

    @property
    def limite_externo(self):
        """
        Gets the limite_externo of this LimiteDisponibilidade.


        :return: The limite_externo of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_externo

    @limite_externo.setter
    def limite_externo(self, limite_externo):
        """
        Sets the limite_externo of this LimiteDisponibilidade.


        :param limite_externo: The limite_externo of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_externo = limite_externo

    @property
    def limite_extra(self):
        """
        Gets the limite_extra of this LimiteDisponibilidade.


        :return: The limite_extra of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_extra

    @limite_extra.setter
    def limite_extra(self, limite_extra):
        """
        Sets the limite_extra of this LimiteDisponibilidade.


        :param limite_extra: The limite_extra of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_extra = limite_extra

    @property
    def limite_global(self):
        """
        Gets the limite_global of this LimiteDisponibilidade.
        Campo que 

        :return: The limite_global of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_global

    @limite_global.setter
    def limite_global(self, limite_global):
        """
        Sets the limite_global of this LimiteDisponibilidade.
        Campo que 

        :param limite_global: The limite_global of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_global = limite_global

    @property
    def limite_internacional_compra(self):
        """
        Gets the limite_internacional_compra of this LimiteDisponibilidade.


        :return: The limite_internacional_compra of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_internacional_compra

    @limite_internacional_compra.setter
    def limite_internacional_compra(self, limite_internacional_compra):
        """
        Sets the limite_internacional_compra of this LimiteDisponibilidade.


        :param limite_internacional_compra: The limite_internacional_compra of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_internacional_compra = limite_internacional_compra

    @property
    def limite_internacional_parcelado(self):
        """
        Gets the limite_internacional_parcelado of this LimiteDisponibilidade.


        :return: The limite_internacional_parcelado of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_internacional_parcelado

    @limite_internacional_parcelado.setter
    def limite_internacional_parcelado(self, limite_internacional_parcelado):
        """
        Sets the limite_internacional_parcelado of this LimiteDisponibilidade.


        :param limite_internacional_parcelado: The limite_internacional_parcelado of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_internacional_parcelado = limite_internacional_parcelado

    @property
    def limite_internacional_parcelas(self):
        """
        Gets the limite_internacional_parcelas of this LimiteDisponibilidade.


        :return: The limite_internacional_parcelas of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_internacional_parcelas

    @limite_internacional_parcelas.setter
    def limite_internacional_parcelas(self, limite_internacional_parcelas):
        """
        Sets the limite_internacional_parcelas of this LimiteDisponibilidade.


        :param limite_internacional_parcelas: The limite_internacional_parcelas of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_internacional_parcelas = limite_internacional_parcelas

    @property
    def limite_internacional_saque_global(self):
        """
        Gets the limite_internacional_saque_global of this LimiteDisponibilidade.


        :return: The limite_internacional_saque_global of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_internacional_saque_global

    @limite_internacional_saque_global.setter
    def limite_internacional_saque_global(self, limite_internacional_saque_global):
        """
        Sets the limite_internacional_saque_global of this LimiteDisponibilidade.


        :param limite_internacional_saque_global: The limite_internacional_saque_global of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_internacional_saque_global = limite_internacional_saque_global

    @property
    def limite_internacional_saque_periodo(self):
        """
        Gets the limite_internacional_saque_periodo of this LimiteDisponibilidade.


        :return: The limite_internacional_saque_periodo of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_internacional_saque_periodo

    @limite_internacional_saque_periodo.setter
    def limite_internacional_saque_periodo(self, limite_internacional_saque_periodo):
        """
        Sets the limite_internacional_saque_periodo of this LimiteDisponibilidade.


        :param limite_internacional_saque_periodo: The limite_internacional_saque_periodo of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_internacional_saque_periodo = limite_internacional_saque_periodo

    @property
    def limite_mensal(self):
        """
        Gets the limite_mensal of this LimiteDisponibilidade.


        :return: The limite_mensal of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_mensal

    @limite_mensal.setter
    def limite_mensal(self, limite_mensal):
        """
        Sets the limite_mensal of this LimiteDisponibilidade.


        :param limite_mensal: The limite_mensal of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_mensal = limite_mensal

    @property
    def limite_parcelado(self):
        """
        Gets the limite_parcelado of this LimiteDisponibilidade.


        :return: The limite_parcelado of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_parcelado

    @limite_parcelado.setter
    def limite_parcelado(self, limite_parcelado):
        """
        Sets the limite_parcelado of this LimiteDisponibilidade.


        :param limite_parcelado: The limite_parcelado of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_parcelado = limite_parcelado

    @property
    def limite_parcelas(self):
        """
        Gets the limite_parcelas of this LimiteDisponibilidade.


        :return: The limite_parcelas of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_parcelas

    @limite_parcelas.setter
    def limite_parcelas(self, limite_parcelas):
        """
        Sets the limite_parcelas of this LimiteDisponibilidade.


        :param limite_parcelas: The limite_parcelas of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_parcelas = limite_parcelas

    @property
    def limite_saque_global(self):
        """
        Gets the limite_saque_global of this LimiteDisponibilidade.


        :return: The limite_saque_global of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_saque_global

    @limite_saque_global.setter
    def limite_saque_global(self, limite_saque_global):
        """
        Sets the limite_saque_global of this LimiteDisponibilidade.


        :param limite_saque_global: The limite_saque_global of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_saque_global = limite_saque_global

    @property
    def limite_saque_periodo(self):
        """
        Gets the limite_saque_periodo of this LimiteDisponibilidade.


        :return: The limite_saque_periodo of this LimiteDisponibilidade.
        :rtype: float
        """
        return self._limite_saque_periodo

    @limite_saque_periodo.setter
    def limite_saque_periodo(self, limite_saque_periodo):
        """
        Sets the limite_saque_periodo of this LimiteDisponibilidade.


        :param limite_saque_periodo: The limite_saque_periodo of this LimiteDisponibilidade.
        :type: float
        """
        self._limite_saque_periodo = limite_saque_periodo

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
