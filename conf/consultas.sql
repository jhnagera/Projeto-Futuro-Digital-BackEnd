
-- ==============================================================================
-- CONSULTA DE DISPONIBILIDADE
-- Verifica se um funcionário pode assumir um posto em um determinado horário/data.
-- ==============================================================================

SELECT * FROM public.funcionarios
WHERE horario_inicio < '12:30' and horario_fim > '13:00'
ORDER BY RANDOM()


SELECT * FROM public.escala
WHERE horario = '12:30' and data = '2026-02-07'