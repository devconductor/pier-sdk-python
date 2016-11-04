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

    def alterar_vencimento_using_put(self, id_conta, novo_dia_vencimento, **kwargs):
        """
        Alterar vencimento
        Esse recurso permite alterar o vencimento de uma conta especifica.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_vencimento_using_put(id_conta, novo_dia_vencimento, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int novo_dia_vencimento: Novo dia de vencimento. (required)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'novo_dia_vencimento']
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

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `alterar_vencimento_using_put`")
        # verify the required parameter 'novo_dia_vencimento' is set
        if ('novo_dia_vencimento' not in params) or (params['novo_dia_vencimento'] is None):
            raise ValueError("Missing the required parameter `novo_dia_vencimento` when calling `alterar_vencimento_using_put`")

        resource_path = '/api/contas/{id_conta}/alterar-vencimento'.replace('{format}', 'json')
        path_params = {}
        if 'id_conta' in params:
            path_params['id_conta'] = params['id_conta']

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

    def consultar_using_get1(self, id_conta, **kwargs):
        """
        Apresenta dados de uma determinada conta
        Este m\u00C3\u00A9todo permite consultar dados de uma determinada conta a partir de seu codigo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get1(id_conta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta']
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

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `consultar_using_get1`")

        resource_path = '/api/contas/{id_conta}'.replace('{format}', 'json')
        path_params = {}
        if 'id_conta' in params:
            path_params['id_conta'] = params['id_conta']

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
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: Conta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id_produto', 'id_origem_comercial', 'id_pessoa', 'id_status_conta', 'dia_vencimento', 'melhor_dia_compra', 'data_status_conta', 'data_cadastro', 'data_ultima_alteracao_vencimento', 'page', 'limit']
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
                                            response_type='Conta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
