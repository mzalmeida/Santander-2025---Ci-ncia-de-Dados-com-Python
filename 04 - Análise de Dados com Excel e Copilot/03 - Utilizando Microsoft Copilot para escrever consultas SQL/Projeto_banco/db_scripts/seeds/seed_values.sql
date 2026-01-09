-------------------------------------------------------------------------------
-- EXEMPLOS DE INSERÇÃO
-------------------------------------------------------------------------------

-- Coleções
INSERT INTO tbl_ccos (collection_set_name, total_cco_collection)
VALUES ('Tecnologia', 0);

INSERT INTO tbl_ccos (collection_set_name, total_cco_collection)
VALUES ('Marketing', 0);

-- Usuários/Currículos
INSERT INTO tbl_cco_user (
    nome, sobre_mim, experiencia, habilidades, idiomas, contato, formacao, idcollectioncco
) VALUES (
    'Rogerio Vieira',
    'Profissional com experiência em soluções de dados',
    '3 anos como Analista de Dados; 2 anos em BI',
    'SQL, Python, Power BI, Azure',
    'pt-BR, en-US',
    'mrogerio@example.com | +55 11 99999-9999',
    'Bacharel em Sistemas de Informação',
    7 -- referência à coleção "Tecnologia"
);


-------------------------------------------------------------------------------
-- MAIS EXEMPLOS DE INSERÇÃO
-------------------------------------------------------------------------------

-- Usuário / Currículo 2
INSERT INTO tbl_cco_user (
    nome, sobre_mim, experiencia, habilidades, idiomas, contato, formacao, idcollectioncco
) VALUES (
    'Ana Paula Ribeiro',
    'Especialista em marketing digital focada em crescimento e performance',
    '5 anos em marketing digital; 3 anos com gestão de tráfego pago',
    'Google Ads, Meta Ads, SEO, Analytics, Copywriting',
    'pt-BR, en-US, es-ES',
    'ana.ribeiro@example.com | +55 11 98888-7777',
    'Pós-graduação em Marketing Digital',
    8 -- referência à coleção "Marketing"
);


-- Usuário / Currículo 3
INSERT INTO tbl_cco_user (
    nome, sobre_mim, experiencia, habilidades, idiomas, contato, formacao, idcollectioncco
) VALUES (
    'Carlos Eduardo Mendes',
    'Desenvolvedor back-end com foco em sistemas escaláveis e APIs',
    '6 anos como desenvolvedor Java e PL/SQL em ambientes corporativos',
    'Java, Spring Boot, Oracle SQL, PL/SQL, Docker',
    'pt-BR, en-US',
    'carlos.mendes@example.com | +55 16 97777-6666',
    'Bacharel em Ciência da Computação',
    7 -- referência à coleção "Tecnologia"
);
