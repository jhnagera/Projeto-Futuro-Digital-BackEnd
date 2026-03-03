--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2026-03-03 11:00:14

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
    descricao text,
    posto_especial boolean
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



--
-- TOC entry 4798 (class 0 OID 16393)
-- Dependencies: 217
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Melissa', 98973, 'me@trt4.jus.br', 'Melissa', '123', '13:40', '19:40', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Hamilton', 71811, 'h@trt4.jus.br', 'Hamilton', '123', '12:00', '18:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('José Augusto', 67938, 'ja@trt4.jus.br', 'Augusto', '123', '14:00', '20:00', NULL);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Rodrigo Dossa', 96679, 'rd@trt4.jus.br', 'Dossa', '12345', '7:40', '13:40', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Eugenio B', 59986, 'eb@trt4.jus.br', 'Eugenio', '123', '6:40', '12:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Roberto V', 18910, 'rv@trt4.jus.br', 'Roberto', '123', '6:20', '12:20', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('José Henrique Luttjohann Nágera', 66621, 'jh@trt4.jus.br', 'Henrique', '12345', '13:00', '19:00', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Marcio Bigolin', 66622, 'mb@trt4.jus.br', 'Bigolin', '123456', '13:00', '19:00', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Marcelo Pereira', 85731, 'mp@trt4.jus.br', 'Marcelo', '123', '07:10', '13:10', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Luis Mirales', 65102, 'lm@trt4.jus.br', 'Mirales', '123', '11:45', '17:45', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Anderson Castalho', 89427, 'ac@trt4.jus.br', 'Castanho', '123', '06:40', '12:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Andre Melero', 97659, 'am@trt4.jus.br', 'Melero', '123', '07:40', '13:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Cristiano Lentz', 85600, 'cl@trt4.jus.br', 'Cristiano', '123', '07:40', '13:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Nereu de Oliveira', 33170, 'no@trt4.jus.br', 'Nereu', '123', '07:40', '13:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Juliano S', 93530, 'js@trt4.jus.br', 'Juliano', '123', '06:40', '12:40', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Claudenir dos Santos', 97128, 'cl@trt4.jus.br', 'Claudenir', '123', '06:40', '14:10', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Adriano D', 45365, 'ad@trt4.jus.br', 'Adriano', '123', '06:40', '14:10', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Rodrigo Maia', 96636, 'rm@trt4.jus.br', 'Maia', '123', '13:10', '19:10', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Manuel Melo', 97802, 'mm@trt4.jus.br', 'Manuel', '123', '12:10', '18:10', false);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('Rafael Faustino', 122874, 'rf@trt4.jus.br', 'Faustino', '123', '13:10', '19:10', true);
INSERT INTO public.funcionarios (nome_completo, matricula, email, apelido, senha, horario_inicio, horario_fim, posto_especial) VALUES ('José Luis Menezes', 20320, 'jm@trt4.jus.br', 'Menezes', '123', '10:10', '16:10', false);


--
-- TOC entry 4799 (class 0 OID 16398)
-- Dependencies: 218
-- Data for Name: postos; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (6, 'Ronda P1', 'Ronda em todo o Prédio 1', NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (7, 'Delta 4', 'Sala cofre para acautelamento de objetos não permitidos', NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (9, 'Galeria/QAP', NULL, NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (8, 'Alfa 3', 'Entrada principal do Forum', NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (10, 'Ronda P2 e P3', 'Ronda geral nos prédios 2 e 3', NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (5, 'Alfa 2', 'Entrada de funcionários', NULL);
INSERT INTO public.postos (id, nome, descricao, posto_especial) VALUES (13, 'Central', 'Gestão administrativa e atendimento ao publico ', true);


--
-- TOC entry 4808 (class 0 OID 0)
-- Dependencies: 216
-- Name: escala_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.escala_id_seq', 3, true);


--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 219
-- Name: postos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.postos_id_seq', 20, true);


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


-- Completed on 2026-03-03 11:00:15

--
-- PostgreSQL database dump complete
--

