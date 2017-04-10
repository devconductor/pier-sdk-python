from __future__ import absolute_import

# import models into sdk package
from .models.ajuste_response import AjusteResponse
from .models.atendimento_cliente import AtendimentoCliente
from .models.auth_token import AuthToken
from .models.base import Base
from .models.body_access_token import BodyAccessToken
from .models.boleto_de_fatura import BoletoDeFatura
from .models.campo_codificado_descricao_response import CampoCodificadoDescricaoResponse
from .models.cartao import Cartao
from .models.cartao_impressao import CartaoImpressao
from .models.cdt_detalhe_oportunidade_aud import CdtDetalheOportunidadeAUD
from .models.conta import Conta
from .models.detalhe_oportunidade_persist import DetalheOportunidadePersist
from .models.detalhe_oportunidade_response import DetalheOportunidadeResponse
from .models.detalhe_oportunidade_update import DetalheOportunidadeUpdate
from .models.detalhes_fatura_response import DetalhesFaturaResponse
from .models.divida_cliente_response import DividaClienteResponse
from .models.endereco import Endereco
from .models.endereco_aprovado_persist import EnderecoAprovadoPersist
from .models.endereco_aprovado_response import EnderecoAprovadoResponse
from .models.estabelecimento import Estabelecimento
from .models.estagio_cartao import EstagioCartao
from .models.extra_info import ExtraInfo
from .models.faq import FAQ
from .models.fatura_consignada_detalhe_response import FaturaConsignadaDetalheResponse
from .models.fatura_consignada_response import FaturaConsignadaResponse
from .models.fatura_response import FaturaResponse
from .models.historico_atraso_fatura_response import HistoricoAtrasoFaturaResponse
from .models.historico_eventos import HistoricoEventos
from .models.historico_impressao_cartao import HistoricoImpressaoCartao
from .models.historico_telefone import HistoricoTelefone
from .models.limite_disponibilidade import LimiteDisponibilidade
from .models.link_historico_assessoria_response import LinkHistoricoAssessoriaResponse
from .models.link_page_historico_assessoria_response import LinkPageHistoricoAssessoriaResponse
from .models.link_page_transferencia_bancaria_response import LinkPageTransferenciaBancariaResponse
from .models.link_transferencia_bancaria_response import LinkTransferenciaBancariaResponse
from .models.lista_produtos import ListaProdutos
from .models.lote_cartoes_pre_pagos import LoteCartoesPrePagos
from .models.notificacao_push_response import NotificacaoPushResponse
from .models.notificacao_sms_body import NotificacaoSMSBody
from .models.notificacao_sms_response import NotificacaoSMSResponse
from .models.oportunidade_aud_response import OportunidadeAUDResponse
from .models.oportunidade_persist import OportunidadePersist
from .models.oportunidade_response import OportunidadeResponse
from .models.oportunidade_update import OportunidadeUpdate
from .models.origem_comercial import OrigemComercial
from .models.page_atendimento_clientes import PageAtendimentoClientes
from .models.page_bases import PageBases
from .models.page_campo_codificado_descricao import PageCampoCodificadoDescricao
from .models.page_cartoes import PageCartoes
from .models.page_contas import PageContas
from .models.page_enderecos import PageEnderecos
from .models.page_estabelecimentos import PageEstabelecimentos
from .models.page_estagios_cartoes import PageEstagiosCartoes
from .models.page_faqs import PageFaqs
from .models.page_faturas import PageFaturas
from .models.page_faturas_consignadas import PageFaturasConsignadas
from .models.page_historico_atraso import PageHistoricoAtraso
from .models.page_historico_eventos import PageHistoricoEventos
from .models.page_lote_cartoes_pre_pagos_response import PageLoteCartoesPrePagosResponse
from .models.page_oprtunidade_aud import PageOprtunidadeAUD
from .models.page_oprtunidades_response import PageOprtunidadesResponse
from .models.page_origens_comerciais import PageOrigensComerciais
from .models.page_pessoas import PagePessoas
from .models.page_portador import PagePortador
from .models.page_push import PagePush
from .models.page_sms import PageSMS
from .models.page_status_cartoes import PageStatusCartoes
from .models.page_status_contas import PageStatusContas
from .models.page_status_impressao import PageStatusImpressao
from .models.page_status_oprtunidades import PageStatusOprtunidades
from .models.page_status_oprtunidades_aud import PageStatusOprtunidadesAUD
from .models.page_telefones import PageTelefones
from .models.page_tipo_ajuste import PageTipoAjuste
from .models.page_tipo_boleto import PageTipoBoleto
from .models.page_tipo_oprtunidades import PageTipoOprtunidades
from .models.page_tipo_oprtunidades_aud import PageTipoOprtunidadesAUD
from .models.page_tipo_telefones import PageTipoTelefones
from .models.page_tipos_endereco import PageTiposEndereco
from .models.page_transacao_response import PageTransacaoResponse
from .models.page_transacoes_correntes import PageTransacoesCorrentes
from .models.page_transferencias import PageTransferencias
from .models.page_usuarios import PageUsuarios
from .models.page_web_hooks import PageWebHooks
from .models.pessoa import Pessoa
from .models.pessoa_detalhe_response import PessoaDetalheResponse
from .models.pessoa_fisica_aprovada_persist import PessoaFisicaAprovadaPersist
from .models.pessoa_fisica_aprovada_response import PessoaFisicaAprovadaResponse
from .models.pessoa_juridica_aprovada_persist import PessoaJuridicaAprovadaPersist
from .models.pessoa_juridica_aprovada_response import PessoaJuridicaAprovadaResponse
from .models.pessoa_persist import PessoaPersist
from .models.portador import Portador
from .models.produto_detalhes_response import ProdutoDetalhesResponse
from .models.produto_response import ProdutoResponse
from .models.push_apns import PushAPNS
from .models.push_fcm_e_gcm import PushFCMEGCM
from .models.risco_fraude_detalhado_response import RiscoFraudeDetalhadoResponse
from .models.risco_fraude_response import RiscoFraudeResponse
from .models.risco_fraude_response_page import RiscoFraudeResponsePage
from .models.sms import SMS
from .models.socio_aprovado_response import SocioAprovadoResponse
from .models.status_cartao import StatusCartao
from .models.status_conta import StatusConta
from .models.status_impressao import StatusImpressao
from .models.status_oportunidade import StatusOportunidade
from .models.status_oportunidade_aud_response import StatusOportunidadeAUDResponse
from .models.status_oportunidade_response import StatusOportunidadeResponse
from .models.telefone import Telefone
from .models.telefone_pessoa_aprovada_persist import TelefonePessoaAprovadaPersist
from .models.telefone_pessoa_aprovada_response import TelefonePessoaAprovadaResponse
from .models.tipo_ajuste_response import TipoAjusteResponse
from .models.tipo_endereco import TipoEndereco
from .models.tipo_oportunidade import TipoOportunidade
from .models.tipo_oportunidade_aud_response import TipoOportunidadeAUDResponse
from .models.tipo_oportunidade_response import TipoOportunidadeResponse
from .models.tipo_telefone import TipoTelefone
from .models.token import Token
from .models.transacao_response import TransacaoResponse
from .models.transacoes_correntes import TransacoesCorrentes
from .models.transferencia import Transferencia
from .models.usuario_persist import UsuarioPersist
from .models.usuario_response import UsuarioResponse
from .models.usuario_update import UsuarioUpdate
from .models.valida_cartao import ValidaCartao
from .models.web_hook import WebHook

# import apis into sdk package
from .apis.base_api import BaseApi
from .apis.cadastros_gerais_api import CadastrosGeraisApi
from .apis.cartao_api import CartaoApi
from .apis.conta_api import ContaApi
from .apis.faq_api import FAQApi
from .apis.notificacoes_api import NotificacoesApi
from .apis.oportunidades_api import OportunidadesApi
from .apis.risco_fraude_api import RiscoFraudeApi
from .apis.status_parametros_api import StatusParametrosApi
from .apis.token_api import TokenApi
from .apis.usuarios_api import UsuariosApi
from .apis.webhooks_api import WebhooksApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
