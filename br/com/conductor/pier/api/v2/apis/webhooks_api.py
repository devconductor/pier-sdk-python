# coding: utf-8

"""
WebhooksApi.py
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


class WebhooksApi(object):
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

    def alterar_using_put2(self, id, evento, metodo, url, **kwargs):
        """
        Alterar Webhook
        Este m\u00C3\u00A9todo permite que seja modificado um webhooks j\u00C3\u00A1 cadastrado

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_using_put2(id, evento, metodo, url, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo identificador do Webhook (required)
        :param Object evento: Evento a ser chamado pelo WebHook (required)
        :param Object metodo: M\u00C3\u00A9todo que a ser chamado pelo WebHook (required)
        :param str url: URL que a ser consumida pelo WebHook (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'evento', 'metodo', 'url']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alterar_using_put2" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alterar_using_put2`")
        # verify the required parameter 'evento' is set
        if ('evento' not in params) or (params['evento'] is None):
            raise ValueError("Missing the required parameter `evento` when calling `alterar_using_put2`")
        # verify the required parameter 'metodo' is set
        if ('metodo' not in params) or (params['metodo'] is None):
            raise ValueError("Missing the required parameter `metodo` when calling `alterar_using_put2`")
        # verify the required parameter 'url' is set
        if ('url' not in params) or (params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `alterar_using_put2`")

        resource_path = '/api/webhooks'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'evento' in params:
            query_params['evento'] = params['evento']
        if 'metodo' in params:
            query_params['metodo'] = params['metodo']
        if 'url' in params:
            query_params['url'] = params['url']

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
                                            response_type='WebHook',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get9(self, id, **kwargs):
        """
        Consultar Webhook
        Este m\u00C3\u00A9todo permite que sejam consultado um webhook do emissor atrav\u00C3\u00A9s de um id especifico

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get9(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Webhook (id). (required)
        :return: WebHook
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
                    " to method consultar_using_get9" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get9`")

        resource_path = '/api/webhooks/{id}'.replace('{format}', 'json')
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
                                            response_type='WebHook',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get10(self, **kwargs):
        """
        Lista os Webhooks
        Este m\u00C3\u00A9todo permite que sejam listados os webhooks existentes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get10(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id do WebHook
        :param Object evento: Evento a ser chamado pelo WebHook
        :param Object metodo: M\u00C3\u00A9todo que a ser chamado pelo WebHook
        :param str url: URL que a ser consumida pelo WebHook
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageWebHooks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'evento', 'metodo', 'url', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get10" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/webhooks'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'evento' in params:
            query_params['evento'] = params['evento']
        if 'metodo' in params:
            query_params['metodo'] = params['metodo']
        if 'url' in params:
            query_params['url'] = params['url']
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
                                            response_type='PageWebHooks',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post3(self, evento, metodo, url, **kwargs):
        """
        Salvar Webhook
        Este m\u00C3\u00A9todo permite que seja adicionado um novo webhook

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post3(evento, metodo, url, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object evento: Evento a ser chamado pelo WebHook (required)
        :param Object metodo: M\u00C3\u00A9todo que a ser chamado pelo WebHook (required)
        :param str url: URL que a ser consumida pelo WebHook (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['evento', 'metodo', 'url']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post3" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'evento' is set
        if ('evento' not in params) or (params['evento'] is None):
            raise ValueError("Missing the required parameter `evento` when calling `salvar_using_post3`")
        # verify the required parameter 'metodo' is set
        if ('metodo' not in params) or (params['metodo'] is None):
            raise ValueError("Missing the required parameter `metodo` when calling `salvar_using_post3`")
        # verify the required parameter 'url' is set
        if ('url' not in params) or (params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `salvar_using_post3`")

        resource_path = '/api/webhooks'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'evento' in params:
            query_params['evento'] = params['evento']
        if 'metodo' in params:
            query_params['metodo'] = params['metodo']
        if 'url' in params:
            query_params['url'] = params['url']

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
                                            response_type='WebHook',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
