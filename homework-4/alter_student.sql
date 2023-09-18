-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE public.student
(
    student_id serial NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    birthday date NOT NULL,
    phone character varying NOT NULL,
    PRIMARY KEY (student_id)
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE IF EXISTS public.student
    ADD COLUMN middle_name character varying;

-- 3. Удалить колонку middle_name
ALTER TABLE student
DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student
RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student
ALTER COLUMN phone TYPE character varying(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO public.student (first_name, last_name, birth_date, phone)
VALUES ('Имя1', 'Фамилия1', '2000-01-01', '123-456-7890'),
 	   ('Имя2', 'Фамилия2', '1999-02-15', '987-654-3210'),
	   ('Имя3', 'Фамилия3', '2001-05-20', '555-123-4567');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE public.student RESTART IDENTITY;
