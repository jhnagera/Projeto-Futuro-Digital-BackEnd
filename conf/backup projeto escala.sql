--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2026-01-31 16:01:12

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
-- TOC entry 215 (class 1259 OID 16387)
-- Name: escala; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.escala (
    horario text NOT NULL,
    data date NOT NULL,
    matricula integer NOT NULL,
    posto_id integer NOT NULL,
    id integer NOT NULL,
    posto_especial boolean
);


ALTER TABLE public.escala OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16392)
-- Name: escala_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.escala_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.escala_id_seq OWNER TO postgres;

--
-- TOC entry 4806 (class 0 OID 0)
-- Dependencies: 216
-- Name: escala_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.escala_id_seq OWNED BY public.escala.id;


--
-- TOC entry 217 (class 1259 OID 16393)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    nome_completo text NOT NULL,
    matricula bigint NOT NULL,
    email text NOT NULL,
    apelido text NOT NULL,
    senha text NOT NULL,
    horario_inicio text,
    horario_fim text,
    posto_especial boolean
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16398)
-- Name: postos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.postos (
    id integer NOT NULL,
    nome text,
    descricao text
);


ALTER TABLE public.postos OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16403)
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
-- TOC entry 4807 (class 0 OID 0)
-- Dependencies: 219
-- Name: postos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.postos_id_seq OWNED BY public.postos.id;


--
-- TOC entry 4643 (class 2604 OID 16404)
-- Name: escala id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escala ALTER COLUMN id SET DEFAULT nextval('public.escala_id_seq'::regclass);


--
-- TOC entry 4644 (class 2604 OID 16405)
-- Name: postos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postos ALTER COLUMN id SET DEFAULT nextval('public.postos_id_seq'::regclass);


--
-- TOC entry 4796 (class 0 OID 16387)
-- Dependencies: 215
-- Data for Name: escala; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.escala (horario, data, matricula, posto_id, id, posto_especial) VALUES ('13:00', '2026-09-01', 4000, 5, 1, NULL);
INSERT INTO public.escala (horario, data, matricula, posto_id, id, posto_especial) VALUES ('13:00', '2026-09-01', 75282, 13, 2, NULL);


--
-- TOC entry 4798 (class 0 OID 16393)
-- Dependencies: 217
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('teste5', 200, 'te5@trt4.jus.br', 'Tchê', '123', NULL, '14:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('José Augusto', 68200, 'ja@trt4.jus.br', 'Augusto', '123', '14:00', '20:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Manuel Melo', 168200, 'mm@trt4.jus.br', 'Manuel', '123', '12:00', '18:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Rodrigo Maia', 80200, 'rm@trt4.jus.br', 'Maia', '123', '13:00', '19:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Rafael Faustino', 180300, 'rf@trt4.jus.br', 'Faustino', '123', '13:00', '19:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Marcelo Pereira', 70000, 'mp@trt4.jus.br', 'Marcelo', '123', '13:00', '19:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Luis Mirales', 50000, 'lm@trt4.jus.br', 'Mirales', '123', '12:00', '18:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Hamilton', 60000, 'h@trt4.jus.br', 'Hamilton', '123', '12:00', '18:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Anderson Castalho', 75210, 'ac@trt4.jus.br', 'Castanho', '123', '7:00', '13:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Andre Melero', 75220, 'am@trt4.jus.br', 'Melero', '123', '7:00', '13:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Cristiano Lentz', 75240, 'cl@trt4.jus.br', 'Cristiano', '123', '7:00', '13:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Juliano S', 75260, 'js@trt4.jus.br', 'Juliano', '123', '7:00', '13:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Nereu de Oliveira', 75280, 'no@trt4.jus.br', 'Nereu', '123', '8:00', '14:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Claudenir dos Santos', 75281, 'cl@trt4.jus.br', 'Claudenir', '123', '8:00', '14:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Adriano D', 75282, 'ad@trt4.jus.br', 'Adriano', '123', '8:00', '14:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('José Henrique Luttjohann Nágera', 66621, 'jh@trt4.jus.br', 'Henrique', '12345', '13:00', '19:00', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('"José Luis Menezes"', 4000, 'jm@trt4.jus.br', 'Menezes', '123', '10:00', '14:00', false);


--
-- TOC entry 4799 (class 0 OID 16398)
-- Dependencies: 218
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
-- TOC entry 4808 (class 0 OID 0)
-- Dependencies: 216
-- Name: escala_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.escala_id_seq', 2, true);


--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 219
-- Name: postos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.postos_id_seq', 17, true);


--
-- TOC entry 4646 (class 2606 OID 16407)
-- Name: escala escala_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_pk PRIMARY KEY (id);


--
-- TOC entry 4648 (class 2606 OID 16409)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (matricula);


--
-- TOC entry 4650 (class 2606 OID 16411)
-- Name: postos postos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postos
    ADD CONSTRAINT postos_pkey PRIMARY KEY (id);


--
-- TOC entry 4651 (class 2606 OID 16412)
-- Name: escala escala_funcionarios_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_funcionarios_fk FOREIGN KEY (matricula) REFERENCES public.funcionarios(matricula);


--
-- TOC entry 4652 (class 2606 OID 16417)
-- Name: escala escala_postos_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_postos_fk FOREIGN KEY (posto_id) REFERENCES public.postos(id);


-- Completed on 2026-01-31 16:01:12

--
-- PostgreSQL database dump complete
--

