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


class OrigemComercialPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrigemComercialPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nome': 'str',
            'descricao': 'str',
            'id_estabelecimento': 'int',
            'id_tipo_origem_comercial': 'int',
            'id_grupo_origem_comercial': 'int',
            'status': 'int',
            'flag_pre_aprovado': 'bool',
            'flag_aprovacao_imediata': 'bool',
            'nome_fantasia_plastico': 'str',
            'flag_cartao_provisorio': 'bool',
            'flag_cartao_definitivo': 'bool',
            'usuario': 'str',
            'senha': 'str',
            'flag_origem_externa': 'bool',
            'flag_modificado': 'bool',
            'flag_envia_fatura_usuario': 'bool',
            'flag_credito_faturamento': 'bool',
            'flag_concede_limite_provisorio': 'bool',
            'flag_digitalizar_doc': 'bool',
            'flag_embossing_loja': 'bool',
            'flag_consulta_previa': 'bool',
            'tipo_pessoa': 'str',
            'id_produto': 'int'
        }

        self.attribute_map = {
            'nome': 'nome',
            'descricao': 'descricao',
            'id_estabelecimento': 'idEstabelecimento',
            'id_tipo_origem_comercial': 'idTipoOrigemComercial',
            'id_grupo_origem_comercial': 'idGrupoOrigemComercial',
            'status': 'status',
            'flag_pre_aprovado': 'flagPreAprovado',
            'flag_aprovacao_imediata': 'flagAprovacaoImediata',
            'nome_fantasia_plastico': 'nomeFantasiaPlastico',
            'flag_cartao_provisorio': 'flagCartaoProvisorio',
            'flag_cartao_definitivo': 'flagCartaoDefinitivo',
            'usuario': 'usuario',
            'senha': 'senha',
            'flag_origem_externa': 'flagOrigemExterna',
            'flag_modificado': 'flagModificado',
            'flag_envia_fatura_usuario': 'flagEnviaFaturaUsuario',
            'flag_credito_faturamento': 'flagCreditoFaturamento',
            'flag_concede_limite_provisorio': 'flagConcedeLimiteProvisorio',
            'flag_digitalizar_doc': 'flagDigitalizarDoc',
            'flag_embossing_loja': 'flagEmbossingLoja',
            'flag_consulta_previa': 'flagConsultaPrevia',
            'tipo_pessoa': 'tipoPessoa',
            'id_produto': 'idProduto'
        }

        self._nome = None
        self._descricao = None
        self._id_estabelecimento = None
        self._id_tipo_origem_comercial = None
        self._id_grupo_origem_comercial = None
        self._status = None
        self._flag_pre_aprovado = None
        self._flag_aprovacao_imediata = None
        self._nome_fantasia_plastico = None
        self._flag_cartao_provisorio = None
        self._flag_cartao_definitivo = None
        self._usuario = None
        self._senha = None
        self._flag_origem_externa = None
        self._flag_modificado = None
        self._flag_envia_fatura_usuario = None
        self._flag_credito_faturamento = None
        self._flag_concede_limite_provisorio = None
        self._flag_digitalizar_doc = None
        self._flag_embossing_loja = None
        self._flag_consulta_previa = None
        self._tipo_pessoa = None
        self._id_produto = None

    @property
    def nome(self):
        """
        Gets the nome of this OrigemComercialPersist.
        Nome da origem comercial

        :return: The nome of this OrigemComercialPersist.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this OrigemComercialPersist.
        Nome da origem comercial

        :param nome: The nome of this OrigemComercialPersist.
        :type: str
        """
        self._nome = nome

    @property
    def descricao(self):
        """
        Gets the descricao of this OrigemComercialPersist.
        Descri\u00C3\u00A7\u00C3\u00A3o da origem comercial

        :return: The descricao of this OrigemComercialPersist.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this OrigemComercialPersist.
        Descri\u00C3\u00A7\u00C3\u00A3o da origem comercial

        :param descricao: The descricao of this OrigemComercialPersist.
        :type: str
        """
        self._descricao = descricao

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this OrigemComercialPersist.
        Identificador do estabelecimento

        :return: The id_estabelecimento of this OrigemComercialPersist.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this OrigemComercialPersist.
        Identificador do estabelecimento

        :param id_estabelecimento: The id_estabelecimento of this OrigemComercialPersist.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def id_tipo_origem_comercial(self):
        """
        Gets the id_tipo_origem_comercial of this OrigemComercialPersist.
        Identificador do tipo de origem comercial

        :return: The id_tipo_origem_comercial of this OrigemComercialPersist.
        :rtype: int
        """
        return self._id_tipo_origem_comercial

    @id_tipo_origem_comercial.setter
    def id_tipo_origem_comercial(self, id_tipo_origem_comercial):
        """
        Sets the id_tipo_origem_comercial of this OrigemComercialPersist.
        Identificador do tipo de origem comercial

        :param id_tipo_origem_comercial: The id_tipo_origem_comercial of this OrigemComercialPersist.
        :type: int
        """
        self._id_tipo_origem_comercial = id_tipo_origem_comercial

    @property
    def id_grupo_origem_comercial(self):
        """
        Gets the id_grupo_origem_comercial of this OrigemComercialPersist.
        Identificador do grupo de origem comercial

        :return: The id_grupo_origem_comercial of this OrigemComercialPersist.
        :rtype: int
        """
        return self._id_grupo_origem_comercial

    @id_grupo_origem_comercial.setter
    def id_grupo_origem_comercial(self, id_grupo_origem_comercial):
        """
        Sets the id_grupo_origem_comercial of this OrigemComercialPersist.
        Identificador do grupo de origem comercial

        :param id_grupo_origem_comercial: The id_grupo_origem_comercial of this OrigemComercialPersist.
        :type: int
        """
        self._id_grupo_origem_comercial = id_grupo_origem_comercial

    @property
    def status(self):
        """
        Gets the status of this OrigemComercialPersist.
        Indica o status da origem comercial

        :return: The status of this OrigemComercialPersist.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OrigemComercialPersist.
        Indica o status da origem comercial

        :param status: The status of this OrigemComercialPersist.
        :type: int
        """
        self._status = status

    @property
    def flag_pre_aprovado(self):
        """
        Gets the flag_pre_aprovado of this OrigemComercialPersist.
        Indica se permite pr\u00C3\u00A9 aprova\u00C3\u00A7\u00C3\u00A3o

        :return: The flag_pre_aprovado of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_pre_aprovado

    @flag_pre_aprovado.setter
    def flag_pre_aprovado(self, flag_pre_aprovado):
        """
        Sets the flag_pre_aprovado of this OrigemComercialPersist.
        Indica se permite pr\u00C3\u00A9 aprova\u00C3\u00A7\u00C3\u00A3o

        :param flag_pre_aprovado: The flag_pre_aprovado of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_pre_aprovado = flag_pre_aprovado

    @property
    def flag_aprovacao_imediata(self):
        """
        Gets the flag_aprovacao_imediata of this OrigemComercialPersist.
        Indica se permite aprova\u00C3\u00A7\u00C3\u00A3o imediata

        :return: The flag_aprovacao_imediata of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_aprovacao_imediata

    @flag_aprovacao_imediata.setter
    def flag_aprovacao_imediata(self, flag_aprovacao_imediata):
        """
        Sets the flag_aprovacao_imediata of this OrigemComercialPersist.
        Indica se permite aprova\u00C3\u00A7\u00C3\u00A3o imediata

        :param flag_aprovacao_imediata: The flag_aprovacao_imediata of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_aprovacao_imediata = flag_aprovacao_imediata

    @property
    def nome_fantasia_plastico(self):
        """
        Gets the nome_fantasia_plastico of this OrigemComercialPersist.
        Nome fantasia impresso no pl\u00C3\u00A1stico

        :return: The nome_fantasia_plastico of this OrigemComercialPersist.
        :rtype: str
        """
        return self._nome_fantasia_plastico

    @nome_fantasia_plastico.setter
    def nome_fantasia_plastico(self, nome_fantasia_plastico):
        """
        Sets the nome_fantasia_plastico of this OrigemComercialPersist.
        Nome fantasia impresso no pl\u00C3\u00A1stico

        :param nome_fantasia_plastico: The nome_fantasia_plastico of this OrigemComercialPersist.
        :type: str
        """
        self._nome_fantasia_plastico = nome_fantasia_plastico

    @property
    def flag_cartao_provisorio(self):
        """
        Gets the flag_cartao_provisorio of this OrigemComercialPersist.
        Indica se permite cart\u00C3\u00A3o provis\u00C3\u00B3rio

        :return: The flag_cartao_provisorio of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_cartao_provisorio

    @flag_cartao_provisorio.setter
    def flag_cartao_provisorio(self, flag_cartao_provisorio):
        """
        Sets the flag_cartao_provisorio of this OrigemComercialPersist.
        Indica se permite cart\u00C3\u00A3o provis\u00C3\u00B3rio

        :param flag_cartao_provisorio: The flag_cartao_provisorio of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_cartao_provisorio = flag_cartao_provisorio

    @property
    def flag_cartao_definitivo(self):
        """
        Gets the flag_cartao_definitivo of this OrigemComercialPersist.
        Indica se permite cart\u00C3\u00A3o definitivo

        :return: The flag_cartao_definitivo of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_cartao_definitivo

    @flag_cartao_definitivo.setter
    def flag_cartao_definitivo(self, flag_cartao_definitivo):
        """
        Sets the flag_cartao_definitivo of this OrigemComercialPersist.
        Indica se permite cart\u00C3\u00A3o definitivo

        :param flag_cartao_definitivo: The flag_cartao_definitivo of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_cartao_definitivo = flag_cartao_definitivo

    @property
    def usuario(self):
        """
        Gets the usuario of this OrigemComercialPersist.
        Usu\u00C3\u00A1rio para autentica\u00C3\u00A7\u00C3\u00A3o

        :return: The usuario of this OrigemComercialPersist.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this OrigemComercialPersist.
        Usu\u00C3\u00A1rio para autentica\u00C3\u00A7\u00C3\u00A3o

        :param usuario: The usuario of this OrigemComercialPersist.
        :type: str
        """
        self._usuario = usuario

    @property
    def senha(self):
        """
        Gets the senha of this OrigemComercialPersist.
        Senha para autentica\u00C3\u00A7\u00C3\u00A3o

        :return: The senha of this OrigemComercialPersist.
        :rtype: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """
        Sets the senha of this OrigemComercialPersist.
        Senha para autentica\u00C3\u00A7\u00C3\u00A3o

        :param senha: The senha of this OrigemComercialPersist.
        :type: str
        """
        self._senha = senha

    @property
    def flag_origem_externa(self):
        """
        Gets the flag_origem_externa of this OrigemComercialPersist.
        Indica se \u00C3\u00A9 origem externa

        :return: The flag_origem_externa of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_origem_externa

    @flag_origem_externa.setter
    def flag_origem_externa(self, flag_origem_externa):
        """
        Sets the flag_origem_externa of this OrigemComercialPersist.
        Indica se \u00C3\u00A9 origem externa

        :param flag_origem_externa: The flag_origem_externa of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_origem_externa = flag_origem_externa

    @property
    def flag_modificado(self):
        """
        Gets the flag_modificado of this OrigemComercialPersist.
        Indica se h\u00C3\u00A1 modifica\u00C3\u00A7\u00C3\u00A3o

        :return: The flag_modificado of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_modificado

    @flag_modificado.setter
    def flag_modificado(self, flag_modificado):
        """
        Sets the flag_modificado of this OrigemComercialPersist.
        Indica se h\u00C3\u00A1 modifica\u00C3\u00A7\u00C3\u00A3o

        :param flag_modificado: The flag_modificado of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_modificado = flag_modificado

    @property
    def flag_envia_fatura_usuario(self):
        """
        Gets the flag_envia_fatura_usuario of this OrigemComercialPersist.
        Indica se envia fatura

        :return: The flag_envia_fatura_usuario of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_envia_fatura_usuario

    @flag_envia_fatura_usuario.setter
    def flag_envia_fatura_usuario(self, flag_envia_fatura_usuario):
        """
        Sets the flag_envia_fatura_usuario of this OrigemComercialPersist.
        Indica se envia fatura

        :param flag_envia_fatura_usuario: The flag_envia_fatura_usuario of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_envia_fatura_usuario = flag_envia_fatura_usuario

    @property
    def flag_credito_faturamento(self):
        """
        Gets the flag_credito_faturamento of this OrigemComercialPersist.
        Indica se permite cr\u00C3\u00A9dito de faturamento

        :return: The flag_credito_faturamento of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_credito_faturamento

    @flag_credito_faturamento.setter
    def flag_credito_faturamento(self, flag_credito_faturamento):
        """
        Sets the flag_credito_faturamento of this OrigemComercialPersist.
        Indica se permite cr\u00C3\u00A9dito de faturamento

        :param flag_credito_faturamento: The flag_credito_faturamento of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_credito_faturamento = flag_credito_faturamento

    @property
    def flag_concede_limite_provisorio(self):
        """
        Gets the flag_concede_limite_provisorio of this OrigemComercialPersist.
        Indica se concede limite provis\u00C3\u00B3rio

        :return: The flag_concede_limite_provisorio of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_concede_limite_provisorio

    @flag_concede_limite_provisorio.setter
    def flag_concede_limite_provisorio(self, flag_concede_limite_provisorio):
        """
        Sets the flag_concede_limite_provisorio of this OrigemComercialPersist.
        Indica se concede limite provis\u00C3\u00B3rio

        :param flag_concede_limite_provisorio: The flag_concede_limite_provisorio of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_concede_limite_provisorio = flag_concede_limite_provisorio

    @property
    def flag_digitalizar_doc(self):
        """
        Gets the flag_digitalizar_doc of this OrigemComercialPersist.
        Indica se digitaliza documento

        :return: The flag_digitalizar_doc of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_digitalizar_doc

    @flag_digitalizar_doc.setter
    def flag_digitalizar_doc(self, flag_digitalizar_doc):
        """
        Sets the flag_digitalizar_doc of this OrigemComercialPersist.
        Indica se digitaliza documento

        :param flag_digitalizar_doc: The flag_digitalizar_doc of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_digitalizar_doc = flag_digitalizar_doc

    @property
    def flag_embossing_loja(self):
        """
        Gets the flag_embossing_loja of this OrigemComercialPersist.
        Indica se realiza embossing em loja

        :return: The flag_embossing_loja of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_embossing_loja

    @flag_embossing_loja.setter
    def flag_embossing_loja(self, flag_embossing_loja):
        """
        Sets the flag_embossing_loja of this OrigemComercialPersist.
        Indica se realiza embossing em loja

        :param flag_embossing_loja: The flag_embossing_loja of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_embossing_loja = flag_embossing_loja

    @property
    def flag_consulta_previa(self):
        """
        Gets the flag_consulta_previa of this OrigemComercialPersist.
        Indica se realiza consulta pr\u00C3\u00A9via

        :return: The flag_consulta_previa of this OrigemComercialPersist.
        :rtype: bool
        """
        return self._flag_consulta_previa

    @flag_consulta_previa.setter
    def flag_consulta_previa(self, flag_consulta_previa):
        """
        Sets the flag_consulta_previa of this OrigemComercialPersist.
        Indica se realiza consulta pr\u00C3\u00A9via

        :param flag_consulta_previa: The flag_consulta_previa of this OrigemComercialPersist.
        :type: bool
        """
        self._flag_consulta_previa = flag_consulta_previa

    @property
    def tipo_pessoa(self):
        """
        Gets the tipo_pessoa of this OrigemComercialPersist.
        Tipo de pessoa

        :return: The tipo_pessoa of this OrigemComercialPersist.
        :rtype: str
        """
        return self._tipo_pessoa

    @tipo_pessoa.setter
    def tipo_pessoa(self, tipo_pessoa):
        """
        Sets the tipo_pessoa of this OrigemComercialPersist.
        Tipo de pessoa

        :param tipo_pessoa: The tipo_pessoa of this OrigemComercialPersist.
        :type: str
        """
        allowed_values = ["PESSOA_FISICA", "PESSOA_JURIDICA"]
        if tipo_pessoa not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_pessoa`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_pessoa = tipo_pessoa

    @property
    def id_produto(self):
        """
        Gets the id_produto of this OrigemComercialPersist.
        Identificador de Produto da origem comercial

        :return: The id_produto of this OrigemComercialPersist.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this OrigemComercialPersist.
        Identificador de Produto da origem comercial

        :param id_produto: The id_produto of this OrigemComercialPersist.
        :type: int
        """
        self._id_produto = id_produto

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

