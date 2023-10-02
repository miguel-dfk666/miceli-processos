interface Processo {
  id: number;
  numero_processo: string | null;
  descricao: string | null;
  data_cadastro: string; // Formato: "dd/mm/AAAA"
  juiz_responsavel: string;
  coligacao: string | null;
  numero_dossie: string | null;
  pasta_antiga: string | null;
  tipo_de_acao: string | null;
  obj_padrao: string | null;
  advogado_adverso: string | null;
  advogado_agressor: string | null;
  advogado_adverso_numero_oab: string | null;
  advogado_colaborador: string | null;
  advogado_colaborador_numero_oab: string | null;
  tipo_sentenca: string | null;
  data_sentenca: string; // Formato: "dd/mm/AAAA"
  descricao_sentenca: string | null;
  tipo_acordo: string | null;
  data_acordo: string; // Formato: "dd/mm/AAAA"
  descricao_acordo: string | null;
  valor_estimado: number;
  valor_contingencia: number;
  valor_causa: number;
  valor_pedido: number;
  valor_risco_provavel: number;
  data_estimada_prevista: string | null; // Formato: "dd/mm/AAAA"
  data_estimada_pagamento: string | null; // Formato: "dd/mm/AAAA"
  valor_risco: number;
  risco: string | null;
  total_pago: number;
  inss_empresa: number;
  honorarios: number;
  custas_processuais: number;
  situacao: string | null;
  nome_desdobramento: string | null;
  data_ajuizamento: string | null; // Formato: "dd/mm/AAAA"
  ult_desdobramento: string | null;
  instancia: string | null;
  rito: string | null;
  juizo: string | null;
  orgao: string | null;
  comarca: string | null;
  uf: string | null;
  numero: string | null;
  cliente: string | null;
  condicao_cliente: string | null;
  parte_adversa: string | null;
  condicao_adversa: string | null;
  cpf_cnpj_adversa: string | null;
  autor_contumaz: string | null;
  motivo_desligamento: string | null;
  cargo: string | null;
  terceiro_interessado: string | null;
  terceiro: string | null;
  terceiro_prestador: string | null;
  cpf_cnpj_terceiro_prestador: string | null;
  advogado_credenciado: string | null;
  handle_perito: string | null;
  perito: string | null;
  data_encerramento: string | null; // Formato: "dd/mm/AAAA"
  motivo_encerramento: string | null;
  exito: string | null;
  id_benner: string | null;
  data_evento: string | null; // Formato: "dd/mm/AAAA"
  evento: string | null;
  tarefas: string | null;
  advogado_centralizador: string | null;
  valor_risco_remoto: number;
  observacao: string | null;
  data_atualizacao: string; // Formato: "dd/mm/AAAA"
}

export default Processo;
