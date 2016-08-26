# coding: utf-8

"""
CartoApi.py
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


class CartoApi(object):
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

    def consultar_using_get(self, id_cartao, **kwargs):
        """
        Apresenta os dados de um determinado Cart\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite consultar as informa\u00C3\u00A7\u00C3\u00B5es b\u00C3\u00A1sicas de um determinado Cart\u00C3\u00A3o a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get(id_cartao, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o (id). (required)
        :return: OrigemComercial
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_cartao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_cartao' is set
        if ('id_cartao' not in params) or (params['id_cartao'] is None):
            raise ValueError("Missing the required parameter `id_cartao` when calling `consultar_using_get`")

        resource_path = '/api/cartoes/{id_cartao}'.replace('{format}', 'json')
        path_params = {}
        if 'id_cartao' in params:
            path_params['id_cartao'] = params['id_cartao']

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
                                            response_type='OrigemComercial',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get(self, **kwargs):
        """
        Lista os Cart\u00C3\u00B5es gerados pelo Emissor
        Este m\u00C3\u00A9todo permite que sejam listados os cart\u00C3\u00B5es existentes na base do emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Cart\u00C3\u00A3o (id).
        :param int id_status_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o (id).
        :param int id_estagio_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o (id).
        :param int id_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o cart\u00C3\u00A3o pertence (id).
        :param int id_pessoa: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa a qual o cart\u00C3\u00A3o pertence (id).
        :param int portador: Indica qual \u00C3\u00A9 a rela\u00C3\u00A7\u00C3\u00A3o do portador do cart\u00C3\u00A3o com a conta. Quando \u00E2\u0080\u00981\u00E2\u0080\u0099, corresponde ao seu titular. Quando diferente disso, corresponde a um cart\u00C3\u00A3o adicional.
        :param str numero_cartao: Apresenta o n\u00C3\u00BAmero do cart\u00C3\u00A3o.
        :param str data_geracao: Apresenta a data em que o cart\u00C3\u00A3o foi gerado.
        :param str data_status_cartao: Apresenta a data em que o idStatusCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.
        :param str data_estagio_cartao: Apresenta a data em que o idEstagioCartao atual do cart\u00C3\u00A3o fora aplicado, quando houver.
        :param str data_validade: Apresenta a data de validade do cart\u00C3\u00A3o em formato AAAA-MM, quando houver.
        :param str data_impressao: Apresenta a data em que o cart\u00C3\u00A3o fora impresso, caso impress\u00C3\u00A3o em loja, ou a data em que ele fora inclu\u00C3\u00ADdo no arquivo para impress\u00C3\u00A3o via gr\u00C3\u00A1fica.
        :param str arquivo_impressao: Apresenta o nome do arquivo onde o cart\u00C3\u00A3o fora inclu\u00C3\u00ADdo para impress\u00C3\u00A3o por uma gr\u00C3\u00A1fica, quando houver.
        :param int flag_impressao_origem_comercial: Quando ativa, indica que o cart\u00C3\u00A3o fora impresso na Origem Comercial.
        :param int flag_provisorio: Quando ativa, indica que o cart\u00C3\u00A3o \u00C3\u00A9 provis\u00C3\u00B3rio. Ou seja, \u00C3\u00A9 um cart\u00C3\u00A3o para uso tempor\u00C3\u00A1rio quando se deseja permitir que o cliente transacione sem que ele tenha recebido um cart\u00C3\u00A3o definitivo.
        :param str codigo_desbloqueio: Apresenta um c\u00C3\u00B3digo espec\u00C3\u00ADfico para ser utilizado como vari\u00C3\u00A1vel no processo de desbloqueio do cart\u00C3\u00A3o para emissores que querem usar esta funcionalidade.
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: ListaDeCartes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_cartao', 'id_status_cartao', 'id_estagio_cartao', 'id_conta', 'id_pessoa', 'portador', 'numero_cartao', 'data_geracao', 'data_status_cartao', 'data_estagio_cartao', 'data_validade', 'data_impressao', 'arquivo_impressao', 'flag_impressao_origem_comercial', 'flag_provisorio', 'codigo_desbloqueio', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/cartoes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id_cartao' in params:
            query_params['id_cartao'] = params['id_cartao']
        if 'id_status_cartao' in params:
            query_params['id_status_cartao'] = params['id_status_cartao']
        if 'id_estagio_cartao' in params:
            query_params['id_estagio_cartao'] = params['id_estagio_cartao']
        if 'id_conta' in params:
            query_params['id_conta'] = params['id_conta']
        if 'id_pessoa' in params:
            query_params['id_pessoa'] = params['id_pessoa']
        if 'portador' in params:
            query_params['portador'] = params['portador']
        if 'numero_cartao' in params:
            query_params['numero_cartao'] = params['numero_cartao']
        if 'data_geracao' in params:
            query_params['data_geracao'] = params['data_geracao']
        if 'data_status_cartao' in params:
            query_params['data_status_cartao'] = params['data_status_cartao']
        if 'data_estagio_cartao' in params:
            query_params['data_estagio_cartao'] = params['data_estagio_cartao']
        if 'data_validade' in params:
            query_params['data_validade'] = params['data_validade']
        if 'data_impressao' in params:
            query_params['data_impressao'] = params['data_impressao']
        if 'arquivo_impressao' in params:
            query_params['arquivo_impressao'] = params['arquivo_impressao']
        if 'flag_impressao_origem_comercial' in params:
            query_params['flag_impressao_origem_comercial'] = params['flag_impressao_origem_comercial']
        if 'flag_provisorio' in params:
            query_params['flag_provisorio'] = params['flag_provisorio']
        if 'codigo_desbloqueio' in params:
            query_params['codigo_desbloqueio'] = params['codigo_desbloqueio']
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
                                            response_type='ListaDeCartes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
