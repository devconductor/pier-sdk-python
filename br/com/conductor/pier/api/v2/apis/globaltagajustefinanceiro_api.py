# coding: utf-8

"""
GlobaltagajustefinanceiroApi.py
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


class GlobaltagajustefinanceiroApi(object):
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

    def ajustar_conta_using_post(self, id_tipo_ajuste, data_ajuste, valor_ajuste, id_conta, **kwargs):
        """
        {{{ajuste_financeiro_resource_ajustar_conta}}}
        {{{ajuste_financeiro_resource_ajustar_conta_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ajustar_conta_using_post(id_tipo_ajuste, data_ajuste, valor_ajuste, id_conta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_tipo_ajuste: {{{ajuste_financeiro_persist_id_tipo_ajuste_value}}} (required)
        :param str data_ajuste: {{{ajuste_financeiro_persist_data_ajuste_value}}} (required)
        :param float valor_ajuste: {{{ajuste_financeiro_persist_valor_ajuste_value}}} (required)
        :param int id_conta: {{{ajuste_financeiro_persist_id_conta_value}}} (required)
        :param str identificador_externo: {{{ajuste_financeiro_persist_identificador_externo_value}}}
        :param int id_transacao_original: {{{ajuste_persist_id_transacao_original}}}
        :return: AjusteFinanceiroResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_tipo_ajuste', 'data_ajuste', 'valor_ajuste', 'id_conta', 'identificador_externo', 'id_transacao_original']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ajustar_conta_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_tipo_ajuste' is set
        if ('id_tipo_ajuste' not in params) or (params['id_tipo_ajuste'] is None):
            raise ValueError("Missing the required parameter `id_tipo_ajuste` when calling `ajustar_conta_using_post`")
        # verify the required parameter 'data_ajuste' is set
        if ('data_ajuste' not in params) or (params['data_ajuste'] is None):
            raise ValueError("Missing the required parameter `data_ajuste` when calling `ajustar_conta_using_post`")
        # verify the required parameter 'valor_ajuste' is set
        if ('valor_ajuste' not in params) or (params['valor_ajuste'] is None):
            raise ValueError("Missing the required parameter `valor_ajuste` when calling `ajustar_conta_using_post`")
        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `ajustar_conta_using_post`")

        resource_path = '/api/ajustes-financeiros'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id_tipo_ajuste' in params:
            query_params['idTipoAjuste'] = params['id_tipo_ajuste']
        if 'data_ajuste' in params:
            query_params['dataAjuste'] = params['data_ajuste']
        if 'valor_ajuste' in params:
            query_params['valorAjuste'] = params['valor_ajuste']
        if 'identificador_externo' in params:
            query_params['identificadorExterno'] = params['identificador_externo']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'id_transacao_original' in params:
            query_params['idTransacaoOriginal'] = params['id_transacao_original']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AjusteFinanceiroResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get3(self, id, **kwargs):
        """
        {{{ajuste_financeiro_resource_consultar}}}
        {{{ajuste_financeiro_resource_consultar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get3(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{ajuste_financeiro_resource_consultar_param_id}}} (required)
        :return: AjusteFinanceiroResponse
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
                    " to method consultar_using_get3" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get3`")

        resource_path = '/api/ajustes-financeiros/{id}'.replace('{format}', 'json')
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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AjusteFinanceiroResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get2(self, **kwargs):
        """
        {{{ajuste_financeiro_resource_listar}}}
        {{{ajuste_financeiro_resource_listar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get2(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param int id_tipo_ajuste: {{{ajuste_request_id_tipo_ajuste_value}}}
        :param str data_ajuste: {{{ajuste_request_data_ajuste_value}}}
        :param float valor_ajuste: {{{ajuste_request_valor_ajuste_value}}}
        :param str identificador_externo: {{{ajuste_request_identificador_externo_value}}}
        :param int id_conta: {{{ajuste_request_id_conta_value}}}
        :return: PageAjusteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'id_tipo_ajuste', 'data_ajuste', 'valor_ajuste', 'identificador_externo', 'id_conta']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get2" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/ajustes-financeiros'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_tipo_ajuste' in params:
            query_params['idTipoAjuste'] = params['id_tipo_ajuste']
        if 'data_ajuste' in params:
            query_params['dataAjuste'] = params['data_ajuste']
        if 'valor_ajuste' in params:
            query_params['valorAjuste'] = params['valor_ajuste']
        if 'identificador_externo' in params:
            query_params['identificadorExterno'] = params['identificador_externo']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageAjusteResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
