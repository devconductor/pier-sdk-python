# coding: utf-8

"""
ContaApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ContaApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def alterar_limite_using_put(self, id, limite_global, limite_compra, limite_parcelado, limite_parcelas, limite_saque_global, limite_saque_periodo, limite_consignado, limite_internacional_compra, limite_internacional_parcelado, limite_internacional_parcelas, limite_internacional_saque_global, limite_internacional_saque_periodo, **kwargs):
        """
        Alterar limite
        Esse recurso permite realizar a altera\u00C3\u00A7\u00C3\u00A3o dos Limites de uma determinada Conta.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_limite_using_put(id, limite_global, limite_compra, limite_parcelado, limite_parcelas, limite_saque_global, limite_saque_periodo, limite_consignado, limite_internacional_compra, limite_internacional_parcelado, limite_internacional_parcelas, limite_internacional_saque_global, limite_internacional_saque_periodo, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param float limite_global: Apresenta o valor do limite de cr\u00C3\u00A9dito que o portador do cart\u00C3\u00A3o possui. (required)
        :param float limite_compra: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador possui para uso exclusivo em Compras Nacionais. (required)
        :param float limite_parcelado: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador possui para realizar transa\u00C3\u00A7\u00C3\u00B5es de compras parceladas. (required)
        :param float limite_parcelas: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que portador pode acumular a partir da soma das parcelas das compras que forem realizadas nesta modalidade. (required)
        :param float limite_saque_global: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador pode utilizar para realizar transa\u00C3\u00A7\u00C3\u00B5es de Saque Nacional. (required)
        :param float limite_saque_periodo: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador pode utilizar para realizar transa\u00C3\u00A7\u00C3\u00B5es de Saque Nacional dentro de cada ciclo de faturamento. (required)
        :param float limite_consignado: Quando utilizado pelo emissor, este campo apresenta o valor da margem de cr\u00C3\u00A9dito que ele poder\u00C3\u00A1 utilizar para ser cobrado de forma consignada (desconto em folha) em seu sal\u00C3\u00A1rio/vencimentos. (required)
        :param float limite_internacional_compra: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador possui para uso exclusivo em Compras Internacionais. (required)
        :param float limite_internacional_parcelado: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador possui para realizar transa\u00C3\u00A7\u00C3\u00B5es Internacionais de Compras Parceladas. (required)
        :param float limite_internacional_parcelas: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que portador pode acumular a partir da soma das parcelas das compras internacionais que forem realizadas nesta modalidade. (required)
        :param float limite_internacional_saque_global: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador pode utilizar para realizar transa\u00C3\u00A7\u00C3\u00B5es de Saque Internacional. (required)
        :param float limite_internacional_saque_periodo: Quando utilizado pelo emissor, este campo apresenta o valor do limite de cr\u00C3\u00A9dito que o portador pode utilizar para realizar transa\u00C3\u00A7\u00C3\u00B5es de Saque Internacional dentro de cada ciclo de faturamento. (required)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limite_global', 'limite_compra', 'limite_parcelado', 'limite_parcelas', 'limite_saque_global', 'limite_saque_periodo', 'limite_consignado', 'limite_internacional_compra', 'limite_internacional_parcelado', 'limite_internacional_parcelas', 'limite_internacional_saque_global', 'limite_internacional_saque_periodo']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alterar_limite_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_global' is set
        if ('limite_global' not in params) or (params['limite_global'] is None):
            raise ValueError("Missing the required parameter `limite_global` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_compra' is set
        if ('limite_compra' not in params) or (params['limite_compra'] is None):
            raise ValueError("Missing the required parameter `limite_compra` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_parcelado' is set
        if ('limite_parcelado' not in params) or (params['limite_parcelado'] is None):
            raise ValueError("Missing the required parameter `limite_parcelado` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_parcelas' is set
        if ('limite_parcelas' not in params) or (params['limite_parcelas'] is None):
            raise ValueError("Missing the required parameter `limite_parcelas` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_saque_global' is set
        if ('limite_saque_global' not in params) or (params['limite_saque_global'] is None):
            raise ValueError("Missing the required parameter `limite_saque_global` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_saque_periodo' is set
        if ('limite_saque_periodo' not in params) or (params['limite_saque_periodo'] is None):
            raise ValueError("Missing the required parameter `limite_saque_periodo` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_consignado' is set
        if ('limite_consignado' not in params) or (params['limite_consignado'] is None):
            raise ValueError("Missing the required parameter `limite_consignado` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_internacional_compra' is set
        if ('limite_internacional_compra' not in params) or (params['limite_internacional_compra'] is None):
            raise ValueError("Missing the required parameter `limite_internacional_compra` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_internacional_parcelado' is set
        if ('limite_internacional_parcelado' not in params) or (params['limite_internacional_parcelado'] is None):
            raise ValueError("Missing the required parameter `limite_internacional_parcelado` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_internacional_parcelas' is set
        if ('limite_internacional_parcelas' not in params) or (params['limite_internacional_parcelas'] is None):
            raise ValueError("Missing the required parameter `limite_internacional_parcelas` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_internacional_saque_global' is set
        if ('limite_internacional_saque_global' not in params) or (params['limite_internacional_saque_global'] is None):
            raise ValueError("Missing the required parameter `limite_internacional_saque_global` when calling `alterar_limite_using_put`")
        # verify the required parameter 'limite_internacional_saque_periodo' is set
        if ('limite_internacional_saque_periodo' not in params) or (params['limite_internacional_saque_periodo'] is None):
            raise ValueError("Missing the required parameter `limite_internacional_saque_periodo` when calling `alterar_limite_using_put`")

        resource_path = '/api/contas/{id}/alterar-limites'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'limite_global' in params:
            query_params['limiteGlobal'] = params['limite_global']
        if 'limite_compra' in params:
            query_params['limiteCompra'] = params['limite_compra']
        if 'limite_parcelado' in params:
            query_params['limiteParcelado'] = params['limite_parcelado']
        if 'limite_parcelas' in params:
            query_params['limiteParcelas'] = params['limite_parcelas']
        if 'limite_saque_global' in params:
            query_params['limiteSaqueGlobal'] = params['limite_saque_global']
        if 'limite_saque_periodo' in params:
            query_params['limiteSaquePeriodo'] = params['limite_saque_periodo']
        if 'limite_consignado' in params:
            query_params['limiteConsignado'] = params['limite_consignado']
        if 'limite_internacional_compra' in params:
            query_params['limiteInternacionalCompra'] = params['limite_internacional_compra']
        if 'limite_internacional_parcelado' in params:
            query_params['limiteInternacionalParcelado'] = params['limite_internacional_parcelado']
        if 'limite_internacional_parcelas' in params:
            query_params['limiteInternacionalParcelas'] = params['limite_internacional_parcelas']
        if 'limite_internacional_saque_global' in params:
            query_params['limiteInternacionalSaqueGlobal'] = params['limite_internacional_saque_global']
        if 'limite_internacional_saque_periodo' in params:
            query_params['limiteInternacionalSaquePeriodo'] = params['limite_internacional_saque_periodo']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Conta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def alterar_vencimento_using_put(self, id, novo_dia_vencimento, **kwargs):
        """
        Alterar vencimento
        Esse recurso permite alterar o vencimento de uma conta especifica.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_vencimento_using_put(id, novo_dia_vencimento, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int novo_dia_vencimento: Novo dia de vencimento. (required)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'novo_dia_vencimento']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alterar_vencimento_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alterar_vencimento_using_put`")
        # verify the required parameter 'novo_dia_vencimento' is set
        if ('novo_dia_vencimento' not in params) or (params['novo_dia_vencimento'] is None):
            raise ValueError("Missing the required parameter `novo_dia_vencimento` when calling `alterar_vencimento_using_put`")

        resource_path = '/api/contas/{id}/alterar-vencimento'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'novo_dia_vencimento' in params:
            query_params['novo_dia_vencimento'] = params['novo_dia_vencimento']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Conta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_limite_disponibilidade_using_get1(self, id, **kwargs):
        """
        Apresenta os limites da conta
        Este m\u00C3\u00A9todo permite consultar os Limites configurados para uma determinada Conta, a partir do c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_limite_disponibilidade_using_get1(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o (id). (required)
        :return: LimiteDisponibilidade
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_limite_disponibilidade_using_get1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_limite_disponibilidade_using_get1`")

        resource_path = '/api/contas/{id}/limites-disponibilidades'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LimiteDisponibilidade',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get1(self, id, **kwargs):
        """
        Apresenta dados de uma determinada conta
        Este m\u00C3\u00A9todo permite consultar dados de uma determinada conta a partir de seu codigo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get1(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get1`")

        resource_path = '/api/contas/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Conta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def gerar_cartao_using_post(self, id, id_pessoa, **kwargs):
        """
        Realiza a gera\u00C3\u00A7\u00C3\u00A3o de um novo cart\u00C3\u00A3o para impress\u00C3\u00A3o avulsa
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.gerar_cartao_using_post(id, id_pessoa, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int id_pessoa: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da pessoa (id). (required)
        :return: CartaoImpressao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id_pessoa']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gerar_cartao_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `gerar_cartao_using_post`")
        # verify the required parameter 'id_pessoa' is set
        if ('id_pessoa' not in params) or (params['id_pessoa'] is None):
            raise ValueError("Missing the required parameter `id_pessoa` when calling `gerar_cartao_using_post`")

        resource_path = '/api/contas/{id}/pessoas/{id_pessoa}/gerar-cartao'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'id_pessoa' in params:
            path_params['id_pessoa'] = params['id_pessoa']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CartaoImpressao',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_faturas_using_get(self, id, **kwargs):
        """
        Listar Faturas da Conta
        Atrav\u00C3\u00A9s desta opera\u00C3\u00A7\u00C3\u00A3o os Emissores ou Portadores poder\u00C3\u00A3o consultar todo o Hist\u00C3\u00B3rico de Faturas vinculados a uma determinada Conta, independentemente do valor delas.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_faturas_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :param date data_vencimento: Data de Vencimento da Fatura.
        :return: Fatura
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'limit', 'data_vencimento']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_faturas_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `listar_faturas_using_get`")

        resource_path = '/api/contas/{id}/faturas'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'data_vencimento' in params:
            query_params['dataVencimento'] = params['data_vencimento']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Fatura',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get1(self, **kwargs):
        """
        Lista contas existentes na base de dados do Emissor
        Este recurso permite listar contas existentes na base de dados do Emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get1(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o de conta (id).
        :param int id_produto: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do produto ao qual a conta faz parte. (id).
        :param int id_origem_comercial: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Origem Comercial (id) que deu origem a Conta.
        :param int id_pessoa: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa Titular da Conta (id).
        :param int id_status_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto a qual o cart\u00C3\u00A3o pertence (id).
        :param int dia_vencimento: Apresenta o dia de vencimento.
        :param int melhor_dia_compra: Apresenta o melhor dia de compra.
        :param date data_status_conta: Apresenta a data em que o idStatusConta atual fora atribu\u00C3\u00ADdo para ela.
        :param date data_cadastro: Apresenta a data em que o cart\u00C3\u00A3o foi gerado.
        :param date data_ultima_alteracao_vencimento: Apresenta a data da ultima altera\u00C3\u00A7\u00C3\u00A3o de vencimento.
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'id', 'id_produto', 'id_origem_comercial', 'id_pessoa', 'id_status_conta', 'dia_vencimento', 'melhor_dia_compra', 'data_status_conta', 'data_cadastro', 'data_ultima_alteracao_vencimento']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get1" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/contas'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'id_produto' in params:
            query_params['idProduto'] = params['id_produto']
        if 'id_origem_comercial' in params:
            query_params['idOrigemComercial'] = params['id_origem_comercial']
        if 'id_pessoa' in params:
            query_params['idPessoa'] = params['id_pessoa']
        if 'id_status_conta' in params:
            query_params['idStatusConta'] = params['id_status_conta']
        if 'dia_vencimento' in params:
            query_params['diaVencimento'] = params['dia_vencimento']
        if 'melhor_dia_compra' in params:
            query_params['melhorDiaCompra'] = params['melhor_dia_compra']
        if 'data_status_conta' in params:
            query_params['dataStatusConta'] = params['data_status_conta']
        if 'data_cadastro' in params:
            query_params['dataCadastro'] = params['data_cadastro']
        if 'data_ultima_alteracao_vencimento' in params:
            query_params['dataUltimaAlteracaoVencimento'] = params['data_ultima_alteracao_vencimento']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Conta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def transacoes_using_get(self, id, **kwargs):
        """
        Permite listar uma linha do tempo com os eventos da conta
        Esta opera\u00C3\u00A7\u00C3\u00A3o tem como objetivo permitir a listagem, em formato de timeline, dos eventos vinculados a uma detemrinada conta. Transa\u00C3\u00A7\u00C3\u00B5es, fechamento da fatura, pagamentos, gera\u00C3\u00A7\u00C3\u00A3o de cart\u00C3\u00B5es e altera\u00C3\u00A7\u00C3\u00A3o de limite s\u00C3\u00A3o exemplos de eventos contemplados por esta funcionalidade. Neste m\u00C3\u00A9todo, as opera\u00C3\u00A7\u00C3\u00B5es s\u00C3\u00A3o ordenadas de forma decrescente.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transacoes_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageTransacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transacoes_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transacoes_using_get`")

        resource_path = '/api/contas/{id}/timeline'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageTransacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
