# MLSecOps pipeline

### Первоочередные действия

1. Ставим trivy: `brew install aquasecurity/trivy/trivy`
2. Ставим pip-audit `pip install pip-audit`
3. Устанавливаем модель, например такую: `https://huggingface.co/EleutherAI/gpt-neo-125m`

### Список первых вопросов к модели

1. Сколько скачиваний?
2. Кто автор?
3. Лицензия?
4. Нет ли embedded credentials в .bin файлах?
5. Есть ли trust_remote_code=True в примерах?

### Пример ответов на вопросы для модели выше

1. В прошлом месяце (май 2025) - модель скачали 101,731 раз.
2. Автор - `https://www.eleuther.ai/`
3. Лицензия - MIT.
4. Ищем ключевые слова следующим образом: `grep -iE 'token|secret|key|password|oauth|authorization' . -R` или ` strings model.safetensors | grep -Ei 'sk-[a-z0-9]{20,}|ghp_[a-z0-9]{30,}|AKIA[a-zA-Z0-9]{16}'`
5. Ищем в примерах или `.py` файлах, `config.json`.

### ModelScan

1. Что это? Ознакомиться можно здесь: `https://github.com/protectai/modelscan`
2. Как его запустить? Через `.venv/bin/modelscan -p ./model/model.<something> --show-skipped`
3. Важно: modelscan, судя по всему, сканировать пока что ничего не умеет.

### Garak

1. Что это? Ознакомиться можно здесь: `https://github.com/NVIDIA/garak`
2. Запуск: ` garak \
  --model_type huggingface.Model \
  --model_name ./model \
  --generations 5 \
  --probes promptinject.HijackKillHumans,exploitation.SQLInjectionEcho,malwaregen.Payload,leakreplay.NYTComplete \
  --report_prefix garak_run
`

