
-------------------------------------------------------------------------------
-- VIEW: v_cco_users_full
-- Mostra currículos + informações da coleção
-------------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_cco_users_full AS
SELECT
    u.id                         AS user_id,
    u.nome                       AS nome,
    u.sobre_mim                  AS sobre_mim,
    u.experiencia                AS experiencia,
    u.habilidades                AS habilidades,
    u.idiomas                    AS idiomas,
    u.contato                    AS contato,
    u.formacao                   AS formacao,
    u.idcollectioncco            AS collection_id,
    c.collection_set_name        AS collection_name,
    c.total_cco_collection       AS collection_total
FROM tbl_cco_user u
LEFT JOIN tbl_ccos c
       ON c.id = u.idcollectioncco;
       
       

-- Ver tudo
SELECT * FROM v_cco_users_full;

-- Filtrar por coleção
SELECT * FROM v_cco_users_full
WHERE collection_name = 'Tecnologia';

-- Buscar por nome
SELECT * FROM v_cco_users_full
WHERE LOWER(nome) LIKE LOWER('%carlos%');
