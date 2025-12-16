--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2025-12-16 11:10:57

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
-- TOC entry 215 (class 1259 OID 41020)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    nome_completo text NOT NULL,
    matricula bigint NOT NULL,
    email text NOT NULL
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- TOC entry 4778 (class 0 OID 41020)
-- Dependencies: 215
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionarios (nome_completo, matricula, email) VALUES ('José Henrique Luttjohann Nágera', 66621, 'jnagera@trt4.jus.br');


--
-- TOC entry 4634 (class 2606 OID 41026)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (matricula);


-- Completed on 2025-12-16 11:10:57

--
-- PostgreSQL database dump complete
--

