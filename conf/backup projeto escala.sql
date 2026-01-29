--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 17.0

-- Started on 2026-01-29 12:17:40

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 4806 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16427)
-- Name: escala; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.escala (
    horario text NOT NULL,
    data date NOT NULL,
    matricula integer NOT NULL,
    posto_id integer NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 16480)
-- Name: escala_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.escala_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4807 (class 0 OID 0)
-- Dependencies: 219
-- Name: escala_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.escala_id_seq OWNED BY public.escala.id;


--
-- TOC entry 216 (class 1259 OID 16432)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: -
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


--
-- TOC entry 217 (class 1259 OID 16437)
-- Name: postos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.postos (
    id integer NOT NULL,
    nome text,
    descricao text
);


--
-- TOC entry 218 (class 1259 OID 16442)
-- Name: postos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.postos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4808 (class 0 OID 0)
-- Dependencies: 218
-- Name: postos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.postos_id_seq OWNED BY public.postos.id;


--
-- TOC entry 4643 (class 2604 OID 16481)
-- Name: escala id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.escala ALTER COLUMN id SET DEFAULT nextval('public.escala_id_seq'::regclass);


--
-- TOC entry 4644 (class 2604 OID 16443)
-- Name: postos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.postos ALTER COLUMN id SET DEFAULT nextval('public.postos_id_seq'::regclass);


--
-- TOC entry 4796 (class 0 OID 16427)
-- Dependencies: 215
-- Data for Name: escala; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.escala VALUES ('13:00', '2026-09-01', 4000, 5, 1);
INSERT INTO public.escala VALUES ('13:00', '2026-09-01', 75282, 13, 2);


--
-- TOC entry 4797 (class 0 OID 16432)
-- Dependencies: 216
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.funcionarios VALUES ('teste5', 200, 'te5@trt4.jus.br', 'Tchê', '123', NULL, '14:00');
INSERT INTO public.funcionarios VALUES ('José Henrique Luttjohann Nágera', 66621, 'jh@trt4.jus.br', 'Henrique', '12345', '12:30', '19:00');
INSERT INTO public.funcionarios VALUES ('José Augusto', 68200, 'ja@trt4.jus.br', 'Augusto', '123', '14:00', '20:00');
INSERT INTO public.funcionarios VALUES ('Manuel Melo', 168200, 'mm@trt4.jus.br', 'Manuel', '123', '12:00', '18:00');
INSERT INTO public.funcionarios VALUES ('Rodrigo Maia', 80200, 'rm@trt4.jus.br', 'Maia', '123', '13:00', '19:00');
INSERT INTO public.funcionarios VALUES ('Rafael Faustino', 180300, 'rf@trt4.jus.br', 'Faustino', '123', '13:00', '19:00');
INSERT INTO public.funcionarios VALUES ('Marcelo Pereira', 70000, 'mp@trt4.jus.br', 'Marcelo', '123', '13:00', '19:00');
INSERT INTO public.funcionarios VALUES ('Luis Mirales', 50000, 'lm@trt4.jus.br', 'Mirales', '123', '12:00', '18:00');
INSERT INTO public.funcionarios VALUES ('Hamilton', 60000, 'h@trt4.jus.br', 'Hamilton', '123', '12:00', '18:00');
INSERT INTO public.funcionarios VALUES ('José Luis Menezes', 4000, 'jlm@trt4.jus.br', 'Menezes', '123', '10:00', '16:00');
INSERT INTO public.funcionarios VALUES ('Anderson Castalho', 75210, 'ac@trt4.jus.br', 'Castanho', '123', '7:00', '13:00');
INSERT INTO public.funcionarios VALUES ('Andre Melero', 75220, 'am@trt4.jus.br', 'Melero', '123', '7:00', '13:00');
INSERT INTO public.funcionarios VALUES ('Cristiano Lentz', 75240, 'cl@trt4.jus.br', 'Cristiano', '123', '7:00', '13:00');
INSERT INTO public.funcionarios VALUES ('Juliano S', 75260, 'js@trt4.jus.br', 'Juliano', '123', '7:00', '13:00');
INSERT INTO public.funcionarios VALUES ('Nereu de Oliveira', 75280, 'no@trt4.jus.br', 'Nereu', '123', '8:00', '14:00');
INSERT INTO public.funcionarios VALUES ('Claudenir dos Santos', 75281, 'cl@trt4.jus.br', 'Claudenir', '123', '8:00', '14:00');
INSERT INTO public.funcionarios VALUES ('Adriano D', 75282, 'ad@trt4.jus.br', 'Adriano', '123', '8:00', '14:00');


--
-- TOC entry 4798 (class 0 OID 16437)
-- Dependencies: 217
-- Data for Name: postos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.postos VALUES (6, 'Ronda P1', 'Ronda em todo o Prédio 1');
INSERT INTO public.postos VALUES (7, 'Delta 4', 'Sala cofre para acautelamento de objetos não permitidos');
INSERT INTO public.postos VALUES (9, 'Galeria/QAP', NULL);
INSERT INTO public.postos VALUES (11, 'Monitoramento', NULL);
INSERT INTO public.postos VALUES (13, 'Central', 'Gestão administrativa e atendimento ao publico ');
INSERT INTO public.postos VALUES (8, 'Alfa 3', 'Entrada principal do Forum');
INSERT INTO public.postos VALUES (10, 'Ronda P2 e P3', 'Ronda geral nos prédios 2 e 3');
INSERT INTO public.postos VALUES (5, 'Alfa 2', 'Entrada de funcionários');
INSERT INTO public.postos VALUES (14, 'Alfa 2iuhgikyg', 'Entrada de funcionários');
INSERT INTO public.postos VALUES (16, 'teste4', 'teste4');


--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 219
-- Name: escala_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.escala_id_seq', 2, true);


--
-- TOC entry 4810 (class 0 OID 0)
-- Dependencies: 218
-- Name: postos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.postos_id_seq', 17, true);


--
-- TOC entry 4646 (class 2606 OID 16488)
-- Name: escala escala_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_pk PRIMARY KEY (id);


--
-- TOC entry 4648 (class 2606 OID 16447)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (matricula);


--
-- TOC entry 4650 (class 2606 OID 16449)
-- Name: postos postos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.postos
    ADD CONSTRAINT postos_pkey PRIMARY KEY (id);


--
-- TOC entry 4651 (class 2606 OID 16450)
-- Name: escala escala_funcionarios_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_funcionarios_fk FOREIGN KEY (matricula) REFERENCES public.funcionarios(matricula);


--
-- TOC entry 4652 (class 2606 OID 16455)
-- Name: escala escala_postos_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.escala
    ADD CONSTRAINT escala_postos_fk FOREIGN KEY (posto_id) REFERENCES public.postos(id);


-- Completed on 2026-01-29 12:17:40

--
-- PostgreSQL database dump complete
--

