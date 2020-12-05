-- QandAのIDを連番にするためのSEQUENCE作成
CREATE SEQUENCE public.faq_qanda_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- QandAインデックスのIDを連番にするためのSEQUENCE作成
CREATE SEQUENCE public.faq_index_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- QandAテーブルの作成
CREATE TABLE public.faq_qanda
(
    id integer NOT NULL DEFAULT nextval('faq_qanda_id_seq'::regclass),
    question character varying(50) COLLATE pg_catalog."default" NOT NULL,
    answer text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT faq_qanda_pkey PRIMARY KEY (id)
)

-- インデックステーブルの作成
CREATE TABLE public.faq_index
(
    id integer NOT NULL DEFAULT nextval('faq_index_id_seq'::regclass),
    token character varying(60) COLLATE pg_catalog."default" NOT NULL,
    qandaid integer NOT NULL,
    count integer NOT NULL,
    CONSTRAINT faq_index_pkey PRIMARY KEY (id)
)
