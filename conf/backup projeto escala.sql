--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2026-01-22 18:35:08

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 49204)
-- Name: escala; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.escala (
    id integer NOT NULL,
    horario text NOT NULL,
    data date NOT NULL,
    matricula text NOT NULL,
    posto text NOT NULL
);


ALTER TABLE public.escala OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 49197)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    nome_completo text NOT NULL,
    matricula bigint NOT NULL,
    email text NOT NULL,
    apelido text NOT NULL,
    senha text NOT NULL,
    horario_inicio text,
    horario_fim text
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 41010)
-- Name: postos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.postos (
    id integer NOT NULL,
    nome text,
    descricao text
);


ALTER TABLE public.postos OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 41015)
-- Name: postos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.postos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.postos_id_seq OWNER TO postgres;

--
-- TOC entry 4801 (class 0 OID 0)
-- Dependencies: 216
-- Name: postos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.postos_id_seq OWNED BY public.postos.id;


--
-- TOC entry 4642 (class 2604 OID 41016)
-- Name: postos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postos ALTER COLUMN id SET DEFAULT nextval('public.postos_id_seq'::regclass);


--
-- TOC entry 4795 (class 0 OID 49204)
-- Dependencies: 218
-- Data for Name: escala; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 4794 (class 0 OID 49197)
-- Dependencies: 217
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('teste5', 200, 'te5@trt4.jus.br', 'Tchê', '123', NULL, '14:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('José Henrique Luttjohann Nágera', 66621, 'jh@trt4.jus.br', 'Henrique', '12345', '12:30', '19:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('José Augusto', 68200, 'ja@trt4.jus.br', 'Augusto', '123', '14:00', '20:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Manuel Melo', 168200, 'mm@trt4.jus.br', 'Manuel', '123', '12:00', '18:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Rodrigo Maia', 80200, 'rm@trt4.jus.br', 'Maia', '123', '13:00', '19:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Rafael Faustino', 180300, 'rf@trt4.jus.br', 'Faustino', '123', '13:00', '19:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Marcelo Pereira', 70000, 'mp@trt4.jus.br', 'Marcelo', '123', '13:00', '19:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Luis Mirales', 50000, 'lm@trt4.jus.br', 'Mirales', '123', '12:00', '18:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Hamilton', 60000, 'h@trt4.jus.br', 'Hamilton', '123', '12:00', '18:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('José Luis Menezes', 4000, 'jlm@trt4.jus.br', 'Menezes', '123', '10:00', '16:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Anderson Castalho', 75210, 'ac@trt4.jus.br', 'Castanho', '123', '7:00', '13:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Andre Melero', 75220, 'am@trt4.jus.br', 'Melero', '123', '7:00', '13:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Cristiano Lentz', 75240, 'cl@trt4.jus.br', 'Cristiano', '123', '7:00', '13:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Juliano S', 75260, 'js@trt4.jus.br', 'Juliano', '123', '7:00', '13:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Nereu de Oliveira', 75280, 'no@trt4.jus.br', 'Nereu', '123', '8:00', '14:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Claudenir dos Santos', 75281, 'cl@trt4.jus.br', 'Claudenir', '123', '8:00', '14:00');
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim) VALUES ('Adriano D', 75282, 'ad@trt4.jus.br', 'Adriano', '123', '8:00', '14:00');


--
-- TOC entry 4792 (class 0 OID 41010)
-- Dependencies: 215
-- Data for Name: postos; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.postos (id, nome, descricao) VALUES (6, 'Ronda P1', 'Ronda em todo o Prédio 1');
INSERT INTO public.postos (id, nome, descricao) VALUES (7, 'Delta 4', 'Sala cofre para acautelamento de objetos não permitidos');
INSERT INTO public.postos (id, nome, descricao) VALUES (9, 'Galeria/QAP', NULL);
INSERT INTO public.postos (id, nome, descricao) VALUES (11, 'Monitoramento', NULL);
INSERT INTO public.postos (id, nome, descricao) VALUES (13, 'Central', 'Gestão administrativa e atendimento ao publico ');
INSERT INTO public.postos (id, nome, descricao) VALUES (8, 'Alfa 3', 'Entrada principal do Forum');
INSERT INTO public.postos (id, nome, descricao) VALUES (10, 'Ronda P2 e P3', 'Ronda geral nos prédios 2 e 3');
INSERT INTO public.postos (id, nome, descricao) VALUES (5, 'Alfa 2', 'Entrada de funcionários');
INSERT INTO public.postos (id, nome, descricao) VALUES (14, 'Alfa 2iuhgikyg', 'Entrada de funcionários');
INSERT INTO public.postos (id, nome, descricao) VALUES (16, 'teste4', 'teste4');


--
-- TOC entry 4802 (class 0 OID 0)
-- Dependencies: 216
-- Name: postos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.postos_id_seq', 16, true);


--
-- TOC entry 4648 (class 2606 OID 49210)
-- Name: escala escala_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_pkey PRIMARY KEY (id);


--
-- TOC entry 4646 (class 2606 OID 49203)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (matricula);


--
-- TOC entry 4644 (class 2606 OID 41020)
-- Name: postos postos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postos
    ADD CONSTRAINT postos_pkey PRIMARY KEY (id);


-- Completed on 2026-01-22 18:35:08

--
-- PostgreSQL database dump complete
--

